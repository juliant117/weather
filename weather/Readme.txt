weatherapp

programa para la visualizacion del pronostico temperatura maxima, temperatura minima y estado de clima para los proximos 4 dias dependiendo la ciudad ingresada

este programa esta implementado principalmente con python y django principalmente
clonar repositorio de github
>git clone https://github.com/juliant117/weather.git

una vez descargado el repositorio es necesario asegurarse con contar con python 3.8 en adelante

crear un entorno virtual
>virtualenv venv
activar entorno virtual
>./venv/Scripts/activate   

en la direccion del proyecto donde se visualice requirements instalar dichas librerias
>pip install -r requirements.txt

el programa consta de una API para poder acceder a openweather map para esto se tiene una api key que es la enviada por correo,
esta se implementara en la misma direccion del archivo manage.py por medio del archivo .env
>OPENWEATHER_API_KEY= '(API_KEY enviada)'

una vez implementada se necesita realizar la migracion de django por medio de 
>python manage.py makemigrations


y correr la migracion
>python manage.py migrate

finalmente podemos correr el proyecto de manera local 
>python manage.py runserver
