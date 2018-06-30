import os
path = 'D:\python\e-dostavka.by\\'
list_urls = []
with open(path+'products.txt', 'r') as f:
    for line in f:
        list_urls.append(line)
    total_set = set(list_urls)
    print('В файле {} удалено {} дубликатов'.format('products.txt', (len(list_urls)-len(total_set))))
    with open(path+'products.txt'+'new_', 'w') as newfile:
        for url in total_set:
            newfile.write(url)