from DFA import determinize
from RegexElement import RegexElement, RegexElemType, create_from_text
import NFA
from real_NFA import build_NFA
from transition_table import build_transition_table, print_transition_table

def main():
    # get regex
    regexString = "({xVy}x)V{x}{y}"
    print(regexString)
    regex = create_from_text(regexString)
    

    nfa = build_NFA(regex) 
    dfa = determinize(nfa)


 #   nfa = NFA.compileNFA(regex)
    # output automata table
 #   table = build_transition_table(nfa)
 #   print_transition_table(table)

main()