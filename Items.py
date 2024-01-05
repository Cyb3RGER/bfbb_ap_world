import typing
from BaseClasses import Item, ItemClassification
from .names import ItemNames


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
    # spats
    ItemNames.spat: ItemData(base_id + 0, ItemClassification.progression),
    # socks
    ItemNames.sock: ItemData(base_id + 1, ItemClassification.progression),
    # shiny objects rewards
    ItemNames.so_100: ItemData(base_id + 2, ItemClassification.filler),
    ItemNames.so_250: ItemData(base_id + 3, ItemClassification.filler),
    ItemNames.so_500: ItemData(base_id + 4, ItemClassification.progression_skip_balancing),
    ItemNames.so_750: ItemData(base_id + 5, ItemClassification.progression_skip_balancing),
    ItemNames.so_1000: ItemData(base_id + 6, ItemClassification.progression_skip_balancing),
    # skills
    ItemNames.bubble_bowl: ItemData(base_id + 7, ItemClassification.progression),
    ItemNames.cruise_bubble: ItemData(base_id + 8, ItemClassification.progression),
    # golden underwear
    ItemNames.golden_underwear: ItemData(base_id + 9, ItemClassification.useful),
    # level pickups
    ItemNames.lvl_itm_jf: ItemData(base_id + 10, ItemClassification.progression),
    ItemNames.lvl_itm_bb: ItemData(base_id + 11, ItemClassification.progression),
    ItemNames.lvl_itm_gl: ItemData(base_id + 12, ItemClassification.progression),
    ItemNames.lvl_itm_rb: ItemData(base_id + 13, ItemClassification.progression),
    ItemNames.lvl_itm_bc: ItemData(base_id + 14, ItemClassification.progression),
    ItemNames.lvl_itm_sm: ItemData(base_id + 15, ItemClassification.progression),
    ItemNames.lvl_itm_kf1: ItemData(base_id + 16, ItemClassification.progression),
    ItemNames.lvl_itm_kf2: ItemData(base_id + 17, ItemClassification.progression),
    ItemNames.lvl_itm_gy: ItemData(base_id + 18, ItemClassification.progression),
    # events
    ItemNames.victory: ItemData(None, ItemClassification.progression)
}

lookup_id_to_name: typing.Dict[int, str] = {data.id: name for name, data in item_table.items() if data.id}
