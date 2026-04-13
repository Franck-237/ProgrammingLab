
def is_list(A):
    
    n = len(A)

    for i in range(n // 2):
        opposto = n - 1 - i

        A[i], A[opposto] = A[opposto], A[i]

    return  A

A = ['Franck', 'Kamdem', 'Christy']

print(is_list(A))