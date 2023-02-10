from room import Room
from item import Item
from character import Character

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

book = Item("Book")
book.set_description("A big fat book")
dining_hall.set_item(book)

wand = Item("Magic Wand")
wand.set_description("Cast your spells with this magical wand")
ballroom.set_item(book)
current_room = kitchen

johnny = Character("Johnny")
johnny.set_description("A skinny, maniacal psychopath")
johnny.set_character_message("There's no point to life...")

kitchen.set_character(johnny)

while True:
    print("\n")
    current_room.display_room()
    item = current_room.get_item()
    character = current_room.get_character()
    if item is not None:
        item.display_item()
    if character is not None:
        character.display_description()
        choice = input(f"\nDo you wish to speak to {character.get_name()}? ")
        if choice == "yes":
            character.display_message()

    command = input("\nEnter direction: ")
    current_room = current_room.move(command)

