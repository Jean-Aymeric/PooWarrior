from character import Character
from race import Race


class Dwarf(Race):
    def __init__(self, character: Character):
        Race.__init__(self, "Nain", character)
