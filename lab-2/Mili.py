def Mili_from_Mur(dfa, final_states):
    output_function = {}
    for vert in dfa:
        output_function[vert] = {}
        for letter in dfa[vert]:
            if dfa[vert][letter] in final_states:
                output_function[vert][letter] = final_states[dfa[vert][letter]]
            else:
                output_function[vert][letter] = '-'
    return output_function