# ApiRest_TipoCambio
Rest API creada en Flask que forma parte del proyecto de Automatización Exchange Rate (PAER)

![Video_11_partI](https://user-images.githubusercontent.com/7143758/224461481-e70f5685-368a-45dd-9088-2e25f3d37d75.png)


El módulo en Python config.py contiene información sobre parámetros de conexión a la BD MYSQL en la nube es por ello que no se compartira, puedes crear el módulo con la información que se explica en los videos.

class DevelopmentConfig:
    DEBUG = True
    MYSQL_HOST = 'HOST'
    MYSQL_USER = 'USER'
    MYSQL_PASSWORD = 'PASS'
    MYSQL_DB = 'PASSWORD'


config = {
    'development': DevelopmentConfig
}

Dentro del GIHUB esta el script de la tabla EXCHANGE RATE , ubícalo en la carpeta script.

Package       Version
------------- -------
click         8.1.3
colorama      0.4.6
Flask         2.2.3
pip           22.3.1
setuptools    65.5.1
Werkzeug      2.2.3
wheel         0.38.4


