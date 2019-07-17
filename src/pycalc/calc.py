import sys
import argparse

def main():
    parser = argparse.ArgumentParser("Calculate with numbers")
    parser.add_argument("operand", type=str)
    parser.add_argument("x", type=int)
    parser.add_argument("y", type=int)

    args = parser.parse_args()

    operand: str = args.operand.lower()
    x = args.x
    y = args.y

    try:
        result = _evaluate(operand, x, y)
    except ValueError as error:
        result = f'Error: {error}'

    print(result)

def _evaluate(operand: str, x: int, y: int) -> int:
    if operand == "add":
        return add(x, y)
    elif operand == "subtract":
        return subtract(x, y)
    else:
        raise ValueError("Unsupported operand!")

def add(x: int, y: int) -> int:
    return x + y

def subtract(x: int, y: int) -> int:
    return x - y

if __name__ == "__main__":
    main()
