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

## نصب و راه‌اندازی

### پیش‌نیازها
- Python 3.8 به بالا
- Django 3.2 به بالا

### مراحل نصب
۱. مخزن را کلون کنید:
   ```bash
   git clone https://github.com/username/repo-name.git
   ```

۲. وارد دایرکتوری پروژه شوید:
   ```bash
   cd repo-name
   ```

۳. محیط مجازی بسازید:
   ```bash
   python -m venv venv
   ```

۴. محیط مجازی را فعال کنید:
   - در ویندوز:
     ```bash
     venv\Scripts\activate
     ```
   - در مک و لینوکس:
     ```bash
     source venv/bin/activate
     ```

۵. بسته‌های مورد نیاز را نصب کنید:
   ```bash
   pip install -r requirements.txt
   ```

۶. مایگریت های پایگاه داده را اعمال کنید:
   ```bash
   python manage.py migrate
   ```

۷. سرور  را اجرا کنید:
   ```bash
   python manage.py runserver
   ```

اکنون می‌توانید به آدرس `http://127.0.0.1:8000/` بروید و وبسایت را مشاهده کنید.

