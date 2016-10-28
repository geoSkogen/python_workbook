from sys import argv

script, filename = argv

target = open(filename, 'a')

print("create a file:")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
line4 = input("line 4: ")
print("writing . . .")

target.write("%s\n%s\n%s\n%s\n" % (line1, line2, line3, line4))

print(". . . closing")
target.close()
