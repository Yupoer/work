import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "rh1we56hy4r5hg14re6h"
USER_NAME = "alex"
ID = "graph1"

user_params = {
    "token": TOKEN,
    "username":USER_NAME ,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{ID}"

today = datetime.now()
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("how many km did you cycle today?"),
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.test)

update_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}
# response = requests.put(url=update_pixel_endpoint, json=new_pixel_data, headers=headers)
# print(response.test)

delete_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.test)

