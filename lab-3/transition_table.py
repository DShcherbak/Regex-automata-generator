import termtables as tt


def print_transition_table(table, final_states):
    header = ["From state", "Input", "Output", "To state"]
    rows = []
    for (from_, (input, output), to) in sorted(table, key=lambda a: a[0]):
        row = []
        if from_ in final_states:
            row.append(f"{str(from_)} F");
        else:
            row.append(str(from_))
        row.append(input)
        row.append(output)
        if to in final_states:
            row.append(f"{str(to)} F");
        else:
            row.append(str(to))
        rows.append(row)
    tt.print(rows, header=header)
