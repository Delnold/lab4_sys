from func.grammar import Grammar
from func.follow_first import FOLLOW_FIRST
from func.llk import buildLLKTable, LLKParser
from func.grammarGenerator import generate_string

def display_first_k_sets(grammar, k):
    print("First K")
    first = FOLLOW_FIRST.firstK(grammar, k)
    for key, val in first.items():
        print(key, val)

def display_follow_k_sets(grammar, k):
    print("-----------------------")
    print("Follow K")
    follow = FOLLOW_FIRST.followK(grammar, k)
    for key, val in follow.items():
        print(key, val)

def build_and_display_llk_table(grammar, k):
    print("--------------------")
    print("LLK table")
    out = buildLLKTable(grammar, k)
    if out:
        table, ordering = out
        for key, val in table.items():
            print(key, val)
        print("-----------------------")
        print("Rules")
        for key, val in ordering.items():
            print(key, val)
        print("-----------------------")
        return table, ordering
    else:
        print(out)
        return None, None

def parse_input_string(grammar, table, ordering, k, input_string):
    print("Input string")
    print(input_string)
    print("-----------------------")
    print("LLk parser")
    sequence = LLKParser(input_string, grammar, table, ordering, k)
    print(sequence)
    return sequence

def generate_and_display_result(grammar, ordering, sequence):
    print("-------------------------")
    print("String result")
    generated_string = generate_string(grammar, ordering, sequence)
    print(generated_string)

if __name__ == "__main__":
    # Read the grammar from a file
    grammar = Grammar.read(open("./grammar.txt", "r"))

    # Set the value of k
    k = 1

    display_first_k_sets(grammar, k)
    display_follow_k_sets(grammar, k)

    table, ordering = build_and_display_llk_table(grammar, k)

    if table is not None:
        input_string = "i+i"
        sequence = parse_input_string(grammar, table, ordering, k, input_string)
        generate_and_display_result(grammar, ordering, sequence)
