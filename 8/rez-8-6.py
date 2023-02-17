s = input()
i = 0
j = len(s) - 1
while i < j and s[i] == s[j]:
    i += 1
    j -= 1
if i >= j:
    print(i + 1)
elif s[:i] + s[i + 1:] == (s[:i] + s[i + 1:])[::-1]:
    print(i + 1)
elif s[:j] + s[j + 1:] == (s[:j] + s[j + 1:])[::-1]:
    print(j + 1)
else:
    print(0)