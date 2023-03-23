# noinspection PyUnresolvedReferences
from flask import Flask, jsonify, request
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


# Listar último dato T.C.
@App.route('/lastexchange')
def Obtener_LastExchange():
    try:
        cursor = conexion.connection.cursor()
        SQL = "SELECT EX.FECHA, EX.COMPRA, EX.VENTA FROM ExchangeRate EX " \
              " WHERE EX.FECHA IN (SELECT MAX(EX.FECHA)FROM  ExchangeRate EX)"
        print(SQL)
        cursor.execute(SQL)
        datos = cursor.fetchall()
        if datos != None:
            exchanges = []
            for fila in datos:
                exchange = {'FECHA': DateFormat.convert_date(fila[0]), 'COMPRA': fila[1], 'VENTA': fila[2]}
                exchanges.append(exchange)
            return jsonify({'Exchange': exchange})
        else:
            return {"ExchangeRates": "Dato no encontrado"}
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Método POST :Agregar T. Cambio
@App.route('/register', methods=['POST'])
def register_Exchange():
    try:
        cursor = conexion.connection.cursor()
        SQLINNSERT = "INSERT INTO ExchangeRate(MONEDA, COMPRA, VENTA, FECHA) VALUES('{0}',{1},{2},'{3}')".format(
            request.json['MONEDA'], request.json['COMPRA'], request.json['VENTA'], request.json['FECHA'])
        cursor.execute(SQLINNSERT)
        conexion.connection.commit()
        return {'mensaje': "dato registrado"}
    except Exception as ex:
        return jsonify({'mensaje': str(ex)})


if __name__ == '__main__':
    App.config.from_object(config['development'])
    App.register_error_handler(404, pagina_no_encontrada)
    App.run()
