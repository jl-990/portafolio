import json
from datetime import datetime
import os

FILENAME = "servicios_diarios.json"


def cargar_servicios():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def guardar_servicios(servicios):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(servicios, f, indent=2, ensure_ascii=False)


def agregar_servicio():
    descripcion = input("Descripci\u00f3n del servicio: ")
    fecha = input("Fecha (YYYY-MM-DD) [hoy]: ")
    if not fecha:
        fecha = datetime.now().strftime("%Y-%m-%d")
    servicio = {"descripcion": descripcion, "fecha": fecha}
    servicios = cargar_servicios()
    servicios.append(servicio)
    guardar_servicios(servicios)
    print("Servicio agregado.")


def listar_servicios():
    servicios = cargar_servicios()
    if not servicios:
        print("No hay servicios registrados.")
    else:
        for s in servicios:
            print(f"{s['fecha']}: {s['descripcion']}")


def main():
    while True:
        print("\n1. Agregar servicio\n2. Listar servicios\n3. Salir")
        opcion = input("Seleccione una opci\u00f3n: ")
        if opcion == "1":
            agregar_servicio()
        elif opcion == "2":
            listar_servicios()
        elif opcion == "3":
            break
        else:
            print("Opci\u00f3n no v\u00e1lida.")


if __name__ == "__main__":
    main()

