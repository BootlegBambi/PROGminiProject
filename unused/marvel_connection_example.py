import marvel_conn

'''
data = marvel_conn.get_data("/v1/public/characters", {'limit': '10', 'offset': '20'})

if data:
    print(data)
else:
    print("Failed to get data!")
'''

character = marvel_conn.get_data("/v1/public/characters", {'offset': '200', 'limit': '1'})
if character:
    print(character)
else:
    print("Failed to get data!")
