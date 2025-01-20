import random
import yoursearch
import yoursort

def main():
    # Generate a random list of elements
    n = int(input("Enter the number of elements in the list: "))
    lst = [random.randint(1, 100) for _ in range(n)]
    print("Generated list:", lst)

    # Prompt user for sorting method
    print("\nSorting Algorithms:")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Selection Sort")
    sort_choice = int(input("Choose a sorting algorithm (1-3): "))

    if sort_choice == 1:
        yoursort.bubble_sort(lst)
        print("List after Bubble Sort:", lst)
    elif sort_choice == 2:
        yoursort.insertion_sort(lst)
        print("List after Insertion Sort:", lst)
    elif sort_choice == 3:
        yoursort.selection_sort(lst)
        print("List after Selection Sort:", lst)
    else:
        print("Invalid choice. Exiting.")
        return

    # Prompt user for a search key
    key = int(input("\nEnter the key to search for: "))

    # Prompt user for search method
    print("\nSearch Algorithms:")
    print("1. Linear Search")
    print("2. Binary Search (List must be sorted)")
    search_choice = int(input("Choose a search algorithm (1-2): "))

    if search_choice == 1:
        index = yoursearch.linear_search(lst, key)
        print(f"Linear Search: Key found at index {index}" if index != -1 else "Key not found.")
    elif search_choice == 2:
        index = yoursearch.binary_search(lst, key)
        print(f"Binary Search: Key found at index {index}" if index != -1 else "Key not found.")
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()