import httpx

def get_wikipedia_path(start_page, end_page):
    url = f'https://ru.wikipedia.org/w/api.php?action=query&format=json&titles={start_page}|{end_page}&prop=links&pllimit=max'
    response = httpx.get(url)
    data = response.json()

    start_page_id = next(iter(data['query']['pages']))
    end_page_id = next(iter(data['query']['pages']), 1)

    links = data['query']['pages'][start_page_id]['links']
    path = [link['title'] for link in links]

    while end_page_id not in data['query']['pages']:
        plcontinue = data['continue']['plcontinue']
        url = f'https://ru.wikipedia.org/w/api.php?action=query&format=json&titles={start_page}|{end_page}&prop=links&pllimit=max&plcontinue={plcontinue}'
        response = httpx.get(url)
        data = response.json()
        links = data['query']['pages'][start_page_id]['links']
        path.extend([link['title'] for link in links])

    return path

# Пример использования
start_page = 'Философия'
end_page = 'Математика'

path = get_wikipedia_path(start_page, end_page)

print(f"Количество переходов: {len(path)}")
print("Переходы:")
for page in path:
    print(page)