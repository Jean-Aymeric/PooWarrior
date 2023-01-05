from dwarf import Dwarf
from warrior import Warrior
from character import Character

jad = Character("JAD-the-Mighty")
jad.setRace(Dwarf(None))
jad.setJob(Warrior(None))
jad.display()
