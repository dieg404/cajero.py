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
    

def inicioc():
    c = 1
    co = 2
    while c <= 3:
        print("-" * 30)
        x = int(input("Digite su cedula para iniciar sesion: "))
        xx = int(input("Ingrese su contrase;a: "))
        if ((x not in cuenta) and (xx not in password)):
            print("Su cuenta o contrase;a no estan registradas, intentelo uevamente tiene", co, "intentos")
            c += 1
            co -= 1
        elif (x in cuenta) and (xx in password):
            for i in range(len(cuenta), len(password)):
                if cuenta[i] == password[i]:
                    print("Hola")
                    break
                elif cuenta[i] != password[i]:
                    print("Su contrase;a es incorrecta, intentelo nuevamente. ")
                else:
                    print("Hay algo aml en el codigo.")  
        
        else: 
            print("Hay algo aml en el codigo.")


            
def inicioc():
    c = 1
    co = 2
    while c <= 3:
        x = int(input("Digite su cedula para iniciar sesion: "))
        xx = int(input("Ingrese su contrase;a: "))
        if (x not in cuenta) and (xx not in password):
            print("Su cuenta o contrase;a no estan registradas, intentelo uevamente tiene", co, "intentos")
            c += 1
            co -= 1
        elif (x in cuenta) and (xx not in password):
            print("Su cuenta o contrase;a no estan registradas, intentelo uevamente tiene", co, "intentos")
            c += 1
            co -= 1

        elif (x not in cuenta) and (xx in password):
            print("Su cuenta o contrase;a no estan registradas, intentelo uevamente tiene", co, "intentos")
            c += 1
            co -= 1

        elif (x in cuenta) and (xx in password):
            for i in range(len(password)):
                if cuenta[i] == password[i]:
                    print(menu())
                elif cuenta[i] != password[i]:
                    print("mal")
                else:
                    print("Hay algo aml en el codigo.")
        else: 
            print("Si sale esto es porque hay algo mal :c.")





#Inicio codigo:
cuenta = []
password = []
b = 1

inicio()
x1 = int(input("Ingrese cuantas cuentas desea registrar: "))
while b <= x1:
    cx = int(input(f"Digite la cuenta numero {b}: "))
    cuenta.append(cx)
    px = int(input(f"Digite la contrase;a de la cuenta numero {b}: "))
    password.append(px)
    b += 1
print("CUENTAS", cuenta)
print("CONTRASE:AS", password)

inicioc()
inicio()
