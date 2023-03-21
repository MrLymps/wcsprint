from django.urls import path

from pages import views

app_name = "pages"

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about-me/', views.about_me, name='about_me'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('form_app_save/', views.form_app_saving, name='form_app_save'),
    path('toilets/', views.toilets, name='toilets'),
    path('toilet_furniture/', views.toilet_furniture, name='toilet_furniture'),
    path('shower_cabins/', views.shower_cabins, name='shower_cabins'),
    path('welcome_site/',views.welcome,name='welcome'),
    path('mobile_index/',views.mobile_index,name='mobile_index'),
    path('mobile_about_me',views.mobile_about_me,name='mobile_about_me'),



	

]
