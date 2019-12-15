from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='rocky-refuge-20221.herokuapp.com', port=33507)