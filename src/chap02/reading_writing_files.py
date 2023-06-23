# The file object has a read method that returns the contents of the file as a string:
file_path = 'bookofdreams.txt'
open_file = open(file_path, 'r')
text = open_file.read()
print(len(text))
print(text[9])
print(open_file)
open_file.close()

# You can also read a file using the readlines method.
open_file = open(file_path, 'r')
text = open_file.readlines()
print(len(text))
print(text[2])
open_file.close()
