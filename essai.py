file = open("/Users/Benjamin/Desktop/essai.txt")
cont = []
new_cont = []
#your code goes here
for line in file.readlines():
    cont = []
    cont += line.split(" ")
    abb = []
    for i in range(len(cont)):
        abb += cont[i][0]
    s = ''.join(abb)
    print(s)