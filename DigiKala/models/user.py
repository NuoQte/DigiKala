from .object_model import Object
from ._user import *

class User(Object):
    id : int
    first_name : str
    last_name : str 
    phone : str
    city_id : int
    mobile : str
    email : str
    avatar_url : str
    is_legal : bool
    is_foreigner : bool
    has_password : bool
    personal_economic_number : int 
    verification_status : str
    national_identity_number : int
    gender : str
    birthday_iso : str
    city_name : str
    state_name : str
    phone_hash : str
       

class FullUser(Object):
    is_logged_in : bool
    digiclub : DigiClub
    digiplus : DigiPlus
    notification : Notification
    user : User
    default_address : list
    data_layer : DataLayer
    show_intrack_web_push : bool
    modules : list[str]
    date_time : str
    social_profile : SocialProfile
    cart : Cart
    
    
    
    