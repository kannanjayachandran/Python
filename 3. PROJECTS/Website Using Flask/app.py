from flask import Flask, render_template, request, url_for, flash

app = Flask(__name__)

app.secret_key = 'secretkey'


@app.route("/")
def index():
    flash("what's your name ?")
    return render_template('index.html')


@app.route("/greet", methods=['post', 'get'])
def greet():
    flash('Hello ' + request.form['name_input'] + " Nice to meet you")
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
