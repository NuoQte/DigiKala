from typing import Any
from .object_model import Object
from .cart import Cart


class DigiClub(Object):
    is_digiclub_activated : bool
    points : int
    reward_url_threshold : int
    claimable_points : int

class DigiPlus(Object):
    subscription_remaining_days : int
    is_activated : bool
    user_state : str
    is_general_location_jet_eligible : bool

class notification_(Object):
    count : int

class Notification(Object):
    notification: notification_


# FullUser


class DataLayerData(Object):
    is_logged_in : bool
    user_id : int
    is_club_user : bool
    club_points :int
    rfm_category : Any
    total_delivered_orders : int
    aov :int
    magnet_membership : bool
    plus_membership : bool 
    plus_membership_duration : int
    
class DataLayer(Object):
    event : str 
    data : DataLayerData

class SocialProfile(Object):
    is_activated : bool
