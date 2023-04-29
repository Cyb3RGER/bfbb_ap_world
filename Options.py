import typing
from Options import Option, Toggle, DeathLink


# ToDo

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


bfbb_options: typing.Dict[str, type(Option)] = {
    "include_socks": IncludeSocks,
    "include_skills": IncludeSkills,
    "include_golden_underwear": IncludeGoldenUnderwear,
    "include_level_items": IncludeLevelItems,
    "include_purple_so": IncludePurpleSO,
    "death_link": DeathLink,
}
