from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

device_id = 0

# Load configuration, and Create the SQLAlchemy object
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api.db'
db = SQLAlchemy(app)

# This is the database model object
class Device(db.Model):
    __tablename__ = 'devices'
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(120), index=True)
    loopback = db.Column(db.String(40))
    mgmt_ip = db.Column(db.String(40))
    role = db.Column(db.String(40))
    vendor = db.Column(db.String(40))
    os = db.Column(db.String(40))
    self_url = db.Column(db.String(120))
    

    def __init__(self, hostname, loopback, mgmt_ip, role, vendor, os, self_url):
        self.hostname = hostname
        self.loopback = loopback
        self.mgmt_ip = mgmt_ip
        self.role = role
        self.vendor = vendor
        self.os = os
        self.self_url = self_url

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
            'self_url': self.self_url
            }


# This is the database model object
data = {
    'hostname': 'iosv-1',
    'loopback': '192.168.0.1',
    'mgmt_ip': '172.16.1.225',
    'role': 'spine',
    'vendor': 'Cisco',
    'self_url': 'http://172.16.1.123:5000/devices/1',
    'os': '15.6'
}

#@app.route('/routers/<hostname>/interface/<int:interface_number>')
#def interface(hostname, interface_number):
#    return jsonify(name=hostname, interface=interface_number)

@app.route('/devices/', methods=['GET'])
def get_devices():

    try:

        last_device = Device.query.order_by(Device.id.desc()).first()

        if not last_device.id:
            device_json = {"device": "http://172.16.1.123:5000/devices/", "message":"Not exist data record"}
            return jsonify(device_json)
        
        if last_device:
            last_id = last_device.id

        device_urls = [f"http://172.16.1.123:5000/devices/{i}" for i in range(1, last_id + 1)]
        device_json = {"device": device_urls}
        return jsonify(device_json)

    except Exception as e:
        print("Error no existe ID en la base de datos: ", str(e))
        return jsonify({"error": "Error al solicitar informacion de devices, no existe ID registrado"}), 400
    
@app.route('/db/', methods=['GET'])
def get_db():
    devices = Device.query.all()
    device_list = [device.to_dict() for device in devices]
    return jsonify(device_list)

@app.route('/devices/', methods=['POST'])
def post_devices():
    # Obtener los datos del nuevo equipo desde la solicitud JSON
    new_device = request.get_json()

    # Verificar que se hayan proporcionado datos válidos
    if not new_device:
        return jsonify({"error": "Datos invalidos"}), 400
    
    global device_id
    # Generar un identificador único para el nuevo equipo (por ejemplo, usando una secuencia)
    device_id = device_id + 1
    print("Device ID: ", device_id)
    # Agregar el nuevo equipo a los datos
    data[device_id] = new_device
    print("Data: ", data)

    # Crear un nuevo objeto Device y agregarlo a la base de datos
    device = Device(
        hostname=new_device['hostname'],
        loopback=new_device['loopback'],
        mgmt_ip=new_device['mgmt_ip'],
        role=new_device['role'],
        vendor=new_device['vendor'],
        os=new_device['os'],
        self_url=new_device['self_url'],
        
    )

    try:
        db.session.add(device)
        db.session.commit()
        print("Device: ", device)
        # Devolver una respuesta con los datos del nuevo equipo y el código de respuesta 201 (Created)
        return jsonify({"message": "Equipo registrado con éxito", "device": new_device}), 201
        # http POST http://172.30.157.251:5000/devices 'hostname'='iosv-1' 'loopback'='192.168.0.1' 'mgmt_ip'='172.16.1.225' 'role'='spine' 'vendor'='Cisco' 'os'='14.6'
    except Exception as e:
        db.session.rollback()
        print("Error al registrar el dispositivo:", str(e))
        return jsonify({"error": "Error al registrar el dispositivo"}), 500
    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crea las tablas en la base de datos si no existen
    app.run(host='0.0.0.0', debug=True)
    