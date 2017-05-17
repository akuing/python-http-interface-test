import requests, time
r = requests.post('http://requestb.in/1j3qsun1', data={"ts":time.time()})
print(r.status_code)
print(r.content)