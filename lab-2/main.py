from Mili import Mili_from_Mur
from RegexElement import RegexElement, RegexElemType, create_from_text
from real_NFA import build_NFA
from DFA import *
from transition_table import build_transition_table, print_transition_table
from print_output_function import print_output_function

def main():
    # get regex
    regexStrings = {'R':"a({a}V{b})", 'S':"abab", 'T': "abb"}
    # regex to enum 
    
    nfa = {}
    final_states = {}
    alphabet = set()
    for letter in regexStrings :
        regexTree = create_from_text(regexStrings[letter])
        (cur_nfa, nfa_final_states, nfa_alphabet) = build_NFA(regexTree) 
        for vertex in cur_nfa: 
            if vertex not in nfa:
                nfa[vertex] = cur_nfa[vertex]
            else:
                nfa[vertex].extend(cur_nfa[vertex])
        for final in nfa_final_states:
            final_states[final] = letter
        alphabet.update(nfa_alphabet)
        
    dfa, final_states = determinize((nfa, final_states, list(alphabet)))

    # output automata table
    table = build_transition_table(dfa, final_states)
    print("Mur's table:")
    print_transition_table(table)

    output_function = Mili_from_Mur(dfa, final_states)
    print("Output function (Mili): ")
    print_output_function(output_function)

main()