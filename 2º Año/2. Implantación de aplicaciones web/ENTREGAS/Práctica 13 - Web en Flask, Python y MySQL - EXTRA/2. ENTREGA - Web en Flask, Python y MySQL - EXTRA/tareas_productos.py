from bd import obtener_conexion


def insertar_producto(producto, descripcion, precio):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO productos(producto, descripcion, precio) VALUES (%s, %s, %s)",
                       (producto, descripcion, precio))
    conexion.commit()
    conexion.close()


def obtener_productos():
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT sku, producto, descripcion, precio FROM productos")
        productos = cursor.fetchall()
    conexion.close()
    return productos


def filtro_productos_precio(precio):
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT sku, producto, descripcion, precio FROM productos WHERE precio = %s", (precio,))
        productos = cursor.fetchall()
    conexion.close()
    return productos

def filtro_productos_producto(producto):
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT sku, producto, descripcion, precio FROM productos WHERE producto LIKE %s", ('%' + producto + '%',))
        productos = cursor.fetchall()
    conexion.close()
    return productos

def filtro_productos_opcion(opcion):
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT sku, producto, descripcion, precio FROM productos WHERE producto LIKE %s", (opcion + '%',))
        productos = cursor.fetchall()
    conexion.close()
    return productos

def filtro_productos_rango(precio_min, precio_max):
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT sku, producto, descripcion, precio FROM productos WHERE precio BETWEEN %s AND %s", (precio_min, precio_max))
        productos = cursor.fetchall()
    conexion.close()
    return productos

def eliminar_producto(sku):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM productos WHERE sku = %s", (sku,))
    conexion.commit()
    conexion.close()


def obtener_producto_por_sku(sku):
    conexion = obtener_conexion()
    producto = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT sku, producto, descripcion, precio FROM productos WHERE sku = %s", (sku,))
        producto = cursor.fetchone()
    conexion.close()
    return producto


def actualizar_producto(producto, descripcion, precio, sku):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE productos SET producto = %s, descripcion = %s, precio = %s WHERE sku = %s",
                       (producto, descripcion, precio, sku))
    conexion.commit()
    conexion.close()
