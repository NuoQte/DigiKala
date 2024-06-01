# DigiKala

[تغییر زبان به فارسی](https://github.com/NuoQTe/DigiKala/blob/main/README_FA.md)

## Create session and work with Digikala API

**Installation:**

   Install the DgiKala library from PyPI or GitHub.
   
   ```bash
   pip install DigiKala
   ```
   
   or
   
   ```bash
   git clone https://github.com/NuoQTe/DigiKala.git
   ```


**Crate session**
   ```python
   import asyncio
   from DigiKala import Client

   async def main()
       app = Client("NuoQTe")
       await app.login()
       await app.close()        
    
   asyncio.run(main())
   ```
    
or

   ```python
   import asyncio
   from DigiKala import Client

   async def main()
       async with Client('NuoQTe',do_login=True) as app:
          pass    

   asyncio.run(main())
   ```

**Examples**:
   ```python
   import asyncio
   from DigiKala import Client , SearchFilter


   async def main():
    
      async with Client('NuoQTe',do_login=True) as app:
            
       # Search in DigiKala
         result = await app.search(SearchFilter(
               query="Laptop",
               classification="notebook-netbook-ultrabook",
               has_selling_stock=True,
               price_range=(50000000 , 80000000),
               sort_code=4
            ))

         product = await result.products[3].get_product()
         product = product.product
         print(product.variants)
         
         # add product in my cart
         await product.add_cart()

   asyncio.run(main())    
   ```

## Capabilities

    - login phone number or email with sent code or password
    - logout
    - crate session file
    - search with all filters
    - search wuth product ID
    - get product comments 
    - get account information
    - get cart information
    - add product to cart
    - remove product from the cart


  
## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/NuoQTe/DigiKala/blob/main/LICENSE) file for details.

<a href="https://pypi.org/project/DigiKala/"><img src="https://img.shields.io/badge/DigiKala-1.0-F5F5F5?style=flat-square&labelColor=DC143C"></a> 

## Developer
- **Telegram**: [t.me/NuoQTe](https://t.me/NuoQTe)

---