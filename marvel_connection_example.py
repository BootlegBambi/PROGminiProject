import marvel_conn

data = marvel_conn.get_data("/v1/public/characters")

if data:
    print(data)
else:
    print("Failed to get data!")
