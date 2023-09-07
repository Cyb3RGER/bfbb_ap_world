import math
import multiprocessing
import os
import random
import sys
import zipfile
from multiprocessing import Process
from typing import TextIO

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
from .Rules import set_rules
from worlds.LauncherComponents import Component, components, Type, SuffixIdentifier
from .names import ItemNames, ConnectionNames


def run_client():
    print('running bfbb client')
    from worlds.bfbb.BfBBClient import main  # lazy import
    file_types = (('BfBB Patch File', ('.apbfbb',)), ('NGC iso', ('.gcm',)),)
    kwargs = {'patch_file': Utils.open_filename("Select .apbfbb", file_types)}
    p = Process(target=main, kwargs=kwargs)
    p.start()


components.append(Component("BfBB Client", func=run_client, component_type=Type.CLIENT,
                            file_identifier=SuffixIdentifier('.apbfbb')))


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
        self.level_order = [ConnectionNames.hub1_bb01, ConnectionNames.hub1_gl01, ConnectionNames.hub1_b1,
                            ConnectionNames.hub2_rb01, ConnectionNames.hub2_sm01, ConnectionNames.hub2_b2,
                            ConnectionNames.hub3_kf01, ConnectionNames.hub3_gy01, ConnectionNames.cb_b3]

    def generate_early(self) -> None:
        if self.multiworld.randomize_gate_cost[self.player].value > 0:
            print(self.multiworld.player_name[self.player], self.multiworld.randomize_gate_cost[self.player])
            self.roll_level_order()
            print(self.level_order)
            self.set_gate_costs()
            for k in self.level_order:
                print(k, self.gate_costs[k])

    def roll_level_order(self):
        level_left = [ConnectionNames.hub1_bb01, ConnectionNames.hub1_gl01, ConnectionNames.hub2_rb01,
                      ConnectionNames.hub2_sm01, ConnectionNames.hub3_kf01, ConnectionNames.hub3_gy01]
        counts = [4,4,2,2, 1, 1]
        cnt = len(level_left)
        self.level_order = []
        for i in range(0, cnt):
            idx = self.random.sample(range(0, len(level_left)), k=1, counts=counts)[0]
            level = level_left[idx]
            if level in [ConnectionNames.hub2_rb01, ConnectionNames.hub2_sm01, ConnectionNames.hub3_kf01,
                         ConnectionNames.hub3_gy01] and ConnectionNames.hub1_b1 not in self.level_order:
                self.level_order.append(ConnectionNames.hub1_b1)
            if level in [ConnectionNames.hub3_kf01,
                         ConnectionNames.hub3_gy01] and ConnectionNames.hub2_b2 not in self.level_order:
                self.level_order.append(ConnectionNames.hub2_b2)
            self.level_order.append(level)
            level_left.remove(level)
            counts.remove(counts[idx])
        self.level_order.append(ConnectionNames.cb_b3)

    def set_gate_costs(self):
        last_level = None
        min_incs = [0, 2, 5]
        last_cost = 1
        for v in self.level_order:
            level_inc_min = min_incs[
                self.multiworld.randomize_gate_cost[self.player].value - 1] if v != ConnectionNames.cb_b3 else 5
            level_inc_max = 8
            if self.multiworld.include_socks[self.player].value:
                level_inc_max += 6
            if self.multiworld.include_level_items[self.player].value:
                level_inc_max += 3
            if self.multiworld.include_purple_so[self.player].value:
                level_inc_max += 1
            if self.multiworld.randomize_gate_cost[self.player].value == 3:
                level_inc_max = round(level_inc_max * 1.35)
            elif self.multiworld.randomize_gate_cost[self.player].value == 1:
                level_inc_max = round(level_inc_max * 0.75)
            # set max increment after boss to 1
            if last_level is not None and last_level in [ConnectionNames.hub1_b1, ConnectionNames.hub2_b2]:
                level_inc_max = 1
            level_inc_min = min(level_inc_min, level_inc_max)
            cost = min(self.random.randint(level_inc_min, level_inc_max) + last_cost, self.multiworld.available_spatulas[self.player].value)
            self.gate_costs[v] = cost
            last_level = v
            last_cost = cost

    def get_filler_item_name(self) -> str:
        return ItemNames.so_100

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

    def write_spoiler(self, spoiler_handle: TextIO) -> None:
        if self.multiworld.randomize_gate_cost[self.player].value > 0:
            spoiler_handle.write(f"\n\nGate Costs ({self.multiworld.get_player_name(self.player)}):\n\n")
            for k, v in self.gate_costs.items():
                spoiler_handle.write(f"{k}: {v}\n")

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
