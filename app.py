from flask import Flask, render_template

app = Flask(__name__)

@app.route('/register')
def pagecad():
    return "Cadastro feito"

@app.route('/profile/<username>')
def profile(username):
    return render_template("profile.html", username=username)


if __name__ == "__main__":
    app.run(debug=True)

