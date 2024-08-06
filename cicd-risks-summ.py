#!/usr/bin/env python3
import requests
import json
import authenticate # authenticate logic hitting the /login endpoint

url = "https://api2.prismacloud.io/code/api/v1/pipeline-risks"
response = json.loads(authenticate.login())
JWTtoken = response["token"]

payload = json.dumps({
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'authorization': JWTtoken
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
print(response)