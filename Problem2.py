import os

directory_path = '/Users'


#list all file ad directories in the specific path
contents = os.listdir(directory_path)

# print each file and directoy name
for item in contents:
    print(item)