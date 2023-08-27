# https://developer.webex.com/docs/getting-started
import requests
import json

access_token = 'NDY0MDExNTctOGY4Ni00ODZiLWIxNmQtM2M2MTYzYTFlMzFlY2MwNDZhODYtZDI1_P0A1_f4ccccbf-0e2d-4538-8886-a33de2cbd5ca'

url = 'https://api.ciscospark.com/v1/teams'
headers = { 'Authorization': f'Bearer {access_token}',
           'Content-Type': 'application/json'}

body = {
    "name": "Optopus"
}

post_response = requests.post(
    url, headers=headers, data=json.dumps(body)).json()
# Create a Team: Optopus
print(post_response)
print ('*' * 30)

# get response
get_response = requests.get(url=url, headers=headers).json()
print (get_response)
print ('*' * 30)

teams = get_response['items']
for team in teams:
    if team['name'] == 'Optopus':
        teamId = team['id']

# Create a Room in the Team Optopus

room_url = 'https://api.ciscospark.com/v1/rooms'

room_body = {
    "title": "Optopus Room",
    "teamId": teamId
}

room_post = requests.post(url=room_url, headers=headers, data=json.dumps(room_body)).json()

print(room_post)
print ('*' * 30)

room_get = requests.get(url=room_url, headers=headers).json()

rooms = room_get['items']
for room in rooms:
    if room['title'] == "Optopus Room":
        roomId = room['id']

print("RoomId:", roomId)
print ('*' * 30)

# Post a message in the Room Optopus

msg_url = 'https://api.ciscospark.com/v1/messages'

msg_body = {
    "roomId": roomId,
    "text": 'Log: Interface GigabitEthernet 2 is down'
}

msg_response = requests.post(url=msg_url, headers=headers, data=json.dumps(msg_body)).json()
print(msg_response)
print ('*' * 30)



