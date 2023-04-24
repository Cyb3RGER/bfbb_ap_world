from BaseClasses import ItemClassification
from .Items import BfBBItem


def create_events(world, player):
    # ToDo: skill rando
    # world.get_location("Bubble Bowl", player).place_locked_item(world.create_item("Bubble Bowl", player))
    # world.get_location("Cruise Bubble", player).place_locked_item(world.create_item("Cruise Bubble", player))

    world.get_location("Robo-Sandy", player).place_locked_item(world.create_item("Defeated Robo-Sandy", player))
    world.get_location("Robo-Patrick", player).place_locked_item(world.create_item("Defeated Robo-Patrick", player))
    world.get_location("Credits", player).place_locked_item(world.create_item("Victory", player))
