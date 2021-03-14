#Quick sort
target_Q = [3, -2, -1, 0, 2, 4, 1]

#Quick sort first trial
# def Quick_sort(A, l, r):
#     l = A[0]
#     r = A[len(A) - 1]
#     pivot = A[r]

#     i = 0
#     for j in range(len(A)):
#         if A[j] <= pivot:
#             i += 1
#             A[i], A[j] = A[j], A[i]
#         A[i], pivot = pivot, A[i]

#     Quick_sort(A, l, pivot - 1)
#     Quick_sort(A, pivot + 1, r)

# print(Quick_sort(target_Q, target_Q[0], target_Q[len(target_Q)-1]))

#Quick sort second trial
def Quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
        element_bigger = []
        element_smaller = []
        for i in sequence:
            if i <= pivot:
                element_smaller.append(i)
            else:
                element_bigger.append(i)
        return Quick_sort(element_smaller) + [pivot] + Quick_sort(element_smaller)

print(Quick_sort(target_Q))


#Merge sort
target_M = [3, -2, -1, 0, 2, 4, 1]