import web

db_host = 'localhost'
db_name = 'productos'
db_user = 'root'
db_pw = ''

db = web.database(
	dbn='mysql',
	host=db_host,
	db=db_name,
	user=db_user,
	pw=db_pw)

def get_productos():
	try:
		return db.select('productos')
	except:
		return None

productos = get_productos()

def get_productos(id_producto):
	try:
		return db.select('productos', where = 'id_producto=$id_producto', vars=local)
	except:
		return None



#for item in productos:
	#print item.id_producto
	#print item.producto
	#print item.descripcion
	#print item.precio_compra
	#print item.precio_venta

#print get_productos()