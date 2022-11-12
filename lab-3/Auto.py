class Auto:
    def __init__(self, A, X, A0, f, F):
        self.A = A 
        self.X = X
        self.A0 = A0 
        self.f = f 
        self.F = F

    # A  - множина станів авотмата
    # X  - вхідний алфавіт
    # a0 - стартова вершина 
    # f  - функція переходів (f[Ai][Xi] = Aj)
    # F  - множина фінальних станів

    def Product(self, auto2):
        C = set()
        f = set()
        F = set()
        c0 = (self.A0, auto2.A0)
        W = set([(self.A0, auto2.A0)])
        while len(W) > 0:
            (a1, b1) = W.pop()
            C.add((a1, b1))
            if a1 in self.F and b1 in auto2.F:
                F.add((a1,b1))
            for (from_a, (leta1,letb1), to_a) in self.f:
                for (from_b, (leta2, letb2) , to_b) in auto2.f:
                    if(letb1 == leta2):
                        f.add(((from_a, from_b), (leta1, letb2), (to_a, to_b)))
                        if (to_a, to_b) not in C:
                            W.add((to_a, to_b))
        result = Auto(C, self.X, c0, f, F)
        return result


    def AddClosure(self, finalSymbol):
        F1 = set()
        W = self.F
        while len(W) > 0:
            a = W.pop()
            F1.add(a)
            for (_, symbol, to) in self.f:
                if symbol == finalSymbol and to not in F1:
                    W.add(to)
        
        self.F = F1

