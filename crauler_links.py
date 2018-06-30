from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException as NoElement


urls = ['https://e-dostavka.by/catalog/400000203.html', 'https://e-dostavka.by/catalog/400000173.html',
        'https://e-dostavka.by/catalog/400000177.html', 'https://e-dostavka.by/catalog/400000172.html',
        'https://e-dostavka.by/catalog/400000175.html', 'https://e-dostavka.by/catalog/400000170.html',
        'https://e-dostavka.by/catalog/400000176.html', 'https://e-dostavka.by/catalog/400000169.html',
        'https://e-dostavka.by/catalog/400000179.html', 'https://e-dostavka.by/catalog/400000178.html',
'https://e-dostavka.by/catalog/400000174.html',
'https://e-dostavka.by/catalog/400000205.html'
]


class Parser:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.product_links = []
        self.current_page = 0


    def start(self):
        for self.category_url in urls:
            self.driver.get(self.category_url)
            # self.driver.get('https://e-dostavka.by/catalog/400000177.html')
            self.get_info()
            self.get_all_product_links()
            print(self.product_links)
        print('Всего товаров: ', len(self.product_links))
        with open('products.txt', 'w') as f:
            for link in self.product_links:
                f.write(link)
                f.write('\n')




    def show_all_page(self):
# На странице помещается 144 товара, это 48 строк по 3 в строке, 24 PageDown
#         self.amount_products_on_page = self.driver.find_element_by_id('filter_submit')
         # 6 - количество товара, помещающегося на экране
        self.counter_PGDWN = 24 if self.count_pages > 1 and self.current_page != self.count_pages else int(
            self.amount_products_on_page % 144 / 6)
        while self.counter_PGDWN>0:
            self.driver.find_element_by_id('filter_submit').send_keys(Keys.PAGE_DOWN)
            self.counter_PGDWN -=1
            time.sleep(0.3)

    def get_product_links_on_page(self):
        products = self.driver.find_elements_by_class_name('products_card')
        for product in products:
            try:
                href = product.find_element_by_class_name('fancy_ajax').get_attribute('href')
                self.product_links.append(href)
            except NoElement:
                pass
        self.current_page +=1


    def get_all_product_links(self):
        while self.count_pages >0:
            self.show_all_page()
            self.get_product_links_on_page()
            self.next_page()
            self.count_pages -=1

    def next_page(self):
        try:
            self.driver.find_element_by_class_name('fa-arrow-right').click()
        except NoElement:
            pass

    def get_info(self):
        self.amount_products_on_page = int(
            self.driver.find_element_by_id('filter_submit').text.split(' ')[1])
        self.count_pages = self.amount_products_on_page // (144) + 1

if __name__ == '__main__':

    parser = Parser()
    parser.start()