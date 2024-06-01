from .object_model import Object

class Question(Object):
    id : int 
    status : str 
    text : str 
    answer_count : int 
    sender : str 
    created_at : str