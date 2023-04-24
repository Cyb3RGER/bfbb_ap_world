import typing
from BaseClasses import Item, ItemClassification


class ItemData(typing.NamedTuple):
    id: typing.Optional[int]
    classification: ItemClassification

    def is_progression(self):
        return self.classification & ItemClassification.progression == ItemClassification.progression

    def is_trap(self):
        return self.classification & ItemClassification.trap == ItemClassification.trap

    def is_filler(self):
        return self.classification & ItemClassification.filler == ItemClassification.filler


class BfBBItem(Item):
    game: str = "Battle for Bikini Bottom"


base_id = 149000

item_table = {
    "Golden Spatula": ItemData(base_id + 0, ItemClassification.progression),
    "Lost Sock": ItemData(base_id + 1, ItemClassification.useful),
    "Red Shiny Object": ItemData(base_id + 2, ItemClassification.filler),
    "Yellow Shiny Object": ItemData(base_id + 3, ItemClassification.filler),
    "Green Shiny Object": ItemData(base_id + 4, ItemClassification.filler),
    "Blue Shiny Object": ItemData(base_id + 5, ItemClassification.filler),
    "Purple Shiny Object": ItemData(base_id + 6, ItemClassification.filler),
    "Bubble Bowl": ItemData(base_id + 7, ItemClassification.progression),
    "Cruise Bubble": ItemData(base_id + 8, ItemClassification.progression),
    "Golden Underwear": ItemData(base_id + 8, ItemClassification.useful),
    "Defeated Robo-Sandy": ItemData(None, ItemClassification.progression),
    "Defeated Robo-Patrick": ItemData(None, ItemClassification.progression),
    "Victory": ItemData(None, ItemClassification.progression)
}

lookup_id_to_name: typing.Dict[int, str] = {data.id: name for name, data in item_table.items() if data.id}