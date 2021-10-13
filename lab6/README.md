# Laboratorio 6
## Parte Dirigida
---
SQL o “Structure Query Language” es un lenguaje de acceso a bases de datos que le permite al usuario ejecutar operaciones entre estos datos relacionados con el apoyo de cálculos relacionales en forma de lenguaje de comandos.

A continuación les presentaremos una guía de los principales comandos para realizar las operaciones más básicas de acceso a base de datos en este lenguaje.

### Creación de tablas:
---
```sql
CREATE TABLE <nombre de la tabla> (
    <nombre de columna> <tipo de dato>,
    <nombre de columna> <tipo de dato>,
    <nombre de columna> <tipo de dato>,
    <nombre de columna> <tipo de dato>,
    PRIMARY KEY <nombre de columna>
);
```

Los nombres de la tabla y nombres de las columnas no deben tener espacios en blanco.

Keywords utiles:
- ```NOT NULL```: Indica que la columna no puede estar en blanco (obligatoria).
- ```PRIMARY KEY```: Indica columna con valores únicos usados para identificar a las filas.
- ```AUTO_INCREMENT```: Indica que el valor de esta columna no se tiene que insertar y va a crecer automáticamente.


### Inserción de datos:
---
```sql
INSERT INTO <nombre de tabla> (<columnas>) VALUES (<datos>);
```

### Selección de datos:
---
```sql
SELECT <columnas> FROM <nombre de tabla> WHERE <condición>;
```

### Eliminar una tabla:
---
```sql
DROP TABLE <nombre de tabla>;
```

## Ejemplo:

```sql
-- Crear la tabla
CREATE TABLE mercado (
    id INTEGER NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    precio FLOAT NOT NULL,
    calorias FLOAT,
    PRIMARY KEY (id)
);

-- Insertar un producto
INSERT INTO mercado (nombre, precio, calorias) VALUES ('Sublime', 1.50, 166);

-- Seleccionar todos los productos con precio mayor a 1.
SELECT * FROM mercado WHERE precio > 1;

-- Borrar una tabla
DROP TABLE mercado;
```

## Parte Calificada
---

### Chess Club

Durante la pandemia, el ajedrez fue uno de los pocos deportes que pudo mantenerse en actividad.

Gracias a las diferentes aplicaciones web para jugar ajedrez online, sumado a las plataformas de streaming, hicieron que el ajedrez sea uno los deportes más seguidos durante la pandemia. Incluso [logró posicionarse como uno de los géneros más vistos](https://www.theverge.com/21292747/chess-twitch-games-viewership-stream-hikaru-nakamura) en plataformas como Twitch.

Adicionalmente, la aparición de series como "The Queen's Gambit" originó el interés de gran parte del mundo por el ajedrez, popularmente conocido como "el deporte ciencia".

### UTEC

La popularidad del ajedrez ha llegado a la UTEC. Muchos alumnos han deseado inscribirse al club de ajedrez de la universidad. El presidente del club, Magnus Carlsen, empezó utilizando un Excel para guardar la lista de los integrantes del club. Sin embargo, al darse cuenta de la gran cantidad de nuevos miembros, ha decido optar por la creación de una base de datos para almacenar la información de los integrantes del club.

La información que desea almacenar de cada integrante es la siguiente:

- Nombre completo
- Ranking Fide (opcional). *Es un número de 0 a 3000*
- Género (opcional).
- Email

Ayúdelo a crear dicha base de datos.

- Cree la tabla `jugador` con las columnas indicadas anteriormente (tomando en cuenta los tipos de dato para cada columna, y asegurese si los datos son obligatorios o no).
- Usa una columna `id` como llave primaria, esta debe incrementarse con cada inserción.
- Inserta en la tabla tus datos y los de tus compañeros.
- Genera un query que te permita seleccionar a todos los jugadores que cuenten con un Ranking FIDE mayor a >1500.

Puede usar su gestor de bases de datos de preferencia, o en caso no tenga uno [instalado](https://www.mysql.com/downloads/), puede utilizar el siguiente [recurso online](https://extendsclass.com/mysql-online.html).

### Entregable

Debe entregar un archivo `.txt` con los queries utilizados para crear la tabla, insertar los datos y finalmente el query para seleccionar a los jugadores.
