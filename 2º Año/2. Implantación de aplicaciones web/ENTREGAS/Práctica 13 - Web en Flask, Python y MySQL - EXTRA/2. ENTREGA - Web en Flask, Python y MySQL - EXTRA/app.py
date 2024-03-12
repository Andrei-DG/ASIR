from flask import Flask, render_template, request, url_for, redirect, flash, url_for
import tareas_productos

app = Flask(__name__)


@app.route("/agregar_producto")
def formulario_agregar_producto():
    return render_template("agregar_producto.html")


@app.route("/guardar_producto", methods=["POST"])
def guardar_producto():
    producto = request.form["producto"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    tareas_productos.insertar_producto(producto, descripcion, precio)
    return redirect("/productos")


@app.route("/formulario_editar_producto/<int:sku>")
def editar_producto(sku):
    # Obtener el producto por SKU
    producto = tareas_productos.obtener_producto_por_sku(sku)
    return render_template("editar_producto.html", producto=producto)


@app.route("/eliminar_producto", methods=["POST"])
def eliminar_producto():
    tareas_productos.eliminar_producto(request.form["sku"])
    return redirect("/productos")


@app.route("/")
@app.route("/productos")
def productos():
    productos = tareas_productos.obtener_productos()
    return render_template("productos.html", productos=productos)


@app.route("/actualizar_producto", methods=["POST"])
def actualizar_producto():
    sku = request.form["sku"]
    producto = request.form["producto"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    tareas_productos.actualizar_producto(producto, descripcion, precio, sku)
    return redirect("/productos")


@app.route("/productos/porPrecio", methods=["POST"])
def filtro_precios():
    precio = request.form["precio"]
    preciosfiltrados = tareas_productos.filtro_productos_precio(precio)
    return render_template("productos.html", productos=preciosfiltrados)

@app.route("/productos/porLetra", methods=["POST"])
def filtro_productos():
    producto = request.form["producto"]
    productosfiltrados = tareas_productos.filtro_productos_producto(producto)
    return render_template("productos.html", productos=productosfiltrados)

@app.route("/productos/porOpcion", methods=["POST"])
def filtro_opcion():
    opcion = request.form["opcion"]
    opcionesfiltradas = tareas_productos.filtro_productos_opcion(opcion)
    return render_template("productos.html", productos=opcionesfiltradas)

@app.route("/productos/porRango", methods=["POST"])
def filtro_rango():
    precio_min = request.form["precio_min"]
    precio_max = request.form["precio_max"]
    rangosfiltrados = tareas_productos.filtro_productos_rango(precio_min, precio_max)
    return render_template("productos.html", productos=rangosfiltrados)


if __name__ == "__main__":
    app.run(port=3000, debug=True)
