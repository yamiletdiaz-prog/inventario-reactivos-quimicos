"""
Módulo de validaciones
"""

def validar_codigo(codigo: int, codigos: set) -> bool:
    """Valida que el codigo no exista en el conjunto de usados."""
    # Evita duplicados en el inventario.
    return codigo not in codigos


def validar_texto(texto: str) -> bool:
    """Valida que el texto no este vacio ni solo con espacios."""
    # Se usa strip para descartar espacios en blanco.
    return texto.strip() != ""


def validar_cantidad(cantidad: float) -> bool:
    """Valida que la cantidad sea positiva."""
    # Rechaza ceros y valores negativos.
    return cantidad > 0
