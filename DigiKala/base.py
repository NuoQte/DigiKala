from .models.search_result import SearchResult
from .models.product import FullProduct
from .models.user import FullUser
from .models.cart import FullCart
from .models.comment import FullComments
from .search_filter import SearchFilter
from .import errors

import aiohttp , asyncio
import os , pickle 


class Client:
    _API_V1 = "https://api.digikala.com/v1/"
    _API_V2 = "https://api.digikala.com/v2/"
    
    def __init__(self,
                 name:str,
                 phone_number:str=None,
                 email:str = None,
                 password:str=None,
                 do_login:bool = None,
                 in_memory:bool=None,
                 workdir:str=None
                 
                 ) -> None:
        
        if phone_number:
            phone_number = phone_number.replace('+98','0')
        
        self.name = name
        self.session_path = workdir + name +'.digikala' if workdir else name +'.digikala'
        self.phone_number = phone_number
        self.email = email
        self.password = password
        self.do_login  = do_login
        self.in_memory = in_memory
        self._session = aiohttp.ClientSession()
        self._is_login = None
        
        self.cart_id : int = None
        
        
    async def logout(self)->bool:
        """
        Sign out of the user account

        Raises:
            errors.SessionExpired: if the session has already expired

        Returns:
            True: if done successfully
        """
        res = await self._session.post(self._API_V1+'user/logout/',json={})    
        if res.json()['status'] == 200: return True     
        raise errors.SessionExpired()


    async def login(self):
        """
        Start logging into the user account in the terminal
        """
        if self._is_login:
            print('Client is already running!')            
        
        else:
            
            if os.path.exists(self.session_path):
                await self.load_session()
                return
            
        
            while not self.phone_number and not self.email:
                username = input('Please enter your phone number or email to log in: ')
                username = username.replace('+98','0')
                
                if not username.strip(" "):
                    continue
                
                if username.isnumeric():
                    self.phone_number = username
                    break
                
                if username.find('@'):
                    self.email = username
                    break
                
                print('The wrong phone number or email was entered!!')
            
            
            if not await self.send_code():
                raise errors.UsernameInvalid()
            
            while True:
                
                if self.password:
                    try:
                        await self.signin_with_password()
                    except errors.SessionWrongPassword as e:
                        self.password = None
                        print(e)
                        continue
                    
                else:    
                    code = input('Please enter the code sent to your phone number or email(enter (r) to resubmit the code!): ')
                    if code == 'r':
                        if not await self.resend_code(): 
                            print('The code could not be sent, please try again in at least one minute!')
                        continue
                    
                    try:
                        await self.sign_in(code)
                            
                    except errors.SessionWrongCode:
                        print('The entered code is wrong!')
                        
                print('Login is done.')
                break

            
    async def resend_code(self)->bool:
        """
        Get the login code again.
        
        Returns:
            True: if done successfully
        
        """
        res = await self._session.post(self._API_V1+'user/authenticate/',json={"backUrl":"/","username":self.phone_number or self.email,"otp_call":False,"force_send_otp":True})
        res = await res.json()
        return True if res['status'] == 200 else False


    async def signin_with_password(self) -> FullUser:
        """
        Go to user account with password

        Raises:
            errors.SessionExpired: if sign in the account is not logged in correctly or the session is blocked
            errors.SessionWrongPassword: if the entered password is wrong

        Returns:
            models.user.FullUser
        """
        res = await self._session.post(self._API_V1+'user/login/password/',json={"backUrl":"/profile/personal-info/","type":"password","username":self.phone_number or self.email,"password":self.password})
        res = await res.json()
        if res['status'] == 200 :
            me = await self.me()
            
            if me and me.is_logged_in:
                await self.save_session()
                self.cart_id = me.cart.id
                return me
            
            raise errors.SessionExpired()
        
        raise errors.SessionWrongPassword()


    async def check_signin(self)-> bool:
        """
        Check if you are logged in or not!

        Returns:
            True: If you are logged in
        """
        me = await self.me()
        return me.is_logged_in
    
    
    async def send_code(self) -> bool:
        """
        Send code to phone number or email

        Returns:
            True: if the code is sent
        """
        res = await self._session.post(self._API_V1+'user/authenticate/',json={"backUrl":"/","username":self.phone_number or self.email,"otp_call":False})
        res = await res.json()
        return True if res['status'] == 200 else False


    async def sign_in(self,code:str) -> FullUser:
        """
        Login to the user account with the SMS code sent to the mobile number or email

        Args:
            code (`str`): Code sent to phone number or email

        Returns:
            models.user.FullUser
        
        Raises:
            errors.SessionExpired: if sign in the account is not logged in correctly or the session is blocked
            errors.SessionWrongCode: if the entered code is wrong
        
        """
        res = await self._session.post(self._API_V1+'user/login/otp/',json={"backUrl":"/","type":"otp","username":self.phone_number or self.email,"code":code})
        res = await res.json()
        if res['status'] == 200 :
            me = await self.me()
            
            if me and me.is_logged_in:
                await self.save_session()
                self.cart_id = me.cart.id
                return me
            
            raise errors.SessionExpired()
        
        raise errors.SessionWrongCode()
        

    async def save_session(self):
        """
        Create a session file
        """
        if not self.in_memory:
            with open(self.session_path,'wb') as session_file:
                session_data = {'cookies': self._session.cookie_jar._cookies,'phone_number':self.phone_number}
                pickle.dump(session_data,session_file)

    async def load_session(self):
        """
        Load a session file

        Raises:
            errors.SessionInvalid: if the session file is invalid
            errors.SessionExpired: if the session is expired
        """
        try:
            with open(self.session_path,'rb') as session_file:
                session_data = pickle.load(session_file)
            
            self._session.cookie_jar._cookies = session_data['cookies']
            self.phone_number = session_data['phone_number']
        except:
            raise errors.SessionInvalid()
        
        me = await self.me()
        if not me.is_logged_in:
            raise errors.SessionExpired()
        
        self.cart_id = me.cart.id
        

    async def me(self) -> FullUser:
        """
        Get your information

        Returns:
            models.user.FullUser
        """
        res = await self._session.get(self._API_V1+'user/init/?backUrl=%2F')
        res = await res.json()
        return FullUser(res['data'],'fulluser',self) if res['status'] == 200 else None

        
    
    async def search(self,filter:SearchFilter) -> SearchResult:
        """
        Start your search to find products

        Args:
            filter: filter type for product search 

        Returns:
            models.search_result.SearchResult
        """
        
        
        res = await self._session.get(self._API_V1+filter.url,params=filter.params)
        res = await res.json()
        return SearchResult(res['data'],self,filter) if res['status'] == 200 else None
    
    
    async def get_product(self,product_id:int) -> FullProduct:
        """
        Search for a product using its ID

        Args:
            product_id (`int`): The unique ID of the product

        Returns:
            models.product.FullProduct
        """
        res = await self._session.get(self._API_V2+f'product/{product_id}/')
        res = await res.json()
        return FullProduct(res['data'],'fullproduct',self) if res['status'] == 200 else None
    
    async def add_cart(self,variant_id:int) -> FullCart:
        """
        Add an item to the cart
        
        Args:
            variant_id (`int`): The unique identifier of the product (note: this identifier is different from the product_id)

        Returns:
            models.cart.FullCart
        """
        data = {"variant_ids":[variant_id],"pass":True}
        res = await self._session.post(self._API_V1+'cart/add/',json=data)
        res = await res.json()
        return FullCart(res['data'],'fullcart',self) if res['status'] == 200 else None
        
    async def get_cart(self) -> FullCart:
        """
        Get shopping cart information
        
        Returns:
            models.cart.FullCart
        """
        res = await self._session.get(self._API_V1+'cart/')
        res = await res.json()
        return FullCart(res['data'],'fullcart',self) if res['status'] == 200 else None
        
    
    async def remove_item_cart(self,cart_item_id:int) -> FullCart:
        """
        Remove an item from the shopping cart

        Args:
            cart_item_id (`int`): ID of the item in the shopping cart

        Returns:
            models.cart.FullCart
        """
        data = {"web_page":"cart","cart_id":self.cart_id,"cart_item_ids":[cart_item_id]}
        res = await self._session.post(self._API_V1+"cart/remove/",json=data)
        res = await res.json()
        return FullCart(res['data'],'fullcart',self) if res['status'] == 200 else None

    
    async def get_comments(self,product_id:int,page:int=1) -> FullComments:
        """
        Get comments on a product
        
        Args:
            product_id (`int`): ID of the desired item 
            page (`int`, optional): The desired page of product comments. (Defaults to 1).

        Returns:
            models.comment.FullComments
        """
        
        res = await self._session.get(self._API_V1+f"rate-review/products/{product_id}/?page={page}")
        res = await res.json()
        return FullComments(res['data'],'fullcomments',self) if res['status'] == 200 else None
    
    
    # ::::::::::::::::::::
    async def __aenter__(self):
        if self.do_login:
            await self.login()
        return self

    async def __aexit__(self, *args, **kwargs):
        await self._session.close()

    async def close(self):
        """stop client"""
        await self.__aexit__()
