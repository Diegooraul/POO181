#importacion del framework
from flask import Flask, render_template,request, redirect,url_for,flash
from flask_mysqldb import MySQL

#inicializacion del APP
app= Flask(__name__)

#Configuracion de la conexion
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='DB_FRUTAS'
app.secret_key= 'mysecretkey'
mysql= MySQL(app)

#declaracion de ruta http://localhost:5000
@app.route('/')
def index():
    CC= mysql.connection.cursor();
    CC.execute('select * from TB_FRUTAS')
    conAlbums= CC.fetchall()
    print(conAlbums)
    return render_template('index.html', listAlbums= conAlbums)

#ruta http:localhost:5000/guardar tipo POST Para Insert

@app.route('/guardar',methods=['POST'])
def guardar():

    #Pasamos a variables el contenido de los input
    if request.method == 'POST':
        Vfruta= request.form['FRUTA']
        Vtemporada= request.form['TEMPORADA']
        Vprecio= request.form['PRECIO']
        Vstock= request.form['STOCK']
    
    #Conectar y ejecutar el insert
    CS= mysql.connection.cursor()
    CS.execute('insert into TB_FRUTAS(FRUTA,TEMPORADA,PRECIO,STOCK) values(%s,%s,%s,%s)',(Vfruta,Vtemporada,Vprecio,Vstock))
    mysql.connection.commit()
    
    flash('La fruta se registro correctamente')   
    return redirect(url_for('index'))


@app.route('/consulta_fruta')
def consulta():
    CC= mysql.connection.cursor();
    CC.execute('select * from TB_FRUTAS')
    conAlbums= CC.fetchall()
    print(conAlbums)
    return render_template('consulta_fruta.html', listAlbums= conAlbums)

@app.route('/editar/<id>')
def editar(id):
  cursoId=mysql.connection.cursor()
  cursoId.execute('select * from TB_FRUTAS where id= %s',(id,))
  consulID= cursoId.fetchone()
  print(consulID)
  return render_template('editarAlbum.html',album=consulID)

@app.route('/actualizar/<id>',methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        Vfruta= request.form['FRUTA']
        Vtemporada= request.form['TEMPORADA']
        Vprecio= request.form['PRECIO']
        Vstock= request.form['STOCK']

        curAct= mysql.connection.cursor()
        curAct.execute('update TB_FRUTAS set FRUTA= %s, TEMPORADA= %s, PRECIO= %s, STOCK = %s where id= %s',(Vfruta,Vtemporada,Vprecio,Vstock,id))
        mysql.connection.commit()

    flash('Se actualizo la fruta: '+Vfruta)
    return redirect(url_for('index'))

@app.route('/eliminar/<id>')
def eliminar(id):
  
  curId=mysql.connection.cursor()
  curId.execute('select * from TB_FRUTAS where id= %s',(id,))
  EliminarID= curId.fetchone()
  return render_template('eliminarAlbum.html',album=EliminarID)


@app.route('/borrar/<id>',methods=['POST'])
def borrar(id):

    if request.method == 'POST':

        curAct= mysql.connection.cursor()
        curAct.execute('delete from TB_FRUTAS where id= %s',(id))
        mysql.connection.commit()

    flash('Se elimino la fruta')
    return redirect(url_for('index'))

@app.route('/consultar_por_nombre', methods=['GET', 'POST'])
def consultar_por_nombre():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM TB_FRUTAS WHERE FRUTA LIKE %s', ('%' + nombre + '%',))
        frutas = cur.fetchall()
        return render_template('consulta_nombre.html', frutas=frutas)
    return render_template('consulta_nombre.html', frutas=[])



#ejecucion del servidor en el puerto 5000
if __name__ == "__main__":
   app.run(port=5000,debug=True)