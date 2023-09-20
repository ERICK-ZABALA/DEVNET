from flask import Flask, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
from app import views

device_id = 0

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///network.db'
db = SQLAlchemy(app)

# Importa la clase Device
#from app.models import Device  # Suponiendo que tienes un archivo models.py en el mismo directorio

class Device(db.Model):
    __tablename__ = 'devices'
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(64), unique=True)
    loopback = db.Column(db.String(120), unique=True)
    mgmt_ip = db.Column(db.String(120), unique=True)
    role = db.Column(db.String(64))
    vendor = db.Column(db.String(64))
    os = db.Column(db.String(64))


    def __init__(self, hostname, loopback, mgmt_ip, role, vendor, os):
        self.hostname = hostname
        self.loopback = loopback
        self.mgmt_ip = mgmt_ip
        self.role = role
        self.vendor = vendor
        self.os = os
        #self_url = db.Column(db.String(120))
    
    def get_url(self):
        return url_for('interface', id=self.id, _external=True)

    def __repr__(self):
        return '<Device %r>' % self.hostname
    
    # format to send as dict for GET DB
    def to_dict(self):
        return {
            'id': self.id,
            'hostname': self.hostname,
            'loopback': self.loopback,
            'mgmt_ip': self.mgmt_ip,
            'role': self.role,
            'vendor': self.vendor,
            'os': self.os,
            #'self_url': self.self_url
            }
    
    def import_data(self, data):
        try:
            self.hostname = data['hostname']
            self.loopback = data['loopback']
            self.mgmt_ip = data['mgmt_ip']
            self.role = data['role']
            self.vendor = data['vendor']
            self.os = data['os']
        
        except Exception as e:
            print("Error al registrar el dispositivo:", str(e))
        return self

