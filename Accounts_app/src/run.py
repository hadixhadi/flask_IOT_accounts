from flask import Flask , session
from apps.accounts.routes import blueprint as accounts_blueprint
from apps import app
from config import BaseConfig






app.register_blueprint(accounts_blueprint)
app.config.from_object(BaseConfig)


if __name__=='__main__':
    app.run(host="0.0.0.0")
