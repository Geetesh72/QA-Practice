file_path = "notes.txt"


# Write to the files 
with open (file_path,'w') as file:
    file.write('And B tech in Software')


# Reading the file 
with open(file_path,'r') as file:
    content = file.read()
content,file_path 