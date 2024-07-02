import requests
def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, "w") as f:
     f.write(r.text) 


url = "https://haqtify.com/about/"


r = requests.get(url)
print(r.text)

fetchAndSaveToFile(url, "Data/times.html")