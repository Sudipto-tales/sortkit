def csv_sort(file_path, column_index=0):
    """Reads a CSV file, sorts data based on a specific column, and returns sorted rows."""
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()  # Read all lines

    header = lines[0].strip().split(",")  # Extract header
    data = [line.strip().split(",") for line in lines[1:]]  # Convert rows into lists

    sorted_data = sorted(data, key=lambda row: row[column_index].strip().lower())  # Case-insensitive sort

    return [header] + sorted_data  # Return sorted data including the header

# Example Usage:
sorted_rows = csv_sort("data.csv", column_index=1)  # Sort by 2nd column
for row in sorted_rows:
    print(row)
