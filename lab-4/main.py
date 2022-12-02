from AutoOnTree import *

if __name__ == "__main__":
    print("Lab 4")
    a = set([1,2,3])
    print(allCombinations(a,2))

    A = set([0,1,2])
    X = set([('g', 1), ('c', 0)])
    L = [{'c': {(): 0}}, {'g': {(1,): 0, (0,): 1, (2,): 0}}]
    F = set([0])
    auto = Auto(A, X, L, F)
    auto.Reduce()

    A = set([0,1,2,3,4])
    X = set([('f', 2), ('g', 1), ('c', 0)])
    L = [{'c': {(): 0}}, {'g': {(0,): 1, (3,): 4, (1,): 1}}, {'f': {(0,2): 3, (0,0): 1, (0,1): 4}}]
    F = set([2,4])
    auto = Auto(A, X, L, F)
    auto.Reduce()

    A = set([0,1,2,3,4])
    X = set([('f', 2), ('g', 1), ('c', 0)])
    L = [{'c': {(): 0}}, {'g': {(0,): 1, (3,): 4, (1,): 1}}, {'f': {(0,2): 3, (0,0): 1, (0,1): 4}}]
    F = set([2,4])
    auto = Auto(A, X, L, F)
    auto.Reduce()

    A = set([0,1,2,3,4])
    X = set([('f', 2), ('g', 1), ('c', 0)])
    L = [{'c': {(): 0}}, {'g': {(0,): 1, (3,): 4, (1,): 1}}, {'f': {(0,2): 3, (0,0): 1, (0,1): 4}}]
    F = set([2,4])
    auto = Auto(A, X, L, F)
    auto.Reduce()



