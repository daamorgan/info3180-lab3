from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY']="Z?a2vb$"
app.config['MAIL_SERVER']="smtp.mailtrap.io"
app.config['MAIL_PORT']='2525'
app.config['MAIL_USERNAME'] = 'unknown'
app.config['MAIL_PASSWORD'] = 'unknown'


mail=Mail(app)
from app import views