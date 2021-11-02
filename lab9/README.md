# Laboratorio 9
## Parte Dirigida
---

La visualización de datos es la representación gráfica de información y datos. Al utilizar elementos visuales como cuadros, gráficos y mapas, las herramientas de visualización de datos proporcionan una manera accesible de ver y comprender tendencias, valores atípicos y patrones en los datos.

La visualización de datos es otra forma de arte visual que capta nuestro interés y mantiene nuestros ojos en el mensaje. . Si podemos ver algo, lo interiorizamos rápidamente. Es contar historias con un propósito. Si alguna vez haz visto una gigantesca hoja de cálculo de datos y no te fue posible ver una tendencia, sabes cuán eficaz puede ser una visualización

### Leer un JSON como un diccionario:
---
```py
import json

f = open('<filename>.json')
d = json.load(f)
```



### Visualizar datos:
---
Para este laboratorio, vamos a utilizar la librería `matplotib`.
```py
import matplotlib.pyplot as plt
```

### Gráfico de barras
```py
plt.bar(<keys>, <values>)
plt.show()
```
Dónde `keys` y `values` son listas de igual longitud. Adicionalmente, se puede pasar el argumento `color` con una lista para poder escoger el color de cada barra.

### Scatterplot

```py
plt.plot(<valores x>, <valores y>)
plt.show()
```
Dónde los valores del eje `x` y `y` son listas de igual longitud. Como tercer parámetro se pueden ingresar distintos símbolos para representar la información como `*` para estrellas `o` para puntos o `x` para cruces.

Adicionalmente, se tiene el método `legend` el cual recibe una lista titulos para la leyenda y los métodos `xlabel` y `ylabel` para darles etiquetas a los ejes `x` e `y`.
```py
plt.legend(<titulos>)
plt.xlabel(<nombre>)
plt.ylabel(<nombre>)
```

### Gráficar sobre un mapa

Si se tiene un mapa como imagen de fondo, podemos graficar sobre este, utlizando los ejes `x` e `y` como coordenadas.

```py
im = plt.imread('imagen.png')
implot = plt.imshow(im)
```


## Ejemplo:

TODO

## Parte Práctica
---

### Ejercicio 1
Gráfico de barras de cuenta de tipos de pokemon

### Ejercicio 2

Scatterplot mostrando las debilidades de los pokemones iniciales (primeros 9)

### Ejercicio 3

Mostrar las ubicaciones de Articuno, Zapdos y Moltres

### Ejercicio 4

Mostrar todas las ubicaciones de Magikarp

### Entregable

Debe entregar un archivo `.py` con la solucion a cada ejercicio en una funcion `ejercicioX` (X siendo el número del ejercicio).