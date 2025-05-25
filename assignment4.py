# try:
  
#   with open('C:\\Users\\Dell\\Documents\\sample.txt','r') as file:
#     file1 = file.read()
#     print(file1)
#     file.close()

# except FileNotFoundError:
#   print("Error: The File 'sample.txt' was not found")


file1 = input("Enter text to write to the file: ")
with open("C:\\Users\\Dell\\Documents\\Output.txt",'w') as file:
 writing_file = file.write(file1 + "\n")
 print("Data succesfully written to the output.txt.\n")
 

file2 = input("Enter additional text to append: ")
with open("C:\\Users\\Dell\\Documents\\Output.txt",'a') as file:
 writing_file = file.write(file2 + "\n")
 print("Data succesfully appended.\n ")
 
print ("Final content of the out.txt:")
with open("C:\\Users\\Dell\\Documents\\Output.txt",'r') as file:
 content = file.read()
 print(content)