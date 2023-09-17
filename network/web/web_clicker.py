import requests
import concurrent.futures

# Define the URL you want to request
url = "https://paidera.com/?r=3002558"

# Define the number of requests you want to make
num_requests = 1000

# Define a function to send HTTP requests


def send_request(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Request to {url} successful.")
        else:
            print(
                f"Request to {url} failed with status code {response.status_code}.")
    except Exception as e:
        print(f"Request to {url} failed with error: {str(e)}")


# Use concurrent.futures to send multiple requests concurrently
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Submit the requests concurrently
    futures = [executor.submit(send_request, url) for _ in range(num_requests)]

    # Wait for all requests to complete
    concurrent.futures.wait(futures)
