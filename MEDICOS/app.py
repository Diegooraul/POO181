#paquteria de flask
from flask import Flask,render_template,request, redirect,url_for,flash
from flask_mysqldb import MySQL

#Inicializacion del APP
app=Flask(__name__)
#coneccion a la base de datos PENDIENTE
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']=''
app.secret_key='mysecretkey'
mysql=MySQL(app)

#Direccionamiento de las rutas
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index.html')
def Ingresar():
    return render_template('index.html')
    #Pasamos a variables el contenido de los input
    #if request.method == 'POST':

#Asignacion del puerto
if __name__ == '__main__':
        app.run(port=4000 ,debug= True)