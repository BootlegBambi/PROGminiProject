import marvel_conn
import marvel_data as mvd
'''
data = marvel_conn.get_data("/v1/public/characters", {'limit': '10', 'offset': '20'})

if data:
    print(data)
else:
    print("Failed to get data!")
'''
# 1493 charachters - mvd.get_numberofcharacters(character)
# off = rand( 0-(total-1) )
# character = marvel_conn.get_data("/v1/public/characters", {'offset': off, 'limit': '1'})

character = marvel_conn.get_data("/v1/public/characters", {'offset': '200', 'limit': '1'})
if character:
    print(character)
else:
    print("Failed to get data!")
