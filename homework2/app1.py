from flask import Flask, render_template, url_for, request, make_response, redirect

app = Flask(__name__)

@app.route('/')
def lider():
    return render_template('base.html')

@app.route('/name/')
def name():
    return render_template('name.html')

@app.post('/hello/')
def hello():
    name = request.form['name']
    mail = request.form['mail']
    response = make_response(render_template("hello.html", name = name, mail = mail))
    response.set_cookie('username', name)
    response.set_cookie('mail', mail)
    return response

@app.route('/nameout/')
def nameout():
    response = make_response(redirect(url_for('name')))
    response.delete_cookie('username')
    response.delete_cookie('mail')
    return response


if __name__ == '__main__':
    app.run(debug=True)