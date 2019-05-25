import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTU4NzcyNTc0LCJqdGkiOiI0M2ZmZDFiZTBjOTU0YjMxOWFhMDI0NmZlMTk3NDk5MCIsInVzZXJfaWQiOjF9.8RqN3JrWzJWngeLjzkbwBDP5NldWtgZFiMuRryetZBo'

r = requests.get('http://127.0.0.1:8000/jobs', headers=headers)

print(r.text)
