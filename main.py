from RegexElement import RegexElement, RegexElemType
import NFA
from transition_table import build_transition_table, print_transition_table

def main():
    # get regex

    # regex to enum list
   
    regex = [RegexElement(RegexElemType.Letter, "a"), 
            RegexElement(RegexElemType.Letter, "b"), 
            RegexElement(RegexElemType.Disjunction),
            RegexElement(RegexElemType.Star)]

    # build automata

    nfa = NFA.compileNFA(regex)
    # output automata table
    table = build_transition_table(nfa)
    print_transition_table(table)

main()