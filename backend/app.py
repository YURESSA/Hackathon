from backend.core import create_app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, use_reloader=True, port=5000)
