#importacion del framework
from flask import Flask, render_template,request, redirect,url_for,flash
from flask_mysqldb import MySQL

#inicializacion del APP
app= Flask(__name__)

#Configuracion de la conexion
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='dbflask'
app.secret_key= 'mysecretkey'
mysql= MySQL(app)

#declaracion de ruta http://localhost:5000
@app.route('/')
def index():
    CC= mysql.connection.cursor();
    CC.execute('select * from tbalbums')
    conAlbums= CC.fetchall()
    print(conAlbums)
    return render_template('index.html', listAlbums= conAlbums)

#ruta http:localhost:5000/guardar tipo POST Para Insert

@app.route('/guardar',methods=['POST'])
def guardar():

    #Pasamos a variables el contenido de los input
    if request.method == 'POST':
        Vtitulo= request.form['txtTitulo']
        Vartista= request.form['txtArtista']
        Vanio= request.form['txtAnio']
    
    #Conectar y ejecutar el insert
    CS= mysql.connection.cursor()
    CS.execute('insert into tbalbums(titulo,artista,anio) values(%s,%s,%s)',(Vtitulo,Vartista,Vanio))
    mysql.connection.commit()
    
    flash('El album fue agregado correctamente')   
    return redirect(url_for('index'))



@app.route('/editar/<id>')
def editar(id):
  cursoId=mysql.connection.cursor()
  cursoId.execute('select * from tbalbums where id= %s',(id,))
  consulID= cursoId.fetchone()
  print(consulID)
  return render_template('editarAlbum.html',album=consulID)

@app.route('/actualizar/<id>',methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        varTitulo= request.form['txtTitulo']
        varArtista= request.form['txtArtista']
        varAnio= request.form['txtAnio']
        
        curAct= mysql.connection.cursor()
        curAct.execute('update tbalbums set titulo= %s, artista= %s, anio= %s where id= %s',(varTitulo,varArtista,varAnio,id))
        mysql.connection.commit()

    flash('Se actualizo el Album'+varTitulo)
    return redirect(url_for('index'))









@app.route('/eliminar')
def eliminar():
    return "Se elimino en la base de datos"

#ejecucion del servidor en el puerto 5000
if __name__ == "__main__":
   app.run(port=5000,debug=True)