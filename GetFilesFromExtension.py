import os

ExtensionType = input("What Extension should i search on? Include the .   !!!! \n")

TargetFolder = input("What folder should i search in\n")

PathTest = "C:\\Users\\Gebruiker\\" + TargetFolder

ListTest = []



for i in os.listdir(PathTest):


    if i.endswith(ExtensionType):
       # print(type(i))

        ListTest.append(i)
        
print(*ListTest, sep="\n")



ShouldFile = input("Should i put them in a file???\n")

if ShouldFile == "Yes":
    testt = open("MyFile.txt", "w", encoding="utf-8") #Encoding thing was needed because it would'nt print an eszett
    for i in ListTest:
        testt.write(i + "\n")


