"""
Sistema de inventario de reactivos químicos
Autor: Yamilet Díaz
Descripción:
Este sistema permite gestionar un inventario de reactivos químicos utilizados en la producción de detergentes.
"""

from inventario import (
    agregar_reactivo,
    obtener_reactivos,
    eliminar_reactivo,
    codigos_usados
)
from validaciones import (
    validar_codigo,
    validar_texto,
    validar_cantidad
)


def mostrar_menu():
    """Imprime el menu principal en pantalla."""
    print("""
🧪 MENÚ INVENTARIO DE REACTIVOS
1. Agregar reactivo
2. Ver inventario
3. Eliminar reactivo
4. Salir
""")


def main():
    """Ejecuta el flujo principal de la aplicacion."""
    while True:
        # Bucle principal: solicita una opcion y ejecuta la accion indicada.
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                # Entrada y validacion campo por campo del nuevo reactivo.
                codigo = int(input("Código del reactivo: "))
                if not validar_codigo(codigo, codigos_usados):
                    print("❌ Código duplicado")
                    continue

                nombre = input("Nombre del reactivo: ")
                if not validar_texto(nombre):
                    print("❌ Nombre inválido")
                    continue

                cantidad = float(input("Cantidad disponible: "))
                if not validar_cantidad(cantidad):
                    print("❌ Cantidad inválida")
                    continue

                unidad = input("Unidad (kg / L / g): ")
                if not validar_texto(unidad):
                    print("❌ Unidad inválida")
                    continue

                # Estructura del reactivo usada por el modulo de inventario.
                reactivo = {
                    "codigo": codigo,
                    "nombre": nombre,
                    "cantidad": cantidad,
                    "unidad": unidad,
                    "estado": ("apto para producción",)
                }

                # Alta en inventario si todas las validaciones fueron correctas.
                agregar_reactivo(reactivo)
                print("✅ Reactivo agregado correctamente")

            except ValueError:
                # Maneja entradas no numericas en codigo o cantidad.
                print("❌ Datos incorrectos")

        elif opcion == "2":
            # Consulta y listado del inventario.
            reactivos = obtener_reactivos()
            if not reactivos:
                print("📭 Inventario vacío")
            else:
                # Imprime cada reactivo en un formato simple y legible.
                for r in reactivos:
                    print(
                        f"Código: {r['codigo']} | "
                        f"{r['nombre']} | "
                        f"{r['cantidad']} {r['unidad']}"
                    )

        elif opcion == "3":
            try:
                # Eliminacion por codigo con confirmacion de existencia.
                codigo = int(input("Código a eliminar: "))
                if eliminar_reactivo(codigo):
                    print("🗑️ Reactivo eliminado")
                else:
                    print("❌ Reactivo no encontrado")
            except ValueError:
                # Entrada invalida si no es un numero entero.
                print("❌ Código inválido")

        elif opcion == "4":
            # Salida del sistema.
            print("👋 Saliendo del sistema")
            break

        else:
            print("❌ Opción inválida")


if __name__ == "__main__":
    main()
