
# Desafío - Manejo de excepciones

## Descripcion del proyecto

Usted trabaja para una empresa que se encuentra desarrollando una aplicación de galería de
fotos. Le han solicitado controlar que no sea posible modificar el alto o el ancho de una foto
creada, en caso de que se esté intentando modificar alguno de estos atributos por un valor
menor a 1, o mayor al valor máximo determinado por el atributo de clase MAX de la clase Foto.
Le solicitan además hacer este control mediante una excepción propia, ya que se desea
utilizar la misma excepción en otro sector del programa que recibe los valores de ancho y
alto, y desea validarlos antes de crear nuevas fotos.
Se le proporciona el código que permite crear instancias de Foto, donde usted debe agregar
el lanzamiento de la excepción en los métodos setter de ancho y alto, según las condiciones
indicadas.

## Requerimientos
- En un archivo error.py, crear la excepción DimensionError derivada de Exception.Sobreescribir el constructor, recibiendo los parámetros mensaje, dimension y maximo,y asignándoles los respectivos atributos de instancia. 
- En la misma clase anterior, sobrecargar el método __str__, de forma tal que si sólo se ha ingresado mensaje al crear la excepción, se retorna el método de la clase padre.En caso contrario, crear y retornar un mensaje de retorno utilizando los atributosmensaje y/o dimension y/o maximo.
- En el archivo foto.py entregado, modificar los métodos setter de alto y ancho, de forma tal que se lance una excepción de tipo DimensionError en caso de que el nuevo valor ingresado no cumpla con las condiciones descritas. En caso contrario, asignar el nuevo valor al atributo de instancia correspondiente.

## Instalacion

Requisitos previos
- Python >= 3.x
- Pip (administrador de paquetes de Python)
## Pasos de instalación
- Clona este repositorio en tu máquina local:
```bash
    git clone https://github.com/Vaniakmt/manejo_exepciones.git

```
