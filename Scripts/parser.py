import requests
from bs4 import BeautifulSoup


def get_categories(data):
    print("Getting categories...")
    categories = {}
    soup = BeautifulSoup(data, "lxml")
    group_divs = soup.find_all("div", {"class": "mw-category-group"})
    for div in group_divs:
        links = div.find_all("a")
        for link in links:
            title = link.get("title")
            href = link.get("href")
            categories[title] = "https://ru.wikipedia.org" + href
    print(f"Found Categories: {len(categories)}")
    return categories


def get_first_paragraph(data):
    soup = BeautifulSoup(data, "lxml")
    parser_output_out = soup.find("div", {"class": "mw-body-content mw-content-ltr"})
    parser_output = parser_output_out.find("div", {"class": "mw-parser-output"})
    first_paragraph = parser_output.find("p", {"class": None}, recursive=False)
    return first_paragraph.text


def process_categories(categories):
    result = {}
    for title, link in categories.items():
        print(f"Processing Piece: {title}, on link: {link}")
        data = requests.get(link).content
        first_paragraph = get_first_paragraph(data)
        result[title] = first_paragraph.strip()
    return result


def clean_categories(categories):
    return {k: v for k, v in categories.items() if "Категория" not in k}


def parsing():
    categories_url = "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%92%D1%8B%D0%BF%D1%83%D1%81%D0%BA%D0%BD%D0%B8%D0%BA%D0%B8_%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B3%D0%BE%D1%80%D0%BD%D0%BE%D0%B3%D0%BE_%D1%83%D0%BD%D0%B8%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82%D0%B0"
    data_categories = requests.get(categories_url).content
    categories = get_categories(data_categories)
    categories = clean_categories(categories)
    result = process_categories(categories)
    return result
    '''print (result)
    for x in result:
        print(x)
        print('Биография', '-', result[x])



if __name__ == "__main__":
    main()'''