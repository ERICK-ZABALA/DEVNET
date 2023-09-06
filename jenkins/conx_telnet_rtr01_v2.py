#!/usr/bin/python3

import pexpect
import json

# Cargar datos de acceso desde un archivo JSON
with open("/home/devnet/devnet/DEVNET/jenkins/routers.json", "r") as json_file:
    routers_data = json.load(json_file)

# Iterar a través de los datos de acceso de los routers
for router_data in routers_data:
    host = router_data["host"]
    port = router_data["port"]
    username = router_data["username"]
    password = router_data["password"]
    prompt = router_data["prompt"]

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
        print(f"Salida del router {host}:\n{tn.before.decode('utf-8')}")

        tn.close()

    except Exception as e:
        print(f"Error en el router {host}:", str(e))
