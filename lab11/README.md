# Lab-Ursina
## Parte Explicativa

**Ursina Engine**

Campo de la informática visual, donde se utilizan computadoras para generar imágenes visuales y espaciales del mundo real. Asi mismo, podemos definirlo como el arte de transmitir información, usando imágenes que son generadas mediante la computación.

En este campo, podemos encontrar un mundo donde visualizamos objetos en 3D, el cual sacamos mucho gusto de ello. Es gratificante poder desarrollar muchos vídeo juegos usando esta librería Ursina. Además, este campo puede ser dividido en diferentes áreas.

- Muestra de las areas, en seguida:

| ÁREAS DE DIVISION|
|:-----: |
| Interpretado 3D en tiempo real|
| Animación de computadora|
| Captura y creación de vídeo interpretado|
| Edición de efectos especiales
| Edición de imagen, y modelado

---
<h1 align="center"> ¿Quieres conocer qué facilita y en qué plataformas está disponible este motor? </h1>


<h2 align="center"> ¡Quédate en este espacio!  </h2>

Lo visualizamos, a continuación:

| FACILITA     | PLATAFORMAS |
| :--------- | :-----|
| El desarrollo de juegos  | Windows
| Visualizaciones y otros tipos de software  |Mac y Linux

---------
Para poder instalar la librería [Ursina Engine](https://www.ursinaengine.org/), se pueden utilizar  diferentes métodos.  En esta oportunidad, usaremos lo siguiente:

>##### Método:
Escribir en el terminal donde programemos, el siguiente comando: 
`pip install ursina` y clic en Enter.

------------
- Una vez instalada la librería, un proyecto de `ursina` tiene la siguiente forma:

![](https://i.ibb.co/qrxdPRL/Im23.png)

---
### DIBUJAR UNA ENTIDAD

Lo que continúa es un ejemplo en el cual, se dibuja un [cubo](https://www.ursinaengine.org/cheat_sheet.html#models "cubo") de color amarillo, en la posicion `(0,0,0)`el cual se ha rotado 45º en su eje `x` y 25º en su eje `y`,y se le aplica una textura `white_cube`.

![]( https://i.ibb.co/bFv2W99/Im3.png)
>**Parámetros que tambien recibe Entity:**
- `position`: Recibe una triple tupla con la forma `(x,y,z)`
- `texture`:Recibe el nombre de un archivo de textura (sin extensión), o puede usar una de las [texturas default](https://www.ursinaengine.org/cheat_sheet.html#textures).
- `color`: Recibe un color.
- `rotation`: Recibe una triple tupla con los grados de rotación en cada eje.

------------
### CÁMARA
Para visualizar los objetos de una mejor manera con diferentes ángulos, añadimos las siguientes líneas de código:

```
camera.orthographic = True
EditorCamera()
```
La cámara utiliza los siguientes controles:
- `click derecho`:Rota la cámara
- `screoll click`: Mueve la cámara
- `scroll`: Controla el zoom

------------
### EJEMPLO
Juntando todo lo mencionado anteriormente, tenemos el siguiente codigo, que genera dos cubos y dos esferas utilizando diferentes texturas, incluida la textura `fruit` proveniente del archivo `fruit.png`.

![Ejemplito](https://i.ibb.co/nRTX7zW/Cod1.png)

Y el resultado sería el siguiente:

![Result1](https://i.ibb.co/jDvyWCk/result1.png)

---
>Por otra parte, realizamos nuestra ejecución en otro ejemplo, con unas líneas de código; básicamente genera dos cubos y dos esferas utilizando diferentes texturas **(utec y estrellas)**, proveniente de los archivos `utec.jpg` y `estrellas.jpg`  e incluyendo un color a nuestra ventana del `result`.

El `result` de esta ejecución es el siguiente:

![Result2](https://i.ibb.co/qy3LZgP/Result2.png)

---
## Parte Práctica
Utilizando las herramientas explicadas anteriormente, dibujaré algunas [palabras](https://i.pinimg.com/564x/bd/b6/cd/bdb6cd9f52015c66fd48ec56a65f6b7e.jpg "iniciales") a base de entidades, utilizando una textura y color diferente para cada letra. Al menos una textura debe ser una externa a las incluidas con `ursina`.

------------
### Entrega del trabajo
En esta práctica, mostraré un gif del resultado de nuestra ejecución.
Para ello, se ha implementado una función del window que le da una forma exclusiva de poder observar nuestro objetivo.
De la misma manera, se añadió diferentes texturas para llevar a cabo nuestra misión.


| TEXTURAS UTILIZADOS     | ARCHIVOS PROVENIENTES |
| :--------- | :-----|
| `<arnold>`  | `arnold.jpg`
| `<estrellita>`  |`estrellita.jpg`
| `<pandita>`  |`pandita.jpg`
| `<iconito>`  |`iconito.jpg`
| `<pandita>`  |`pandita.jpg`
| `<lunita>`  |`lunita.jpg`

> **El gif resultante de nuestra práctica:**
  
![](https://media.giphy.com/media/mcMZwEWYMB3siTqdls/giphy.gif)
