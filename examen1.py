#logica en sistemas
#primer semestre
#Angel Maria Cabrera Veliz
#0907-19-22417

#declare y pido al usuario que ingrese 3 numeros
num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese un segundo numero: "))
num3 = int(input("ingrese un tercer numero: "))

print("")
print("")

#pido al usuario que ingrese que opcion desea realizar
print("que opcion desea realizar.")
print("No.1 realizar opcion numero uno")
print("No 2 realizar opcion numero dos")
op1= int(input())
#veo si el valor de op1 
if(op1==1):
    if(num1>num3):
        print("ya que el primer numero que ingreso es mayor que el tercero se realizo la multiplicacion de los 3 numeros ingresados.")
        print("su resultado es: ",num1*num2*num3)
    elif (num1==num3):
        print("ya que el valor de las variables uno y dos es el mismo se realizara la suma de estos.")
        print("el resultado es: ",num1+num3)
    elif (num2==0):
        print("ya que el valor de la segunda variable es 0 se restara el mayor de las otras variables por el menor")
        if(num1>num3):
            print("el resultado es: ",num1-num3)
        elif (num3>num1):
            print("el resultado es: ", num3-num1)
elif(op1==2):
    for resultado in range(num1*num2+num3):
        print("el resultado de unir todas las variables es: ",num1,num2,num3)
