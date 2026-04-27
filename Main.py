
from lista import Lista

def menu():
    print("\n--- MENÚ LISTA ENLAZADA ---")
    print("--- ADVERTENCIA ESTE PROGRAMA--- \n---SOLO ACEPTA VALORES NUMÉRICOS--- \n---DE 0 A 9 ---")
    print("1. Insertar al inicio")
    print("2. Insertar al final")
    print("3. Mostrar lista")
    print("4. Buscar elemento")
    print("5. Eliminar primer elemento")
    print("6. Eliminar por valor")
    print("7. Tamaño de la lista")
    print("8. Invertir lista")
    print("9. Jose")
    print("0. Salir")
    return input("Seleccione una opción: ")

def main():
    mi_lista = Lista()

    while True:
        opcion = menu()

        if opcion == "1":
            dato = input("Ingrese valor: ")
            mi_lista.insert_at_beginning(dato)

        elif opcion == "2":
            dato = input("Ingrese valor: ")
            mi_lista.insert_at_end(dato)

        elif opcion == "3":
            mi_lista.display()

        elif opcion == "4":
            objetivo = input("Buscar: ")
            if mi_lista.buscarNodo(objetivo):
                print("Encontrado")
            else:
                print("No encontrado")

        elif opcion == "5":
            mi_lista.borrarPrimerNodo()

        elif opcion == "6":
            valor = input("Eliminar: ")
            mi_lista.eliminar_por_valor(valor)

        elif opcion == "7":
            print("Tamaño:", mi_lista.tamano())

        elif opcion == "8":
            mi_lista.invertir()

        elif opcion == "9":
            k=int(input("la secuencia de eliminacion:"))
            mi_lista.jose(k)

        elif opcion == "0":
            break

        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()