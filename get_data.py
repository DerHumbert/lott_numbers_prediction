import requests
import bs4
import re 

def get_links(links):
	urls = []
	for link in links:
		urls.append(link.get('href'))
	return urls

def download_file(link):
	file = requests.get(link, verify=False)
	print(file.text)
	write_path = 'data/Melate.csv'

	print("Writing file: ", write_path)
	with open(write_path, 'w') as fp:
		fp.write(file.text)

if __name__ == "__main__":
    WEB_ROOT = 'https://www.loterianacional.gob.mx'
    r = requests.get('https://www.loterianacional.gob.mx/Melate/Resultados', verify=False)

    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a', href=True)
    urls = get_links(links)

    q = re.compile(".*/Home/Historicos")
    hist = list(filter(q.match,urls))

    url = hist[0][5:]
    url = WEB_ROOT + url 
    print(url)
    
    download_file(url)
