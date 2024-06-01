from .object_model import Object
from .color import Color
from .seller import Seller

class CommandReaction(Object):
    likes : int 
    dislikes : int 

class PurchasedItem(Object):
    seller : Seller
    color : Color

class Tag(Object):
    positive : int 
    negative : int
    neutral : int

class Files(Object):
    storage_ids : list[str]
    url : list[str]
    thumbnail_url : list[str]
    
class Sort(Object):
    default : str

class SortOptions(Object):
    id : str
    title : str
    
class Pager(Object):
    current_page : int
    total_pages : int
    total_items : int

