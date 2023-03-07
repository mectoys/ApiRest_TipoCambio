# noinspection PyUnresolvedReferences
from flask import Flask, jsonify
from config import config
from flask_mysqldb import MySQL
from utils.Dateformat import DateFormat

App = Flask(__name__)
conexion = MySQL(App)


def pagina_no_encontrada(error):
    return "<h1>La página que intentas acceder no existe </h1>"


@App.route('/exchanges')
# Creación de una vista en forma de función
def list_exchanges():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT MONEDA, COMPRA, VENTA, FECHA FROM ExchangeRate"
        cursor.execute(sql)
        datos = cursor.fetchall()
        exchanges = []
        for fila in datos:
            exchange = {'MONEDA': fila[0], 'COMPRA': fila[1], 'VENTA': fila[2],
                        'FECHA': DateFormat.convert_date(fila[3])}
            exchanges.append(exchange)
        print(exchange)
        return jsonify({'Exchange': exchange})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


@App.route('/verifier/<fecha>')
# Creación de una vista en forma de función
def verificar_siexsiste(fecha):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT COUNT(ID) AS CONTEO FROM ExchangeRate WHERE FECHA=CAST('{0}' AS DATE)".format(fecha)
        cursor.execute(sql)
        datos = cursor.fetchall()
        exchanges = []
        for fila in datos:
            exchange = {'Conteo': fila[0]}
            exchanges.append(exchange)
        return jsonify({'ExchangeRates': exchange})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


if __name__ == '__main__':
    App.config.from_object(config['development'])
    App.register_error_handler(404, pagina_no_encontrada)
    App.run()
