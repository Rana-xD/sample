from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the home page'

@app.route('/profile/<name>', methods=['GET','POST'])
def profile(name):
    return render_template("profile.html", name=name)
if __name__ == "__main__":
    app.run(debug=True)
