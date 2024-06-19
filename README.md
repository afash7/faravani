# پروژه سایت فراوانی

این پروژه یک وبسایت مشابه سایت دیوار است که با استفاده از فریمورک جنگو پیاده‌سازی شده است. کاربران می‌توانند در این سایت ثبت‌نام کرده، کالاهای خود را آگهی کنند، و با دیگر کاربران از طریق سیستم چت ارتباط بگیرند.

## ویژگی‌ها

### ۱. ثبت‌نام و ورود کاربران
- کاربران با استفاده از فرم ثبت‌نام، اطلاعات خود را وارد می‌کنند.
- سیستم یک کد تایید به شماره موبایل کاربر ارسال می‌کند.
- کاربر با وارد کردن کد تایید، حساب کاربری خود را فعال می‌کند.

### ۲. مدیریت پروفایل کاربران
- کاربران می‌توانند پروفایل خود را با اطلاعاتی مانند عکس، بیوگرافی و موقعیت مکانی به‌روزرسانی کنند.

### ۳. آگهی‌دهی کالاها
- کاربران فرم آگهی‌دهی کالا را با اطلاعاتی مانند نام، توضیحات، دسته‌بندی و تصویر پر می‌کنند.
- سیستم اطلاعات را دریافت و در دیتابیس ذخیره می‌کند.

### ۴. جستجو و فیلتر کالاها
- کاربران می‌توانند بر اساس دسته‌بندی، شرایط کالا و موقعیت مکانی جستجو کنند.
- سیستم نتایج مرتبط را بر اساس فیلترهای اعمال شده نمایش می‌دهد.

### ۵. چت و مذاکره
- کاربران می‌توانند از طریق سیستم چت با آگهی‌دهنده تماس بگیرند.
- سیستم پیام‌ها را بین کاربران رد و بدل می‌کند.

### ۶. مدیریت دسته‌بندی‌ها
- ادمین می‌تواند دسته‌بندی‌های جدید ایجاد، ویرایش یا حذف کند.

### ۷. مدیریت شهرها و استان‌ها
- ادمین می‌تواند شهرها و استان‌ها را در سیستم اضافه یا به‌روزرسانی کند.

## ساختار دایرکتوری‌ها

```
.
├── ad_app
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── api
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── __pycache__
│   ├── serializers.py
│   ├── templates
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── blog
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── __pycache__
│   ├── templates
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── categories
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── __pycache__
│   ├── tests.py
│   └── views.py
├── communications
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── __pycache__
│   ├── templates
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── faravani
│   ├── asgi.py
│   ├── __init__.py
│   ├── local_settings.py
│   ├── __pycache__
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── forum
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── items
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── __pycache__
│   ├── templates
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── locations
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
├── package.json
├── package-lock.json
├── README.md
├── requirements.txt
├── styles
│   ├── base.css
│   ├── communications.css
│   ├── items.css
│   ├── uploads.css
│   ├── users.css
│   └── verification.css
├── tailwind.config.js
├── tree_structures.txt
├── uploads
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── __pycache__
│   ├── templates
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── users
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── __pycache__
│   ├── tasks.py
│   ├── templates
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── verification
	├── admin.py
	├── apps.py
	├── forms.py
	├── __init__.py
	├── migrations
	├── models.py
	├── __pycache__
	├── tasks.py
	├── templates
	├── tests.py
	├── urls.py
	└── views.py

41 directories, 102 files
```

## اپلیکیشن‌ها

### اپلیکیشن `users`:
- `register_user`: ثبت‌نام کاربر جدید.
- `login_user`: ورود کاربر به سیستم.
- `send_verification_code`: ارسال کد تایید به شماره موبایل کاربر.
- `verify_user`: تایید کد و فعال‌سازی حساب کاربری.

### اپلیکیشن `items`:
- `create_item`: ایجاد یک آگهی کالای جدید.
- `update_item`: به‌روزرسانی اطلاعات یک آگهی کالا.
- `delete_item`: حذف یک آگهی کالا.
- `list_items_by_category`: لیست کردن کالاها بر اساس دسته‌بندی.

### اپلیکیشن `locations`:
- `add_city`: اضافه کردن یک شهر جدید به دیتابیس.
- `add_province`: اضافه کردن یک استان جدید به دیتابیس.
- `list_cities`: لیست کردن تمام شهرها.
- `list_provinces`: لیست کردن تمام استان‌ها.

### اپلیکیشن `communications`:
- `start_chat`: شروع یک چت جدید بین دو کاربر.
- `send_message`: ارسال پیام در یک چت.
- `list_messages`: لیست کردن پیام‌ها در یک چت.

### اپلیکیشن `verification`:
- `generate_verification_code`: تولید کد تایید.
- `send_verification_code`: ارسال کد تایید به کاربر.
- `check_verification_code`: بررسی صحت کد تایید وارد شده توسط کاربر.

### اپلیکیشن `api`:
- `get_item_details`: دریافت جزئیات یک کالای آگهی‌شده.
- `search_items`: جستجوی کالاها بر اساس فیلترهای مختلف.
- `user_profile`: دریافت اطلاعات پروفایل کاربر.

## روابط دیتابیس

- `User` به `UserProfile`: رابطه‌ی `One-to-One`
- `UserProfile` به `City`: رابطه‌ی `Many-to-One`
- `Item` به `User`: رابطه‌ی `Many-to-One`
- `Item` به `Category`: رابطه‌ی `Many-to-One`
- `Category` به خودش (برای دسته‌بندی‌های سلسله‌مراتبی): رابطه‌ی `Self-referencing`
- `City` به `Province`: رابطه‌ی `Many-to-One`

## نصب و راه‌اندازی

### پیش‌نیازها
- Python 3.8 به بالا
- Django 3.2 به بالا


### مراحل نصب

1. مخزن را کلون کنید:
   ```bash
   git clone https://github.com/username/repo.git
   cd repo
   ```

2. محیط مجازی ایجاد و فعال کنید:
   ```bash
   python -m venv venv
   source venv/bin/activate  # برای سیستم‌های یونیکس
   venv\Scripts\activate     # برای سیستم‌های ویندوز
   ```

3. وابستگی‌ها را نصب کنید:
   ```bash
   pip install -r requirements.txt
   ```

4. مایگریت های دیتابیس را اعمال کنید:
   ```bash
   python manage.py migrate
   ```

5. کاربر ادمین ایجاد کنید:
   ```bash
   python manage.py createsuperuser
   ```

6. سرور را اجرا کنید:
   ```bash
   python manage.py runserver
   ```

سپس می‌توانید به آدرس `http://127.0.0.1:8000` مراجعه کنید و پروژه را مشاهده کنید.



## تماس

اگر سوالی دارید یا نیاز به کمک دارید، می‌توانید با ایمیل [afashseven@gmail.com](mailto:youremail@example.com) تماس بگیرید.




