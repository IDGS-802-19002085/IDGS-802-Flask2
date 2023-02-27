f=open('Alumnos.txt','r')
# nombres=f.read()
# print(nombres)
nombres2=f.readlines()
print(nombres2)
f.close()

for items in nombres2:
    print(items, end= '')

f=open('Alumnos1.txt','a')
f.write('Mario\n')
f.write('Pedro \n')
f.close()

alumno={'Matricula':'123','Nombre':'Mario','Apellido Paterno':'Garcia','Apellido Materno':'Garcia','Correo Electronico':'mario@gmail.com'}
f=open('Alumnos1.txt','a')
f.write('\n'+'Mario')
f.write('\n'+'Pedro')
for items in alumno:
    f.write('\n'+alumno[items])
    f.close()






