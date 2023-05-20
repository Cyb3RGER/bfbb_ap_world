import multiprocessing
import os
import random
import sys
import zipfile
from multiprocessing import Process

import Utils
from BaseClasses import Item, Tutorial
from worlds.AutoWorld import World, WebWorld
from .Events import create_events
from .Items import item_table, BfBBItem
from .Locations import location_table, BfBBLocation
from .Options import bfbb_options
from .Regions import create_regions
from .Rom import BfBBDeltaPatch
from .Rules import set_rules
from worlds.LauncherComponents import Component, components, Type
from .names import ItemNames


def run_client():
    print('running bfbb client')
    from .BfBBClient import main  # lazy import
    file_types = (('BfBB Patch File', ('.apbfbb',)), ('NGC iso', ('.gcm',)),)
    kwargs = {'patch_file': Utils.open_filename("Select .apbfbb", file_types)}
    p = Process(target=main, kwargs=kwargs)
    p.start()


components.append(Component("BfBB Client", func=run_client))


class BattleForBikiniBottomWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the The Binding Of Isaac Repentance integration for Archipelago multiworld games.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Cyb3R"]
    )]


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

    def generate_early(self) -> None:
        pass

    def create_items(self):
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

        self.multiworld.itempool += itempool

    def set_rules(self):
        create_events(self.multiworld, self.player)
        set_rules(self.multiworld, self.player)

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
                               seed=self.multiworld.seed_name.encode('utf-8')
                               )
        patch.write()
