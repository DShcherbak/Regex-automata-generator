from DFA import determinize
from RegexElement import RegexElement, RegexElemType, create_from_text
import NFA
from real_NFA import build_NFA
from transition_table import build_transition_table, print_transition_table

def main():
    # get regex
    regexString = "(abcVcba)"
    regex = create_from_text(regexString)
    
    nfa = build_NFA(regex) 
    dfa, final_states = determinize(nfa)

    table = build_transition_table(dfa, final_states)
    print_transition_table(table)

main()