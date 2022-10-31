from dataclasses import dataclass
from typing import List, Any, Dict, Set, ClassVar
from RegexElement import RegexElement, RegexElemType

@dataclass
class Transition:
    label: str
    to: Any

@dataclass
class State: 
    transitions: Set[Transition]
    object_id: int
    object_id_counter: ClassVar[int] = 0

    def __init__(self) -> None:
        self.transitions = ()
        self.object_id = State.object_id_counter
        State.object_id_counter += 1

    def __hash__(self):
        return hash(self.object_id)

@dataclass
class NFA:
    initial: State = None
    accept: State = None

'''Builds NFA. Accepts list of elements in inverse notation'''

def compileNFA(regex: List[RegexElement]) -> NFA:
    nfaStack: List[State] = []

    for elem in regex: 
        if elem.type == RegexElemType.Iteration:
            nfa1 = nfaStack.pop() 

            initial = State()
            accept = State()

            initial.transitions = (Transition(label=None, to=nfa1.initial), Transition(label=None, to=accept))
            nfa1.accept.transitions = (Transition(label=None, to=nfa1.initial), Transition(label=None, to=accept))

            nfaStack.append(NFA(initial, accept))
        elif elem.type == RegexElemType.Disjunction:

            nfa2 = nfaStack.pop() 
            nfa1 = nfaStack.pop()

            initial = State()

            initial.transitions = (Transition(label=None, to=nfa1.initial), Transition(label=None, to=nfa2.initial))

            accept = State()
            nfa1.accept.transitions = (Transition(label=None, to=accept), )
            nfa2.accept.transitions = (Transition(label=None, to=accept), )

            nfaStack.append(NFA(initial, accept))
        elif elem.type == RegexElemType.Conjunction:
            nfa2 = nfaStack.pop() 
            nfa1 = nfaStack.pop()

            nfa1.accept.transitions = (Transition(label=None, to=nfa2.initial), )
            nfaStack.append(NFA(initial=nfa1.initial, accept=nfa2.accept))
        elif elem.type == RegexElemType.Letter:
            accept = State()
            initial = State()

            initial.transitions = (Transition(label=elem.value, to=accept), )
            nfaStack.append(NFA(initial, accept))
    
    return nfaStack.pop()