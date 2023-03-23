from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def innit():
    return render_template("sucesso.html")

@app.route('/register')
def register():
    return render_template("index.html")

@app.route('/profile/<username>')
def profile(username):
    return render_template("profile.html", username=username)


if __name__ == "__main__":
    app.run(debug=True)

