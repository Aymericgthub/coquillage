
@app.route("/artists", methods=["GET", "POST"])
def show_artists():
    artists = None
    if request.method == "POST":
        query = request.form.get("query")
        conn = mariadb.connect(
            user=DB_USER,
            password="uimm",
            host="localhost",  # ou le nom du service mysql/mariadb du docker-compose
            port=3306,
            database="tourneur")
        cursor = conn.cursor(dictionary=True)
        print(f"SELECT * FROM artiste WHERE nom LIKE '{query}'")
        # cursor.execute(f"SELECT * FROM artiste WHERE nom LIKE '{query}'")
        cursor.execute("SELECT * FROM artiste WHERE nom LIKE %s", (f"{query}",))
        result = cursor.fetchall()
        artists = [artist["nom"] for artist in result]
    return render_template("index.html", artists=artists)


#from app import create_app

#app = create_app()

#if __name__ == "__main__":
   # app.run(debug=True)

