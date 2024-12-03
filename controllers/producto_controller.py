from flask import request,redirect,Blueprint,url_for
from models.producto_model import Producto
from views import producto_view
producto_bp=Blueprint('producto',__name__,url_prefix="/productos")
@producto_bp.route("/")
def index():
    productos=Producto.get_all()
    return producto_view.list(productos)
@producto_bp.route("/create",methods=['GET','POST'])
def create():
    if request.method=='POST':
        descripcion=request.form['descripcion']
        precio=request.form['precio']
        stock=request.form['stock']
        producto=Producto(descripcion,precio,stock)
        producto.save()
        return redirect(url_for('producto.index'))
    return producto_view.create()
@producto_bp.route("/edit/<int:id>",methods=['GET','POST'])
def edit(id):
    producto=Producto.get_by_id(id)
    if request.method=='POST':
        descripcion=request.form['descripcion']
        precio=request.form['precio']
        stock=request.form['stock']
        #actualizar
        producto.update(descripcion=descripcion,precio=precio,stock=stock)
        return redirect(url_for('producto.index'))

    return producto_view.edit(producto)
@producto_bp.route("/delete/<int:id>")
def delete(id):
    producto=Producto.get_by_id(id)
    producto.delete()
    return redirect(url_for('producto.index'))