slovo = input("Введите слово с гласными буквами:")

eg=slovo.count("e") #считает кол-во гласных e
ag=slovo.count("a") #считает кол-во гласных a
ig=slovo.count("i") #считает кол-во гласных i
ug=slovo.count("u") #считает кол-во гласных u
og=slovo.count("o") #считает кол-во гласных o

scgetglas=eg+ag+ig+ug+og #суммирует кол-во гласных
print("всего гласных",scgetglas) #выводит количество гласных
print("всего согласных",len(slovo)-scgetglas) #считает сколько букв в слове и минусует от общего кол-ва букв гласные, выводит количество согласных
if (eg==0):
    print("гласной e в слове False")
else:
    print("e=",eg)
if (ug==0):
    print("гласной u в слове False")
else:
    print("u=",ug)
if (og==0):
    print("гласной o в слове False")
else:
    print("o=",og)
if (ag==0):
    print("гласной a в слове False")
else:
    print("a=",ag)
if (ig==0):
    print("гласной i в слове False")
else:
    print("i=",ig)