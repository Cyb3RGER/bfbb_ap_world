import math
import multiprocessing
import os
import random
import sys
import zipfile
from multiprocessing import Process

import Utils
from BaseClasses import Item, Tutorial
from Fill import fill_restrictive, FillError
from worlds.AutoWorld import World, WebWorld
from .Events import create_events
from .Items import item_table, BfBBItem
from .Locations import location_table, BfBBLocation
from .Options import bfbb_options
from .Regions import create_regions
from .Rom import BfBBDeltaPatch
from .Rules import set_rules, set_gate_rules, reset_gate_rules
from worlds.LauncherComponents import Component, components, Type
from .names import ItemNames, ConnectionNames


def run_client():
    print('running bfbb client')
    from .BfBBClient import main  # lazy import
    file_types = (('BfBB Patch File', ('.apbfbb',)), ('NGC iso', ('.gcm',)),)
    kwargs = {'patch_file': Utils.open_filename("Select .apbfbb", file_types)}
    p = Process(target=main, kwargs=kwargs)
    p.start()


components.append(Component("BfBB Client", func=run_client, component_type=Type.CLIENT))


class BattleForBikiniBottomWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the The Binding Of Isaac Repentance integration for Archipelago multiworld games.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Cyb3R"]
    )]


default_gate_costs = {
    # ConnectionNames.pineapple_hub1: 1,
    ConnectionNames.hub1_bb01: 5,
    ConnectionNames.hub1_gl01: 10,
    ConnectionNames.hub1_b1: 15,
    ConnectionNames.hub2_rb01: 25,
    ConnectionNames.hub2_sm01: 30,
    ConnectionNames.hub2_b2: 40,
    ConnectionNames.hub3_kf01: 50,
    ConnectionNames.hub3_gy01: 60,
    ConnectionNames.cb_b3: 75,
}


class BattleForBikiniBottom(World):
    """
    SpongeBob SquarePants: Battle for Bikini Bottom
    ToDo
    """
    game: str = "Battle for Bikini Bottom"
    option_definitions = bfbb_options
    topology_present = False

    item_name_to_id = {name: data.id for name, data in item_table.items()}
    location_name_to_id = location_table

    data_version = 5
    web = BattleForBikiniBottomWeb()

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)
        self.gate_costs = default_gate_costs.copy()

    def test_gate_cost_beatable(self) -> bool:
        old_rules = set_gate_rules(self.player, {self.multiworld.get_entrance(k, self.player): v for k, v in
                                                 self.gate_costs.items()})
        spat_locations = self.multiworld.get_unfilled_locations(self.player)
        prog_items = list(
            filter(lambda item: item.player == self.player and item.advancement, self.multiworld.itempool))
        for item in prog_items:
            self.multiworld.itempool.remove(item)
        try:
            fill_restrictive(self.multiworld, self.multiworld.get_all_state(False), spat_locations.copy(),
                             prog_items.copy(), True)
            # print("successfully filled spats!")
            beatable = True
        except FillError:
            # print(">>> failed to fill spats")
            reset_gate_rules(old_rules)
            beatable = False
        # Undo what was done
        for item in prog_items:
            item.location = None
        for location in spat_locations:
            location.item = None
            location.locked = False
            location.event = False
        self.multiworld.itempool += prog_items
        return beatable

    def reroll_gate_costs(self):
        randomize_gate_cost = self.multiworld.randomize_gate_cost[self.player].value
        # get the 3 keys (prioritize hub connections and earlier connections and higher values)
        weights = [5, 5, 15, 3, 3, 10, 1, 1, 0]
        values = [v for _, v in self.gate_costs.items()]
        weights = [x * (y / 5) for x, y in zip(weights, values)]
        k = 2 if randomize_gate_cost < 4 else 2
        keys = random.choices([k for k in self.gate_costs], weights=weights, k=k)
        gate_cost_fact = 0.25 if randomize_gate_cost == 1 else 0.5 if randomize_gate_cost == 2 else 0.75
        min_value = 0
        # print(keys)
        for k in keys:
            if randomize_gate_cost != 4:
                min_value = round(default_gate_costs[k] * (max(1 - gate_cost_fact, 0)))
            self.gate_costs[k] = self.multiworld.random.randint(min_value, self.gate_costs[k])

        # print(self.gate_costs, min_value)

    def roll_gate_costs(self):
        randomize_gate_cost = self.multiworld.randomize_gate_cost[self.player].value
        max_value = self.multiworld.available_spatulas[self.player].value
        if max_value == 100 and not self.multiworld.include_socks[self.player].value and not \
                self.multiworld.include_golden_underwear[self.player].value and not \
                self.multiworld.include_level_items[self.player].value and not \
                self.multiworld.include_purple_so[self.player].value:
            max_value -= 2
        if 0 < randomize_gate_cost < 4:
            gate_cost_fact = 0.25 if randomize_gate_cost == 1 else 0.5 if randomize_gate_cost == 2 else 0.75
            for k, v in self.gate_costs.items():
                self.gate_costs[k] = min(self.multiworld.random.randint(round(v * (max(1 - gate_cost_fact, 0))),
                                                                        round(v * (1 + gate_cost_fact))),
                                         max_value)
        elif randomize_gate_cost == 4:
            for k, v in self.gate_costs.items():
                self.gate_costs[k] = self.multiworld.random.randint(0, max_value)

        # print(randomize_gate_cost, self.gate_costs)

    def generate_early(self) -> None:
        self.roll_gate_costs()

    def pre_fill(self) -> None:
        max_tries = 20
        tries = 0
        while not self.test_gate_cost_beatable() and tries < max_tries:
            # print(f"reroll gate costs try {tries + 1}")
            self.reroll_gate_costs()
            tries = tries + 1
            if tries >= max_tries:
                raise FillError(f"failed to find beatable gate costs after {max_tries}")

    def get_items(self):
        filler_items = [ItemNames.so_100, ItemNames.so_250]
        filler_weights = [1, 2]
        # Generate item pool
        itempool = [ItemNames.spat] * self.multiworld.available_spatulas[self.player].value
        if 100 - self.multiworld.available_spatulas[self.player].value > 0:
            itempool += random.choices(filler_items, weights=filler_weights,
                                       k=100 - self.multiworld.available_spatulas[self.player].value)
        if self.multiworld.include_socks[self.player].value:
            itempool += [ItemNames.sock] * 80
        if self.multiworld.include_skills[self.player].value:
            itempool += [ItemNames.bubble_bowl, ItemNames.cruise_bubble]
        if self.multiworld.include_golden_underwear[self.player].value:
            itempool += [ItemNames.golden_underwear] * 3
        if self.multiworld.include_level_items[self.player].value:
            itempool += [ItemNames.lvl_itm_jf]
            itempool += [ItemNames.lvl_itm_bb] * 11
            itempool += [ItemNames.lvl_itm_gl] * 5
            itempool += [ItemNames.lvl_itm_rb] * 6
            itempool += [ItemNames.lvl_itm_bc] * 4
            itempool += [ItemNames.lvl_itm_sm] * 8
            itempool += [ItemNames.lvl_itm_kf1] * 6
            itempool += [ItemNames.lvl_itm_kf2] * 6
            itempool += [ItemNames.lvl_itm_gy] * 4
        if self.multiworld.include_purple_so[self.player].value:
            so_items = [ItemNames.so_100, ItemNames.so_250, ItemNames.so_500, ItemNames.so_750, ItemNames.so_1000]
            weights = [1, 2, 5, 3, 2]
            itempool += random.choices(so_items, weights=weights, k=38)

        # adjust for starting inv prog. items
        k = 0
        for item in self.multiworld.precollected_items[self.player]:
            if item.name in itempool and item.advancement:
                itempool.remove(item.name)
                k = k + 1
        if k > 0:
            itempool += random.choices(filler_items, weights=filler_weights, k=k)
        # Convert itempool into real items
        itempool = list(map(lambda name: self.create_item(name), itempool))
        return itempool

    def create_items(self):
        self.multiworld.itempool += self.get_items()

    def set_rules(self):
        create_events(self.multiworld, self.player)
        set_rules(self.multiworld, self.player, self.gate_costs)

    def create_regions(self):
        create_regions(self.multiworld, self.player)

    def fill_slot_data(self):
        return {
            "death_link": self.multiworld.death_link[self.player].value,
            "include_socks": self.multiworld.include_socks[self.player].value,
            "include_skills": self.multiworld.include_skills[self.player].value,
            "include_golden_underwear": self.multiworld.include_golden_underwear[self.player].value,
            "include_level_items": self.multiworld.include_level_items[self.player].value,
            "include_purple_so": self.multiworld.include_purple_so[self.player].value,
            "gate_costs": self.gate_costs
        }

    def create_item(self, name: str) -> Item:
        item_data = item_table[name]
        item = BfBBItem(name, item_data.classification, item_data.id, self.player)
        return item

    def generate_output(self, output_directory: str) -> None:
        patch = BfBBDeltaPatch(path=os.path.join(output_directory,
                                                 f"{self.multiworld.get_out_file_name_base(self.player)}{BfBBDeltaPatch.patch_file_ending}"),
                               player=self.player,
                               player_name=self.multiworld.player_name[self.player],
                               include_socks=bool(self.multiworld.include_socks[self.player].value),
                               include_skills=bool(self.multiworld.include_skills[self.player].value),
                               include_golden_underwear=bool(
                                   self.multiworld.include_golden_underwear[self.player].value),
                               include_level_items=bool(self.multiworld.include_level_items[self.player].value),
                               include_purple_so=bool(self.multiworld.include_purple_so[self.player].value),
                               seed=self.multiworld.seed_name.encode('utf-8'),
                               randomize_gate_cost=self.multiworld.randomize_gate_cost[self.player].value,
                               gate_costs=self.gate_costs,
                               )
        patch.write()
