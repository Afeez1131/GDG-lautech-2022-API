import requests
from rest_framework.reverse import reverse

token = "30e7ce4c48bf4cceed984ed00cfa38e446845ebe"
headers = {'Authorization': "Token %s" % token}
url = "http://127.0.0.1:3000/api/v1/gdg/5/"
# data = {
#     'name': 'Emmanuel Seun',
#     'state': 'Kwara State',
#     'phone': '08055922312',
#     'email': 'emmanuel-nduka@gmail.com',
#     'interest': 'Web. Development'
# }
data = {
    "name": "Badmus Lateef",
    "state": "Kano State",
    "interest": "Data Science.",
    "phone": "08105505012",
    "email": "adm2@gmail.com"
}
# response = requests.post(url, data=data, headers=headers)
response = requests.delete(url, headers=headers)
print(response.status_code, response.text)
