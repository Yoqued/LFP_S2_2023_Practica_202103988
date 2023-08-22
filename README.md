# MANUAL TECNICO
    - ## Introducción
    - ## Lógica

## *Introducción*
El programa desarrollado; es para la facilidad de la laectura de de un archivo tipo texto; efectuando acciones que se necestian; 
Dichas acciones son *crear_producto* ,  *agregar_stock*  y  *vender_producto*, dicha sintaxis usada para poder hacer acciones dentro del sistema
que vendran en un archivos de tipo *Texyto*. El sistema tiene la capacidad de poder dectectar errores tales como, si la *Ubicación* no coinciden, si la cantidad *Vendida* supera la cantidad que hay en stock, o si tambien si no existe cantidad disponible para vender; dichas acciones no se pueden ver; para ver que se efecturaron los cambios, el programa genera un archivo .txt donde podran ver un resumen de la cantidad cantidad de producto, cantidad del total que queda, precios, etc.

## *Lógica*

### Fución *MenuInicial()*
Esta función esta almacenada la lógica del menú; aqui en la funcion se podran mostrar las opciones que tiene disponible el programa, entonces se le presentaran en forma numerica y en base a los numero que ingrese ara las acciones necesarias, de tal modo que al usuario pueda ingresar un valor no considerado, se le mostrara un mensaje que dira: ingrese valores dentro del rango.

### Función *InventarioInicial() y limpiadorRuta()*
La primera funcion se estara ejecutando la lectura del archivo de texto que se usara para poder tener un valor con el cual trabajar; dichas acciones se comenzara pidiendo la ruta del archivo que se desea leer, al pedir esta ruta pasara a la funcion *limpiadorRuta*. En esta función lo que hara es poder limpiar la ruta para que pueda hacer la lectura correcta y no puedad dar un error que pueda afectar el funcionamiento del programa. Siguiendo con la función *InventarioInicial* aqui a la hora de la lectura; el programa separa los datos en base a 2 limitadores que son " "(Espacio)  y ";"(Punto y coma) cuya sintaxis es necesaria par poder tener el mejor funcionamiento del programa; el programa separa los datos en "Nombre", "Cantidad", "Precio unitario" y "Ubicación".

### Función *Movimientos()*
se estara ejecutando la lectura del archivo de texto que se usara para poder tener un valor con el cual trabajar; dichas acciones se comenzara pidiendo la ruta del archivo que se desea leer, al pedir esta ruta pasara a la funcion *limpiadorRuta*. En esta función lo que hara es poder limpiar la ruta para que pueda hacer la lectura correcta y no puedad dar un error que pueda afectar el funcionamiento del programa. Siguiendo con la funcion *Movimientos* en la lectura se pude separar en 2 opciones *agregar_stock*  y  *vender_producto*; cuyas opciones son aumentar datos o bien restar datos, tomando en cuenta que si no hay un producto en la ubicación no se podra efectuar dicho cambio; si no se hay la cantidad necesario que se necesita vender, de igual manera no podra vender porque no hay cantidad necesaria de restar o si no hay nada de producto no se podra vender.

### Función *CrearInforme()*
En esta funcion se estara crenado un archivo .txt cuyo usuario podra nombrar de la manera que el quiera, este informe se podra visualizar el Nombre de cada producto, cantidad existente, precio unitario, total que es la cantidad multiplicada por el precio unitario y la ubicación de cada una de esta.