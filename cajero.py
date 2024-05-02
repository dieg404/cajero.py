import time

x = None
xx = None
p1 = None
p2 = None

def inicio():
    print("-" * 30)
    print("Bienvenid@s a Desfacol, si usted no pierde su plata nosotros la perdemos por usted :D")
    print("-" * 30)


def inicio2():
    global plata, cuenta, x, xx, password, p1, p2
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
    global plata, cuenta, x, xx, password, p1, p2
    valor = 0
    pp = plata.index(x)
    vc = int(input("Puede consignar maximo tres veces, cuantas veces desea realizar el proceso? "))
    while vc >= 1 and vc <=3:
        if pp == p1:
            print(f"Su saldo inicial es {plata[pp]}")
            valor = int(input("Ingrese cuanta plata desea consignar, valor maximo que puede tener en su cuenta es de 10000000: "))
            if valor > 10000000:
                print("No puede hacer consignaciones mayores a 10000000, intentelo nuevamente:")
            elif valor == 10000000:
                plata[pp] += valor
                print(f"Consigno {valor}, su saldo actual es de {plata[pp]} ya no puede consignar mas plata, que pase buen dia. ")
                break
            elif 0 < valor <= 10000000:
                if valor <= 10000000:
                    plata[pp] += valor
                    print(f"Consigno {valor}, su saldo actua es de {plata[pp]}.")
                elif valor > 10000000:
                    print("Su consignacion", valor, "excede los 10000000, intentelo nuevamente.")
                else:
                        print("Esto no debe salir. 3")
            else:
                    print("Esto no debe salir. 2")
        else:
            print("Esto no debe salir. 1")


def retirar():
    global plata, cuenta, x, xx, password, p1, p2
    valor = 0
    pp = plata.index(x)
    vc = int(input("Puede retirar maximo dos veces, cuantas veces desea realizar el proceso? "))
    while vc >= 1 and vc <=2:
        if pp == p1:
            print(f"Su saldo inicial es {plata[pp]}")
            valor = int(input("Ingrese cuanta plata desea retirar, valor maximo 3000000."))
            if valor > 3000000:
                print("No puede hacer retiros mayores a 3000000, intentelo nuevamente.")
            elif valor == 3000000:
                plata[pp] -= valor
                print(f"Retiro {valor}, su saldo actual es de {plata[pp]} ya no puede retirar mas plata, que pase buen dia. ")
                break
            elif 0 < valor <= 3000000:
                if valor <= 3000000:
                    plata[pp] -= valor
                    print(f"Retiro {valor}, su saldo actua es de {plata[pp]}.")
                elif ((plata[pp] - valor) < plata[pp]):
                    print("Su retiro", valor, "excede el valor que tiene en su cuenta, intentelo nuevamente.")
                else:
                        print("Esto no debe salir. 3")
            else:
                print("Esto no debe salir. 2")
        else:
            print("Esto no debe salir. 1")


def consulta():
    global plata, cuenta, x, xx, password, p1, p2
    pp = plata.index(p1 and p2)
    print("Su saldo final es", plata[pp])


def salir():
    print("chao")





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
    inicio2()
    xop = int(input("Ingrese la opcion que desea: "))
    if 1 <= xop <= 4:
        if xop == 1:
            consignar()
        elif xop == 2:
            retirar()
        elif xop == 3:
            consulta()
        elif xop == 4:
            salir()
        else:
            print("esto no debe salir")
    else:
        print("Opcion invalida, intentelo nuevamente.")
        
#guardado version 12


