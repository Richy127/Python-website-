from flask import Flask

def create_app():
    app = Flask(__name__, static_url_path="/static\\images")
    
#inputs flask
    app.config['SECRET_KEY'] = 'COOL BEANS'

    from website import webfront
    from website import sign_in

    app.register_blueprint(webfront.webfront, url_prefix='/')
    app.register_blueprint(sign_in.sign_in2, url_prefix='/')
  
    return app
    
