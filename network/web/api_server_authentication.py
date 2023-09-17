
from flask import Flask, jsonify, request, url_for
from flask_sqlalchemy import SQLAlchemy
from nornir_custom.ssh_nornir_server import show_list

from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
# authentication instance
auth = HTTPBasicAuth()

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

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    
    if user is None:
        return False
    if user.verify_password(password) is True:
        #g.user = user
        return True
    return False


@app.before_request
@auth.login_required
def before_request():
    pass

@auth.error_handler
def unathorized():
    response = jsonify({'status': 401, 'error': 'unauthorized','message': 'please authenticate'})
    response.status_code = 401
    return response

"""
http --auth erick:secret GET http://172.30.157.251:5000/devices

Output:

HTTP/1.1 200 OK
Connection: close
Content-Length: 231
Content-Type: application/json
Date: Sun, 17 Sep 2023 06:52:49 GMT
Server: Werkzeug/2.3.7 Python/3.11.4

{
    "device": [
        "http://172.16.1.123:5000/devices/1",
        "http://172.16.1.123:5000/devices/2",
        "http://172.16.1.123:5000/devices/3",
        "http://172.16.1.123:5000/devices/4",
        "http://172.16.1.123:5000/devices/5"
    ]
}



"""

"""
http GET http://172.30.157.251:5000/devices
"""
@app.route('/devices', methods=['GET'])
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
    
@app.route('/db', methods=['GET'])
def get_db():
    devices = Device.query.all()
    device_list = [device.to_dict() for device in devices]
    return jsonify(device_list)
"""
http POST http://172.30.157.251:5000/devices/ 'hostname'='iosv-4' 'loopback'='192.168.1.4' 'mgmt_ip'='172.16.1.4' 'role'='spine-4' 'vendor'='Fortinet' 'os'='4.0'

http POST http://172.30.157.251:5000/devices/ 'hostname'='iosv-4'
 'loopback'='192.168.1.4' 'mgmt_ip'='172.16.1.4' 'role'='spine-4' 
 'vendor'='Fortinet' 'os'='4.0'
"""
@app.route('/devices/', methods=['POST'])
def post_devices():
    # Obtener los datos del nuevo equipo desde la solicitud JSON
    new_device = request.get_json()

    # Verificar que se hayan proporcionado datos válidos
    if not new_device:
        return jsonify({"error": "Datos invalidos"}), 400
    
    # Crear un nuevo objeto Device y agregarlo a la base de datos
    device = Device(
        hostname=new_device['hostname'],
        loopback=new_device['loopback'],
        mgmt_ip=new_device['mgmt_ip'],
        role=new_device['role'],
        vendor=new_device['vendor'],
        os=new_device['os']
    )

    try:
        # insert device to db
        db.session.add(device)
        db.session.commit()
        # get all info from db
        devices = Device.query.all()
        devices_list = [device.to_dict() for device in devices]
        # captured last device id
        device_id = devices_list [-1]["id"]
        print("Device ID: ", device_id)
        # update parameter id into instance device
        device.id = device_id
        print(device)
        # Generate a URL for the 'get_device' route with id=x
        device_url = device.get_url()
        print(device_url)

        # Get the existing device from the database
        existing_device = Device.query.get(device_id)
        existing_device.self_url = device_url
        db.session.commit()
        # Devolver una respuesta con los datos del nuevo equipo y el código de respuesta 201 (Created)
        return jsonify({"message": "Equipo registrado con éxito", "device": new_device}), 201, {'Location': device_url}
        # http POST http://172.30.157.251:5000/devices 'hostname'='iosv-1' 'loopback'='192.168.0.1' 'mgmt_ip'='172.16.1.225' 'role'='spine' 'vendor'='Cisco' 'os'='14.6'
    except Exception as e:
        db.session.rollback()
        print("Error al registrar el dispositivo:", str(e))
        return jsonify({"error": "Error al registrar el dispositivo"}), 500
"""
http GET http://172.30.157.251:5000/device/1
"""    
@app.route('/device/<int:id>', methods=['GET'])
def get_device(id):
    devices = Device.query.get_or_404(id).to_dict()
    return jsonify(devices)
"""
http GET http://172.30.157.251:5000/devices/1
"""
@app.route('/devices/<int:id>', methods=['GET'])
def interface(id):
    if id == 0:
        print("Error al solicitar el request, ID :", str(id))
        return jsonify({"error": "Error al solicitar GET, verifica el ID "}), 400
    else:
        try:
            devices = Device.query.all()
            device_list = [device.to_dict() for device in devices]
            return jsonify(device_list[id - 1])
        except Exception as e:
            print("Error al solicitar GET Verifica ID fuera de rango:", str(e))
            return jsonify({"error": "Error al solicitar GET Verifica ID fuera de rango:"}), 400
    

"""
http PUT http://172.30.157.251:5000/devices/1 'hostname'='iosv-1' 'loopback'='192.168.1.0' 'mgmt_ip'='172.16.1.1' 'role'='spine-1' 'vendor'='Cisco' 'os'='1.0'

http PUT http://172.30.157.251:5000/devices/1 'hostname'='iosv-1' 
'loopback'='192.168.1.0' 'mgmt_ip'='172.16.1.1' 'role'='spine-1' 
'vendor'='Cisco' 'os'='1.0'
"""
@app.route('/devices/<int:id>', methods=['PUT'])
def update_device(id):
    print("id:",id)
    # Get the existing device from the database
    existing_device = Device.query.get(id)
    print("device:", existing_device)

    if not existing_device:
        return jsonify({"error": "Device not found"}), 404

    # Obtener los datos del nuevo equipo desde la solicitud JSON
    updated_data = request.get_json()

        # Update the fields of the existing device
    existing_device.hostname = updated_data.get('hostname', existing_device.hostname)
    existing_device.loopback = updated_data.get('loopback', existing_device.loopback)
    existing_device.mgmt_ip = updated_data.get('mgmt_ip', existing_device.mgmt_ip)
    existing_device.role = updated_data.get('role', existing_device.role)
    existing_device.vendor = updated_data.get('vendor', existing_device.vendor)
    existing_device.os = updated_data.get('os', existing_device.os)
    
    try:
        db.session.commit()
        return jsonify({"message": "Device updated successfully", "device": existing_device.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error updating device", "details": str(e)}), 500

"""
http GET http://172.30.157.251:5000/devices/list/1
"""

@app.route('/devices/list/<int:id>', methods=['GET'])
def get_show_list(id):
    result = show_list()
    print(result)
    return jsonify({"show list": result})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crea las tablas en la base de datos si no existen
        
        #u = User(username='erick')
        #u.set_password('secret')
        #db.session.add(u)
        #db.session.commit()
      
    app.run(host='0.0.0.0', debug=True)
    