import requests
from cookiesForRequests import cookies_for_requests, userAgent

with requests.Session() as s:

    s.headers.update({"user-agent": userAgent})
    for cookie in cookies_for_requests:
        s.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'])
    response = s.get("https://www.sahibinden.com")
    print(response.status_code)

