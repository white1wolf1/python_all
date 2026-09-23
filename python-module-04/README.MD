The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

NOTE : "t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)


EX:f = open("demofile.txt") = f = open("demofile.txt", "rt")

open() function returns a file object, which has a read() method for reading the content of the file:


with open("demofile.txt") as f:
with key word  closes the file so no neef for close()


good exemle :

f = open("demofile.txt")
print(f.readline())
f.close()

read: funk can be spesifyed = print(f.read(5)) reeds only first 5 char
or readline()= only first line

with open("demofile.txt") as f:
  for x in f:
    print(x)

loops all the file !

To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content

open("sa.txt,x) =creates empty file

To delete a file, you must import the OS module, and run its os.remove() function:

if os.path.exists("demofile.txt"): = checks if the file is exist

To delete an entire folder, use the os.rmdir() method but ou can only remove empty folders!

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)¶

Note :If the file cannot be opened, an OSError is raised
