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
    """Randomize how many golden spatulas are required for taxi gates
    off = vanilla
    low = cost will be between +/- 25% from vanilla cost
    mid = cost will be between +/- 50% variance from vanilla cost
    high = cost will be between +/- 75% variance from vanilla cost
    full_random = cost will be between 0 and available spatulas for each gate
                  (not recommended as it can extend generation time quite a bit since it tents reroll a bunch)
    """
    display_name = "Randomize Gate Cost"
    option_off = 0
    option_low = 1
    option_mid = 2
    option_high = 3
    option_full_random = 4


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
