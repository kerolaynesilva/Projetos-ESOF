import re

print("\nThis program searches for lines with your string in them\n")
search_str = raw_input("Enter with string you are searching for: \n")

file = open("C:/Users/giord/PycharmProjects/untitled/Doc1.txt")
content = file.read()
file.close()

regex = re.compile(r"(.*)?(%s)(.*)?" % search_str)

if regex.search(content) is None:
    print("No matches was found.")
else:
    print(regex.findall(content))