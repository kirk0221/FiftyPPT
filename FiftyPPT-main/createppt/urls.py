from django.urls import path
from . import views

urlpatterns = [
    path('create-ppt/', views.create_ppt, name='create_ppt'),
    path('myppt/', views.myppt, name='myppt'),  # myppt 페이지로 이동
    path('download_ppt/<int:ppt_id>/', views.download_ppt, name='download_ppt'),  # PPT 다운로드
    path('allppt/', views.all_ppt_list, name='all_ppt_list'),
    path('add_to_cart/<int:ppt_id>/', views.add_to_cart, name='add_to_cart'),  # 장바구니 추가 API
    path('my_cart/', views.my_cart, name='my_cart'),
    path('delete_ppt/<int:ppt_id>/', views.delete_ppt, name='delete_ppt'),

    path('login_required/', views.login_required_view, name='login_required'),
]
