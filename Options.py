import typing
from Options import Toggle, DeathLink, Range, AssembleOptions, Choice


# ToDo

class AvailableSpatulas(Range):
    """Amount of available golden spatulas"""
    display_name = "Available Spatulas"
    range_start = 75
    range_end = 100
    default = 100


class IncludeSocks(Toggle):
    """Include Socks as AP Locations/Items"""
    display_name = "Include Socks"
    default = 1


class IncludeSkills(Toggle):
    """Include Skills (Bubble Bowl & Cruise Bubble) as AP Locations/Items"""
    display_name = "Include Skills"
    default = 1


class IncludeGoldenUnderwear(Toggle):
    """Include Golden Underwear as AP Locations/Items"""
    display_name = "Include Golden Underwear"
    default = 1


class IncludeLevelItems(Toggle):
    """Include Level Pickups (steering wheels, balloon kids etc.) as AP Locations/Items"""
    display_name = "Include Level Items"
    default = 1


class IncludePurpleSO(Toggle):
    """Include Purple Shiny Objects as AP Locations/Items"""
    display_name = "Include Purple Shiny Objects Items"
    default = 1


class RandomizeGateCost(Choice):
    """Randomize how many golden spatulas are required for taxi gates.
    This will pick a random level order and increment on gate cost according to the level order.
    Low, mid and high refer to possible increment between levels.
    High will likely fail to generate on single player seeds or seeds with few filler locations.
    """
    display_name = "Randomize Gate Cost"
    option_off = 0
    option_low = 1
    option_mid = 2
    option_high = 3
    default = 0


bfbb_options: typing.Dict[str, AssembleOptions] = {
    "available_spatulas": AvailableSpatulas,
    "include_socks": IncludeSocks,
    "include_skills": IncludeSkills,
    "include_golden_underwear": IncludeGoldenUnderwear,
    "include_level_items": IncludeLevelItems,
    "include_purple_so": IncludePurpleSO,
    "randomize_gate_cost": RandomizeGateCost,
    "death_link": DeathLink,

}
