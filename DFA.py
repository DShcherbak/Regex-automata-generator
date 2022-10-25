from RegexElement import RegexElement, RegexElemType

class Set:
    def __init__(self):
        self._value = []

    def append(self, value):
        if value not in self._value:
            self._value.append(value)

    def remove(self, value):
        if value in self._value:
            self._value = [i for i in self._value if i != value]

    def contains(self, value):
        return value in self._value

    def to_tuple(self):
        self._value.sort()
        return tuple(self._value)

    def is_empty(self):
        return self._value == []
    


array_to_number = {}
dfa = {}
_alfabet = []


def determinize(nfa_tuple):
    global array_to_number, dfa, _alfabet
    (nfa, final_states, alfabet) = nfa_tuple
    _alfabet = alfabet

    array_to_number = {}
    array_to_number[(0,)] = 0

    dfa = {}
    dfa[0] = {}

    current_vertice = Set()
    current_vertice.append(0)

    determinize_dfs(current_vertice, nfa)

    print("RESULT::::::::")
    print(dfa)

def determinize_dfs(current_vertice, nfa):
    cur_vert_num = array_to_number[current_vertice.to_tuple()]
    for letter in _alfabet:
        next_vertice = Set()
        for key in nfa:
            if current_vertice.contains(key):
                for (next_letter, next_vert) in nfa[key]:
                    if letter == next_letter:
                        next_vertice.append(next_vert)
        next_vertice_tuple = next_vertice.to_tuple()
        print(current_vertice.to_tuple(), "---", letter, "--->", next_vertice_tuple)
        if not next_vertice_tuple in array_to_number:
            array_to_number[next_vertice_tuple] = len(array_to_number)
            dfa[len(array_to_number)-1] = {}
            dfa[cur_vert_num][letter] = len(array_to_number)-1
            determinize_dfs(next_vertice, nfa)
        else:
            dfa[cur_vert_num][letter] = array_to_number[next_vertice_tuple]  




