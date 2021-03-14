#Quick sort
target_Q = [3, -2, -1, 0, 2, 4, 1]

def Quick_sort(A, l, r):
    l = A[0]
    r = A[len(A) - 1]
    pivot = A[r]

    i = l - 1
    for j in range(len(A)):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
        A[i], pivot = pivot, A[i]

    Quick_sort(A, l, pivot - 1)
    Quick_sort(A, pivot + 1, r)

print(Quick_sort(target_Q, target_Q[0], target_Q[len(target_Q)]))

#Merge sort
target_M = [3, -2, -1, 0, 2, 4, 1]