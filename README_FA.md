<<<<<<< HEAD
# DigiKala

[Change the language to English](https://github.com/NuoQTe/DigiKala/blob/main/README.md)

## ایجاد حساب کاربری و کار با API سایت دیجیکالا

**روش های نصب کردن پکیج:**

   نصب از طریق Pypi:
   
   ```bash
   pip install DigiKala
   ```

 یا نصب از طریق گیتهاب:

   ```bash
   git clone https://github.com/NuoQTe/DigiKala.git
   ```


**ایجاد جلسه**
   ```python
   import asyncio
   from DigiKala import Client

   async def main()
       app = Client("NuoQTe")
       await app.login()
       await app.close()        
    
   asyncio.run(main())
   ```
    
    یا

   ```python
   import asyncio
   from DigiKala import Client

   async def main()
       async with Client('NuoQTe',do_login=True) as app:
          pass    

   asyncio.run(main())
   ```

**مثال ها**:
   ```python
   import asyncio
   from DigiKala import Client , SearchFilter


   async def main():
    
      async with Client('NuoQTe',do_login=True) as app:
            
       # جستجوی کالا در دیجیکالا
         result = await app.search(SearchFilter(
               query="Laptop",
               classification="notebook-netbook-ultrabook",
               has_selling_stock=True,
               price_range=(50000000 , 80000000),
               sort_code=4
            ))

         product = await result.products[3].get_product()
         product = product.product
         print(product)
         
         # اضافه کردن کالا به سبد خرید
         await product.add_cart()

   asyncio.run(main())    
   ```

## قابلیت ها :

    - وارد شدن به حساب کاربری با شماره تلفن یا ایمیل با کد ارسال شده یا پسورد
    - خروج از حساب کاربری
    - ساخت فایل سشن برای استفاده مجدد
    - جستجو در دیجی کالا با تمام فیلتر ها
    - جستجوی محصولات با آیدی محصر به فرد آنها
    - دریافت کامنت ها
    - دریافت اطلاعات حساب کاربری
    - دریافت اطلاعات سبد خرید
    - اضافه کردن محصولات به سبد خرید
    - حرف محصولات به سبد خرید


  
## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/NuoQTe/DigiKala/blob/main/LICENSE) file for details.

<a href="https://pypi.org/project/DigiKala/"><img src="https://img.shields.io/badge/DigiKala-1.0-F5F5F5?style=flat-square&labelColor=DC143C"></a> 

## Developer
- **Telegram**: [t.me/NuoQTe](https://t.me/NuoQTe)

=======
# DigiKala

[Change the language to English](https://github.com/NuoQTe/DigiKala/blob/main/README.md)

## ایجاد حساب کاربری و کار با API سایت دیجیکالا

**روش های نصب کردن پکیج:**

   Install the DgiKala library from PyPI or GitHub.
   
   ```bash
   pip install DigiKala
   ```

 یا  

   ```bash
   git clone https://github.com/NuoQTe/DigiKala.git
   ```


**ایجاد جلسه**
   ```python
   import asyncio
   from DigiKala import Client

   async def main()
       app = Client("NuoQTe")
       await app.login()
       await app.close()        
    
   asyncio.run(main())
   ```
    
    یا

   ```python
   import asyncio
   from DigiKala import Client

   async def main()
       async with Client('NuoQTe',do_login=True) as app:
          pass    

   asyncio.run(main())
   ```

**مثال ها**:
   ```python
   import asyncio
   from DigiKala import Client , SearchFilter


   async def main():
    
      async with Client('NuoQTe',do_login=True) as app:
            
       # جستجوی کالا در دیجیکالا
         result = await app.search(SearchFilter(
               query="Laptop",
               classification="notebook-netbook-ultrabook",
               has_selling_stock=True,
               price_range=(50000000 , 80000000),
               sort_code=4
            ))

         product = await result.products[3].get_product()
         product = product.product
         print(product)
         
         # اضافه کردن کالا به سبد خرید
         await product.add_cart()

   asyncio.run(main())    
   ```

## قابلیت ها :

    - وارد شدن به حساب کاربری با شماره تلفن یا ایمیل با کد ارسال شده یا پسورد
    - خروج از حساب کاربری
    - ساخت فایل سشن برای استفاده مجدد
    - جستجو در دیجی کالا با تمام فیلتر ها
    - جستجوی محصولات با آیدی محصر به فرد آنها
    - دریافت کامنت ها
    - دریافت اطلاعات حساب کاربری
    - دریافت اطلاعات سبد خرید
    - اضافه کردن محصولات به سبد خرید
    - حذف محصولات از سبد خرید


  
## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/NuoQTe/DigiKala/blob/main/LICENSE) file for details.

<a href="https://pypi.org/project/DigiKala/"><img src="https://img.shields.io/badge/DigiKala-1.0-F5F5F5?style=flat-square&labelColor=DC143C"></a> 

## Developer
- **Telegram**: [t.me/NuoQTe](https://t.me/NuoQTe)

>>>>>>> 4f4ca4e (initial commit)
---
