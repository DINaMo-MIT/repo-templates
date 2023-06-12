import argparse
import math


def parse_args():
    # Argument parsing (https://docs.python.org/3/library/argparse.html)
    parser = argparse.ArgumentParser(
        description="Example python script/function.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-v",
        "--verbosity",
        help="increase output verbosity (eg -v, -vv, -vvv, etc)",
        action="count",
        default=0,
    )
    parser.add_argument("-f", "--filename", default="test.txt", help="Filename to do something")
    return parser.parse_args()


def simple_function(filename: str, verbosity: int = 0) -> bool:
    """Simple function to illustrate type hints, verbosity, doc strings, etc.

    This example uses Google style docstrings (you can pick other options)
    See: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
    Use VS Code extension autoDocstring (https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
    to make generation very easy.

    Args:
        filename (str): the filename of something
        verbosity (int, optional): Debug verbosity. Defaults to 0.

    Returns:
        bool: the output of something to return
    """
    if verbosity > 0:
        print(f"Verbose message, since verbosity = {verbosity}")
    print(f"Doing something with file: {filename}")

    # flake8 test
    # Here is a really long line ----------------------------------------------------------------------------------- so long that flake8 would complain # noqa: E501
    # You can either manually break the line or add a #noqa at the end (as was done above to stop pre-commit failure).

    return True


def quadratic_solver(a: float, b: float, c: float) -> tuple:
    """Returns solutions to the quadratic equation a*x^2 + b*x + c = 0.

    Inspired by http://cwiki.merl.com/display/MCS/Create+simple+Matlab+unit+test

    Args:
        a (float): x^2 coefficient
        b (float): x coefficient
        c (float): constant coefficient

    Raises:
        ValueError: if 0 is zero

    Returns:
        tuple: Two solutions to quadratic equation
    """

    # Check if a is exactly zero, which would cause ZeroDivisionError and provide a more useful error message.
    # Note the use of "ValueError" (ie the user gave an invalid number) rather than "assert" which is used to check
    # for programatic bugs.
    if a == 0:
        raise ValueError("a is zero, which causes division by 0 error (so equation is linear, not quadratic)")

    roots1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    roots2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)

    return roots1, roots2


# Allow python file to act as either a reusable module (for import), or as standalone program (as command line script)
if __name__ == "__main__":
    args = parse_args()
    simple_function(args.filename, verbosity=args.verbosity)