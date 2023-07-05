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
        # Read the rows of the file into a dictionary
        reader = csv.DictReader(file)

        # Process each row of the dictionary
        for row in reader:
            return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])

    return return_string


# Call the function
print(contents_of_file("flowers.csv"))
