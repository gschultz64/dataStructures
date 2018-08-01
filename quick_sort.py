#  QUICK SORT
def quick_sort(list):
    # base case
    if len(list) <= 1:
        return list
    pivot = list[0]
    mid = []
    left = []
    right = []

#  iterate over list
    for item in list:
        if item > pivot:
            right.append(item)
        elif item < pivot:
            left.append(item)
        elif item == pivot:
            mid.append(item)

#   return sorted items
    return quick_sort(left) + mid + quick_sort(right)


data = [5, 10, 3, 90, 95, 654, 24, 9112, -6, 80]
print(quick_sort(data))
