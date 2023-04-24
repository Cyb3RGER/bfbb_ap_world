from BaseClasses import Item, Tutorial
from worlds.AutoWorld import World, WebWorld
from .Events import create_events
from .Items import item_table, BfBBItem
from .Locations import location_table, BfBBLocation
from .Options import bfbb_options
from .Regions import create_regions
from .Rules import set_rules


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
        # Generate item pool
        itempool = [
                       "Golden Spatula"
                   ] * 100
        if self.multiworld.include_socks[self.player].value:
            itempool += ["Lost Sock"] * 80
        if self.multiworld.include_skills[self.player].value:
            itempool += ["Cruise Bubble", "Bubble Bowl"]
        if self.multiworld.include_level_pickups[self.player].value:
            pass # ToDo
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
            "deathLink": self.multiworld.death_link[self.player].value
        }

    def create_item(self, name: str) -> Item:
        item_data = item_table[name]
        item = BfBBItem(name, item_data.classification, item_data.id, self.player)
        return item



