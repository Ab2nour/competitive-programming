a, b, c, d = map(int, input().split())
n, m = map(int, input().split())
LOWER_LIMIT = 0
UPPER_LIMIT = 100 * 1000
queue = [n]
already_seen = [False for _ in range(UPPER_LIMIT + 1)]


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
