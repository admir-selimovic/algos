
def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def max_heapify(A, n, i):
    """
    Helper function to maintain the heap property for a subtree rooted at index i.
    """
    l = left(i)
    r = right(i)
    largest = i
    
    if l < n and A[l] > A[i]:
        largest = l
    if r < n and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, n, largest)


def build_max_heap(A):
    """
    Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure.
    This function sorts an array in-place using a max heap.
    
    Parameters:
        A (list): The list of elements to be sorted.
        
    Returns:
        None: The function sorts the list in-place.
    """
    n = len(A)
    
    # Build max heap
    for i in range(n, -1, -1):
        max_heapify(A, n, i)
    
    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        max_heapify(A, i, 0)


# Test the heap sort function
A = [33, 35, 42, 10, 7, 8, 14, 19, 48]
build_max_heap(A)
print(A)