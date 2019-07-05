from django.contrib import admin
from.models import Product
from.models import Cart
from home.models import Board


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("username", "product_id","product_name","price","description","picture_url")
     
admin.site.register(Product, ProductAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ("cart_id", "userid","product_id","amount")
     
admin.site.register(Cart, CartAdmin)


class BoardAdmin(admin.ModelAdmin):
    list_display=("writer","title","content")
    
#관리자 사이트에 테이블 등록
admin.site.register(Board, BoardAdmin)