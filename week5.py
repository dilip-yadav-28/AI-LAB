def attacks(x):
    count = 0
    n = len(x)

    for i in range(n):
        for j in range(i + 1, n):
            if abs(x[i] - x[j]) == abs(i - j):
                count += 1

    return count


def hill_climbing():
    x = [1, 2, 3, 0]
    iteration = 1

    while True:
        current = attacks(x)

        print("\nIteration:", iteration)
        print("Current state:", x)
        print("Attacks:", current)

        if current == 0:
            print("Solution found!")
            break

        best = x[:]
        min_attacks = current

        for i in range(4):
            for j in range(i + 1, 4):
                new_x = x[:]
                new_x[i], new_x[j] = new_x[j], new_x[i]
                h = attacks(new_x)

                print("Swap X", i, "and X", j,
                      ":", new_x, "Attacks:", h)

                if h < min_attacks:
                    min_attacks = h
                    best = new_x

        if best == x:
            print("Local minimum reached!")
            break

        x = best
        iteration += 1

    print("\nFinal state:", x)
    print("Final attacks:", attacks(x))


hill_climbing()