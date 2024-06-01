

class SearchFilter:
    params = {}
    url = 'search/'
    def __init__(self,
                query:str = None,
                classification : str = None,
                sort_code:int = None,
                page:int = 1,
                brands:list[int] =None,
                has_jet_delivery:bool = None,
                has_ship_by_seller:bool = None,
                has_selling_stock:bool = None,
                has_ready_to_shipment:bool = None,
                seller_types:list[str] = None,
                price_range: tuple[int,int]= None
                ) -> None:
        """
        Create a filter to search for content

        Args:
            query (`str`, optional): Text search
            classification (`str`, optional): Classification
            sort_code (`int`): Order by (The most relevant=22, most visited=4, the newest=1, Bestselling=7, cheapest=20, the most expensive=21, Fastest shipping=25, Buyers' suggestion=27, selected=29)
            page (`int`, optional): The desired page. (Defaults to 1).
            brands (`list`[`int`], optional): A list of brands
            has_jet_delivery (`bool`, optional): Shipping tomorrow
            has_ship_by_seller (`bool`, optional): Sent by seller
            has_selling_stock (`bool`, optional): Only available items
            has_ready_to_shipment (`bool`, optional): Only items available in Digikala warehouse
            seller_types (`str`, optional): A list of types of sellers. (official,trusted,digikala,roosta)
            price_range (`tuple`[`int`,`int`], optional): Price range(in Toman) --> (min , max)

        
        """
        
            
        if brands :
            for i in range(len(brands)) : self.params[f'brands[{i}]'] = brands[i] 

        if seller_types:     
            for i in range(len(seller_types)) :self.params[f'seller_types[{i}]'] = seller_types[i] 
   
        if classification : self.url + classification + "/"
        if query : self.params["q"] = query                 
        if has_jet_delivery : self.params["has_jet_delivery"] = 1
        if has_ship_by_seller : self.params["has_ship_by_seller"] = 1
        if has_selling_stock : self.params["has_selling_stock"] = 1
        if has_ready_to_shipment : self.params["has_ready_to_shipment"] = 1
        if price_range : self.params['price[min]'],self.params['price[max]'] = price_range[0],price_range[1]
        if sort_code : self.params["sort"] = sort_code 
        self.params['page'] = page

