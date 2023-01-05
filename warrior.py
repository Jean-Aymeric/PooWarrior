from job import Job
from character import Character


class Warrior(Job):
    def __init__(self, character: Character):
        Job.__init__(self, "Guerrier", character)
        