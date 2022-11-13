from Auto import Auto
from transition_table import print_transition_table

def print_automata_info(name: str, automata):
    print("-------------------------------------\n")
    print(f"Automata {name}\n")
    print(f"States: {automata.A}")
    print(f"Alphabet: {automata.X}")
    print(f"Start state: {automata.A0}")
    print(f"Final states: {automata.F}")
    print(f"Transitions: ")
    print_transition_table(automata.f, automata.F)
    print("")


def main():
    A = set([0,1,2])
    X = set(['0', '1'])
    a0 = 0
    f = set([(0, ('0', '1'), 2), 
        (0, ('1', '0'), 1),
        (1, ('0', '0'), 0),
        (1, ('1', '1'), 1),
        (2, ('1', '1'), 0),
        (2, ('0', '0'), 2)])
    F = set([2])

    auto1 = Auto(A, X, a0, f, F)
    print_automata_info("f(x) = 3x + 1", auto1)

    auto3 = auto1.Product(auto1)
    print_automata_info("(f(x) = 3x + 1) x (f(x) = 3x + 1)", auto3)

    A2 = set([0,1])
    f_inc = set([(0, ('1','0'), 0),(0, ('0','1'), 1),(1, ('1','1'), 1),(1, ('0','0'), 1)])
    f_x2 = set([(0, ('0','0'), 0),(0, ('1','0'), 1),(1, ('1','1'), 1),(1, ('0','1'), 0)])
    F_inc = set([1])
    F_x2 = set([0])

    auto_inc = Auto(A2, X, 0, f_inc, F_inc) 
    print_automata_info("f(x) = x + 1", auto_inc)

    auto_x2 = Auto(A2, X, 0, f_x2, F_x2)
    print_automata_info("f(x) = 2x", auto_x2)

    auto_ex = auto_x2.Product(auto_inc) 
    print_automata_info("((f(x) = 2x) x (f(x) = x + 1))", auto_ex)

    auto_ex = auto_inc.Product(auto_x2) 
    print_automata_info("(f(x) = x + 1) x (f(x) = 2x)", auto_ex)

    auto_ex = auto1.Product(auto_x2) 
    print_automata_info("(f(x) = 3x + 1) x (f(x) = 2x)", auto_ex)
      
main()
