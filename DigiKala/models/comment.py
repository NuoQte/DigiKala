from .object_model import Object
from ._comment import *


class Comment(Object):
    order_item_id : int
    product_id : int
    rate : int
    review_user_type : str
    status : str
    purchased_item : PurchasedItem
    id : int
    body : str
    created_at : str 
    rate : int
    reactions : CommandReaction
    recommendation_status : str 
    is_buyer : bool 
    user_name : str 
    is_anonymous : bool 
    relative_date : str
    files : list[Files]


class IntentData(Object):
    title : str
    number_of_comments : int
    tag_data : Tag
    tag_percentage : Tag
    productId : int
    intentId : int
    
    
class FullComments(Object):
    comments : list[Comment]
    intent_data : list[IntentData]
    media_comments : list[Comment]
    sort : Sort
    sort_options : list[SortOptions]
    pager : Pager
    
    async def get_next_page(self):
        "دریافت کامنت های صفحه بعدی | Getting next comments"
        await self._client.get_comments(self.intent_data[0].productId,self.pager.current_page+1)
    