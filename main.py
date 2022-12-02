from flask import Flask, render_template, request
from model import model
import this

this.dados          = ""
this.modelo         = model()
this.msg            = ""
this.campo          = ""
this.dado           = ""
this.conteudo       = ""
this.email          = ""
this.senha          = ""
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def inserirConteudo():
    if request.method == 'POST':
        this.conteudo    = request.form['tNewConteudo']
        this.dados       = this.modelo.inserir(this.conteudo)
    return render_template('/', titulo="Diário", resultado=this.dados)

@app.route('/home.html', methods=['GET','POST'])
def consultConteudo():
    if request.method == 'POST':
        this.cod   = request.form['tNewCod']
        this.msg   = this.modelo.consultar(this.cod)
    return render_template('home.html', titulo="Consultar", dados=this.msg)

@app.route('/', methods=['GET','POST'])
def updateConteudo():
    if request.method == 'POST':
        this.cod   = request.form['tCod']
        this.campo = request.form['tCampo']
        this.dado  = request.form['tDado']
        this.msg   = this.modelo.atualizar(this.cod, this.campo, this.dado)
    return render_template('.html', titulo="Atualizar", dados=this.msg)

@app.route('/', methods=['GET','POST'])
def deleteConteudo():
    if request.method == 'POST':
        this.cod = request.form['tCod']
        this.msg = this.modelo.excluir(this.cod)
    return render_template('excluir.html', titulo="Excluir", dados=this.msg)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        this.email  = request.form['tNewEmail']
        this.senha = request.form['tNewSenha']
        this.msg  = this.modelo.cad(this.email, this.senha)
    return render_template('consultar.html', titulo="Login", dados=this.msg)