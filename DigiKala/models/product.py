from .comment import FullComments , Comment
from .question import Question
from ._product import *
import DigiKala    

class Product(Object):
    id : int  
    title_fa : str  
    title_en : str  
    url : Url
    status : str  
    has_quick_view : bool  
    data_layer : DataLayer  
    product_type : str  
    digiplus : Digiplus  
    images : Images  
    rating : Rating  
    default_variant : Variant  
    properties : Properties
    category : Category
    brand : Brand
    review : Review
    variants : list[Variant]
    badges : list  
    colors : list[Color] 
    questions_count : int
    comments_count : int
    breadcrumb : list[Breadcrumb]
    specifications : list[Specification]
    expert_reviews : ExpertReviews
    meta : Meta
    last_comments : list[Comment]
    last_questions : list[Question]
    digify_touchpoint : str 
    st_cmp_tacker : ST_CmpTacker
    
    async def get_product(self) -> 'FullProduct':
        "دریافت اطلاعات کامل محصول | Get complete product information"
        return await self._client.get_product(self.id)
    
    async def get_comments(self) -> 'FullComments':
        "دریافت کامنت ها | Get comments "
        return await self._client.get_comments(self.id)
    
    async def add_cart(self) -> 'DigiKala.models.cart.FullCart':
        "اضافه کردن محصول پیش فرض به سبد خرید | Add default product to cart"
        return await self._client.add_cart(self.default_variant.id)
    

class FullProduct(Object):
    product : Product  
    data_layer : FullData  
    seo : Seo  
    intrack : Intrack  
    landing_touchpoint : list  
    dynamic_touch_points : list  
    flat_shipping_badge	: str  
    promotion_banner : Any
    bigdata_tracker_data : BigdataTrackerData  

