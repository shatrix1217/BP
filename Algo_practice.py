#Quick sort
target_Q = [3, 2, 4, 1, 8, 9, 12, 7, 14, 6]
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

    elements_bigger = []
    elements_smaller = []

    for item in sequence:
        if item > pivot:
            elements_bigger.append(item)
        else:
            elements_smaller.append(item)

    return Quick_sort(elements_smaller) + [pivot] + Quick_sort(elements_bigger)

print(Quick_sort(target_Q))

#Merge sort
target_M = [3, 0, 2, 4, 1, 8, 9, 12, 7, 14, 6, -5]