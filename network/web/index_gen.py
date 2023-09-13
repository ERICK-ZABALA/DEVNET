from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'You are at index()'

@app.route('/routers/<hostname>')
def routers(hostname):
    return 'You are at %s' % hostname

@app.route('/routers/<hostname>/interface/<int:interface_number>')
def interface(hostname, interface_number):
    return 'You are at %s interface %d' % (hostname, interface_number)

@app.route('/cisco/<hostname>/list_interfaces')
def devices(hostname):
    if hostname in routers:
        return 'Listing iterfaces for %s' % hostname
    else:
        return 'invalid hostname'
routers = ['r1', 'r2', 'r3']
for router in routers:
    with app.test_request_context ():
        print(url_for('devices', hostname=router))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    