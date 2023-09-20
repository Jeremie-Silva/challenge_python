"""Challenge 00
Send a GET request to URL and get the value of specific key on the response JSON.
Get the value of `token`.
Note: this is web service API, so you won't see a visual display.
    Test
Access URL -> https://pythonidae.herokuapp.com/web/generate
"""

import httpx


url: str = "https://pythonidae.herokuapp.com/web/generate"
r = httpx.get(url)

try:
    r.raise_for_status()
except httpx.HTTPStatusError:
    print(f"-----------ERROR : {r.status_code} -----------")
else:
    print(r.text)
    print(r.status_code)
