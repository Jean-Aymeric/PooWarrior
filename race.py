from abc import ABC
from character import Character
from namedelement import NamedElement


class Race(ABC, NamedElement):
    __character: Character

    def __init__(self, name: str, character: Character):
        NamedElement.__init__(self, name)
        self.__character = character

    def getCharacter(self) -> Character:
        return self.__character

    def setCharacter(self, character) -> None:
        self.__character = character
