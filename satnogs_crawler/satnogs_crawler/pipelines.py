import scrapy
from scrapy.pipelines.images import FilesPipeline

class SatnogsCrawlerPipeline(FilesPipeline):

    def get_media_requests(self, item, info):
        file_urls = item['file_urls']
        for url in file_urls:
            meta = {'filename': url.split('/')[-1]}
            yield scrapy.Request(url=url, meta=meta)


    def file_path(self, request, response=None, info=None):
        filename = request.meta.get('filename','')
        if (filename.split('_')[0] == 'waterfall'):
            return '/waterfall/' + request.meta.get('filename','')
        else:
            return '/audio/' + request.meta.get('filename','')