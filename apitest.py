import requests

url = 'https://api.thecatapi.com/v1/images/search'

def main():
	request = requests.get(url)
	request = request.json()
	listUrl = request[0]

	title = listUrl['id']
	image = listUrl['url']

	
	print(image)
	print(title)

	
