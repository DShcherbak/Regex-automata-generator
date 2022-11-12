import termtables as tt

def print_output_function(func):
    sorted_func = {state: dict(sorted(mapping.items())) for state, mapping in func.items()}
    rows = [[state] + list(mapping.values()) for state, mapping in sorted_func.items()]
    tt.print(rows, header=[''] + list(sorted_func[0].keys()))    