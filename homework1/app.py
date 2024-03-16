from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/shop/')
def mag():
    return render_template('mag.html')

@app.route('/shop/categories/')
def categories():
    return render_template('mag1.html')

@app.route('/shop/categories/buts/')
def buts():
    return render_template('buts.html')

if __name__ == '__main__':
    app.run(debug=True)