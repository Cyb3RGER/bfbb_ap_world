from typing import Callable, Dict

from BaseClasses import MultiWorld, CollectionState
from worlds.bfbb.names import ConnectionNames, ItemNames, LocationNames
from worlds.generic.Rules import set_rule, add_rule, CollectionRule

# ToDo:
# double check access rules

spat_rules = [
    # connections
    {
        ConnectionNames.pineapple_hub1: lambda player: lambda state: state.has(ItemNames.spat, player, 1),
        ConnectionNames.hub1_bb01: lambda player: lambda state: state.has(ItemNames.spat, player, 5),
        ConnectionNames.hub1_gl01: lambda player: lambda state: state.has(ItemNames.spat, player, 10),
        ConnectionNames.hub1_b1: lambda player: lambda state: state.has(ItemNames.spat, player, 15),
        ConnectionNames.hub2_rb01: lambda player: lambda state: state.has(ItemNames.spat, player, 25),
        ConnectionNames.hub2_sm01: lambda player: lambda state: state.has(ItemNames.spat, player, 30),
        ConnectionNames.hub2_b2: lambda player: lambda state: state.has(ItemNames.spat, player, 40),
        ConnectionNames.hub3_kf01: lambda player: lambda state: state.has(ItemNames.spat, player, 50),
        ConnectionNames.hub3_gy01: lambda player: lambda state: state.has(ItemNames.spat, player, 60),
        ConnectionNames.cb_b3: lambda player: lambda state: state.has(ItemNames.spat, player, 75),
    },
    # locations
    {
        LocationNames.spat_ks_01: lambda player: lambda state: state.has(ItemNames.spat, player, 5),
        LocationNames.spat_ks_02: lambda player: lambda state: state.has(ItemNames.spat, player, 10),
        LocationNames.spat_ks_03: lambda player: lambda state: state.has(ItemNames.spat, player, 15),
        LocationNames.spat_ks_04: lambda player: lambda state: state.has(ItemNames.spat, player, 20),
        LocationNames.spat_ks_05: lambda player: lambda state: state.has(ItemNames.spat, player, 25),
        LocationNames.spat_ks_06: lambda player: lambda state: state.has(ItemNames.spat, player, 30),
        LocationNames.spat_ks_07: lambda player: lambda state: state.has(ItemNames.spat, player, 35),
        LocationNames.spat_ks_08: lambda player: lambda state: state.has(ItemNames.spat, player, 40),
    }
]
sock_rules = [
    # connections
    {},
    # locations
    {
        LocationNames.spat_ps_01: lambda player: lambda state: state.has(ItemNames.sock, player, 10),
        LocationNames.spat_ps_02: lambda player: lambda state: state.has(ItemNames.sock, player, 20),
        LocationNames.spat_ps_03: lambda player: lambda state: state.has(ItemNames.sock, player, 30),
        LocationNames.spat_ps_04: lambda player: lambda state: state.has(ItemNames.sock, player, 40),
        LocationNames.spat_ps_05: lambda player: lambda state: state.has(ItemNames.sock, player, 50),
        LocationNames.spat_ps_06: lambda player: lambda state: state.has(ItemNames.sock, player, 60),
        LocationNames.spat_ps_07: lambda player: lambda state: state.has(ItemNames.sock, player, 70),
        LocationNames.spat_ps_08: lambda player: lambda state: state.has(ItemNames.sock, player, 80),
    }
]

skill_rules = [
    # connections
    {
        ConnectionNames.hub2_b2: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player),
        ConnectionNames.cb_b3: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player) and state.has(
            ItemNames.cruise_bubble, player),
        ConnectionNames.bc01_bc02: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player),
        # ToDo: can we backtrack from bc02 without bubble bowl? only relevant when we have warp rando
        # ConnectionNames.bc02_bc01: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player),
        ConnectionNames.bc02_bc03: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player),
        ConnectionNames.bc02_bc05: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player),
        ConnectionNames.kf04_kf05: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
        ConnectionNames.kf04_kf02: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
    },
    # locations
    {
        # ToDo: does cruise bubble even work here?
        LocationNames.spat_hb_02: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player) or state.has(
            ItemNames.cruise_bubble, player),
        LocationNames.spat_hb_03: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
        LocationNames.spat_bb_08: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
        # ToDo: test Cruise Bubble
        LocationNames.spat_bc_03: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player),
        LocationNames.spat_bc_07: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player),
        # ToDo: test Cruise Bubble
        LocationNames.spat_bc_08: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player),
        LocationNames.spat_kf_02: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
        LocationNames.spat_kf_05: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
        LocationNames.spat_kf_06: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
        LocationNames.spat_db_02: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player),
        LocationNames.sock_jf01_06: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player),
        LocationNames.sock_jf03_02: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
        LocationNames.sock_bb04_01: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
        LocationNames.sock_gl03_02: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player) or state.has(
            ItemNames.cruise_bubble, player),
        LocationNames.sock_kf01_03: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player),
        LocationNames.sock_kf04_01: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
        LocationNames.lvl_itm_bc_01: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player),
        LocationNames.lvl_itm_bc_02: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player),
        LocationNames.lvl_itm_bc_03: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player),
        LocationNames.lvl_itm_bc_04: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player),
        LocationNames.lvl_itm_kf1_06: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
        LocationNames.lvl_itm_kf2_01: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
        LocationNames.lvl_itm_kf2_02: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
        LocationNames.lvl_itm_kf2_03: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
        LocationNames.lvl_itm_kf2_04: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
        LocationNames.lvl_itm_kf2_05: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
        LocationNames.lvl_itm_kf2_06: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
        LocationNames.purple_so_bb04_01: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
        LocationNames.purple_so_bc01_01: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player),
        LocationNames.purple_so_bc02_01: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player),
        LocationNames.purple_so_kf04_01: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
    }
]

golden_underwear_rules = [
    # connections
    {},
    # locations
    {}
]

lvl_itm_rules = [
    # connections
    {
        ConnectionNames.gy03_gy04: lambda player: lambda state: state.has(ItemNames.lvl_itm_gy, player, 4),
    },
    # locations
    {
        LocationNames.spat_jf_08: lambda player: lambda state: state.has(ItemNames.lvl_itm_jf, player),
        LocationNames.spat_bb_01: lambda player: lambda state: state.has(ItemNames.lvl_itm_bb, player, 11),
        LocationNames.spat_gl_03: lambda player: lambda state: state.has(ItemNames.lvl_itm_gl, player, 5),
        LocationNames.spat_rb_03: lambda player: lambda state: state.has(ItemNames.lvl_itm_rb, player, 6),
        LocationNames.spat_bc_03: lambda player: lambda state: state.has(ItemNames.lvl_itm_bc, player, 4),
        LocationNames.spat_kf_02: lambda player: lambda state: state.has(ItemNames.lvl_itm_kf1, player, 6),
        LocationNames.spat_kf_06: lambda player: lambda state: state.has(ItemNames.lvl_itm_kf2, player, 6),
        LocationNames.spat_gy_06: lambda player: lambda state: state.has(ItemNames.lvl_itm_gy, player, 4),
        LocationNames.spat_gy_07: lambda player: lambda state: state.has(ItemNames.lvl_itm_gy, player, 4),
        LocationNames.sock_sm03_01: lambda player: lambda state: state.has(ItemNames.lvl_itm_sm, player, 8),
        LocationNames.purple_so_gy03_01: lambda player: lambda state: state.has(ItemNames.lvl_itm_gy, player, 4),
    }
]

so_krabs_rules = [
    # connections
    {},
    # locations
    {
        LocationNames.spat_ks_01: lambda player: lambda state: state.has(ItemNames.so_500, player, 2),
        LocationNames.spat_ks_02: lambda player: lambda state: state.has(ItemNames.so_500, player, 4),
        LocationNames.spat_ks_03: lambda player: lambda state: state.has(ItemNames.so_500, player, 6),
        LocationNames.spat_ks_04: lambda player: lambda state: state.has(ItemNames.so_500, player, 9),
        LocationNames.spat_ks_05: lambda player: lambda state: state.has(ItemNames.so_500, player, 12),
        LocationNames.spat_ks_06: lambda player: lambda state: state.has(ItemNames.so_500, player, 15),
        LocationNames.spat_ks_07: lambda player: lambda state: state.has(ItemNames.so_500, player, 19),
        LocationNames.spat_ks_08: lambda player: lambda state: state.has(ItemNames.so_500, player, 24),
    }
]


def _add_rules(world: MultiWorld, player: int, rules: list[dict[str, Callable[[int], CollectionRule]]]):
    for name, rule_factory in rules[0].items():
        add_rule(world.get_entrance(name, player), rule_factory(player))
    for name, rule_factory in rules[1].items():
        add_rule(world.get_location(name, player), rule_factory(player))


def _set_rules(world: MultiWorld, player: int, rules: list[dict[str, Callable[[int], CollectionRule]]]):
    for name, rule_factory in rules[0].items():
        set_rule(world.get_entrance(name, player), rule_factory(player))
    for name, rule_factory in rules[1].items():
        set_rule(world.get_location(name, player), rule_factory(player))


def set_rules(world: MultiWorld, player: int):
    _add_rules(world, player, spat_rules)
    if world.include_socks[player].value:
        _add_rules(world, player, sock_rules)
    if world.include_skills[player].value:
        _add_rules(world, player, skill_rules)
    if world.include_golden_underwear[player].value:
        _add_rules(world, player, golden_underwear_rules)
    if world.include_level_items[player].value:
        _add_rules(world, player, lvl_itm_rules)
    if world.include_purple_so[player].value:
        _set_rules(world, player, so_krabs_rules)  # we override krabs requirements here

    world.completion_condition[player] = lambda state: state.has("Victory", player)
