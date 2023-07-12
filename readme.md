# django env setup

* install
> pip3 install django
* check django is work
> django-admin
* create a new project
> django-admin startproject django_practice

(django_practice 是Project name)

----

* build up new virtual env

> sudo pip3 install virtualenv

Now, create a virtual environment within the project directory by typing
 
> source newenv/bin/activate

---

# django介紹

* 最外層的django_practice可以更改名稱不影醒Django的運作。
* manage.py:利用他在終端機中下命令，請他去執行一些工作。
* 內層的django_practice的名稱如果重新命名，你必須做一些檔案內容的更改，比如settings.py，如果該改的沒改到會會出現錯誤，注意使用。
* settings.py:像Django的大腦，一些配置設定都在這裡處理。
* urls.py:我們可以在這個檔案中編排網頁的網址。
* wsgi.py: 詳細的意義我還沒有完全理解，只能先說最後部署網站到Heroku時會用到。

## run django project
> python manage.py runserver

go to (http://127.0.0.1:8000) 可以看到server已被架好
