from app import create_app
print("main.py is running ")



app = create_app()

if __name__ == '__main__':
    print("starting flask app")
    app.run(debug=True)
