# yoursearch.py

# Linear Search
def linear_search(lst, key):
    return next((i for i, val in enumerate(lst) if val == key), -1)

# Binary Search (assumes the list is sorted)
def binary_search(lst, key):
    def search(low, high):
        if low > high:
            return -1
        mid = (low + high) // 2
        if lst[mid] == key:
            return mid
        elif lst[mid] < key:
            return search(mid + 1, high)
        else:
            return search(low, mid - 1)
    
    return search(0, len(lst) - 1)