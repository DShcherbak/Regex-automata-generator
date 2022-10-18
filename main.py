from RegexElement import RegexElement, RegexElemType, create_from_text
import NFA
from transition_table import build_transition_table, print_transition_table

def main():
    # get regex
    regexString = "abVba{a}"
    print(regexString)
    regex = create_from_text(regexString)
    # regex to enum list
   

    # regex = [RegexElement("a"), RegexElement("b"), RegexElement('V')]

    # build automata

    nfa = NFA.compileNFA(regex)
    # output automata table
    table = build_transition_table(nfa)
    print_transition_table(table)

main()