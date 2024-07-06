from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

# Hardcoded credentials (username: user, password: pass)
USERNAME = 'user'
PASSWORD = 'pass'

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['email']
    password = request.form['password']
    
    if username == USERNAME and password == PASSWORD:
        return redirect(url_for('beranda'))
    else:
        flash('Username atau password salah. Silahkan coba lagi.')
        return redirect(url_for('index'))

@app.route('/beranda')
def beranda():
    return render_template('beranda.html')

@app.route('/jual')
def jual():
    return render_template('jual.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/beli')
def beli():
    return render_template('beli.html')

if __name__ == '__main__':
    app.run(debug=True)
