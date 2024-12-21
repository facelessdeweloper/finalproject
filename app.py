from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import sqlite3
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def index_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        text = request.form['message']

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('user_data.txt', 'a', encoding='utf-8') as f:
            f.write(f"Date: {current_time}\nName: {name}\nEmail: {email}\nMessage: {text}\n\n")

        return redirect(url_for('success'))

    return render_template("index.html")

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(debug=True)
