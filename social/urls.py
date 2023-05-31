from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', views.home, name='home-page'),
    path('base/', views.base, name='base-page'),
    path('post_add/', views.post_add, name='post-add-page'),
    path('test_post/', views.test_post, name='test-post'),
    path('vendor-admin/', views.vendor_admin, name='vendor-admin'),
    path('blank/', views.blank, name='blank'),
    path('test_home/', views.testh, name='test-home'),
    path('nav2/', views.main, name='test-nav'),
    path('base2/', views.testbase, name='test-base'),
    path('login/', views.login, name='login-page'),
    path('testlogin/', views.testlogin, name='testlogin-page'),
    path('become_vend/', views.become_vend, name='become_vend'),
    path('register/', views.register, name='register-page'),
    path('add_product/', views.add_product, name='add_product-page'),
    path('cart/', views.cart, name='cart-page'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home_page'), name='logout'),
    path('landing/', views.landing, name='landing'),
    path('footer/', views.footer, name='footer'),
    path('signup/', views.signup, name='signup'),
    path('products/', views.products, name='products'),
    path('', views.home_page, name='home_page'),
    path('view_product/', views.view_product, name='view_product'),
    path('vendor_adm/', views.vendor_adm, name='vendor_adm'),
]
