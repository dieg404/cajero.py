def menu():
    print("1. Consignar plata.")
    print("2. Retirar plata.")
    print("3. Consultar saldo.")
    print("4. Salir")


def inicio():
    





#Inicio codigo:

cedula =[]
password = []
b = 1


x1 = int(input("Ingrese cuantas cuentas desea registrar. "))
while b <= x1:
    cx = int(input(f"Digite la cuenta numero {b}"))
    cedula.append(cx)
    px = int(input(f"Digite la contrase;a de la cuenta nuemro {b}"))