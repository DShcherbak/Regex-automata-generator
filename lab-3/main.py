from Auto import Auto

def main():
    print("Lab 3")

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

    auto3 = auto1.Product(auto1)

    print(auto3.A)
    print(auto3.X)
    print(auto3.A0)
    print(auto3.f)
    print(auto3.F)
    print("---------------------------")

    A2 = set[0,1]
    f_inc = set([(0, ('1','0'), 0),(0, ('0','1'), 1),(1, ('1','1'), 1),(1, ('0','0'), 1)])
    f_x2 = set([(0, ('0','0'), 0),(0, ('1','0'), 1),(1, ('1','1'), 1),(1, ('0','1'), 0)])
    F_inc = set([1])
    F_x2 = set([0])

    auto_inc = Auto(A2, X, 0, f_inc, F_inc) 
    auto_x2 = Auto(A2, X, 0, f_x2, F_x2)

    auto_ex = auto_x2.Product(auto_inc) 

    print(auto_ex.A)
    print(auto_ex.X)
    print(auto_ex.A0)
    print(auto_ex.f)
    print(auto_ex.F)
    print("---------------------------")

    auto_ex = auto_inc.Product(auto_x2) 

    print(auto_ex.A)
    print(auto_ex.X)
    print(auto_ex.A0)
    print(auto_ex.f)
    print(auto_ex.F)
    print("---------------------------")

    auto_ex = auto1.Product(auto_x2) 

    print(auto_ex.A)
    print(auto_ex.X)
    print(auto_ex.A0)
    print(auto_ex.f)
    print(auto_ex.F)
    print("---------------------------")
      
main()
