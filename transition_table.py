from typing import List, Dict
import termtables as tt
from NFA import NFA, State


TransitionTable = Dict[str, Dict[str, str]]

def build_transition_table(dfa, final_states: List[int]) -> TransitionTable:
    return {f"[{state}]" if state in final_states else state: transitions for state, transitions in dfa.items()}

def print_transition_table(table: TransitionTable):
    letters = []
    for values in table.values():
        for key in values.keys():
            if key not in letters:
                letters.append(key)

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

