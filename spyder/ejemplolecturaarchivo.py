
f=open('concentrado.txt', 'r')
#print(f.readline())  #Lee por linea
#print(f.read()) #Es todo un texto y le puedes colocar un dato numerico al read(3)

#for x in f:
#    print(x,'\n')

linea=f.readlines()
print(linea)
#print (linea[2])

f.close()
