#naive search
def naive_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i

    return -1

#binary search
def binary_search(list, target, low = None, high = None):
    if low is None:
        low = 0

    if high is None:
        high = len(list) - 1

    if high < low:
        return -1

    mid_point = (low + high) // 2
    if list[mid_point] == target:
        return mid_point

    elif list[mid_point] > target:
        return binary_search(list, target, low, mid_point-1)

    else:
        return binary_search(list, target, mid_point+1, high)


if __name__ == "__main__":
    list = [1, 10, 20, 24, 25, 74, 85, 97, 102]
    target = 10

    print(binary_search(list, target))




