import time


def menu():
    print("1. Consignar plata.")
    print("2. Retirar plata.")
    print("3. Consultar saldo.")
    print("4. Salir")


def inicio():
    print("-" * 30)
    print("Bienvenid@s a Desfacol, si usted no pierde su plata nosotros la perdemos por usted :D")
    print("-" * 30)

       
def inicio2():
    intento = 3
    co = 3
    for i in range(intento):
        print("-" * 30)
        x = int(input("Digite su cedula para iniciar sesion: "))
        xx = int(input("Ingrese su contrase;a: "))
        print("-" * 30)

        if ((x in cuenta) and (xx in password)):
            p1 = cuenta.index(x)
            p2 = password.index(xx)
            if p1 == p2:
                print("Bienvenid@ a su cuenta")
                menu()
                break
            elif ((p1 != p2) or (p2 != p1)):
                co -= 1
                if co == 0:
                    print("No tiene mas intentos")
                elif co > 0:
                    print("Su contrase;a es incorrecta, intentelo nuevamente tiene", co, "intentos")
                else:
                    print("Esto no debe salir")  
            else:
                print("Esto no debe salir.")
                
        elif ((x in cuenta) and (xx not in password)):
            co -= 1
            if co == 0:
                print("No tiene mas intentos")
            elif co > 0:
                print("Su cuenta o contrase;a no estan registradas, intentelo nuevamente tiene", co, "intentos")
            else:
                print("Esto no debe salir")
        elif (((x not in cuenta) and (xx in password)) or ((x not in cuenta) and (xx not in password))):
            co -= 1
            if co == 0:
                print("No tiene mas intentos")
            elif co > 0:
                print("Su cuenta o contrase;a no estan registradas, intentelo nuevamente tiene", co, "intentos")
            else:
                print("Esto no debe salir")
         
        else:
            print("Esto no debe salir")
            break




#Inicio codigo:
cuenta = []
password = []
b = 1

inicio()
x1 = int(input("Ingrese cuantas cuentas desea registrar: "))
print("-" * 30)
while b <= x1:
    cx = int(input(f"Digite la cuenta numero {b}: "))
    cuenta.append(cx)
    px = int(input(f"Digite la contrase;a de la cuenta numero {b}: "))
    password.append(px)
    print("-" * 30)
    b += 1
print("CUENTAS", cuenta)
print("CONTRASE:AS", password)

inicio2()