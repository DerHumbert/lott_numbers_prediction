import requests
import bs4


def filter_links(tag):
	if isinstance(tag, str):
		return tag.endswith('csv')

def get_links(tags_list):
	return [WEB_ROOT + tag.attrs['href'] for tag in tags_list]

def download_file(link, directory):
	file = requests.get(link).content
	name = file_link.split('/')[-1]
	write_path = directory + name

	print("Writing file: ", write_path)
	with open(write_path, 'wb') as fp:
		fp.write(file)

if __name__ == "__main__":
    WEB_ROOT = 'https://www.loterianacional.gob.mx'
    write_path = '~/data/'

    r = requests.get('https://www.loterianacional.gob.mx/Melate/Resultados', verify=False)

    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    results = soup.select("p#melate > a")
    links = get_links(results)

    print(links)