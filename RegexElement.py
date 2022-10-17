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

    def __init__(self, value):
        self.value = value
        self.type = self.define_type(value)

    def __str__(self):
        return self.value.__str__()

    def define_type(self, symbol):
        if symbol == '*':
            return RegexElemType.Conjunction
        if symbol == 'V':
            return RegexElemType.Disjunction
        if symbol == '@':
            return RegexElemType.Iteration
        return RegexElemType.Letter

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
            result.append(RegexElement(symbol))
        elif symbol == '*' or symbol == '(' or symbol == '{':
            stack.append(symbol)
        elif symbol == 'V':
            while len(stack) > 0 and stack[-1] == '*':
                result.append(RegexElement(stack.pop()))
            stack.append(symbol)
        elif symbol == ')':
            while(len(stack) > 0 and stack[-1] != '('):
                result.append(RegexElement(stack.pop()))
            stack.pop()
        elif symbol == '}':
            while(len(stack) > 0 and stack[-1] != '{'):
                result.append(RegexElement(stack.pop()))
            stack.pop()
            result.append(RegexElement('@'))
    while(len(stack) > 0):
        result.append(RegexElement(stack.pop()))
    print(result)
    return result
                

def apply(polish):
    if len(polish) == 0:
        return (None, polish) 
    if polish[0] not in ['*', 'V', '@']:
        return (RegexElement(RegexElemType.Letter, polish[0]), polish[1:])
    if polish[0] == '@':
        (inner, rest) = apply(polish[1:]) 
        return (RegexElement(RegexElemType.Iteration, inner), rest)

    operation_type = RegexElemType.Conjunction if polish[i] == '*'  else RegexElemType.Disjunction
    (first_operand, rest) = apply(polish[1:])
    (second_operand, rest) = apply(rest[1:])
    return (RegexElemType(operation_type, first_operand, second_operand), rest)
        
     
    

def create_from_text(text):
    text = preprocess(text)
    polish = inverse_polish(text)
    print(polish)
    # regexElem, _ = apply(polish)
    return polish