class Graph:
    def __init__(
        self,
        a: int,
        b: int,
        c: int,
        d: int,
        lower_limit: int,
        upper_limit: int,
    ):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.already_seen: list[bool] = [False for _ in range(upper_limit + 1)]

    def get_neighbors(self, number: int) -> list[int]:
        neighbors = [
            number + self.a,
            number - self.b,
            number * self.c,
        ]

        if self.d != 0 and number % self.d == 0:
            neighbors.append(number // self.d)

        return neighbors

    def check_bounds(self, number: int) -> bool:
        return self.lower_limit <= number <= self.upper_limit


def main():
    a, b, c, d = map(int, input().split())
    n, m = map(int, input().split())

    LOWER_LIMIT = 0
    UPPER_LIMIT = 100 * 1000

    g = Graph(a, b, c, d, LOWER_LIMIT, UPPER_LIMIT)
    queue = [n]


def test_number(number):
    global m

    if number == m:
        print(1)
        exit()

    if LOWER_LIMIT <= number <= UPPER_LIMIT:
        if not already_seen[number]:
            already_seen[number] = True
            queue.append(number)


while queue:
    next_number = queue.pop(0)
    test_number(next_number + a)
    test_number(next_number - b)
    test_number(next_number * c)
    if d != 0 and next_number % d == 0:
        test_number(next_number // d)

print(0)
