import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt


URL = 'https://www.mashina.kg/'

HEADERS = {
    'Accept': 'text/css,*/*;q=0.1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}
@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)


@csrf_exempt
def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='app-shows-item-full')
    series = []

    for item in items:
        series.append({

            'title_url': URL + item.find('a').get('href'),
            'title_text': item.find('div', class_='app-shows-item-full').get_text(),
            'image': URL + item.find('div', class_='app-shows-item-full').find('img').get('src'),

        })
    return series()


@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        series2 = []
        for page in range(0,1):
            html = get_html(f'https://www.ts.kg/', params=page)
            series2.extend(get_data(html.text))
        print(f'\n{series2}\n')
    else:
        raise Exception('Parse Error...')

parser()



