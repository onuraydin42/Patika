z = int(input())
for i in range(z):
    s = input()
    n = len(s)
    even = ''
    odd = ''  
    for i in range(n):
        if i % 2 == 0:
            even = even + s[i]
        else:
            odd = odd + s[i]
    print(even,odd)
