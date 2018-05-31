# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonItemExporter

class SteamshanPipeline(object):
    def open_spider(self,spider):
        self.file=open('G:\\shan\\shansteam.json','wb')
        self.exporter = JsonItemExporter(self.file,encoding='utf-8',ensure_ascii=False)
        # self.file=open('G:\\shan\\shansteam.csv','wb')
        # self.exporter=CsvItemExporter(self.file,fields_to_export=['title','cost','price','urld'])
        self.exporter.start_exporting()

    def process_item(self,item,spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self,spider):
        self.exporter.finish_exporting()
        self.file.close()



    # def __init__(self):
    #     store_file=os.path.dirname('G:\\shan\\shansteam.csv')
    #     self.file=open(store_file,'wb')
    #     self.writer=csv.writer(self.file)
    # self.wb=Workbook()
    # self.ws=self.wb.active
    # self.ws.append(['name','cost','price','address'])
    # def process_item(self, item, spider):
    #     f=file('G:\\shan\\shansteam.csv','a+')
    #     writer=csv.writer(f)
    #     writer.writerow(item['title'],item['cost'],item['price'],item['urld'])
        # line=[item['title'],item['cost'],item['price'],item['urld']]
        # self.ws.append(line)
        # self.save('G:\\shan\\shansteam.xlsx')
        # return item
        # line=[item['title'],item['cost'],item['price'],item['urld']]
        # tpl = "%s\n%s\n%s\n%s\n" %(item['title'],item['cost'],item['price'],item['urld'])
        # print(tpl)
        # f = open('news.json', 'a')
        # f.write(tpl)
        # f.close()
    # def close_spider(self,spider):
    #     self.file.close()

