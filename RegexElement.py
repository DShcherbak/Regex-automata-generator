from enum import Enum

class EnumRegexElemType(Enum):
    Letter = 0
    Range = 1
    NotRange = 2
    AnySymbol = 3
    Plus = 4
    Star = 5
    Question = 6
    ExactlyN = 7
    MoreThanN = 8
    FromNtoM = 9
    GreedyPlus = 10
    GreedyStar = 11
    GreedyQuestion = 12
    GreedyMoreThanN = 13
    GreedyFromNtoM = 14



class RegexElement:
    def __init__(self, type, value):
        self.type = type 
        self.value = value 

    def CreateFromText(text):
        
   