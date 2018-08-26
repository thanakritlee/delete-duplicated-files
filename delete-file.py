"""
delete-file.py

This program is use to delete duplicated files.
This program was tested on Microsoft Windows 10 64 bit.

Approach used for writing this program:
1. Hard code the if statements to each file types and duplicates number(1-3).
2. Refactor the code to make it more elegant and efficient by making the file types variables in an array
   and then iterate through the file type's array for each file to see if a match occur, in which the file is
   then deleted.
3. Refactor the duplicates number to a variable so that it could be change easily.
4. Instead of having to run the script from the directory of the photos to delete, now the
   program will traverse the directory trees into the sub directories and delete duplicated
   photo files. The program now can be places and run from the root directory of folders
   of photos to delete.
"""

# For working with the file system.
import os
# For working with the regular expression.
import re


def option_1():
    # Regular expression to match against duplicated files.

    # The regular expression represents:
    # '\S+' matches any 1 or more non-whitespace character(s).
    # '\s' matches any whitespace character.
    # '\(' matches the character '(', the backslash is use to escape the RE syntax.
    # '\d+' matches any 1 or more decimal digit(s).
    # '\)' matches the character '(', the backslash is use to escape the RE syntax.
    # '[.]' matches the character '.'.
    # '\S+' matches any 1 or more non-whitespace character(s).

    duplicate_pattern = re.compile('\S+\s\(\d+\)[.]\S+')

    rootDir = '.'
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            if duplicate_pattern.match(fname):
                os.remove(dirName + '\\' + fname)


def option_2():
    # For loop and If statements to match against duplicated files of selected types
    # and duplicated copies.

    # This variable represents how many duplicate copies of a file there are.
    # Change as needed.
    duplicate_amount = 6

    # An array that holds the extension types to match against.
    extension_array = []

    # Extension types to match against.
    # Add as needed.
    JPG = ".JPG"
    jpg = ".jpg"
    PNG = ".PNG"
    png = ".png"
    MOV = ".MOV"
    mov = ".mov"
    mp4 = ".mp4"

    # Appending  the extension types to the array.
    # If any change from the above list of extension types, match the change here as well.
    extension_array.append(JPG)
    extension_array.append(jpg)
    extension_array.append(PNG)
    extension_array.append(png)
    extension_array.append(MOV)
    extension_array.append(mov)
    extension_array.append(mp4)

    # The test loop.
    # This loop is use to go through each file in the current directory and test it against the
    # file extension type and its duplicate

    rootDir = '.'
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            for extension in extension_array:
                for i in range(1, duplicate_amount):
                    if fname.endswith("(%s)%s" % (i, extension)):
                        os.remove(dirName + '\\' + fname)                

print("Options:   ")
print("(1) Match against all file extension type.")
print("(2) Match against selected file extension type.\n")

while True:
    try:
        selected_option = int(input("Select an option (Enter '1' or '2'):   "))
        print("\n")
        break
    except ValueError as err:
        print("Option must be a number.\n")

if selected_option == 1:
    print("Option (1) selected. Match against all file extension type using regular expression.\n")
    option_1()
elif selected_option == 2:
    print("Option (2) selected. Match against selected file extension type using for loop and if statement.\n")
    option_2()
else:
    print("Selected option unavailable.\n")


print('------FINISHED------')
print('Duplicated files deleted.')
done = input("Type any key to exit the program:   ")
