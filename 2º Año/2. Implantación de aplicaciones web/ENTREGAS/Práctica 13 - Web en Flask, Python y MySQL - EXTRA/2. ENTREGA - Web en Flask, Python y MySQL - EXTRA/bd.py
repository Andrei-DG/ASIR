import pymysql


def obtener_conexion():
    return pymysql.connect(host='informatica.iesquevedo.es',
                           port=3333,
                           user='root',
                           password='1asir',
                           db='andrei')

#    return pymysql.connect(host='localhost',
#                            port=6033,
#                            user='andrei',
#                            password='1asir',
#                            db='andrei')
