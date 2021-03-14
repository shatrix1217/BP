#Quick sort
target_Q = [3, 2, 4, 1, 8, 9, 12, 7, 14, 6, -11, -4, -5, 44]
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
target_M = [3, 0, 2, 4, 1, 8, 9, 12, 7, 14, 6]

#Merge sort first trial
def Merge_sort(array):

    if len(array) <= 1:
        return array

    mid_point = int(len(array)/2)
    left, right = Merge_sort(array[ :mid_point]), Merge_sort(array[mid_point: ])
    
    return Merge(left, right)

def Merge(left, right):
    left_pointer = 0
    right_pointer = 0
    
    result = []

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] > right[right_pointer]:
            result.append(right[right_pointer])
            right_pointer += 1

        else:
            result.append(left[left_pointer])
            left_pointer += 1

    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])

    return result

print(Merge_sort(target_M))

#Merge sort second trial