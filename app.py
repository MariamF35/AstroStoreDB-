from flask import Flask
from db_config import get_db_connection

app = Flask(__name__)

@app.route("/")
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 'Database Connected Successfully!'")
    result = cursor.fetchone()
    conn.close()
    return result[0]

if __name__ == "__main__":
    app.run(debug=True)
