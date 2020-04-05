file_toOpen = "sample.txt"
file = open(file_toOpen)
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()
for line in file.readlines():
    print(line)
file.close()
with open(file_toOpen) as file1:
    print(file1.read())