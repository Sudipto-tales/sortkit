Here's your updated README with a **functionality chart** included for better clarity:  

---

# **SortKit - A Python Sorting Library**  

SortKit is a Python library that provides efficient implementations of various sorting algorithms. This package allows users to easily sort **lists** and **CSV data** using different sorting techniques.  

## **Features**  
✅ Supports multiple sorting algorithms:  
- **Bubble Sort**  
- **Selection Sort**  
- **Insertion Sort**  
- **Quick Sort**  
- **Merge Sort**  
- **Heap Sort**  
- **Counting Sort** (for numerical values)  

✅ Supports **integers, floating-point numbers, and strings**  
✅ Can **sort data from CSV files**  
✅ Simple and efficient API  
✅ Well-tested with `unittest`  

## **Installation**  
Install SortKit using `pip`:  

```sh
pip install sortkit
```  

## **Functionality Chart**  

| Function Name  | Sorting Type        | Description                                  | Example Usage |
|--------------|------------------|----------------------------------|--------------|
| `bubble_sort()`  | Bubble Sort        | Simple, compares adjacent elements   | `bubble_sort(arr)` |
| `selection_sort()`  | Selection Sort    | Selects the smallest and swaps    | `selection_sort(arr)` |
| `insertion_sort()`  | Insertion Sort    | Builds sorted list one item at a time  | `insertion_sort(arr)` |
| `quick_sort()`  | Quick Sort        | Efficient, divide and conquer approach | `quick_sort(arr)` |
| `merge_sort()`  | Merge Sort        | Splits, sorts, and merges lists   | `merge_sort(arr)` |
| `heap_sort()`  | Heap Sort        | Uses heap structure to sort data  | `heap_sort(arr)` |
| `counting_sort()`  | Counting Sort    | Efficient for small integer ranges   | `counting_sort(arr)` |
| `csv_sort()`  | CSV Sorting       | Sorts a CSV file by a given column   | `csv_sort("file.csv", column_index=1)` |

## **Usage**  

### **Example 1: Sorting a List with Bubble Sort**  

```python
from sortkit import bubble_sort

arr = [5, 3, 8, 6, 2, 7, 4, 1]

sorted_arr = bubble_sort(arr)
print(sorted_arr)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
```  

### **Example 2: Sorting a CSV File by a Specific Column**  

```python
from sortkit import csv_sort

csv_file = "data.csv"  # Your CSV file path
sorted_data = csv_sort(csv_file, column_index=1)  # Sorting by second column

for row in sorted_data:
    print(row)
```  

## **Running Tests**  

To run tests, use the following command:  

```sh
python -m unittest discover tests
```  
Or  

```sh
py -m unittest discover tests
```  

## **Contributing**  

If you'd like to contribute, feel free to fork the repository and submit a pull request.  

## **License**  

This project is licensed under the **MIT License**.  

---

### 🚀 **Now with a clear function reference chart!** Let me know if you need more improvements. 😊