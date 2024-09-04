import sys
import io


def define_string_as_input(string: str) -> None:
    """Tout appel à "input" ou sys.stdin.readline lira en réalité cette string."""
    sys.stdin = io.StringIO(string)
    input = io.StringIO(string)
