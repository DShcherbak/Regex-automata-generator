from enum import Enum, auto
from logging.config import fileConfig

class RegexElemType(Enum):
    Letter = auto()
    Disjunction = auto()
    Conjunction = auto()
    Iteration = auto()

class RegexElement:
    def __init__(self, type, value = None, second_value = None):
        self.type = type 
        self.value = value
        self.second_value = second_value
        self.First = []
        self.Follow = []
        self.number = -1

    def __str__(self):
        return self.value.__str__()

def define_type(symbol):
    if symbol == '*':
        return RegexElemType.Conjunction
    if symbol == 'V':
        return RegexElemType.Disjunction
    if symbol == '@':
        return RegexElemType.Iteration
    return RegexElemType.Letter

def from_symbol(symbol):
    derived_type = define_type(symbol)
    return RegexElement(derived_type, symbol)

def preprocess(text):
    new_text = ""
    for i in range(len(text)-1):
        new_text += text[i]
        if(text[i] not in ['*', 'V', '(', '{'] and text[i+1] not in ['*', 'V', ')', '}']):
            new_text += '*'
    new_text += text[-1]
    return new_text

def inverse_polish(text):
    stack = []
    result = []
    for symbol in text:
        if symbol not in ['*', 'V', '(', ')', '{', '}']:
            result.append(from_symbol(symbol))
        elif symbol == '*' or symbol == '(' or symbol == '{':
            stack.append(symbol)
        elif symbol == 'V':
            while len(stack) > 0 and stack[-1] == '*':
                result.append(from_symbol(stack.pop()))
            stack.append(symbol)
        elif symbol == ')':
            while(len(stack) > 0 and stack[-1] != '('):
                result.append(from_symbol(stack.pop()))
            stack.pop()
        elif symbol == '}':
            while(len(stack) > 0 and stack[-1] != '{'):
                result.append(from_symbol(stack.pop()))
            stack.pop()
            result.append(from_symbol('@'))
    while(len(stack) > 0):
        result.append(from_symbol(stack.pop()))
    return result
                

def apply(polish):
    if len(polish) == 0:
        return (None, polish) 
    if polish[0].type == RegexElemType.Letter:
        return (polish[0], polish[1:])
    if polish[0].type == RegexElemType.Iteration:
        (inner, rest) = apply(polish[1:]) 
        return (RegexElement(RegexElemType.Iteration, inner), rest)

    (first_operand, rest) = apply(polish[1:])
    (second_operand, rest) = apply(rest)
    return (RegexElement(polish[0].type, second_operand, first_operand), rest)
        
     
    

def create_from_text(text):
    text = preprocess(text)
    polish = inverse_polish(text)
    for elem in polish:
        print(elem.value, end='')
    print()
    polish.reverse()
    regexElem, _ = apply(polish)
    print(regexElem.value)
    return regexElem