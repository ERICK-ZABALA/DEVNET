from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI(
    access_token='NDY0MDExNTctOGY4Ni00ODZiLWIxNmQtM2M2MTYzYTFlMzFlY2MwNDZhODYtZDI1_P0A1_f4ccccbf-0e2d-4538-8886-a33de2cbd5ca'
)

# GET TEAM INFO
teams = api.teams.list()

for team in teams:
    print(team)
    if getattr(team, 'name') != 'Optopus':
        create_team = api.teams.create('Optopus')
        teamId = getattr(create_team, "id")
    else:
        teamId = team.id

# ROLES
#roles = api.roles.list()
#for role in roles:
#    print(role)


# PEOPLE 
# Need privilege of admin to create a people

print(api.people.me())
print(api.people.list())

#email= ['devnet.code@gmail.com']
#api.people.create(emails=email)

# ROOMS
rooms = api.rooms.list()

evaluator = False
for room in rooms:
    if room.title == 'Optopus':
        evaluator = True
        roomId = room.id

if evaluator is False:
    new_room = api.rooms.create('Optopus', teamId=teamId)
    roomId = new_room.id

# MESSAGE

api.messages.create(roomId=roomId, text="Posted from SDK Webex")
