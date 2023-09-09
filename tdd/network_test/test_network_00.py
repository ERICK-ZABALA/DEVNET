import subprocess

host_list = ['www.cisco.com', 'www.google.com']
ping_time = []

for host in host_list:
    p = subprocess.Popen(['ping', '-c', '1', host], stdout=subprocess.PIPE)
    result, _ = p.communicate()  # Captura la salida estándar y descarta la salida de error
    result = result.decode('utf-8')  # Convierte la salida binaria a una cadena de texto
    #print(result)
    # Dividir la salida en líneas y obtener la línea que contiene la información del tiempo
    lines = result.splitlines()
    print("Lines: ",lines)

    for line in lines:
        if 'time=' in line:
            parts = line.split()
            print("parts: ", parts)
            host = parts[4]
            time = parts[7]  # Obtiene el valor del tiempo sin el "time=" al principio
            ping_time.append((host, time))

print("ping time:", ping_time)

