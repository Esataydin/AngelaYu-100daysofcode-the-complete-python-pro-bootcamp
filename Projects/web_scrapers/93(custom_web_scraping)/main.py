from bs4 import BeautifulSoup
import urllib.request

import csv


link = 'https://www.audible.com/search?keywords=book&node=18573211011'


def get_data(link) -> list[list[str]]:
    """Gets data and organizes it from the specified website link given"""
    data_list = []
    web_url = urllib.request.urlopen(link)
    data = web_url.read()
    soup = BeautifulSoup(data, 'html.parser')
    products = soup.find_all(class_='productListItem')
    for product in products:
        list_items = product.find_all('li', class_='bc-list-item')
        book_data = []
        for item in list_items:
            if item.string:
                if 'Narrated by:' not in str(item.string):
                    str_data = str(item.string.replace('\\n', '')).strip()
                    if 'By:' in str_data:
                        str_data = str_data[27:]
                    if 'Length:' in str_data:
                        str_data = str_data[8:]
                    if ',' in str_data:
                        str_data = str_data.replace(',', ' -')
                    book_data.append(str_data)
        data_list.append(book_data)
    return data_list


def create_write_csv(data):
    """Creates and writes data in csv file"""
    with open('books.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["Book_name", "Author", "Length", 'Is_abridged']
        writer.writerow(field)
        for row in data:
            writer.writerow(row)


def main() -> None:
    data_list = get_data(link)
    create_write_csv(data_list)


if __name__ == '__main__':
    main()
