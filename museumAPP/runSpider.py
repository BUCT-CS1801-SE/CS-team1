import sys
import os
import time


if __name__ == '__main__':
    path = "C:\\Users\\彤彤\Desktop\\文件\\museum\\webDataCollectionSystem\\MUSEUMS\\spiders"
    spiderLists = os.listdir(path)
    museum = []
    collect = []
    exhibition = []
    for spider in spiderLists:
        if spider == '__pycache__' or spider == '__init__.py':
            continue
        if spider[0] == 'm':
            museum.append(spider[0:-3])
        elif spider[0] == 'c':
            collect.append(spider[0:-3])
        else:
            exhibition.append(spider[0:-3])
    be = "scrapy crawl "
    # for i in museum:
    #     command = be + i
    #     ok = os.system(command)
    #     if ok != 0:
    #         print("error! -> " + command)
    #     else:
    #         print("yes! -> " + i)
    # for i in collect:
    #     command = be + i
    #     ok = os.system(command)
    #     if ok != 0:
    #         print("error! -> " + command)
    #         exit(0)
    #     else:
    #         print("yes! -> " + i)
    for i in exhibition:
        command = be + i
        ok = os.system(command)
        if ok != 0:
            print("error! -> " + command)
            exit(0)
        else:
            print("yes! -> " + i)
    
