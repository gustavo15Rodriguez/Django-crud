# Django crud

Primer proyecto realizado en django. 

## Dependencias 

* Django==2.2.3
* django-crispy-forms==1.9.0
* psycopg2==2.8.5
* pytz==2019.3
* sqlparse==0.3.1


## Instalar dependencias 

~~~
pip install -r requirements.txt
~~~


## Comandos para Django

No olvide antes de ejecutar los dos comandos siguientes, crear una base de datos en postgreSQL con el 
nombre de `miprueba` y añadir la contraseña de su usuario de postgres (Puede editar 
esta configuracion en el apartado la base de datos en los `settings.py`  del proyecto).
~~~
python manage.py makemigrations
~~~

~~~
python manage.py migrate
~~~

~~~
python manage.py collectstatic
~~~


~~~
python manage.py createsuperuser
~~~

~~~
python manage.py runserver
~~~

## Funcionamiento

Para ejecutar el proyecto usted debe instalar las dependencias, despues ejecutar los comandos de django en el
orden especificado.