import pymysql
from flask import render_template, request
from .engine import SessionLocal
from .artiste import Artiste


def register_routes(app):

    @app.route("/")
    def home():
        return "<p>page d'accueil</p>"

    @app.route("/artistes", methods=["GET", "POST"])
    def artistes():
        artists = None
        query = ""

        if request.method == "POST":
            query = request.form.get("query", "").strip()

            # Connexion MySQL brute
            conn = pymysql.connect(
                host="localhost",
                user="root",
                password="uimm",
                database="tourneur",
                cursorclass=pymysql.cursors.DictCursor,
                port=3306,
                charset="utf8mb4"
            )
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM artiste WHERE nom LIKE %s",
                        (f"%{query}%",)
                    )
                    artists = cursor.fetchall()

        return render_template("artistes.html", artists=artists)

    @app.route("/artistes-sqlalchemy", methods=["GET", "POST"])
    def artistes_sqlalchemy():
        artists = None
        query = ""

        if request.method == "POST":
            query = request.form.get("query", "").strip()
            db = SessionLocal()
            try:
                artists = db.query(Artiste).filter(Artiste.nom.like(f"%{query}%")).all()
            finally:
                db.close()

        return render_template("artistes.html", artists=artists)

