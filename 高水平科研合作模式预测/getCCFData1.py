import requests
from lxml import etree


with open(r'CCFUrl.txt', 'r') as f_url:
    for ll in f_url:
        li = 79
        line = 'http://dblp.uni-trier.de/db/conf/cscw'
        file_CCF_A = open("CCF_A/CCF-A" + str(li) + ".txt", "w", encoding="utf-8")
        line = line.strip('\n')
        for i in range(1000):
            url = line + 'index.html'
            # print(url)
            response = requests.get(url)
            selector = etree.HTML(response.content)
            # print(selector.xpath('//*[@id="headline"]/h1/text()'))
            # if selector.xpath('//*[@id="headline"]/h1/text()')[0] == "Error 404: Not Found":
            #     file_CCF_A.close()
            #     break
            # print('第{}个url的第{}个'.format(li, i+1))
            for j in range(1000):
                if len(selector.xpath('//*[@id="main"]/ul[' + str(j+1) + ']//li//text()')) == 0:
                    break
                for k in range(1000):
                    result = selector.xpath('//*[@id="main"]/ul[' + str(j + 1) + ']/li[' + str(k+1) + ']//text()')
                    if len(result) == 0:
                        break
                    ind = 0
                    max_long = 0
                    for item in result:
                        if len(item) > max_long:
                            max_long = len(item)
                            ind = result.index(item)
                    print(result[ind])

                    file_CCF_A.write(result[ind] + '\n')
            break
        break


