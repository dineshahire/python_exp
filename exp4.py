with open ("example.txt", "a") as file: file.write ("This is some new data.\n") file.write("This is some more new data.\n") with open ("example.txt", "r") as file:
contents = file.read () with open("example.txt", "a") as file: file.write("This is some new data.\n") file.write("This is some more new data.\n") with open ("example.txt", "r") as file:
contents = file.read () print (contents) with open ("example.txt", "w") as file:
file.write ("This is some replacement data.\n") with open ("example.txt", "r") as file: contents = file.read ()
print(contents)
import os
os.remove ("example.txt") with open ("newfile.txt", "w") as file:
file.write ("This is some data in a new file.\n") with open ("newfile.txt", "r") as file:
contents = file.read() print(contents) print(contents)

