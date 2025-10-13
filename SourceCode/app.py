from flask import Flask, request, session
import sqlite3

app = Flask(__name__)
app.secret_key = "insecure_secret_key"  # 🔴 Security Risk!

@app.route('/login', methods=['POST'])
def login():
    """ ❌ Vulnerable to SQL Injection """
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cur.execute(query)
    user = cur.fetchone()
    conn.close()
    if user:
        return "Login Successful!"
    return "Login Failed!"

@app.route('/fetch')
def fetch_url():
    """ ❌ Allows fetching any URL (SSRF Vulnerability) """
    url = request.args.get('url')
    return requests.get(url).text  # 🚨 Can access internal services!

if __name__ == '__main__':
    app.run(debug=True)
