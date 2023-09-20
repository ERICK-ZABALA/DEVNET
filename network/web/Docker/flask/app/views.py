from flask import Flask, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from app import app, db  
# Importa la aplicación Flask y la instancia de la base de datos desde el paquete actual

@app.route('/')
def home():
    return "Hello Python Netowrking!"


@app.route('/db', methods=['GET'])
def get_db():
    devices = Device.query.all()
    device_list = [device.to_dict() for device in devices]
    return jsonify(device_list)
    