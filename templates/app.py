
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:pass@localhost/maria_db'
db = SQLAlchemy(app)

class SwiftRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100))
    status = db.Column(db.String(20)) 

@app.route('/crm/dashboard')
def crm_dashboard():
    requests = SwiftRequest.query.all()
    return render_template('crm_dashboard.html', requests=requests)