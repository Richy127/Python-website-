from website import create_app 

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
#when we add code will automatically reload the website 
