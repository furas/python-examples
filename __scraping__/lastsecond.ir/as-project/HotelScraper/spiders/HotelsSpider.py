import scrapy

class For_Spider(scrapy.Spider):

    name = "for"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 

        #print('spider args:', args)
        #print('spider kwargs:', kwargs)

        # get value from variable `dc` or set default value `hello`
        self.table = kwargs.get('dc', 'hello')
    
