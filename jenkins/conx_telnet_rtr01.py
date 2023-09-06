import pexpect

# Datos de acceso al dispositivo
host = '10.10.20.173'
port = 23  # Puerto Telnet por defecto
username = 'cisco'
password = 'cisco'
prompt = "RP/0/RP0/CPU0:core-rtr01#"

try:
    # Crear una instancia de Telnet usando pexpect
    tn = pexpect.spawn(f"telnet {host} {port}")

    # Esperar a que el dispositivo solicite el nombre de usuario
    tn.expect("Username:")
    
    # Ingresar el nombre de usuario
    tn.sendline(username)

    # Esperar a que el dispositivo solicite la contraseña
    tn.expect("Password:")
    
    # Ingresar la contraseña
    tn.sendline(password)

    # Esperar a que el dispositivo responda (ajusta según sea necesario)
    tn.expect(prompt)  # Reemplaza "prompt_del_dispositivo" con el prompt real del dispositivo

    # Enviar el comando 'show version'
    tn.sendline("show version")

    # Esperar a que el dispositivo responda (ajusta según sea necesario)
    tn.expect(prompt)  # Reemplaza "prompt_del_dispositivo" con el prompt real del dispositivo

    # Imprimir la salida del comando
    print(tn.before.decode('utf-8'))

    tn.close()

except Exception as e:
    print("Error:", str(e))

