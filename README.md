# SortKit - A Python Sorting Library

SortKit is a Python library that provides efficient implementations of various sorting algorithms. This package allows users to easily sort lists using different sorting techniques.

## Features
- Supports multiple sorting algorithms:
  - Bubble Sort
  - Selection Sort
  - Insertion Sort
  - Quick Sort
  - Merge Sort
  - Heap Sort
  - Counting Sort (for numerical values)
- Handles integers and floating-point numbers
- Simple and efficient API
- Well-tested with `unittest`

## Installation
You can install the package using `pip`:

```sh
pip install sortkit
```

## Usage

### Example: Bubble Sort
```python
from sortkit import bubble_sort

arr = [5, 3, 8, 6, 2, 7, 4, 1]

sorted_arr = bubble_sort(arr)
print(sorted_arr)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
```

## Running Tests
To run tests, use the following command:

```sh
python -m unittest discover tests
```

## Contributing
If you'd like to contribute, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

