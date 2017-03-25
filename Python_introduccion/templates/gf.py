import web
        
urls = ('/index', 'Index','/about', 'About', '/formulario', 'Formulario')

app = web.application(urls, globals())

render = web.template.render('templates')

web.config.debug = False


class Index:        
    def GET(self): 
    	productos = model.get_productos()
        return render.index()

class About:
	def GET(self):
		return render.about()

class Formulario:
	def GET(self):
		return render.formulario()

	def POST(self):
		form = web.input() #Atrapa el formulario enviado
		return"Hola" + form.nombre
		

if __name__ == "__main__":
    app.run()