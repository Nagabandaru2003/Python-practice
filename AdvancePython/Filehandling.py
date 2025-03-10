
with open('test.txt','r') as file:
    print(file.read())
#data = file.read()
# firstLine = file.readline()
# print(firstLine)
#file.close()
# print(data)
# print(data[0])

#print(file.readlines())

file1 = open('test2.txt','a')
file1.write('\nhello from java')
file1.close()

#print(file1.read())
# file1.write('Hello from Python\n')
# file1.write('Hello from js')