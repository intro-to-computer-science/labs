# Laboratorio 8
## Parte Dirigida
---

Las bases de datos NoSQL están diseñadas específicamente para modelos de datos específicos y tienen esquemas flexibles para crear aplicaciones modernas. Las bases de datos NoSQL son ampliamente reconocidas porque son fáciles de desarrollar, por su funcionalidad y el rendimiento a escala. Esta página incluye recursos que lo ayudan a comprender mejor las bases de datos NoSQL y comenzar a usarlas.

Dentro de las bases de datos NoSQL, probablemente una de las más famosas sea MongoDB. Con un concepto muy diferente al de las bases de datos relacionales, se está convirtiendo en una interesante alternativa.

MongoDB es una base de datos orientada a documentos. Esto quiere decir que en lugar de guardar los datos en registros de tablas, guarda los datos en documentos. Estos documentos son almacenados en BSON, que es una representación binaria de [JSON](https://beginnersbook.com/2015/04/json-tutorial/).

### Creación de colección:
---
```
db.createCollection(<nombre>);
```



### Inserción de datos:
---
Insertar un elemento
```
db.<collectionName>.insertOne({<data>})
```
Insertar múltiples elementos
```
db.<collectionName>.insertMany([{<data>},{<data>},{<data>},{<data>}])
```

### Búsqueda de datos:
---
Seleccionar todos los elementos de la colección:
```
db.<collectionName>.find()
```
Seleccionar todos los elementos que cumplan una condición:
```
db.<collectionName>.find({<key>: <value>})
```
Seleccionar elementos usando operadores lógicos:
```
db.<collectionName>.find({$and: [{<key>: <value>},{<key2>: <value2>}]})
```
```
db.<collectionName>.find({$or: [{<key>: <value>},{<key2>: <value2>}]})
```
Seleccionar elementos con comparadores:
```
db.<collectionName>.find({<key>: {$gt: <value>}})
```
- `$gt` busca los elementos cuyo valor en el `key` sea `mayor` a el valor indicado en `value`.
- `$lt` busca los elementos cuyo valor en el `key` sea `menor` a el valor indicado en `value`.
- `$gte` busca los elementos cuyo valor en el `key` sea `mayor o igual` a el valor indicado en `value`.
- `$lte` busca los elementos cuyo valor en el `key` sea `menor o igual` a el valor indicado en `value`.

Se le puede agregar el método `.count()` para que te indique cuantos elementos coinciden con la consulta.
### Actualización de datos:
---
```
db.<collectionName>.update(<query>, {$set: {<key>: <newValue>}}, {"multi": true/false})
```
- `query`: Busca los datos a actualizar, sigue el mismo formato que una consulta find (`{<key>: <value>}`)
- `multi`: `true` indica que se actualizan todos los valores que coincidan con el query, `false` indica que solo el primer valor que coincida se va a actualizar.

### Borrar una colección
```
db.<collectionName>.drop()
```

## Ejemplo:
Crear la colección:

```
db.createCollection("iris");
```
Insertar datos:
```
db.iris.insertMany([
  {"sepalLength": 5.1, "sepalWidth": 3.5, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"},
  {"sepalLength": 4.9, "sepalWidth": 3.0, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"},
  {"sepalLength": 4.7, "sepalWidth": 3.2, "petalLength": 1.3, "petalWidth": 0.2, "species": "setosa"},
  {"sepalLength": 4.6, "sepalWidth": 3.1, "petalLength": 1.5, "petalWidth": 0.2, "species": "setosa"},
  {"sepalLength": 5.6, "sepalWidth": 2.5, "petalLength": 3.9, "petalWidth": 1.1, "species": "versicolor"},
  {"sepalLength": 5.9, "sepalWidth": 3.2, "petalLength": 4.8, "petalWidth": 1.8, "species": "versicolor"},
  {"sepalLength": 6.1, "sepalWidth": 2.8, "petalLength": 4.0, "petalWidth": 1.3, "species": "versicolor"},
  {"sepalLength": 6.3, "sepalWidth": 2.5, "petalLength": 4.9, "petalWidth": 2.0, "species": "virginica"},
  {"sepalLength": 6.2, "sepalWidth": 3.4, "petalLength": 5.4, "petalWidth": 2.3, "species": "virginica"},
  {"sepalLength": 5.9, "sepalWidth": 3.0, "petalLength": 5.1, "petalWidth": 1.8, "species": "virginica"}
]);
```
Buscar las flores de especie `setosa` con una longitud de sepalo mayor a `4.8`
```
db.iris.find({$and: [{"species": "setosa"}, {"sepalLength": {$gt: 4.8}}]});
```
Cambiar todas la especie de todas las entradas de especie `setosa` a el numero `1`.
```
db.iris.update({"species": "setosa"}, {$set: {"species": 1}});
```


## Parte Práctica
---

### Pokédex

Existen 151 Pokémon nativos a la región Kanto. Puedes encontrar un `dataset` con la información de estos en el archivo `pokemon.json`. El entrenador Paolo, busca convertirse en un verdadero maestro Pokémon, para esto, necesita tu ayuda para aprender más sobre ellos.

- Genere una colección de MongoDB llamada `pokedexsucodigoutec` e inserte los datos que se encuentran en el archivo `pokemon.json`.

Paolo tiene un Charizard muy poderoso; sin embargo, quiere saber cuales son los Pokémon que son débiles a sus ataques.

- Genere una consulta que te muestre la información de `Charizard`. Podrás encontrar sus tipos en el campo `types`.
- A partir de esos tipos, genere una consulta que te indique aquellos Pokémon que sean débiles a los tipos de `Charizard`. Este dato se encuentra en el campo `weaknesses`.

Adicionalmente, deberás generar las siguientes consultas:
- Genera una consulta que actualice la entrada del Pokémon cuyo `id` coincida con los dos últimos dígitos de tu código de alumno. Utilizando `update`, agregue el campo `owner` e indicale tu nombre.
- Genera una consulta que muestre todos los Pokémon cuyo `type` sea `Dragon` o `Psychic`.
- Genera una consulta que muestre todos los Pokémon cuyo `type` sea `Bug` y cuyo `weakness` también lo sea.
- Genera una consulta que muestre todos los Pokémon cuyo `spawn chance` sea menor a 1.

Puede usar su gestor de bases de datos local, o en caso no tenga uno [instalado](https://www.mongodb.com/try/download/community), puede utilizar el siguiente [recurso online](https://www.pdbmbook.com/playground/mongo/wine/view/pgdb____1635317177_6178f5b93eac0).

### Entregable

Debe entregar un archivo `.txt` con los queries pedidos anteriormente.
