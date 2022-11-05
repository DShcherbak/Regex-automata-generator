from RegexElement import RegexElement, RegexElemType, create_from_text
from real_NFA import build_NFA
from DFA import *
from transition_table import build_transition_table, print_transition_table

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
            if final not in final_states:
                final_states[final] = set()
            final_states[final].add(letter)
        alphabet.update(nfa_alphabet)
        
    dfa, final_states = determinize((nfa, final_states, list(alphabet)))


    # output automata table
    table = build_transition_table(dfa, final_states)
    print_transition_table(table)

main()