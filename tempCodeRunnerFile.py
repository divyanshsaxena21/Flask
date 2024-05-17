from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'kanpur'
app.config['MYSQL_DB'] = 'project'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    # Perform database query to check username and password
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM registered_users WHERE username = %s AND password = %s", (username, password))
    result = cur.fetchall()
    cur.close()

    if result:
        return jsonify(success=True, message='Login successful')
    else:
        return jsonify(success=False, message='Invalid username or password')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
