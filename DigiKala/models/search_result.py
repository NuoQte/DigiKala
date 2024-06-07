from .product import Product
import DigiKala

class SearchResult:
    def __init__(self,data:dict,client:DigiKala.Client,filter:DigiKala.SearchFilter) -> None :
        self.products : list[Product] =  [Product(i,'product',client) for i in data['products']]
        self.total_items : int = data['pager']['total_items']
        self.total_pages : int = data['pager']['total_pages']
        self.current_page : int = data['pager']['current_page']
        self.query : str = filter.params['q']
        self._filter = filter
        self._client = client

    async def next_page(self):
        """برای دریافت صفحه بعدی این جستجو از این متود استفاده کنید | Use this method to get the next page of this search"""
        _filter = self._filter
        _filter.params['page'] += 1
        return await self._client.search(_filter)
        
    
    async def get_page(self,page:int|str):
        """برای دریافت یک صفحه خاص در این جستجو از این متود استفاده کنید و شماره صفحه را به عنوان ورودی ارسال کنید | To get a specific page in this search, use this method and pass the page number as input"""
        
        _filter = self._filter
        _filter.params['page'] = page
        return await self._client.search(_filter)


    def __str__(self) -> str:
        return f"""
query : {self.query}
current_page : {self.current_page}
total_pages : {self.total_pages}
total_items : {self.total_items}
products : {self.products}
"""
