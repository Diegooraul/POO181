#importacion del framework
from flask import Flask, render_template,request, redirect,url_for,flash
from flask_mysqldb import MySQL

#inicializacion del APP
app= Flask(__name__)

#Configuracion de la conexion
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='DB_Papeleria'
app.secret_key= 'mysecretkey'
mysql= MySQL(app)

#declaracion de ruta http://localhost:5000
@app.route('/')
def index():
    CC= mysql.connection.cursor();
    CC.execute('select * from TB_UTILES')
    conAlbums= CC.fetchall()
    print(conAlbums)
    return render_template('index.html', listAlbums= conAlbums)

#ruta http:localhost:5000/guardar tipo POST Para Insert

@app.route('/guardar',methods=['POST'])
def guardar():

    #Pasamos a variables el contenido de los input
    if request.method == 'POST':
        Vnombrec= request.form['NOMBRE_CLASIFICACION']
        Vcantidad= request.form['CANTIDAD']
        Vprecio= request.form['PRECIO_COMPRA']

    #Conectar y ejecutar el insert
    CS= mysql.connection.cursor()
    CS.execute('insert into TB_UTILES (NOMBRE_CLASIFICACION,CANTIDAD,PRECIO_COMPRA) values(%s,%s,%s)',(Vnombrec,Vcantidad,Vprecio))
    mysql.connection.commit()
    
    flash('LOS UTILES SE REGISTRARON CORRECTAMENTE')   
    return redirect(url_for('index'))

@app.route('/consulta_utiles')
def consulta():
    CC= mysql.connection.cursor();
    CC.execute('select * from TB_UTILES')
    conAlbums= CC.fetchall()
    print(conAlbums)
    return render_template('consultar.html', listAlbums= conAlbums)

@app.route('/consulta_empleado')
def consultaempleado():
    CC= mysql.connection.cursor();
    CC.execute('select * from TB_EMPLEADOS')
    conAlbums= CC.fetchall()
    print(conAlbums)
    return render_template('consultaremp.html', listAlbums= conAlbums)


@app.route('/regresar')
def regresar():
    CC= mysql.connection.cursor();
    CC.execute('select * from TB_UTILES')
    conAlbums= CC.fetchall()
    print(conAlbums)
    return render_template('index.html', listAlbums= conAlbums)

@app.route('/empleados')
def empleados():
    CC= mysql.connection.cursor();
    CC.execute('select * from TB_EMPLEADOS')
    conAlbums= CC.fetchall()
    print(conAlbums)
    return render_template('empleados.html', listAlbums= conAlbums)

@app.route('/guardarempleado',methods=['POST'])
def guardarempleado():

    #Pasamos a variables el contenido de los input
    if request.method == 'POST':
        Vnombre= request.form['NOMBRE']
        Vapp= request.form['APP']
        Vapm= request.form['APM']
        Vpuesto= request.form['PUESTO']
        Vcontraseña= request.form['CONTRASEÑA']


    #Conectar y ejecutar el insert
    CS= mysql.connection.cursor()
    CS.execute('insert into TB_EMPLEADOS (NOMBRE,APP,APM,PUESTO,CONTRASEÑA) values(%s,%s,%s,%s,%s)',(Vnombre,Vapp,Vapm,Vpuesto,Vcontraseña))
    mysql.connection.commit()
    
    flash('EL EMPLEADO SE REGISTRO CORRECTAMENTE')   
    return redirect(url_for('empleados'))

@app.route('/editar/<id>')
def editar(id):
  cursoId=mysql.connection.cursor()
  cursoId.execute('select * from TB_UTILES where id= %s',(id,))
  consulID= cursoId.fetchone()
  print(consulID)
  return render_template('editar.html',album=consulID)

@app.route('/actualizar/<id>',methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        Vnombrec= request.form['NOMBRE_CLASIFICACION']
        Vcantidad= request.form['CANTIDAD']
        Vprecio= request.form['PRECIO_COMPRA']

        curAct= mysql.connection.cursor()
        curAct.execute('update TB_UTILES set NOMBRE_CLASIFICACION= %s, CANTIDAD= %s, PRECIO_COMPRA= %s where id= %s',(Vnombrec,Vcantidad,Vprecio,id))
        mysql.connection.commit()

    flash('Se actualizo el util: '+Vnombrec)
    return redirect(url_for('consulta'))

@app.route('/eliminar/<id>')
def eliminar(id):
  
  curId=mysql.connection.cursor()
  curId.execute('select * from TB_EMPLEADOS where id= %s',(id,))
  EliminarID= curId.fetchone()
  return render_template('eliminar.html',album=EliminarID)


@app.route('/borrar/<id>',methods=['POST'])
def borrar(id):

    if request.method == 'POST':

        curAct= mysql.connection.cursor()
        curAct.execute('delete from TB_EMPLEADOS where id= %s',(id))
        mysql.connection.commit()

    flash('Se elimino el empleado')
    return redirect(url_for('consultaempleado'))

@app.route('/consultar_utiles_nombre', methods=['GET', 'POST'])
def consultar_utiles_nombre():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM TB_UTILES WHERE NOMBRE_CLASIFICACION LIKE %s', ('%' + nombre + '%',))
        frutas = cur.fetchall()
        return render_template('nombreutiles.html', frutas=frutas)
    return render_template('nombreutiles.html', frutas=[])


@app.route('/consultar_empleados_nombre', methods=['GET', 'POST'])
def consultar_empleados_nombre():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM TB_EMPLEADOS WHERE APP LIKE %s', ('%' + nombre + '%',))
        empleados = cur.fetchall()
        return render_template('nombreemp.html', empleados=empleados)
    return render_template('nombreemp.html', empleados=[])



#ejecucion del servidor en el puerto 5000
if __name__ == "__main__":
   app.run(port=5000,debug=True)