def exception_handler(func):
    """Decorator to handle exceptions globally for all sorting functions."""
    def wrapper(arr):
        try:
            # Ensure the input is a list
            if not isinstance(arr, list):
                raise TypeError("Input must be a list of numbers.")

            # Ensure all elements in the list are integers or floats
            if not all(isinstance(x, (int, float)) for x in arr):
                raise ValueError("List must contain only numbers.")

            return func(arr)  # Call the actual sorting function

        except TypeError as te:
            print(f"Type Error: {te}")
            return []
        except ValueError as ve:
            print(f"Value Error: {ve}")
            return []
        except MemoryError:
            print("Memory Error: Input list is too large!")
            return []
        except Exception as e:
            print(f"Unexpected Error: {e}")
            return []

    return wrapper
