fileName = 'test.py'
fileOpen = open(fileName,'r')
fileOpen.readline()
#fileOpen.close()

'''
# While loop to read a file
line = fileOpen.readline()
while line != '':
    print(line, end='')
    line = fileOpen.readline()

fileOpen.close()

# While loop to read a file
while line != '\n':
    print(line)
    line = fileOpen.readline()

fileOpen.close()

# For loop to read a file
for line in fileOpen:
    print(line, end='')

fileOpen.close()
'''
# print(fileOpen.read()) #Read a file  -> all line with a print


# print(fileOpen.readlines()) # Read a file as a single String

lines = fileOpen.readlines()
for line in lines:
    print(line, end='')

fileOpen.close
