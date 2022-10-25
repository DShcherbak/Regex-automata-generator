from RegexElement import RegexElement, RegexElemType

def build_NFA(regexTree):
    general_tree = RegexElement(RegexElemType.Letter, '#')
    regexTree = RegexElement(RegexElemType.Conjunction, regexTree, general_tree)
    countFirst(regexTree)
    result = countFollow(regexTree)
    result.append((0, '0', regexTree.First))
    dict = pretty_result(result)
    return dict

def pretty_result(result):
    dict = {}
    result = [(x,y,z) for (x,y,z) in result if x != -1]
    final_states = [x for (x,_,z) in result if (-1) in z]
    alfabet = list(dict.fromkeys([y for (_,y,_) in result if y != '0']))
    for (number, _, _) in result:
        dict[number] = []

    for (number, letter, _) in result:
        for (next_num, _, next_edges) in result:
            for edge in next_edges:
                if(edge == number):
                    dict[next_num].append((letter, number))
                    
    return (dict, final_states, alfabet)


def countFirst(regexTree, number = 1):
    if regexTree.type == RegexElemType.Letter:
        if regexTree.value == '#':
            regexTree.number = -1
        else:
            regexTree.number = number
        regexTree.First = [regexTree.number]
        return number + 1
    
    if regexTree.type == RegexElemType.Iteration:
        num = countFirst(regexTree.value, number)
        regexTree.First = regexTree.value.First + [0]
        return num

    if regexTree.type == RegexElemType.Conjunction:
        num1 = countFirst(regexTree.value, number)
        num2 = countFirst(regexTree.second_value, num1)
        regexTree.First = regexTree.value.First
        if 0 in regexTree.First:
            regexTree.First = [i for i in regexTree.First if i != 0]
            regexTree.First += regexTree.second_value.First
        return num2

    if regexTree.type == RegexElemType.Disjunction:
        num1 = countFirst(regexTree.value, number)
        num2 = countFirst(regexTree.second_value, num1)
        regexTree.First = regexTree.value.First + regexTree.second_value.First
        return num2

def countFollow(regexTree):
    if regexTree.Follow == []:
        regexTree.Follow = [-1]

    if regexTree.type == RegexElemType.Letter:
        return [(regexTree.number, regexTree.value, regexTree.Follow)]
    
    if regexTree.type == RegexElemType.Iteration:
        fw = regexTree.First + regexTree.Follow
        regexTree.value.Follow = [i for i in fw if i != 0]
        return countFollow(regexTree.value)

    if regexTree.type == RegexElemType.Conjunction:
        regexTree.value.Follow = regexTree.second_value.First
        if 0 in regexTree.value.Follow:
            regexTree.value.Follow = [i for i in regexTree.value.Follow if i != 0]
            regexTree.value.First += regexTree.Follow
        regexTree.second_value.Follow = regexTree.Follow
        result = countFollow(regexTree.value)
        result += countFollow(regexTree.second_value)
        return result

    if regexTree.type == RegexElemType.Disjunction:
        regexTree.value.Follow = regexTree.Follow
        regexTree.second_value.Follow = regexTree.Follow
        result = countFollow(regexTree.value)
        result += countFollow(regexTree.second_value)
        return result



    
