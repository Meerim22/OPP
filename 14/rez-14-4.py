n = int(input())
group1 = set()
group2 = set()
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = [int(x) for x in guess.split()]
    answer = input()
    if answer == 'YES':
        for i in guess:
            group1.add(i)
    else:
        for i in guess:
            group2.add(i)
number = group1.difference(group2)
print(*sorted(number))