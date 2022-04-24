import json
import requests
import xmltojson
import html2text
headers = {'Authorization': 'Bearer %s' % 'iwGMY9elHMjQqzt7rjlN9nerHSEYL-7zB0wvuMaRsOsgw_ntKrpjVlzWBwsmezjnNpaz8ypTnlEIvieJnnRAKbB3WrrVL2DSa2vE6KzElWCn_pVu6lUha7luToQ3YnYx'}
response = requests.get("https://api.yelp.com/v3/businesses/search?location=MI", headers=headers)
temp = json.loads(response.text)
print(temp['businesses'][0])
#
# # print(response.text)
# from bs4 import BeautifulSoup
# # f = open("sample.html")
# # html_text = f.read()
#
#
# soup = BeautifulSoup(response.text, 'html.parser')
# # for a in soup.findAll('a', href=True):
# #     a.extract()
# all_h4 = soup.find_all('h4')
# print(all_h4[0].text.strip())
#
# prices = tree.xpath('/html/body/div/div/div[1]/strong/text()')
# print(type(response.text))
# print(response)
# json_str = response.text
# print(json_str)
# json_str_ = json.loads(json_str).values()
# print(json_str_)
#
# import requests
#
# url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=40.6655101%2C-73.89188969999998&destinations=40.659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626&key=AIzaSyCVllA-JyoB6yYuLevEg1IY_n0tNy7CBYk"
#
# payload={}
# headers = {}
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.text)


# Generate token
import jwt.utils
import time
import math

{
  "developer_id": "b783aa4d-e753-4398-9fe8-6d9b4fbb5a30",
  "key_id": "40cb2153-3220-42e3-9f74-27ab0c9861c9",
  "signing_secret": "QgZXFpXK_p07E_r7uF6_vSwCQJFYcF85u98bGK7IOFw"
}

token = jwt.encode(
    {
        "aud": "doordash",
        "iss": "b783aa4d-e753-4398-9fe8-6d9b4fbb5a30",
        "kid": "40cb2153-3220-42e3-9f74-27ab0c9861c9",
        "exp": str(math.floor(time.time() + 60)),
        "iat": str(math.floor(time.time())),
    },
    jwt.utils.base64url_decode("QgZXFpXK_p07E_r7uF6_vSwCQJFYcF85u98bGK7IOFw"),
    algorithm="HS256",
    headers={"dd-ver": "DD-JWT-V1"})

# Generate delivery
import requests
import uuid

endpoint = "https://openapi.doordash.com/drive/v2/deliveries" # DRIVE API V2

headers = {"Authorization": "Bearer " + token,
            "Content-Type": "application/json"}

delivery_id = str(uuid.uuid4()) # Randomly generated UUID4

request_body = { # Modify pickup and drop off addresses below
    "external_delivery_id": delivery_id,
    "pickup_address": "901 Market Street 6th Floor San Francisco, CA 94103",
    "pickup_business_name": "Wells Fargo SF Downtown",
    "pickup_phone_number": "+16505555555",
    "pickup_instructions": "Enter gate code 1234 on the callbox.",
    "dropoff_address": "901 Market Street 6th Floor San Francisco, CA 94103",
    "dropoff_business_name": "Wells Fargo SF Downtown",
    "dropoff_phone_number": "+16505555555",
    "dropoff_instructions": "Enter gate code 1234 on the callbox.",
    "order_value": 1999
}

create_delivery = requests.post(endpoint, headers=headers, json=request_body) # Create POST request


# print(create_delivery.status_code)
print(json.loads(create_delivery.text)['tracking_url'])
# print(create_delivery.reason)
# print(create_delivery.url)

# # Check delivery status
# import requests
# import uuid
#
# endpoint = "https://openapi.doordash.com/drive/v2/deliveries/" # DRIVE API V2
#
# headers = {"Authorization": "Bearer " + token,
#             "Content-Type": "application/json"}
#
# get_delivery = requests.get(endpoint + '4028fc49-27ab-49ce-8984-66b52dbf6d49', headers=headers) # Create GET request
#
# print(get_delivery.status_code)
# print(get_delivery.text)
# print(get_delivery.url)

# from fatsecret import Fatsecret
#
# fs = Fatsecret(consumer_key='d4259f1c129e40159ed5e427ced6cbef', consumer_secret='65f44c2bb457449bb1d59b6cbbd9e58d')
# foods = fs.foods_search("Special Hot and Sour Soup")
# print(foods)