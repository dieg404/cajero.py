import time

def censurar(texto):
    return '*' * len(texto)

x = None
xx = None
p1 = None
p2 = None

def inicio():
    print("-" * 30)
    print("Bienvenid@s a Desfacol, si usted no pierde su plata nosotros la perdemos por usted :D")
    print("-" * 30)


def inicio2():
    global x, xx
    global p1, p2
    intento = 3
    co = 3
    for i in range(intento):
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
                    bloqueo()
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
                bloqueo()
            elif co > 0:
                print("Su cuenta o contrase;a no estan registradas, intentelo nuevamente tiene", co, "intentos")
            else:
                print("Esto no debe salir")
        elif (((x not in cuenta) and (xx in password)) or ((x not in cuenta) and (xx not in password))):
            co -= 1
            if co == 0:
                print("No tiene mas intentos")
                bloqueo() 
            elif co > 0:
                print("Su cuenta o contrase;a no estan registradas, intentelo nuevamente tiene", co, "intentos")
            else:
                print("Esto no debe salir")
         
        else:
            print("Esto no debe salir")
            break



def menu():
    print("1. Consignar plata.")
    print("2. Retirar plata.")
    print("3. Consultar saldo.")
    print("4. Salir")


def bloqueo():
    print("-" * 30)
    print("El cajero se bloqueo, gracias por su visita.")
    print("-" * 30)


def consignar():
    pp = plata.index(x and xx)
    if p1 and p2 == pp:
        print(f"Su saldo inicial es {cuenta}")
        valor = int(input("Ingrese cuanta plata desea consignar, valor maximo 10000000."))
        if valor > 10000000:
            print("No puede hacer consignaciones mayores a 10000000, intentelo nuevamente.")
        elif valor == 10000000:
            








#Inicio codigo:
cuenta = []
password = []
plata = []
cantidad = 0
b = 1


inicio()
x1 = int(input("Ingrese cuantas cuentas desea registrar: "))
print("-" * 30)
while b <= x1:
    cx = int(input(f"Digite la cuenta numero {b}: "))
    cuenta.append(cx)
    px = int(input(f"Digite la contrase;a de la cuenta numero {b}: "))
    password.append(px)
    plata.append(cantidad)

    print("-" * 30)
    b += 1
print("CUENTAS", cuenta)
print("CONTRASE:AS", password)
print("PLATA", plata)

while True:
    print("-" * 30)
    x = int(input("Digite su cedula para iniciar sesion: "))
    xx = int(input("Ingrese su contrase;a: "))
    print("-" * 30)
    inicio2()
    break