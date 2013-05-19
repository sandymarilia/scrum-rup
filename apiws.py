from bottle import route, run, request,post
import psycopg2

@route('/rol')
def listar():
	conec=psycopg2.connect("dbname='scrum' user='undac'  host='localhost' password='sistemas'")
	nn=conec.cursor()
	nn.execute("select * from rol where rid=%(rid)s",{'rid':'AF'})
	datos=nn.fetchall()
	print datos


#/action?rid=4&nombre=administrador
@route('/action')
def select_action():
	rid = request.query.rid
	nombre = request.query.nombre
	conec=psycopg2.connect("dbname='scrum' user='undac'  host='localhost' password='sistemas'")
	nn=conec.cursor()
	a=nn.execute("INSERT INTO rol (rid,nombre,estado) VALUES (%s,%s,%s)",(rid,nombre,'A'))
	da=conec.commit()
	print {'rid':rid, 'nombre':nombre}

#/modificar?rid=AD&nombre=administra&estado=B
@route('/modificar')
def select_modificar():
	rid = request.query.rid
	nombre = request.query.nombre
	estado = request.query.estado
	conec=psycopg2.connect("dbname='scrum' user='undac'  host='localhost' password='sistemas'")
	nn=conec.cursor()
	nn.execute("update rol set nombre=%(nombre)s, estado=%(estado)s  where rid=%(rid)s",{'nombre':nombre,'estado':estado,'rid':rid})
	da=conec.commit()
	print {'rid':rid, 'nombre':nombre}

#/eliminar?rid=AD
@route('/eliminar')
def select_modificar():
	rid = request.query.rid
	conec=psycopg2.connect("dbname='scrum' user='undac'  host='localhost' password='sistemas'")
	nn=conec.cursor()
	nn.execute("delete from rol where rid=%(rid)s",{'rid':rid})
	da=conec.commit()
	print "se elimino"


run(host='localhost', port=8000, debug=True)






