import requests

BASE = "http://127.0.0.1:5000/"

"""data = [{"name": "HI my video","likes":50000,"views": 1001},
        {"name": "HI my video2","likes":500000,"views": 1111},
        {"name": "HI my video3","likes":500000,"views": 1908}]

for i in range(len(data)):
    response = requests.put(BASE + "video/"+ str(i), data[i])
    print(response.json())"""

#input()
response= requests.get(BASE + "video/2")
print(response.json())

#input()
#response= requests.patch(BASE + "video/1", {"views": 3333, "likes":1613})
#print(response.json())

#response= requests.delete(BASE + "video/2")
#print(response)