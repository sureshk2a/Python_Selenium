file_toOpen = "sample.txt"
file_toWrite = "writeFile.txt"
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()
with open(file_toOpen,'r') as file1:
    content = file1.readlines()
    with open(file_toWrite,'w') as file2:
        for line in reversed(content):
            file2.write(line)
