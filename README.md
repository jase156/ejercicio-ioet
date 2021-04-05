# Ejercicio práctico ioet 
Ejercicio práctico elaborado en Python para el cálculo de valores a pagar según las horas trabajadas.  
 
 
## Comenzando 🚀 
Para el cálculo de las horas trabajadas se basa en la tabla  
 
 
... 
Monday - Friday  
00:01 - 09:00 25 USD  
09:01 - 18:00 15 USD  
18:01 - 00:00 20 USD  
Saturday and Sunday  
00:01 - 09:00 30 USD  
09:01 - 18:00 20 USD  
18:01 - 00:00 25 USD  
... 
  
El input será un archivo de texto “.txt” que tendrá líneas con el formato   
 
 
... 
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00  
... 
  
Lo cual representa el horario de trabajo por cada día de la semana   
 
 
### Acerca del ejercicio 🔩 
 
 
Para la construcción del ejercicio se hizo uso del patrón de arquitectura modelo vista controlador y se estructuro dividiéndolo en 2 paquetes principales, el cual son “core” y “modules”.  
Dentro de core, se encuentra todos los módulos que pueden ser reutilizados en otros ejercicios, así como un módulo provider, el cual provee los datos; para esta versión se obtiene los datos de un archivo txt, pero si se desea, al crear otro provider y modificar a donde apunta Model el cambio seria transparente y de poco impacto.  
En modules, se creó el subpaquete pay, el cual tiene la funcionalidad en sí, dividida en un modelo, una vista, un controlador y la lógica de negocio. El controlador se encarga de conectar el modelo con las vistas previo procesamiento de datos con ayuda de las funciones de business.   
 
 
### Pre-requisitos 📋 
Tener instalado Python 3 
 
 
## Ejecutar programa ⚙️ 
En la carpeta raíz ejecutar  
 
 
... 
python main.py 
... 
 
 
## Ejecutando las pruebas ⚙️ 
En la carpeta raiz ejecutar  
 
 
... 
python test.py 
... 
 
 
## Autores ✒️ 
* **Javier Sarango** - *Construcción* 
 