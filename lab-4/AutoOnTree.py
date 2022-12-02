from functools import lru_cache

class Auto:
    def __init__(self, A, X, L, F):
        self.A = A 
        self.X = X
        self.L = L 
        self.F = F

    # A  - множина станів авотмата
    # X  - алфавіт термів
    # L  - функція переходів (L[n][Xi][(Ai1, Ai2, ... Ain)] = Aj)
    # F  - множина фінальних станів

    def Reduce(self):
        Marked = set()
        isNewElementFound = True
        while True:
            isNewElementFound = False 
            Marked2 = Marked.copy()
            for i in range(len(self.L)):
                funcs = self.L[i]
                for func_name in [f for (f,arity) in self.X if arity == i]:
                    f = funcs[func_name]
                    for arguments in allCombinations(Marked, i):
                        if arguments in f:
                            res = f[arguments]
                            Marked2.add(res)
            if len(Marked) == len(Marked2):
                break
            Marked = Marked2
        self.A = Marked
        self.F = Marked.intersection(self.F)
        self.L = self.filterFunctions(Marked)
        print(self.A)
        print(self.F)
        print(self.L)

    def filterFunctions(self, Marked):
        result = []
        for i in range(len(self.L)):
            arity_result = {}
            funcs = self.L[i]
            for func_name in [f for (f,arity) in self.X if arity == i]:
                f = funcs[func_name]
                new_f = {}
                for tuple in allCombinations(Marked, i):
                    if tuple in f and f[tuple] in Marked:
                        new_f[tuple] = f[tuple]
                if len(new_f) > 0:
                    arity_result[func_name] = new_f
            result.append(arity_result)
        return result


def allCombinations(Marked, i):
    if i <= 0:
        return [()]
    previous_combinations = allCombinations(Marked, i-1)
    result = []
    for elem in Marked:
        for tuple in previous_combinations:
            result.append((*tuple, elem))
    return result






