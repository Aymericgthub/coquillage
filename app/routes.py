from flask import render_template
from .database import get_db_connection

def register_routes(app):

    @app.route("/")
    def home():
        return "<p>page d'accueil</p>"

    @app.route("/artistes")
    def artistes():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM artistes")
        artistes = cursor.fetchall()
        conn.close()

        return render_template("artistes.html", artistes=artistes)

