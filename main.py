import requests

def getting401():
    response1 = requests.get('https://httpbin.org/status/401', )
    if response1.status_code < 400:
        print(response1.ok)
    else:
        for i in range(10):
            if not response1.ok:
                response1 = response1
                print(response1.status_code)

def gettingOK():
    response = requests.get('https://httpbin.org/get')
    if response.status_code < 400:
        print(response.ok)
    else:
        for i in range(10):
            if not response.ok:
                response = response
                print(response.status_code)

getting401()
gettingOK()
