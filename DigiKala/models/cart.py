from .object_model import Object    
from ._cart import *

class Cart(Object):
    id : int
    items_count : int
    payable_price : int
    digiclub : CartDigiClub
    voucher_code : int
    cash_back : CashBack
    temporary_plus_subscription : list
    bnpl_active : bool
    rrp_price : int
    shipping_cost : int
    voucher_discount : int
    shipping_cost_discount : int
    items_discount : int
    total_discount : int
    insurance : Insurance
    plus : list
    cart_items : list[CartItem]



class FullCart(Object):
    cart_items : list[CartItem] 
    cart : Cart
    digiplus : Digiplus
    data_layer : list[DataLayer]
    recommendation : Recommendation
    new_recommendation : Recommendation
    bigdata_tracker_data : BigdataTrackerData
    intrack : Intrack

