import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt

URL = "https://www.ts.kg/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}


@csrf_exempt
def get_html(url, params=""):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


@csrf_exempt
def get_data(html):
    soup = BS(html, "html.parser")
    items = soup.find_all("div", class_="app-shows-container")
    movies = []

    for item in items:
        movies.append(
            {
                "title_url": URL + item.find("a").get("href"),
                "title_text": item.find("span", class_="app-shows-card-title").get_text(),
                "image": URL + item.find("div", class_="app-shows-item-full").find("img").get("src"),
            }
        )

    return movies


@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        movies2 = []
        for page in range(0, 1):
            html = get_html(f"https://www.ts.kg/category/films", params=page)
            movies2.extend(get_data(html.text))
        return movies2
        # print(f'\n{movies2}\n')
    else:
        raise Exception("Parse Error...")


# parser()
