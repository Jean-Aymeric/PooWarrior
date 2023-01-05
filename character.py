from namedelement import NamedElement


class Character(NamedElement):
    def __init__(self, name):
        NamedElement.__init__(self, name)
        self.__race = None
        self.__job = None

    def getRace(self):
        return self.__race

    def setRace(self, race):
        self.__race = race
        self.__race.setCharacter(self)

    def getJob(self):
        return self.__job

    def setJob(self, job):
        self.__job = job
        self.__job.setCharacter(self)

    def display(self) -> None:
        print(self.getName(), self.getRace().getName(), self.getJob().getName())
