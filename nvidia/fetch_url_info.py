import requests
from bs4 import BeautifulSoup
import json

def extract_data(url):
    data = {}

    try:
        
        response = requests.get(url)
        response.raise_for_status()  

        
        soup = BeautifulSoup(response.text, 'html.parser')

    
        data['title'] = soup.title.string if soup.title else 'No title found'

    
        description_meta = soup.find('meta', attrs={'name': 'description'})
        data['description'] = description_meta['content'] if description_meta else 'No description found'

        
        keywords_meta = soup.find('meta', attrs={'name': 'keywords'})
        data['keywords'] = keywords_meta['content'] if keywords_meta else 'No keywords found'

        
        paragraphs = [p.get_text() for p in soup.find_all('p')]
        data['paragraphs'] = paragraphs

        
        links = [a['href'] for a in soup.find_all('a', href=True)]
        data['links'] = links

    except requests.exceptions.RequestException as e:
        data['error'] = str(e)

    return data


url_input = input("Enter a URL: ")
result = extract_data(url_input)


print(json.dumps(result, indent=4))
