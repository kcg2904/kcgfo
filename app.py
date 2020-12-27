from flask import Flask, request, render_template, redirect

app = Flask(__name__)

app.secret_key = b'aaa!111/'

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/webapp')
def webapp():
    return render_template('webapp.html')

@app.route('/web')
def web():
    return render_template('web.html')

@app.route('/pw')
def String():
    return render_template('PW.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/cp')
def cp():
    return render_template('cp.html')

@app.route('/keep')
def keep():
    return render_template('keep.html')
@app.route('/linx')
def linx():
    return render_template('linx.html')


if __name__ == '__main__':
    app.run(debug=False)
