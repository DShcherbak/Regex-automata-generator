from typing import List, Any, Dict, Set
import termtables as tt
from NFA import NFA, State


TransitionTable = Dict[str, Dict[str, Set[str]]]

def build_transition_table(nfa: NFA) -> TransitionTable:
    table: TransitionTable = {}
    state_to_index = {nfa.accept : "F"}
    counter = 0

    def index_of_state(state: State):
        if state in state_to_index.keys():
            return state_to_index[state]
        nonlocal counter
        text = "q{}".format(counter)
        state_to_index[state] = text
        counter += 1
        return text
    
    def traverse(state: State):
        index = index_of_state(state)
        if index in table.keys():
            return
        table.update({index: {t.label: set() for t in state.transitions}})
        for t in state.transitions:
            table[index][t.label].add(index_of_state(t.to))
            traverse(t.to)

    traverse(nfa.initial)
    return table

def print_transition_table(table: TransitionTable):
    letters = set()
    for values in table.values():
        letters |= {k for k in values.keys()}
    letters = list(letters)

    rows = []
    for qN, dic in table.items():
        row = [qN]
        for letter in letters:
            if letter in dic.keys():
                row.append(", ".join(dic[letter]))
            else: 
                row.append("")
        rows.append(row)
    
    if None in letters:
        letters.remove(None)
        letters.insert(0, 'e-transition')
    letters.insert(0, '')

    tt.print(rows, header=letters)    

