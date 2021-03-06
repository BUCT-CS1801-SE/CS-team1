# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置

# 故宫博物院

class Musume1Spider(scrapy.Spider):
    name = 'museum1'
    allowed_domains = ['dpm.org.cn']
    start_urls = ['https://www.dpm.org.cn/Home.html']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=1
        item["museumName"]='故宫博物院'
        item["Location"]='北京市东城区景山前街4号'
        item["Link"]='https://www.dpm.org.cn/Home.html'
        data = response.xpath("//div[@class='list']/*/div[@class='li']/p/text()").extract()
        time = response.xpath("//div[@class='list']/*/div[@class='li']/h1/text()").extract()
        newdata=response.xpath("//div[@class='list']/*/div[@class='li last']/p/text()").extract_first()
        newtime=response.xpath("//div[@class='list']/*/div[@class='li last']/h1/text()").extract_first()
        # print(data)
        # print(time)
        opentime = data[0]+time[0]+"   "+data[1]+time[1]+"   "+data[3]+time[2]+"   "+newdata+newtime
        item["opentime"]=opentime
        #item["opentime"]=response.xpath("//div[@class='list']/ul/li[@class='transition translateX-100']/p/text()").extract()
        item["telephone"]='gugong@dpm.org.cn'
        item["introduction"]=response.xpath("//meta[@name='description']/@content").extract()
        yield item 


# //*[@id="container"]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/h1
# //*[@id="container"]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[2]/h1