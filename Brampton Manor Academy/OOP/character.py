class Character():
    def __init__(self, character_name):
        self.name = character_name
        self.description = None
        self.character_message = None

    def get_name(self):
        return self.name

    def set_name(self, character_name):
        self.name = character_name

    def get_description(self):
        return self.description

    def set_description(self, character_description):
        self.description = character_description

    def get_character_message(self):
        return self.character_message

    def set_character_message(self, character_message):
        self.character_message = character_message

    def display_description(self):
        print(f'{self.name} is in this room - {self.description}')

    def display_message(self):
        print(f'{self.name}: {self.character_message}')