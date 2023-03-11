# ApiRest_TipoCambio
Rest API creada en Flask que forma parte del proyecto de Automatización Exchange Rate (PAER)


![Video_10](https://user-images.githubusercontent.com/7143758/223303768-8c8ee266-97f1-4534-a884-1419317fa57d.png)

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

