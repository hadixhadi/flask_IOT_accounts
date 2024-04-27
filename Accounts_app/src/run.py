from flask import Flask
from apps.accounts.routes import blueprint as accounts_blueprint
from apps import app
app.register_blueprint(accounts_blueprint)




if __name__=='__main__':
    app.run(host="0.0.0.0",port="5000",debug=True)
