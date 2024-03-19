import os
import requests

authorization_whapi = os.environ['authorization_whapi']
group_id = os.environ['group_id']
mycredential = os.environ['mycredential']
proxy_link = os.environ['proxy_link']
spreadsheet_link = os.environ['spreadsheet_link']

for var in [authorization_whapi, group_id]:
  for q in var:
    print(q)
