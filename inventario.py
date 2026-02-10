"""
Módulo de gestión de reactivos químicos
"""

reactivos = []
codigos_usados = set()


def agregar_reactivo(reactivo: dict) -> None:
    """Agrega un reactivo y registra su codigo como usado."""
    # Mutacion de estructuras en memoria: lista y set permanecen sincronizados.
    reactivos.append(reactivo)
    codigos_usados.add(reactivo["codigo"])


def obtener_reactivos() -> list:
    """Devuelve la lista actual de reactivos."""
    # Retorna la referencia directa; los cambios impactan el inventario.
    return reactivos


def eliminar_reactivo(codigo: int) -> bool:
    """Elimina un reactivo por codigo y confirma si se logro."""
    # Busca el reactivo y, si existe, lo remueve de ambas estructuras.
    for reactivo in reactivos:
        if reactivo["codigo"] == codigo:
            reactivos.remove(reactivo)
            codigos_usados.remove(codigo)
            return True
    # No se encontro el codigo solicitado.
    return False
