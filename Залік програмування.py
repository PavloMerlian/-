a = input("Введіть слово, або букву яку ви хочете замінити: ")
b = input("Введіть слово на яке ви хочете замінити: ")
with open('file.txt', 'r') as file :
  filedata = file.read()
  filedata = filedata.replace(a, b)
with open('file.txt', 'w') as file:
  file.write(filedata)
    




   
