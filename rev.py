def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
A = [11,22,33,44,55,66,77]
print(A)
reverseList(A, 0, 6)
print("Reversed list is")
print(A)
