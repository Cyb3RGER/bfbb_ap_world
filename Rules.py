import typing
from typing import Dict, List

from BaseClasses import MultiWorld, CollectionState, Entrance
from worlds.generic.Rules import set_rule, add_rule
from . import BfBBOptions
from .constants import ConnectionNames, ItemNames, LocationNames, RegionNames


def can_farm_so(state: CollectionState, player: int) -> bool:
    return not state.multiworld.worlds[player].options.death_link and (
            state.can_reach(RegionNames.gl01, "Region", player) and
            state.has(ItemNames.cruise_bubble, player) or
            state.can_reach(RegionNames.db02, "Region", player)
    )

so_values = {
    ItemNames.so_100: 0,
    ItemNames.so_250: 0,
    ItemNames.so_500: 500,
    ItemNames.so_750: 750,
    ItemNames.so_1000: 1000,
}

def has_so_amount(state: CollectionState, player: int, amount: int):
    return get_so_amount(state, player) >= amount

def get_so_amount(state: CollectionState, player: int):
    if can_farm_so(state, player):
        # ToDo: maybe return some lower number?
        return 999999
    return sum(state.count(item_name, player) * amount for item_name, amount in so_values.items())


spat_rules = [
    # connections
    {
        ConnectionNames.pineapple_hub1: lambda player: lambda state: state.has(ItemNames.spat, player, 1),
        # ConnectionNames.hub1_bb01: lambda player: lambda state: state.has(ItemNames.spat, player, 5),
        # ConnectionNames.hub1_gl01: lambda player: lambda state: state.has(ItemNames.spat, player, 10),
        # ConnectionNames.hub1_b1: lambda player: lambda state: state.has(ItemNames.spat, player, 15),
        # ConnectionNames.hub2_rb01: lambda player: lambda state: state.has(ItemNames.spat, player, 25),
        # ConnectionNames.hub2_sm01: lambda player: lambda state: state.has(ItemNames.spat, player, 30),
        # ConnectionNames.hub2_b2: lambda player: lambda state: state.has(ItemNames.spat, player, 40),
        # ConnectionNames.hub3_kf01: lambda player: lambda state: state.has(ItemNames.spat, player, 50),
        # ConnectionNames.hub3_gy01: lambda player: lambda state: state.has(ItemNames.spat, player, 60),
        # ConnectionNames.cb_b3: lambda player: lambda state: state.has(ItemNames.spat, player, 75),
    },
    # locations
    {
        ItemNames.spat: {
            LocationNames.spat_ks_01: lambda player: lambda state: state.has(ItemNames.spat, player, min(5, state.multiworld.worlds[player].options.required_spatulas.value)),
            LocationNames.spat_ks_02: lambda player: lambda state: state.has(ItemNames.spat, player, min(10, state.multiworld.worlds[player].options.required_spatulas.value)),
            LocationNames.spat_ks_03: lambda player: lambda state: state.has(ItemNames.spat, player, min(15, state.multiworld.worlds[player].options.required_spatulas.value)),
            LocationNames.spat_ks_04: lambda player: lambda state: state.has(ItemNames.spat, player, min(20, state.multiworld.worlds[player].options.required_spatulas.value)),
            LocationNames.spat_ks_05: lambda player: lambda state: state.has(ItemNames.spat, player, min(25, state.multiworld.worlds[player].options.required_spatulas.value)),
            LocationNames.spat_ks_06: lambda player: lambda state: state.has(ItemNames.spat, player, min(30, state.multiworld.worlds[player].options.required_spatulas.value)),
            LocationNames.spat_ks_07: lambda player: lambda state: state.has(ItemNames.spat, player, min(35, state.multiworld.worlds[player].options.required_spatulas.value)),
            LocationNames.spat_ks_08: lambda player: lambda state: state.has(ItemNames.spat, player, min(40, state.multiworld.worlds[player].options.required_spatulas.value)),
        }
    }
]
sock_rules = [
    # connections
    {},
    # locations
    {
        ItemNames.spat: {
            LocationNames.spat_ps_01: lambda player: lambda state: state.has(ItemNames.sock, player, 10),
            LocationNames.spat_ps_02: lambda player: lambda state: state.has(ItemNames.sock, player, 20),
            LocationNames.spat_ps_03: lambda player: lambda state: state.has(ItemNames.sock, player, 30),
            LocationNames.spat_ps_04: lambda player: lambda state: state.has(ItemNames.sock, player, 40),
            LocationNames.spat_ps_05: lambda player: lambda state: state.has(ItemNames.sock, player, 50),
            LocationNames.spat_ps_06: lambda player: lambda state: state.has(ItemNames.sock, player, 60),
            LocationNames.spat_ps_07: lambda player: lambda state: state.has(ItemNames.sock, player, 70),
            LocationNames.spat_ps_08: lambda player: lambda state: state.has(ItemNames.sock, player, 80),
            # ToDo: we need rules for pat spatulas for if socks are disabled
        }
    }
]

skill_rules = [
    # connections
    {
        ConnectionNames.hub2_b2: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player) or state.has(ItemNames.cruise_bubble, player),
        ConnectionNames.cb_b3: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
        ConnectionNames.bc01_bc02: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player),
        ConnectionNames.bc02_bc03: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player),
        ConnectionNames.bc02_bc05: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player),
        ConnectionNames.kf04_kf05: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
        ConnectionNames.kf04_kf02: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
        ConnectionNames.kf01_kf05: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
    },
    # locations
    {
        ItemNames.spat: {
            LocationNames.spat_hb_02: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player) or state.has(ItemNames.cruise_bubble, player),
            LocationNames.spat_hb_03: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
            LocationNames.spat_bb_08: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
            LocationNames.spat_bc_01: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player),
            LocationNames.spat_kf_02: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
            LocationNames.spat_kf_05: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
            LocationNames.spat_kf_06: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
            LocationNames.spat_gy_02: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
            LocationNames.spat_gy_03: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
            LocationNames.spat_db_02: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player),
            LocationNames.spat_b3_02: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player) and state.has(ItemNames.cruise_bubble, player),
        },
        ItemNames.sock: {
            LocationNames.sock_jf01_06: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player) or state.has(ItemNames.cruise_bubble, player),
            LocationNames.sock_jf03_02: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
            LocationNames.sock_bb04_01: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
            LocationNames.sock_bc01_01: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player),
            LocationNames.sock_kf01_03: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player),
            LocationNames.sock_kf04_01: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
        },
        ItemNames.golden_underwear: {
            LocationNames.golden_under_02: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player) or state.has(ItemNames.cruise_bubble, player),
            LocationNames.golden_under_03: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
        },
        ItemNames.lvl_itm: {
            LocationNames.lvl_itm_kf1_01: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
            LocationNames.lvl_itm_kf1_02: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
            LocationNames.lvl_itm_kf1_03: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
            LocationNames.lvl_itm_kf1_06: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
            LocationNames.lvl_itm_kf2_01: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
            LocationNames.lvl_itm_kf2_02: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
            LocationNames.lvl_itm_kf2_03: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
            LocationNames.lvl_itm_kf2_04: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
            LocationNames.lvl_itm_kf2_05: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
            LocationNames.lvl_itm_kf2_06: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
        },
        ItemNames.so_purple: {
            LocationNames.purple_so_bb04_01: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
            LocationNames.purple_so_bc01_01: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player) or state.has(ItemNames.cruise_bubble, player),
            LocationNames.purple_so_bc02_01: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player),
            LocationNames.purple_so_bc02_02: lambda player: lambda state: state.has(ItemNames.bubble_bowl, player),
            LocationNames.purple_so_kf01_01: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
            LocationNames.purple_so_kf04_01: lambda player: lambda state: state.has(ItemNames.cruise_bubble, player),
        }
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
        ConnectionNames.bc02_bc05: lambda player: lambda state: state.has(ItemNames.lvl_itm_bc, player, 4),
        ConnectionNames.gy03_gy04: lambda player: lambda state: state.has(ItemNames.lvl_itm_gy, player, 4),
    },
    # locations
    {
        ItemNames.spat: {
            LocationNames.spat_jf_08: lambda player: lambda state: state.has(ItemNames.lvl_itm_jf, player),
            LocationNames.spat_bb_01: lambda player: lambda state: state.has(ItemNames.lvl_itm_bb, player, 11),
            LocationNames.spat_gl_03: lambda player: lambda state: state.has(ItemNames.lvl_itm_gl, player, 5),
            LocationNames.spat_rb_03: lambda player: lambda state: state.has(ItemNames.lvl_itm_rb, player, 6),
            LocationNames.spat_bc_03: lambda player: lambda state: state.has(ItemNames.lvl_itm_bc, player, 4),
            LocationNames.spat_kf_02: (lambda player: lambda state: state.has(ItemNames.lvl_itm_kf1, player, 6), True),
            LocationNames.spat_kf_06: lambda player: lambda state: state.has(ItemNames.lvl_itm_kf2, player, 6),
            LocationNames.spat_gy_06: lambda player: lambda state: state.has(ItemNames.lvl_itm_gy, player, 4),
            LocationNames.spat_gy_07: lambda player: lambda state: state.has(ItemNames.lvl_itm_gy, player, 4),
        },
        ItemNames.sock: {
            LocationNames.sock_sm03_01: lambda player: lambda state: state.has(ItemNames.lvl_itm_sm, player, 8),
        },
        ItemNames.so_purple: {
            LocationNames.purple_so_gy03_01: lambda player: lambda state: state.has(ItemNames.lvl_itm_gy, player, 4),
        }
    }
]

so_krabs_rules = [
    # connections
    {},
    # locations
    {
        ItemNames.spat: {
            LocationNames.spat_ks_01: lambda player: lambda state: has_so_amount(state, player, 3000 / 2),
            LocationNames.spat_ks_02: lambda player: lambda state: has_so_amount(state, player, 6500 / 2),
            LocationNames.spat_ks_03: lambda player: lambda state: has_so_amount(state, player, 10500 / 2),
            LocationNames.spat_ks_04: lambda player: lambda state: has_so_amount(state, player, 15000 / 2),
            LocationNames.spat_ks_05: lambda player: lambda state: has_so_amount(state, player, 20000 / 2),
            LocationNames.spat_ks_06: lambda player: lambda state: has_so_amount(state, player, 25500 / 2),
            LocationNames.spat_ks_07: lambda player: lambda state: has_so_amount(state, player, 32000 / 2),
            LocationNames.spat_ks_08: lambda player: lambda state: has_so_amount(state, player, 39500 / 2),
        }
    }
]


def _add_rules(world: MultiWorld, player: int, rules: List, allowed_loc_types: List[str]):
    for name, rule_factory in rules[0].items():
        if type(rule_factory) == tuple and len(rule_factory) > 1 and rule_factory[1]:  # force override
            rule_factory = rule_factory[0]
            set_rule(world.get_entrance(name, player), rule_factory(player))
        else:
            add_rule(world.get_entrance(name, player), rule_factory(player))
    for loc_type, type_rules in rules[1].items():
        if loc_type not in allowed_loc_types:
            continue
        for name, rule_factory in type_rules.items():
            if type(rule_factory) == tuple and len(rule_factory) > 1 and rule_factory[1]:  # force override
                rule_factory = rule_factory[0]
                set_rule(world.get_location(name, player), rule_factory(player))
            else:
                add_rule(world.get_location(name, player), rule_factory(player))


def _set_rules(world: MultiWorld, player: int, rules: List, allowed_loc_types: List[str]):
    for name, rule_factory in rules[0].items():
        set_rule(world.get_entrance(name, player), rule_factory(player))
    for loc_type, type_rules in rules[1].items():
        if loc_type not in allowed_loc_types:
            continue
        for name, rule_factory in type_rules.items():
            set_rule(world.get_location(name, player), rule_factory(player))


def reset_gate_rules(old_rules: Dict[Entrance, any]):
    for ent, v in old_rules.items():
        ent.access_rule = v


def set_gate_rules(player: int, gate_costs: Dict[Entrance, int]):
    old_rules = {}
    for ent, v in gate_costs.items():
        old_rules[ent] = ent.access_rule
        add_rule(ent, (lambda val=v: lambda state: state.has(ItemNames.spat, player, val))())
    return old_rules


def set_rules(world: MultiWorld, options: BfBBOptions, player: int, gate_costs: typing.Dict[str, int]):
    allowed_loc_types = [ItemNames.spat]
    if options.include_socks.value:
        allowed_loc_types += [ItemNames.sock]
    # if world.include_skills[player].value:
    #     allowed_loc_types += [ItemNames.skills]
    if options.include_golden_underwear.value:
        allowed_loc_types += [ItemNames.golden_underwear]
    if options.include_level_items.value:
        allowed_loc_types += [ItemNames.lvl_itm]
    if options.include_purple_so.value:
        allowed_loc_types += [ItemNames.so_purple]

    _add_rules(world, player, spat_rules, allowed_loc_types)
    if options.include_socks.value:
        _add_rules(world, player, sock_rules, allowed_loc_types)
    if options.include_skills.value:
        _add_rules(world, player, skill_rules, allowed_loc_types)
    if options.include_golden_underwear.value:
        _add_rules(world, player, golden_underwear_rules, allowed_loc_types)
    if options.include_level_items.value:
        _add_rules(world, player, lvl_itm_rules, allowed_loc_types)
    if options.include_purple_so.value:
        _set_rules(world, player, so_krabs_rules, allowed_loc_types)  # we override krabs requirements here

    set_gate_rules(player, {world.get_entrance(k, player): v for k, v in gate_costs.items()})

    world.completion_condition[player] = lambda state: state.has("Victory", player)
