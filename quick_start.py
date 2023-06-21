import httpx

# r = httpx.get('https://httpbin.org/get')
# print(r)
# print(r.text)

# r = httpx.post('https://httpbin.org/post', data={'key': 'value'})
# print(r.text)

# r = httpx.put('https://httpbin.org/put', data={'key': 'value'})
# print(r.text)

# r = httpx.delete('https://httpbin.org/delete')
# print(r.text)

# r = httpx.head('https://httpbin.org/get')
# print(r.headers)

# r = httpx.options('https://httpbin.org/get')
# print(r.headers)

# params = {'key1': 'value1', 'key2': 'value2'}
# r = httpx.get('https://httpbin.org/get', params=params)
# print(r.url)

# params = {'key1': 'value1', 'key2': ['value2', 'value3']}
# r = httpx.get('https://httpbin.org/get', params=params)
# print(r.url)

# r = httpx.get('https://www.example.org/')
# print(r.text)
# print(r.encoding)
# print(r.content)

# r = httpx.get('https://api.github.com/events')
# print(r.json())

# url = 'https://httpbin.org/headers'
# headers = {'user-agent': 'my-app/0.0.1'}
# r = httpx.get(url, headers=headers)
# print(r.text)

# data = {'key1': 'value1', 'key2': 'value2'}
# r = httpx.post("https://httpbin.org/post", data=data)
# print(r.text)

# data = {'key1': ['value1', 'value2']}
# r = httpx.post("https://httpbin.org/post", data=data)
# print(r.text)

# files = {'upload-file': open('quick_start.py', 'rb')}
# r = httpx.post("https://httpbin.org/post", files=files)
# print(r.text)

# files = {'upload-file': ('quick_start.py', open('quick_start.py', 'rb'), 'text/plain')}
# r = httpx.post("https://httpbin.org/post", files=files)
# print(r.text)

# data = {'message': 'Hello, world!'}
# files = {'file': open('quick_start.py', 'rb')}
# r = httpx.post("https://httpbin.org/post", data=data, files=files)
# print(r.text)

# data = {'integer': 123, 'boolean': True, 'list': ['a', 'b', 'c']}
# r = httpx.post("https://httpbin.org/post", json=data)
# print(r.text)

# content = b'Hello, world'
# r = httpx.post("https://httpbin.org/post", content=content)
# print(r.text)

# r = httpx.get('https://httpbin.org/get')
# print(r.status_code)
# print(r.status_code == httpx.codes.OK)

# not_found = httpx.get('https://httpbin.org/status/404')
# print(not_found.status_code)
# not_found.raise_for_status()

# r = httpx.get('https://httpbin.org/get')
# print(r.raise_for_status())
# print(r.headers)
# print(r.headers['Content-Type'])
# print(r.headers.get('content-type'))

# with httpx.stream("GET", "https://www.example.com") as r:
#     for data in r.iter_bytes():
#         print(data)

# with httpx.stream("GET", "https://www.example.com") as r:
#     for text in r.iter_text():
#         print(text)

# with httpx.stream("GET", "https://www.example.com") as r:
#     for line in r.iter_lines():
#         print(line)

# with httpx.stream("GET", "https://www.example.com") as r:
#     for chunk in r.iter_raw():
#         print(chunk)

# with httpx.stream("GET", "https://www.example.com") as r:
#     print(r.headers['Content-Length'])
#     if int(r.headers['Content-Length']) < 1000:
#         r.read()
#         print(r.text)

# r = httpx.get('https://httpbin.org/cookies/set?chocolate=chip')
# print(r.cookies['chocolate'])

# cookies = {"peanut": "butter"}
# r = httpx.get('https://httpbin.org/cookies', cookies=cookies)
# print(r.json())

# cookies = httpx.Cookies()
# cookies.set('cookie_on_domain', 'hello, there!', domain='httpbin.org')
# cookies.set('cookie_off_domain', 'nope.', domain='example.org')
# r = httpx.get('http://httpbin.org/cookies', cookies=cookies)
# print(r.json())

# r = httpx.get('http://github.com/')
# print(r.status_code)
# print(r.history)
# print(r.next_request)

# r = httpx.get('http://github.com/', follow_redirects=True)
# print(r.url)
# print(r.status_code)
# print(r.history)

# httpx.get('https://github.com/', timeout=0.001)

# httpx.get('https://github.com/', timeout=None)

# httpx.get("https://example.com", auth=("my_user", "password123"))

# auth = httpx.DigestAuth("my_user", "password123")
# httpx.get("https://example.com", auth=auth)

# try:
#     response = httpx.get("https://www.example.com/", timeout=0.001)
# except httpx.RequestError as exc:
#     print(f"An error occurred while requesting {exc.request.url!r}.")

# response = httpx.get("https://www.example.com/")
# try:
#     response.raise_for_status()
# except httpx.HTTPStatusError as exc:
#     print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")

# try:
#     response = httpx.get("https://www.example.com/")
#     response.raise_for_status()
# except httpx.HTTPError as exc:
#     print(f"Error while requesting {exc.request.url!r}.")

try:
    response = httpx.get("https://www.example.com/")
    response.raise_for_status()
except httpx.RequestError as exc:
    print(f"An error occurred while requesting {exc.request.url!r}.")
except httpx.HTTPStatusError as exc:
    print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
