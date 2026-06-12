import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "contraseña.json"


def load_passwords():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("El archivo de contraseñas está dañado o vacío. Se usará una lista nueva.")
        return []


def save_passwords(data):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        file.write("\n")


def ask_required_value(label):
    while True:
        value = input(label).strip()
        if value:
            return value
        print("Este campo no puede estar vacío.")


def add_password():
    service = ask_required_value("Servicio: ")
    username = ask_required_value("Usuario o correo: ")
    password = ask_required_value("Contraseña: ")

    entry = {
        "service": service,
        "username": username,
        "password": password
    }

    data = load_passwords()
    data.append(entry)
    save_passwords(data)

    print("Contraseña guardada correctamente.")


def view_passwords():
    data = load_passwords()

    if not data:
        print("No hay contraseñas guardadas.")
        return

    print("\nContraseñas guardadas:")
    for index, entry in enumerate(data, start=1):
        print(f"{index}. Servicio: {entry['service']}")
        print(f"   Usuario: {entry['username']}")
        print(f"   Contraseña: {entry['password']}")


def buscar_contraseña():
    data = load_passwords()

    if not data:
        print("No hay contraseñas guardadas.")
        return

    search = ask_required_value("Servicio a buscar: ").lower()
    results = [
        entry for entry in data
        if search in entry["service"].lower()
    ]

    if not results:
        print("No se encontraron contraseñas para ese servicio.")
        return

    print("\nResultados:")
    for index, entry in enumerate(results, start=1):
        print(f"{index}. Servicio: {entry['service']}")
        print(f"   Usuario: {entry['username']}")
        print(f"   Contraseña: {entry['password']}")


def eliminar_contraseña():
    data = load_passwords()

    if not data:
        print("No hay contraseñas guardadas.")
        return

    view_passwords()
    option = input("Número de la contraseña a eliminar: ").strip()

    if not option.isdigit():
        print("Debe ingresar un número válido.")
        return

    index = int(option) - 1
    if index < 0 or index >= len(data):
        print("No existe una contraseña con ese número.")
        return

    deleted = data.pop(index)
    save_passwords(data)
    print(f"Contraseña de {deleted['service']} eliminada correctamente.")


def buscar_password():
    buscar_contraseña()


def eliminar_password():
    eliminar_contraseña()
