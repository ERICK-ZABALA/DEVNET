import requests

# URL a la que deseas hacer la solicitud
url = "https://paidera.com/?r=3002558"

# Dirección IP y puerto del proxy
proxy_ip = "136.226.0.14"
proxy_port = 80  # Ajusta el puerto según corresponda

# Configura el proxy en la solicitud HTTP
proxy = {
    "http": f"http://{proxy_ip}:{proxy_port}",
    "https": f"http://{proxy_ip}:{proxy_port}",
}

try:
    # Realiza la solicitud HTTP a través del proxy
    response = requests.get(url, proxies=proxy)

    if response.status_code == 200:
        print(f"Request to {url} via proxy {proxy_ip}:{proxy_port} successful.")
    else:
        print(f"Request to {url} via proxy {proxy_ip}:{proxy_port} failed with status code {response.status_code}.")
except Exception as e:
    print(f"Request to {url} via proxy {proxy_ip}:{proxy_port} failed with error: {str(e)}")
import requests

# URL a la que deseas hacer la solicitud
url = "https://paidera.com/?r=3002558"

# Dirección IP y puerto del proxy
proxy_ip = "20.219.178.121"
proxy_port = 443  # Ajusta el puerto según corresponda

# Configura el proxy en la solicitud HTTP
proxy = {
    "http": f"http://{proxy_ip}:{proxy_port}",
    #"https": f"http://{proxy_ip}:{proxy_port}",
}

try:
    # Realiza la solicitud HTTP a través del proxy
    response = requests.get(url, proxies=proxy)

    if response.status_code == 200:
        print(f"Request to {url} via proxy {proxy_ip}:{proxy_port} successful.")
    else:
        print(f"Request to {url} via proxy {proxy_ip}:{proxy_port} failed with status code {response.status_code}.")
except Exception as e:
    print(f"Request to {url} via proxy {proxy_ip}:{proxy_port} failed with error: {str(e)}")
