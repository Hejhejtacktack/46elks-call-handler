import argparse
import json
import os
import requests

parser = argparse.ArgumentParser(description="Make a call and forward it to {who?} using 46elks' API")

parser.add_argument("API_USERNAME", type=str, help="Your 46elks API username")
parser.add_argument("API_PASSWORD", type=str, help="Your 46elks API password")
parser.add_argument("Caller", type=str, help="Caller's phone number in E.164 format (e.g.+46701234567)."
                                             "This number shows as caller (also when forwarding call)")
parser.add_argument("Callee", type=str, help="Callee's phone number in E.164 format (e.g.+46701234567)")

args = parser.parse_args()

auth = (
    args.API_USERNAME,
    args.API_PASSWORD
    )

action = {
    "connect" : os.getenv('API_USERNAME') # Make user choose action?
}

fields = {
    'from': args.Caller,
    'to': args.Callee,
    'voice_start': json.dumps(action),
    }

response = requests.post(
    "https://api.46elks.com/a1/calls",
    data=fields,
    auth=auth
    )

print(response.text)