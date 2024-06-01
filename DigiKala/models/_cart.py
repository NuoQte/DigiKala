
from .object_model import Object
from .product import Product , Variant , Digiplus


class CartDigiClub(Object):
    points : int
 
class CashBack(Object):
    amount : int 
    digiplus_amount : int 
    return_days : int
 
class Insurance(Object):
    amount : int 
    discount : int

class Price(Object):
    price : int
    discount : int 
    is_incredible : bool
    is_promotion : bool
    is_lightening_deal : bool
    is_digiplus_promotion : bool 
    
class Properties(Object):
    is_drop_off_eligible : bool

class ShipmentMethod(Object):
    is_digikala : bool
    is_ship_by_seller : bool    

class PriceDecreased(Object):
    to : int
    from_price : int
    def __init__(self, data: dict, name: str, client) -> None:
        self.from_price : int = data['from']
        super().__init__(data, name, client)
        
class Warnings(Object):
    price_decreased : PriceDecreased

class CartItem(Object):
    id : int
    cart_id : int
    quantity : int 
    price : Price
    product : Product
    variant : Variant
    properties : Properties
    shipment_methods : ShipmentMethod
    is_switchable : bool
    gifts : list
    has_insurance : bool
    e_gift_card_properties : list
    warnings : list[Warnings]



# FullCart 


class ActionField(Object):
    step : int
    option : str

class CheckoutOption(Object):
    actionField : ActionField

class CheckoutProduct(Object):
    brand : str
    category : list[str]
    metric6 : int
    dimension2 : int
    dimension6 : int
    dimension7 : str
    dimension9 : float
    dimension11 : int
    dimension20 : str
    item_category2 : str
    item_category3 : str
    item_category4 : str
    item_category5 : str
    name : str
    id : int
    price : int
    quantity : int
    list : str
    metric8 : int
    dimension3 : str
    dimension10 : int
    dimension15 : int
    metric15 : int

class Checkout(Object):
    actionField : ActionField
    products : list[CheckoutProduct]
    
class Ecommerce(Object):
    checkout : Checkout
    checkout_option : CheckoutOption

class DataLayer(Object):
    event : str
    ecommerce : Ecommerce

class Recommendation(Object):
    title : str
    products : list[Product]

class PageInfo(Object):
    cart_id : int

class BigdataTrackerData(Object):
    page_name : str
    page_info : PageInfo

class Intrack(Object):
    eventName : str
    userId : int
