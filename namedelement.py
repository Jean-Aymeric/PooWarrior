class NamedElement:
    __name: str

    def __init__(self, name: str):
        self.__name = name

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str) -> None:
        self.__name = name
