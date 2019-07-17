# Consider using isort
import sys
import argparse


# PEP8 says two newlines between top-level functions. Consider using flake8 (or similar)

def main():  # If using strict mypy, this should be `-> None`
    parser = argparse.ArgumentParser("Calculate with numbers")
    parser.add_argument("operand", type=str)  # The type argument can be any callable. It's pretty neat
    parser.add_argument("x", type=int)
    parser.add_argument("y", type=int)

    args = parser.parse_args()

    operand: str = args.operand.lower()  # (Not python related) this should be operator. x and y are the operands :)
    x = args.x
    y = args.y

    try:
        result = _evaluate(operand, x, y)  # If you wanted to be fancy, you could return a function and call it here
    except ValueError as error:
        result = f'Error: {error}'

    print(result)

def _evaluate(operand: str, x: int, y: int) -> int:
    if operand == "add":
        # You _could_ use https://docs.python.org/3/library/operator.html#operator.add
        return add(x, y)
    elif operand == "subtract":
        return subtract(x, y)
    else:
        raise ValueError("Unsupported operand!")

    # An alternative implementation could be something like:
    """
    functions = {
        "add": add,
        "subtract": subtract,
    }
    try:
        functions[operand](x, y)
    except KeyError:
        # It's important to catch Exception! If you don't, CTRL+C won't do anything (it has a different base class) :)
        raise ValueError("Unsupported operand!")
    """

def add(x: int, y: int) -> int:
    return x + y

def subtract(x: int, y: int) -> int:
    return x - y

if __name__ == "__main__":
    main()
