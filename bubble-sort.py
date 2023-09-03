def bubble_sort(elements):
    """
    Bubble Sort is a simple sorting algorithm that repeatedly steps through the list,
    compares adjacent elements, and swaps them if they are in the wrong order.
    
    Parameters:
        elements (list): The list of elements to be sorted.
        
    Returns:
        None: The function sorts the list in-place.
    """
    size = len(elements)  # Calculate the array length once for efficiency

    for i in range(size - 1):
        swapped = False  # Initialize the 'swapped' flag to False for each outer loop iteration

        for j in range(size - 1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]  # Pythonic tuple swapping
                swapped = True  # Set the 'swapped' flag to True if any swapping occurred

        if not swapped:
            break  # Break the loop if no swapping occurred in the inner loop

elements = [5, 9, 2, 1, 67, 34, 88, 34]
bubble_sort(elements)
print(elements)