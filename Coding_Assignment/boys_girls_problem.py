def can_arrange_students(boys, girls):
    boys.sort()
    girls.sort()

    # Try two different arrangements: Starting with a boy or a girl
    possible1, possible2 = True, True

    # Checking for boy-girl order
    for i in range(len(boys)):
        if i > 0 and (boys[i] < girls[i - 1] or girls[i] < boys[i - 1]):
            possible1 = False
            break

    # Checking for girl-boy order
    for i in range(len(girls)):
        if i > 0 and (girls[i] < boys[i - 1] or boys[i] < girls[i - 1]):
            possible2 = False
            break

    return "YES" if possible1 or possible2 else "NO"


# Input handling
t = int(input())  # Number of test cases
for _ in range(t):
    n = int(input())  # Number of boys and girls
    boys = list(map(int, input().split()))
    girls = list(map(int, input().split()))

    print(can_arrange_students(boys, girls))
