import os
import datetime

def file_date(filename):
    # Create the file in the current directory
    with open(filename, "w") as file:
        pass

    # Get the current timestamp
    timestamp = os.path.getmtime(filename)

    # Convert the timestamp into a readable format
    date = datetime.datetime.fromtimestamp(timestamp)

    # Format the date as "yyyy-mm-dd"
    formatted_date = date.strftime("%Y-%m-%d")

    # Return just the date portion
    return formatted_date

print(file_date("newfile.txt"))
