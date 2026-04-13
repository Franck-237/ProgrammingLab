
def control_list(A, B):

    for i in A:
        for j in B:
            if i == j:
                print(f"{i} is in the two list")
    return 0
            
A = [1, 2, 3, 5]
B = [9, 0, 2, 3]

print(control_list(A, B))