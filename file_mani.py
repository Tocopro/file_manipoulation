with open("C:\\Users\\NEAK\\Downloads\\file_one.txt", "r") as file1:
    with open("C:\\Users\\NEAK\\Downloads\\copy_file.txt", "w") as file2:
        for line in file1:
            file2.write(line)

file1.close()
file2.close()
