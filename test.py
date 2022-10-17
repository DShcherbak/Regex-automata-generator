import unittest

import NFA
from RegexElement import create_from_text
from transition_table import build_transition_table



class MyTestCase(unittest.TestCase):

    def test_1(self):
        table = self.build_transition_table_from_refex("abVba{a}")
        self.assertEqual(table, {'q0': {None: {'q1', 'q5'}}, 'q1': {'a': {'q2'}}, 'q2': {None: {'q3'}}, 'q3': {'b': {'q4'}}, 'q4': {None: {'F'}}, 'F': {}, 'q5': {'b': {'q6'}}, 'q6': {None: {'q7'}}, 'q7': {'a': {'q8'}}, 'q8': {None: {'q9'}}, 'q9': {None: {'q12', 'q10'}}, 'q10': {'a': {'q11'}}, 'q11': {None: {'q12', 'q10'}}, 'q12': {None: {'F'}}})

    def test_2(self):
        table = self.build_transition_table_from_refex("aVb{aVb}")
        self.assertEqual(table, {'q0': {None: {'q1', 'q3'}}, 'q1': {'a': {'q2'}}, 'q2': {None: {'F'}}, 'F': {}, 'q3': {'b': {'q4'}}, 'q4': {None: {'q5'}}, 'q5': {None: {'q10', 'q6'}}, 'q6': {None: {'q11', 'q7'}}, 'q7': {'a': {'q8'}}, 'q8': {None: {'q9'}}, 'q9': {None: {'q10', 'q6'}}, 'q10': {None: {'F'}}, 'q11': {'b': {'q12'}}, 'q12': {None: {'q9'}}})

    def test_3(self):
        table = self.build_transition_table_from_refex("{aVb}")
        self.assertEqual(table, {'q0': {None: {'q1', 'F'}}, 'q1': {None: {'q2', 'q5'}}, 'q2': {'a': {'q3'}}, 'q3': {None: {'q4'}}, 'q4': {None: {'q1', 'F'}}, 'F': {}, 'q5': {'b': {'q6'}}, 'q6': {None: {'q4'}}})

    def test_4(self):
        table = self.build_transition_table_from_refex("(a{ba})V(b{ab})V{ab}V{ba}")
        self.assertEqual(table, {'q0': {None: {'q1', 'q9'}}, 'q1': {'a': {'q2'}}, 'q2': {None: {'q3'}}, 'q3': {None: {'q8', 'q4'}}, 'q4': {'b': {'q5'}}, 'q5': {None: {'q6'}}, 'q6': {'a': {'q7'}}, 'q7': {None: {'q8', 'q4'}}, 'q8': {None: {'F'}}, 'F': {}, 'q9': {None: {'q10', 'q19'}}, 'q10': {'b': {'q11'}}, 'q11': {None: {'q12'}}, 'q12': {None: {'q13', 'q17'}}, 'q13': {'a': {'q14'}}, 'q14': {None: {'q15'}}, 'q15': {'b': {'q16'}}, 'q16': {None: {'q13', 'q17'}}, 'q17': {None: {'q18'}}, 'q18': {None: {'F'}}, 'q19': {None: {'q27', 'q20'}}, 'q20': {None: {'q21', 'q25'}}, 'q21': {'a': {'q22'}}, 'q22': {None: {'q23'}}, 'q23': {'b': {'q24'}}, 'q24': {None: {'q21', 'q25'}}, 'q25': {None: {'q26'}}, 'q26': {None: {'q18'}}, 'q27': {None: {'q28', 'q32'}}, 'q28': {'b': {'q29'}}, 'q29': {None: {'q30'}}, 'q30': {'a': {'q31'}}, 'q31': {None: {'q28', 'q32'}}, 'q32': {None: {'q26'}}})

    def build_transition_table_from_refex(self, regex_string):
        regex = create_from_text(regex_string)
        nfa = NFA.compileNFA(regex)
        table = build_transition_table(nfa)
        return table


if __name__ == '__main__':
    unittest.main()
