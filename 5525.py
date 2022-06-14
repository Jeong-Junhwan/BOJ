# IOIOI

n = int(input())
m = int(input())
s = input()

cnt = 0

index = 1
IOI = 0
while index < m - 1:
    if s[index - 1] == "I" and s[index] == "O" and s[index + 1] == "I":
        IOI += 1
        if IOI == n:
            IOI -= 1
            cnt += 1
        index += 1
    else:
        IOI = 0

    index += 1

print(cnt)
