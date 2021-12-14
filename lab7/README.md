# Lab 7 - PC1 Office Hours

Se les recomienda a los alumnos revisar los siguientes temas para la PC1

## Puertas lógicas

Repasar el ejercicio que hicimos utilzando:

https://academo.org/demos/logic-gate-simulator/

Solo podra utilizar AND, OR y NOT.

## Operaciones binarias en Python

- `&` : And
- `|` : Or
- `^` : XOR

[Ejemplo](./op_binarios.py)

## GitHub Markdown

Repasar la sintaxis de GitHub Markdown:

https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

## Crear un API

Recordar que los pasos para crear un api son:

1. Agregar números a la url.
```python
@app.route('/operaciones/<num1>/<num2>', methods=['GET'])
```

2. Agregar los números como parámetros de la función.
```python.
def ejercicio2(num1, num2):
```

3. Codificar lo que nos pide el problema.
```python.
suma = int(num1) + int(num2)
resta = int(num1) - int(num2)
mult = int(num1) * int(num2)
divi = int(num1) / int(num2)
```

4. Devolver el resultado del problema.
```python.
return f"suma: {suma} resta: {resta} mult: {mult} divi: {divi}"
```

## SQL

Repasar los comandos SQL para:

- Crear una tabla (CREATE TABLE)
- Insertar valores (INSERT INTO)
- Mostrar valores de la tabla (SELECT)
- Borrar tabla (DROP TABLE)