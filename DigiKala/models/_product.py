from typing import Any 
from .object_model import Object
from .color import Color
from .seller import Seller


class DataLayer(Object) :
    brand : str  
    category : list[str]  
    metric6 : int  
    dimension2 : int  
    dimension6 : int|float  
    dimension7 : str  
    dimension9 : int  
    dimension11 : int|float  
    dimension20 : str  
    item_category2 : str  
    item_category3 : str  
    item_category4 : str  
    item_category5 : str  

class Digiplus(Object):
    services : list[str]  
    is_jet_eligible : bool  
    cash_back : int|float  
    is_general_location_jet_eligible : bool  
    fast_shipping_text : str  

class ImagesMain(Object):
    storage_ids : list  
    url : list[str]  
    thumbnail_url : Any
    temporary_id : Any
    webp_url :list[str]  
  
class Images(Object): 
    main : ImagesMain  

class Rating(Object): 
    rate : float|int  
    count : int  

class StatisticsRating(Object) :
    rate_count : int  
    rate : float  

class Statistics(Object):
    totally_satisfied : StatisticsRating  
    satisfied : StatisticsRating  
    neutral : StatisticsRating  
    dissatisfied : StatisticsRating  
    totally_dissatisfied : StatisticsRating  
    total_count : int
    total_rate : float

class VariantProperties(Object):
    is_fast_shipping : bool  
    is_ship_by_seller : bool  
    is_multi_warehouse : bool  
    has_similar_variants : bool  
    is_rural : bool  
    in_digikala_warehouse : bool  
   
class Warranty(Object):
    id : int  
    title_fa : str  
    title_en : str  
   
   
class Digiclub(Object): 
    point : int  

class Badge(Object):
    title : str  
    color : str  
    icon : Any

class Price(Object):
    selling_price : int  
    rrp_price : int  
    order_limit : int  
    is_incredible : bool  
    is_promotion : bool  
    is_locked_for_digiplus : bool  
    bnpl_active : bool  
    marketable_stock : int  
    discount_percent : int  
    badge : Badge  
    is_digiplus_promotion : bool  
    is_digiplus_early_access : bool  
    is_application_incredible : bool  
    is_lightening_deal : bool  
    is_plus_early_access : bool  

class Provider(Object):
    title : str  
    description : str  
    has_lead_time : bool  
    type : str  

class ShipmentMethods(Object):
    description : str  
    has_lead_time : bool  
    providers : list[Provider] 

class Payload(Object): 
    text : str  
    text_color : str  
    icon : Any

class VariantBadge(Object):
    id : int  
    type : str  
    slot : str  
    priority : int   
    payload : Payload  

class Size(Object):
    id : int  
    title : str  


class Variant(Object): 
    id :int   
    lead_time : int|float  
    rank : float  
    rate : int  
    statistics : Statistics  
    status : str  
    properties : VariantProperties    
    digiplus : Digiplus   
    warranty : Warranty  
    color : Color  
    seller : Seller  
    digiclub : Digiclub  
    buy_box_lead_time : int|float  
    price : Price  
    shipment_methods : ShipmentMethods  
    has_importer_price : bool  
    manufacture_price_not_exist : bool  
    has_best_price_in_last_month : bool  
    buy_box_notices : list  
    variant_badges : list[VariantBadge]  
    size : Size  
    
class Properties(Object):
    is_fast_shipping : bool  
    is_ship_by_seller : bool  
    free_shipping_badge : bool  
    is_multi_warehouse : bool  
    is_fake : bool  
    has_gift : bool  
    min_price_in_last_month : int  
    is_non_inventory : bool  
    is_ad : bool  
    ad : list  
    is_jet_eligible : bool  
    is_medical_supplement : bool  

class Category(Object):
    id : int
    title_fa : str
    title_en : str
    code : str
    return_reason_alert : str

class Url(Object):
    uri : str


class Logo(Object):
    url : list[str]

class Brand(Object):
    id : int
    code : str
    title_fa : str
    title_en : str
    url : Url
    visibility : bool
    logo : Logo
    is_premium : bool
    is_miscellaneous : bool
    is_name_similar : bool

class Reviewattribute(Object):
    title : str
    values : list[str]

class Review(Object):
    description : str
    attributes : list[Reviewattribute]

class Breadcrumb(Object):
    title : str
    url : Url

class Specification(Object):
    title : str
    attributes : list[Reviewattribute]

class Section(Object):
    template : str
    image : str

class ReviewSection(Object):
    title : str
    sections : list[Section]

class ExpertReviews(Object):
    description : str
    short_review : str
    review_sections : list[ReviewSection]
    technical_properties : list

class BrandCategoryUrl(Object):
    uri : str

class Meta(Object):
    brand_category_url : BrandCategoryUrl

class ST_CmpTacker(Object):
    neo : str 
    cx : str 
    dx : str     
    data_fx : str 
    zero : str
    
    def __init__(self, data: dict, name: str, client) -> None:
        try:self.data_fx = self._data.get('data-fx',None)
        except:pass
        super().__init__(data, name, client)





# FullProduct :::::::::::::::::::::::::: 



class ProductDataLayer(Object) :
    brand : str  
    category : list[str]  
    metric6 : int  
    dimension2 : int  
    dimension6 : int|float  
    dimension7 : str  
    dimension9 : int  
    dimension11 : int|float  
    dimension20 : str  
    item_category2 : str  
    item_category3 : str  
    item_category4 : str  
    item_category5 : str  
    name : str  
    id : int  
    price : int   
    metric8 : int  
    dimension3 : str  
    dimension10	: int  
    dimension15	: int  
    metric15	: int  
    metric11	: int  
    metric12	: int  

class ActionField(Object) :
    list : str  

class Detail(Object):
    actionField : ActionField   	
    products : list[ProductDataLayer]  

class ECommerce(Object):
    detail : Detail  	
    

class FullData(Object):
    event : str  
    ecommerce : ECommerce  

class TwitterCard(Object):	
    title : str  
    image : str  
    price : int  
    description : str  

class OpenGraph(Object):	
    title : str  
    url : str  
    image : str  
    availability : str  
    type : str  
    site : str  
    price : int  
    description : Any

class Header(Object):
    title : str  
    description : str  
    canonical_url : str  

class MarkupSchemaBrand(Object):
    name : str  
    url	: str  
    
class Offers(Object):	
    priceCurrency : str  
    price : int  
    itemCondition : str  
    availability : str  
    
class ReviewRating(Object):	
        bestRating : int  
        ratingValue	: int     

class Author(Object):	
    name : str  

class Review(Object):	
    reviewRating : ReviewRating  	
    author : Author  	
    datePublished : str  
    reviewBody : str  
    name : str  


class MarkupSchema(Object):	
    name : str   
    alternateName : str  
    images : list[str]  
    description : str  
    mpn : int  
    sku : int  
    category : str  
    brand : MarkupSchemaBrand  
    aggregateRating	: Any 
    offers : Offers  
    review : Review  

class ItemListElement(Object):
    position : int  
    name : str  
    item : str  
    
class ItemListElementMarkupSchema(Object):
    itemListElement : list[ItemListElement]  
    
class Seo(Object):
    title : str  
    description	: str  
    twitter_card : TwitterCard  
    open_graph : OpenGraph  
    header : Header  
    markup_schema : list[MarkupSchema|list[ItemListElementMarkupSchema]]  


class EventData(Object):	
    currency : str  
    deviceType : str  
    name : str  
    productId : int  
    productImageUrl	: list[str]  
    quantity : int  
    leafCategory : str  
    unitPrice : int  
    url	: str  
    supplyCategory : str  
    categoryLevel1 : str  
    categoryLevel2 : str  
    categoryLevel3 : str  
    categoryLevel4 : str  
    categoryLevel5 : str  


class Intrack(Object):	
    eventName : str  
    eventData : EventData  	
    userId : Any

class PageInfo(Object):	
    product_id : int  
    
class BigdataTrackerData(Object):	
    page_name : str  
    page_info : PageInfo  

