from func.grammar import Grammar, Rule, Terminal, NonTerminal
from typing import Dict, List

def generate_string(grammar: Grammar, ordering: Dict[int, Rule], sequence: List[int]) -> List[Terminal]:
    """
    Generate a list of terminal symbols given a sequence of rule numbers in the grammar.
    Returns None if there is a problem during string generation.
    """
    try:
        generated_string = [grammar.start_symbol]

        for rule_num in sequence:
            non_terminal_pos = -1

            for i, symbol in enumerate(generated_string):
                if isinstance(symbol, NonTerminal):
                    non_terminal_pos = i
                    break

            if non_terminal_pos == -1:
                print(f"Error: No nonterminals found in the string.")
                return None

            rule = ordering[rule_num]
            non_terminal = generated_string[non_terminal_pos]

            if rule.st != non_terminal:
                print(f"Error: Incorrect nonterminal at position {non_terminal_pos}. {non_terminal} != {rule.st}")
                return None

            if rule.en[0] == Terminal("eps"):
                generated_string.pop(non_terminal_pos)
            else:
                generated_string = generated_string[:non_terminal_pos] + list(rule.en) + generated_string[non_terminal_pos + 1:]

        return generated_string

    except Exception as e:
        print("Error generating string due to incompatibility with LLK table!")
        return None
