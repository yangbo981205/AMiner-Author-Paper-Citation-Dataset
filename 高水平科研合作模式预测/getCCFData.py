import requests
from lxml import etree


with open(r'CCFUrl.txt', 'r') as f_url:
    count = 78
    for l in f_url:
        line = 'http://dblp.uni-trier.de/db/journals/ijmms/'
        file_CCF_A = open("CCF_A/CCF-A" + str(count) + ".txt", "w", encoding="utf-8")
        line = line.strip('\n')
        for i in range(18, 1000):
            url = line + line.split('/')[len(line.split('/'))-2] + str(i+1) + '.html'
            # print(url)
            response = requests.get(url)
            selector = etree.HTML(response.content)
            # print(selector.xpath('//*[@id="headline"]/h1/text()'))
            if selector.xpath('//*[@id="headline"]/h1/text()')[0] == "Error 404: Not Found":
                count = count + 1
                file_CCF_A.close()
                break
            print('第{}个url的第{}个Volume'.format(count, i+1))
            for j in range(1000):
                if len(selector.xpath('//*[@id="main"]/ul[' + str(j+1) + ']//li//text()')) == 0:
                    break
                for k in range(1000):
                    result = selector.xpath('//*[@id="main"]/ul[' + str(j + 1) + ']/li[' + str(k+1) + ']//text()')
                    if len(result) == 0:
                        break
                    # print(result[len(result)-3])
                    file_CCF_A.write(result[len(result)-3] + '\n')
        break



