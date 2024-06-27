from argparse import ArgumentParser, Namespace
import sys

from cuipy.cuiapp import CuiApp

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Cannot divide by zero")

def get_parser() -> ArgumentParser:
    # Create the ArgumentParser object
    parser = ArgumentParser(description="Simple calculator script.")
    
    # Define the expected arguments
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], 
                        help="The operation to perform: add, subtract, multiply, or divide.")
    parser.add_argument("a", type=float, help="The first number.")
    parser.add_argument("b", type=float, help="The second number.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Include verbose.")

    return parser


def main(args: Namespace):
    print(args)
    if args.operation == "add":
        if args.verbose:
            print(f"Addition between {args.a} and {args.b}.")
        res = args.a + args.b
    elif args.operation == "subtract":
        if args.verbose:
            print(f"Substraction of {args.a} by {args.b}.")
        res = args.a - args.b
    elif args.operation == "multiply":
        if args.verbose: 
            print(f"Multiplication between {args.a} and {args.b}.")
        res = args.a * args.b
    elif args.operation == "divide":
        if args.verbose: 
            print(f"Division of {args.a} by {args.b}.")
        res = args.a / args.b
    else:
        raise ValueError(f"Invalid operation: {args.operation}")
    print(res)


# Ensure the script runs only when executed directly
if __name__ == "__main__":
    cuiapp = CuiApp(main, get_parser())
    cuiapp.run(debug=True)
