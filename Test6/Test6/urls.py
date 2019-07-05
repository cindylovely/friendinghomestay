from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #메인ㅎ페이지
    path('', views.home),
    #이벤트 패이지
    path('blog', views.blog),
    #부킹 페이지
    path('room_listAll',views.room_listAll),     
    path('booking', views.booking),
    #게시판 페이지
    path('contact', views.contact),
    path('elements', views.elements),
    #사이트 정보제공  페이지
    path('about/', views.about),
    #마이페이지
    path('mypage', views.mypage),
    #홈스테이방관련
    path('product_list',views.product_list),
    #등록된 홈스테이 전체 리스트
    path('product_listAll',views.product_listAll),
    #로그인
    path('login/',views.login_check, name="login"),
    #회워가입
    path('join/',views.join, name="join"),
    #로그아웃
    path('logout/',views.logout, name="logout"),
    #카트담기
    path('cart_insert',views.cart_insert),
    #카트리스트
    path('cart_list',views.cart_list),
    #카트수정
    path('cart_update',views.cart_update),
    #카트삭제
    path('cart_del',views.cart_del),
    #카트전체삭제
    path('cart_del_all',views.cart_del_all),
    #홈스테이 등록페이지
    path('product_write',views.product_write),
    #홈스테이 등록
    path('product_insert',views.product_insert),
    #홈스테이 등록정보 수정
    path('product_edit',views.product_edit),
    #홈스테이 정보등록
    path('product_update',views.product_update),
    #홈스테이 등록 정보 삭제
    path('product_delete',views.product_delete),
    #개인정보 등록 페이지
    path('detail_infowrite', views.detail_infowrite),
    #개인정보 등록 
    path('detailinfo_insert',views.detailinfo_insert),
    #개인정보 보기
    path('detailinfo_list',views.detailinfo_list),
    #개인정보 수정
    path('detailinfo_edit', views.detailinfo_edit),
    #개인정보 등록
    path('detailinfo_update', views.detailinfo_update),
    #개인정보 삭제
    path('detailinfo_delete', views.detailinfo_delete), 
    #호스트게스트 매칭   
    path('detailinfo_matching', views.detailinfo_matching),  
    #홈스테이 상세정보  링크 
    path('product_detail',views.product_detail),
    
    #게시판
    path('list',views.list),
    path('write',views.write),
    path('insert',views.insert),
    path('download',views.download),
    path('detail', views.detail),
    path('detail/', views.detail),
    path('reply_insert', views.reply_insert),
    path('update', views.update),
    path('delete', views.delete),
    
    #가격책정 리스트
    path('price_list', views.price_list),
    #가격 등록
    path('price_write', views.price_write),
    #최종가격 선택
    path('price_update', views.price_update),
   
    path('culture1', views.culture1),
    path('product_list1', views.product_list1),
    path('test1', views.test1), 
    
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/',include(debug_toolbar.urls)),
    ]