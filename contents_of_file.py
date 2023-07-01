import os
import csv

# Create a file with data in it
def create_file(filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "color", "type"])
        writer.writerow(["carnation", "pink", "annual"])
        writer.writerow(["daffodil", "yellow", "perennial"])
        writer.writerow(["iris", "blue", "perennial"])
        writer.writerow(["poinsettia", "red", "perennial"])
        writer.writerow(["sunflower", "yellow", "annual"])


# Read the file contents and format the information about each row
def contents_of_file(filename):
    return_string = ""

    # Call the function to create the file
    create_file(filename)

    # Open the file
    with open(filename, "r") as file:
        # Read the rows of the file
        rows = csv.reader(file)

        # Process each row
        for row in rows:
            if row[0] != "name":
                name, color, type_ = row
                # Format the return string for data rows only
                return_string += "a {} {} is {}\n".format(color, name, type_)

    return return_string

# Call the function
print(contents_of_file("flowers.csv"))
