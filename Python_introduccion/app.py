import web
import model

urls = (
	'/', 'Index',
	'/ver/(.+)', 'Ver',
	'/edit/(.+)','Edit',
	'/insertar/(.+)','Insertar',
)

app = web.application(urls, globals())

render = web.template.render('templates', base = 'bases')

web.config.debug = False


class Index:        
    def GET(self): 
    	productos = model.get_productos()
    	return render.index(productos)

class Ver:        
	def GET(self, id):
		id_producto = int(id)
		producto = model.get_producto(id_producto)
		return render.ver(producto)    

class Insertar:
	def GET(self):
		return render.insertar()
	def POST(self):
		form = web.input()
		model.insertar(form.producto, form.descripcion,form.precio_compra, form.precio_venta,)
		return render.index()

class Delete:
    def POST(self, id):
        model.del_post(int(id))
        raise web.seeother('/') 

class Edit:

    def GET(self, id):
        post = model.get_producto(int(id))
        form = New.form()
        form.fill(post)
        return render.edit(post, form)



if __name__ == "__main__":
    app.run()