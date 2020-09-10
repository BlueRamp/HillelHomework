A = int(input("Input A:"))
B = int(input("Input B:"))
if A < B:
    a = []
    for i in range(A, B+1):
        a.append(i)
    print(a)
if A > B:
    b = []
    for k in range(B, A+1):
        b.append((A + 1) - k)
    print(b)