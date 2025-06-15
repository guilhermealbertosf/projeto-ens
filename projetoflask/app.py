from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
db = SQLAlchemy(app)


class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String, nullable= False)
    senha = db.Column(db.String, nullable = False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    produtos = Produto.query.all()
    return render_template('dados.html', produtos=produtos)

@app.route('/novo', methods=['GET', 'POST'])
def novo():
    if request.method =='POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        db.session.add(Produto(nome=nome, email=email, senha=senha))
        db.session.commit()
        return redirect('/')
    return render_template('dados.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def aditar(id):
    produto = Produto.query.get_or_404(id)
    if request.method == 'POST':
        produto.nome = request.form['nome']
        produto.email = request.form['email']
        produto.senha = request.form['senha']
        db.session.commit()
        return redirect('/')
    return render_template('aditar.html', produto=produto)

@app.route('/deletar/<int:id>')
def deletar(id):
    produto = Produto.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)