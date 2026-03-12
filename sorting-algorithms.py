import os 
import time
import random

# SORTING ALGORITHMS IN PYTHON

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#bubble sort algorithm 
def bubble_sort(array):
    n = len(array)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                #swap them
                array[j], array[j+1] = array[j+1], array[j]
                
    return array

#selection sort algorithm
def selection_sort(array):
    n = len(array)
    
    for i in range(n):
        min_index = i
        
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
                
        array[i], array[min_index] = array[min_index], array[i]
        
    return array

#insertion sort algorithm
def insertion_sort(array):
    n = len(array)
    
    for i in range(1, n):
        key = array[i]
        j = i - 1
        
        while j >= 0 and array[j] > key: 
            array[j + 1] = array[j]
            j -= 1
            
        array[j + 1] = key  
        
    return array

#quick sort algorithm
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            
    array[i + 1], array[high] = array[high], array[i + 1]
    
    return i + 1

def quick_sort(array, low = 0, high = None):
    if high is None:
        high = len(array) - 1
    
    if low < high:
        pivot_index = partition(array, low, high)
        quick_sort(array, low, pivot_index - 1)
        quick_sort(array, pivot_index + 1, high)
        
    return array

#merge sort algorithm
def merge(array, left, mid, right):
    left_half = array[left:mid + 1]
    right_half = array[mid + 1:right + 1]
    
    i = j = 0
    k = left    
    
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            array[k] = left_half[i]
            i += 1
        else:
            array[k] = right_half[j]
            j += 1
        k += 1
        
    while i < len(left_half):
        array[k] = left_half[i]
        i += 1
        k += 1
        
    while j < len(right_half):
        array[k] = right_half[j]
        j += 1
        k += 1   
        
# VISUALIZATION OF SORTING ALGORITHMS

def display_array(array, comparing=(-1, -1), sorted_indices=set(), delay=0.3):
    clear_screen()
    print("Sorting Visualization:")
    print("-" * 50)
    
    for i, value in enumerate(array):
        bar = "#" * value
        prefix = ">" if i in comparing else " "
        suffix = "*" if i in sorted_indices else " "
        print(f"{prefix} {bar:<20} ({value}) {suffix}") 

    time.sleep(delay)
    
# Visualizer wrappers
def bubble_sort_visual(array, delay):
    n = len(array)
    sorted_indices = set()
    for i in range(n):
        for j in range(0, n-i-1):
            display_array(array, comparing=(j, j+1), sorted_indices=sorted_indices, delay=delay)
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                display_array(array, comparing=(j, j+1), sorted_indices=sorted_indices, delay=delay)
        sorted_indices.add(n-i-1)
    display_array(array, sorted_indices=set(range(n)), delay=delay)
    
def selection_sort_visual(array, delay):
    n = len(array)
    sorted_indices = set()
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            display_array(array, comparing=(min_index, j), sorted_indices=sorted_indices, delay=delay)
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        sorted_indices.add(i)
        display_array(array, sorted_indices=sorted_indices, delay=delay)
        
def insertion_sort_visual(array, delay):
    n = len(array)
    sorted_indices = {0}
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            display_array(array, comparing=(j, j+1), sorted_indices=sorted_indices, delay=delay)
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
        sorted_indices.add(i)
        display_array(array, sorted_indices=sorted_indices, delay=delay)
        
def quick_sort_visual(array, low, high, sorted_indices, delay):
    if low < high:
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            display_array(array, comparing=(j, high), sorted_indices=sorted_indices, delay=delay)
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i+1], array[high] = array[high], array[i+1]
        sorted_indices.add(i+1)
        display_array(array, sorted_indices=sorted_indices, delay=delay)
        pivot_index = i + 1
        quick_sort_visual(array, low, pivot_index-1, sorted_indices, delay)
        quick_sort_visual(array, pivot_index+1, high, sorted_indices, delay)
def merge_sort_visual(array, left, right, sorted_indices, delay):
    if left < right:
        mid = (left + right) // 2
        merge_sort_visual(array, left, mid, sorted_indices, delay)
        merge_sort_visual(array, mid+1, right, sorted_indices, delay)
        merge(array, left, mid, right)
        for idx in range(left, right+1):
            sorted_indices.add(idx)
        display_array(array, sorted_indices=sorted_indices, delay=delay)
        
# Menu System
SPEEDS = {
    "1": ("Very Slow ", 1.0),
    "2": ("Slow", 0.5),
    "3": ("Medium", 0.2),
    "4": ("Fast", 0.05),
    "5": ("Very Fast", 0.01),
}

def get_speed():
    print("Select Speed: ")
    for key, (name, _) in SPEEDS.items():
        print(f" {key}. {name}")
    choice = input("\nEnter choice: (1-5): ").strip()
    return SPEEDS.get(choice, ("Medium", 0.2))[1]

def get_array_size():
    try: 
        size = int(input("\nEnter array size (5-20): "))
        return max(5, min(size, 20))
    except ValueError:
        return 10

def show_menu():
    clear_screen()
    print("\n" + "=" * 50)
    print("      SORTING ALGORITHM VISUALIZER")
    print("=" * 50)
    print("\n  1. Bubble Sort    — O(n²)")
    print("     Repeatedly compares adjacent elements and")
    print("     swaps them if they are in the wrong order.\n")
    print("  2. Selection Sort — O(n²)")
    print("     Repeatedly finds the minimum element from")
    print("     the unsorted region and places it at front.\n")
    print("  3. Insertion Sort — O(n²)")
    print("     Builds sorted array one item at a time by")
    print("     inserting each element into its correct spot.\n")
    print("  4. Quick Sort     — O(n log n)")
    print("     Selects a pivot element and partitions the")
    print("     array into smaller and larger elements.\n")
    print("  5. Merge Sort     — O(n log n)")
    print("     Recursively splits array in half, sorts each")
    print("     half, then merges them back together.\n")
    print("  0. Exit")
    print("\n" + "-" * 50)

def run():
    while True:
        show_menu()
        choice = input("\nSelect algorithm (0-5): ").strip()

        if choice == "0":
            print("\nGoodbye! 👋")
            break

        if choice not in "12345":
            print("Invalid choice! Try again.")
            time.sleep(1)
            continue

        size  = get_array_size()
        delay = get_speed()
        array = [random.randint(1, 20) for _ in range(size)]

        print("\nStarting sort...")
        time.sleep(1)

        display_array(array, delay=delay)
        start = time.time()
        
        if   choice == "1": bubble_sort_visual(array, delay)
        elif choice == "2": selection_sort_visual(array, delay)
        elif choice == "3": insertion_sort_visual(array, delay)
        elif choice == "4": quick_sort_visual(array, 0, len(array)-1, set(), delay)
        elif choice == "5": merge_sort_visual(array, 0, len(array)-1, set(), delay)
        
        end = time.time()
        print(f"\n✅ Sorting complete!")
        print(f"⏱  Time: {end - start:.2f} seconds")
        input("\nPress Enter to continue...")
        
# Entry Point
if __name__ == "__main__":
    run()