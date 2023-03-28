from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'uabjpsychoatendsecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:yuOk0SXUYkFmnOSxzxcw@containers-us-west-205.railway.app:6391/railway'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    Sname = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    sex = db.Column(db.String(120), unique=False, nullable=False)
    date = db.Column(db.String(120), unique=False, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def innit():
    return render_template("home.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/term')
def term():
    return render_template("term.html")

@app.route('/register-db', methods=['POST'])
def register_db():
    email = request.form.get('email')
    name = request.form.get('name')
    Sname = request.form.get('Sname')
    password = request.form.get('password')
    sex = request.form.get('sex')
    date = request.form.get('date')

    user = User.query.filter_by(email=email).first() # se o email já existir, não deixa registrar

    if user: # se um usuário for encontrado, queremos redirecionar de volta para a página de inscrição para que o usuário possa tentar novamente
        flash('Este e-mail já foi registrado')
        return redirect(url_for('register'))

    # crie um novo usuário com os dados do formulário. Faça o hash da senha para que a versão em texto simples não seja salva.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'), Sname=Sname, sex=sex, date=date)

    # Adicione o novo usuário ao banco de dados
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('innit'))

if __name__ == "__main__":
    app.run(debug=True)

