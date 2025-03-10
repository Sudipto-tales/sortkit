Here's an updated and improved README with a CSV sorting example added:  

---

# **SortKit - A Python Sorting Library**  

SortKit is a Python library that provides efficient implementations of various sorting algorithms. This package allows users to easily sort lists and CSV data using different sorting techniques.  

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

This updated README now includes a **CSV sorting example**, **better formatting**, and **more clarity on features**. 🚀 Let me know if you need further improvements!