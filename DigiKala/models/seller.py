from typing import Any
from .object_model import Object


class SellerRating(Object): 
    total_rate : int  
    total_count : int  
    commitment : int  
    no_return : float  
    on_time_shipping : int  

class SellerProperties(Object):
   is_trusted : bool  
   is_official : bool  
   is_roosta : bool  
   is_new : bool   

class Grade(Object):
    label : str  
    color : str  


class Seller(Object):
    id : int  
    title : str  
    code : str  
    url : str  
    rate : float
    rating : SellerRating
    properties : SellerProperties  
    stars : int  
    grade : Grade
    logo : Any 
    registration_date : str  
