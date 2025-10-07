import csv
import os

"""
This script has examples of:
* using the os module to get the current working directory
* using the os module to create a new subdirectory
* how to test if a file exists
* using the csv module to read and write data to CSV files
* how to compare the contents of two lists
* how to break out of a loop when a condition is met
* how to safely convert a string to an integer

In VS Code, the starting current working directory is the directory of
your workspace.  These are the files displayed in the File Explorer, by
clicking the top icon in the left pane.
"""


def current_directory():
    """
    Return the current working directory as a string.

    This is the directory from which the script is being run, not the
    directory of the script itself.

    Returns:
        str: The current working directory.
    """
    return os.getcwd()


def create_subdirectory(new_directory):
    """
    Create a new subdirectory at the given path.
    Use exist_ok=True to avoid raising an error if the directory already exists.

    Parameters:
        new_directory (str): The path to the new subdirectory.

    Returns:
        None
    """
    os.makedirs(new_directory, exist_ok=True)


def get_sample_data():
    """
    Return a sample list of data with a CSV header.
    The CSV header is a list of strings that describe the columns.

    Returns:
        list: A list of lists.
    """
    return [
        ["Name", "Age", "Country"],
        ["John", 25, "USA"],
        ["Alice", 30, "Canada"],
        ["Bob", 28, "UK"],
    ]


def write_to_csv(data, filename="data.csv"):
    """
    Write data to a CSV file.

    Parameters:
        data (list of lists): The data to be written to the file.
        filename (str): The name of the file to be written. 
        Defaults to "data.csv".

    Returns:
        None
    """
    with open(filename, mode="w", newline="") as file:
        # Create a CSV writer
        writer = csv.writer(file)

        # Write data to the file
        writer.writerows(data)


def file_exists(filename):
    """
    Check if a file exists at the given path.

    Parameters:
        filename (str): The path to the file to be checked.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.exists(filename)


def read_from_csv(filename="data.csv"):
    """
    Read data from a CSV file.

    Parameters:
        filename (str): The name of the file to be read. 
            Defaults to "data.csv".

    Returns:
        list of lists: The data read from the file, or None if the file does not exist.

    Notes:
        The function will print a message if the file does not exist.
    """
    if file_exists(filename):
        # Open the CSV file
        with open(filename, "r") as file:
            # Create a CSV reader
            reader = csv.reader(file)

            # Read data from the file
            data = list(reader)
            return data
    else:
        print(f"File does not exist: {filename}")
        return None


def compare_list_contents(list1, list2):
    """
    Compare the contents of two lists to see if they are equal.

    Parameters:
        list1 (list): The first list to compare.
        list2 (list): The second list to compare.

    Returns:
        bool: True if the lists have the same contents, False otherwise.
    """
    return sorted(list1) == sorted(list2)


def convert_age_in_list_to_int(data_list):
    """
    Convert the age column in the given list to integers.

    The function will first find the column with the header "Age". 
    If it cannot find the column, it will print a message and return.

    Then it will iterate over the list and convert the age values to integers.
    If a value cannot be converted (for example, if it is not a number), 
    it will print a message and continue to the next value.

    Parameters:
        data_list (list of lists): The data to be converted.

    Returns:
        list of lists: The converted data.
    """
    age_column = None
    for i in range(len(data_list)):
        row = data_list[i]
        # the first row is the header
        if i == 0:
          # find the column with the age
          for column_name in row:
            if column_name == "Age":
              age_column = row.index(column_name)
              # now that we found the column, we can break out of the loop
              break 
          if not age_column:
              print("Could not find age column")
              return
        else:
            try:
                row[age_column] = int(row[age_column])
            except ValueError:
                print(f"Could not convert {row[age_column]} to an integer")
    return data_list


def run():
    """
    This function tests all the functions in this module.
    It first prints the current directory, then creates a new directory for writing the sample data.
    It then gets the sample data, writes it to a CSV file, and reads it back from the file.
    It then compares the data read from the file with the sample data and prints a message if they match.
    Finally, it converts the age column in the data to integers and compares the data again with the sample data.
    """
    print(current_directory())
    # create a new directory for writing the sample data
    create_subdirectory("data_files")
    # get the sample data
    sample_data = get_sample_data()
    print("sample data:")
    print(sample_data)
    write_to_csv(sample_data, "data_files/data.csv")
    # now test if we can read the data
    data_from_file = read_from_csv("data_files/data.csv")
    print()
    print("data read from file:")
    print(data_from_file)
    print()
    if compare_list_contents(sample_data, data_from_file):
        print("Data read from file matches sample data")
    else:
        print("Data read from file does not match sample data")
    # convert the age to an integer
    data_from_file = convert_age_in_list_to_int(data_from_file)
    print()
    print("After converting age to int:")
    print(data_from_file)
    print()
    if compare_list_contents(sample_data, data_from_file):
        print("Data read from file matches sample data")
    else:
        print("Data read from file does not match sample data")

"""
The output of running this script is:

sample data:
[['Name', 'Age', 'Country'], ['John', 25, 'USA'], ['Alice', 30, 'Canada'], ['Bob', 28, 'UK']]

data read from file:
[['Name', 'Age', 'Country'], ['John', '25', 'USA'], ['Alice', '30', 'Canada'], ['Bob', '28', 'UK']]

Data read from file does not match sample data

After converting age to int:
[['Name', 'Age', 'Country'], ['John', 25, 'USA'], ['Alice', 30, 'Canada'], ['Bob', 28, 'UK']]

Data read from file matches sample data
"""


"""
The __name__ variable is automatically set by the Python interpreter to the 
name of the module or script being executed.

When a script is executed directly, the value of __name__ is set to "__main__". 
This allows you to use the if __name__ == "__main__": block to ensure that 
code is only executed when the script is run directly, and not when it is 
imported as a module by another script.
"""
if __name__ == "__main__":
    run()
