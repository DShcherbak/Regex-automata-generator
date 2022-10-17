from enum import Enum, auto

class RegexElemType(Enum):
    Letter = auto()
    Disjunction = auto()
    Conjunction = auto()
    Star = auto()

class RegexElement:
    def __init__(self, type, value = None):
        self.type = type 
        self.value = value 

    def CreateFromText(text):
       pass 
   