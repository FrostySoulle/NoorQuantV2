#==========================================================
# Part 1 Imports
#==========================================================

from kiteconnect import KiteConnect
from urllib.parse import urlparse, parse_qs
import json

#==========================================================
# Part 2 Credentials
#==========================================================

API_KEY = "uqjd28ofefv3je62"
API_SECRET = "q0tqjptdeqm2cynsxu49pmg9gnsd7jd8"

kite = KiteConnect(api_key=API_KEY)

#==========================================================
# Part 3 Login
#==========================================================

print("Open this URL in your browser:\n")
print(kite.login_url())

print()
redirect_url = input("Paste redirected URL:\n")

#==========================================================
# Part 4 Extract Request Token
#==========================================================

request_token = parse_qs(
    urlparse(redirect_url).query
)["request_token"][0]

print("\nRequest Token:", request_token)

#==========================================================
# Part 5 Generate Access Token
#==========================================================

data = kite.generate_session(
    request_token=request_token,
    api_secret=API_SECRET
)

access_token = data["access_token"]

print("\nAccess Token Generated Successfully")

#==========================================================
# Part 6 Save Credentials
#==========================================================

config = {
    "api_key": API_KEY,
    "api_secret": API_SECRET,
    "access_token": access_token
}

with open("config.json", "w") as f:
    json.dump(config, f, indent=4)

print("Saved to config.json")