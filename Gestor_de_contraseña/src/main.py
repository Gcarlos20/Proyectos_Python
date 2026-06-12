from gestor_contraseña import (
    add_password,
    buscar_contraseña,
    eliminar_contraseña,
    view_passwords,
)


def menu():
    print("Bienvenido al gestor de contraseñas")

    while True:
        print("\n1. Agregar contraseña")
        print("2. Mostrar contraseñas")
        print("3. Buscar contraseña")
        print("4. Eliminar contraseña")
        print("5. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            add_password()
        elif opcion == "2":
            view_passwords()
        elif opcion == "3":
            buscar_contraseña()
        elif opcion == "4":
            eliminar_contraseña()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    menu()
