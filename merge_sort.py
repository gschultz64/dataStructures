def merge(left, right):
    smallest = 0
    # base cases
    if len(right) == 0:
        return left
    if len(left) == 0:
        return right
    # Find the smallest number and remove it
    if left[0] <= right[0]:
        smallest = left.pop(0)
    else:
        smallest = right.pop(0)

    # Keep merging until either list is empty
    # recursive call:
    merged = merge(left, right)
    merged.insert(0, smallest)
    return merged

def merge_sort(l):
    # base case
    # a list of one or fewer items is considered sorted
    if len(l) <= 1:
        return l

    mid = round(len(l) / 2)
    # Divide the list around the mid point
    # start at the beg and stop at mid
    left_list = l[:mid]
    # start at mid and stop at end
    right_list = l[mid:]
    sorted_left_list = merge_sort(left_list)
    sorted_right_list = merge_sort(right_list)

    return merge(sorted_left_list, sorted_right_list)

data = [5, 10, 3, 90, 95, 654, 24, 9112, -6, 80]

print(merge_sort(data))