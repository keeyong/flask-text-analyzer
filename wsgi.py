from app import create_app

app = create_app()

if __name__ == "__main__":
    # Simple dev server; for production use a WSGI server (gunicorn, uwsgi)
    app.run(debug=True)
