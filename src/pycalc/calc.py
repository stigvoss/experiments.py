import sys

def main():
    args = sys.argv[1:]

    if len(args) != 3:
        raise ValueError("Too few args!")

    operand: str = args[0].lower()
    x: int = int(args[1])
    y: int = int(args[2])

    try:
        result = __evaluate__(operand, x, y)
    except ValueError as error:
        result = f'Error: {error}'

    print(result)

def __evaluate__(operand: str, x: int, y: int) -> int:
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
