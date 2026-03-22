# Sistema de Inventario de Reactivos Químicos

## Descripción del proyecto

Este repositorio contiene un **sistema de inventario de reactivos químicos** desarrollado en **Python**, orientado a un entorno real de **producción de detergentes**.

El proyecto forma parte de un proceso de formación en programación y tiene como objetivo demostrar el dominio de los **fundamentos de Python**, aplicados a un caso práctico relacionado con el área química e industrial.

El sistema permite **registrar, visualizar y eliminar reactivos químicos**, incorporando validaciones para evitar errores comunes como códigos duplicados.

---

## Objetivos

* Aplicar los fundamentos de Python en un proyecto práctico.
* Integrar conocimientos de programación con un contexto químico-industrial.
* Desarrollar un sistema claro, funcional y fácil de mantener.
* Demostrar buenas prácticas de organización y modularización del código.
* Crear un proyecto apto para evaluación académica y portafolio profesional.

---

## Funcionalidades

* Agregar reactivos químicos al inventario.
* Visualizar todos los reactivos registrados.
* Eliminar reactivos por código.
* Validar entradas del usuario.
* Evitar códigos duplicados.

---

## Estructura del proyecto

```
inventario_reactivos/
│
├── main.py          # Programa principal
├── inventario.py    # Gestión de reactivos
├── validaciones.py  # Validaciones de datos
└── README.md        # Documentación del proyecto
```

---

## Descripción de los módulos

### main.py

Archivo principal que contiene el menú del sistema y controla el flujo del programa. Se encarga de interactuar con el usuario y llamar a las funciones de los otros módulos.

### inventario.py

Módulo encargado de la gestión de los reactivos químicos. Utiliza listas, diccionarios y sets para almacenar y manipular los datos.

### validaciones.py

Contiene funciones que validan los datos ingresados por el usuario, como códigos, textos y cantidades.

---

## Estructuras de datos utilizadas

* **Listas (`list`)**: almacenan los reactivos.
* **Diccionarios (`dict`)**: representan cada reactivo químico.
* **Conjuntos (`set`)**: evitan códigos duplicados.
* **Tuplas (`tuple`)**: almacenan datos inmutables como el estado del reactivo.

---

## Requisitos técnicos cumplidos

* Uso de `input()` y `print()`.
* Condicionales (`if`, `elif`, `else`).
* Bucles (`while`, `for`).
* Funciones personalizadas.
* Modularización del código.
* Manejo de errores con `try / except`.
* Código limpio y comentado.

---

## Cómo ejecutar el programa

1. Abrir una terminal.
2. Navegar a la carpeta del proyecto.
3. Ejecutar el siguiente comando:

```
python main.py
```

---

## Explicación para evaluación

> *Este proyecto demuestra el uso de estructuras de control, funciones, estructuras de datos y modularización en Python, aplicados a un sistema realista de inventario de reactivos químicos para la producción de detergentes.*

---

## Posibles mejoras futuras

* Control de stock mínimo.
* Registro de lotes.
* Clasificación por tipo de reactivo.
* Estado del reactivo: apto / no apto.
* Persistencia de datos en archivos `.txt` o `.csv`.

---

## Contexto aplicado

El proyecto está orientado a un entorno real de **producción química**, integrando conocimientos de programación con procesos industriales, lo que aporta valor práctico y profesional al sistema.

---

## Conclusión

Este proyecto demuestra una correcta aplicación de los conceptos fundamentales de Python, junto con una organización clara del código y documentación adecuada.
