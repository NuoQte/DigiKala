from typing import Any
from json import dumps
# from DigiKala import Client
import DigiKala

class Object:
    def __init__(self,data:dict,name:str,client:'DigiKala.Client') -> None:
        self._data = data
        self.__class__.__name__ = name
        self._client = client        
        self._dict_types = {
            'dict' : self._return_object,
            'str'  : self._return_str,
            'list' : self._return_list
        }

    
    
    def _return_object(self,value,name)-> "Object" :
        return Object(value,name,self._client)
    
    def _return_list(self,value,name)->list["Object" or "Any"]:
        return [Object(i,name,self._client) if isinstance(i,dict) else i for i in value]
    
    def _return_str(self,value,_)->str|list[str]:
        return [str(i) for i in value.strip('[]').split(',')] if value[0] == '[' else value 
    
    
    def __getattr__(self, key: str) -> Any:
        try:
    
            value = self._data[key]
            _type = value.__class__.__name__
            
            try:
                return self._dict_types[_type](value,key)
            except:
                return value
                
        except :
            return None
    
    
    @staticmethod
    def default(obj: "Object"):
        if isinstance(obj, bytes):
            return obj.decode()


        return {
            "->": obj.__class__.__name__,
            **{
                attr: obj._data[attr] for attr in  obj._data if obj._data[attr] is not None
            }
        }


    def __str__(self) -> str:
        return dumps(self, indent=4, default=Object.default, ensure_ascii=False)

    def __repr__(self) -> str:
        return dumps(self, indent=4, default=Object.default, ensure_ascii=False)
        