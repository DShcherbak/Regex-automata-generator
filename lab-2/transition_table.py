from typing import List, Dict
import termtables as tt
from NFA import NFA, State


TransitionTable = Dict[str, Dict[str, str]]

FinalStateForText = "State is final for"

def build_transition_table(dfa, final_states) -> TransitionTable:
    return {state: {**transitions, FinalStateForText : final_states.get(state, "")} for state, transitions in dfa.items()}

def print_transition_table(table: TransitionTable):
    letters = []
    for values in table.values():
        for key in sorted(values.keys()):
            if key not in letters and key is not FinalStateForText:
                letters.append(key)
    letters.append(FinalStateForText)

    rows = []
    for qN, dic in table.items():
        row = [qN]
        for letter in letters:
            if letter in dic.keys():
                row.append(dic[letter])
            else: 
                row.append("")
        rows.append(row)
    
    if None in letters:
        letters.remove(None)
        letters.insert(0, 'e-transition')
    letters.insert(0, '')

    tt.print(rows, header=letters)    
