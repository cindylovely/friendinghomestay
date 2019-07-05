from django.db import models
from django import forms
from django.contrib.auth.models import User
import pickle
import gzip
from multiselectfield import MultiSelectField
from datetime import datetime
from twisted import internet
from commctrl import TV_FIRST
  


class Product(models.Model):
    username= models.CharField(null=False , max_length=150)
    product_id = models.AutoField(primary_key=True)
    product_name= models.CharField(null=False , max_length=150)
    price=models.IntegerField(default=0)
    description=models.TextField(null=False, max_length=500)
    picture_url=models.CharField(null=True, max_length=150)
    #언어교류
    language= models.TextField(default='',null=True)
    #문화교류
    culture= models.TextField(default='',null=True)
    gas = models.TextField(default='',null=True)
    #facility

    real_price=models.IntegerField(default=0)
    locate= models.TextField(null=True)
    location = models.TextField(default='',null=True)
    house = models.TextField(default='',null=True)
    room = models.TextField(default='',null=True)
    bed = models.TextField(default='',null=True)
    bathroom = models.TextField(default='',null=True)
    family = models.TextField(default='',null=True)
    pet = models.TextField(default='',null=True)
    #homo
    공용화장실 = models.TextField(null=True)
    객실내화장실 = models.TextField(null=True)
    객실밖화장실 = models.TextField(null=True, default=0)
    경기도고양시 = models.TextField(null=True, default=0)
    경기도광주시 = models.TextField(null=True, default=0)
    경기도김포시 = models.TextField(null=True, default=0)
    경기도부천시 = models.TextField(null=True, default=0)
    경기도성남시 = models.TextField(null=True, default=0)
    경기도수원시 = models.TextField(null=True, default=0)
    경기도안양시 = models.TextField(null=True, default=0)
    경기도양평군 = models.TextField(null=True, default=0)
    경기도오산시 = models.TextField(null=True, default=0)
    경기도용인시 = models.TextField(null=True, default=0)
    경기도이천시 = models.TextField(null=True, default=0)
    경기도파주시 = models.TextField(null=True, default=0)
    서울특별시강남구 = models.TextField(null=True, default=0)
    서울특별시강동구 = models.TextField(null=True, default=0)
    서울특별시강북구 = models.TextField(null=True, default=0)
    서울특별시강서구 = models.TextField(null=True, default=0)
    서울특별시구로구 = models.TextField(null=True, default=0)
    서울특별시도봉구 = models.TextField(null=True, default=0)
    서울특별시동대문구 = models.TextField(null=True, default=0)
    서울특별시동작구 = models.TextField(null=True, default=0)
    서울특별시마포구 = models.TextField(null=True, default=0)
    서울특별시서대문구 = models.TextField(null=True, default=0)
    서울특별시서초구 = models.TextField(null=True, default=0)
    서울특별시성북구 = models.TextField(null=True, default=0)
    서울특별시송파구 = models.TextField(null=True, default=0)
    서울특별시양천구 = models.TextField(null=True, default=0)
    서울특별시영등포구 = models.TextField(null=True, default=0)
    서울특별시용산구 = models.TextField(null=True, default=0)
    서울특별시종로구 = models.TextField(null=True, default=0)
    서울특별시중구 = models.TextField(null=True, default=0)
    internet = models.TextField(null=True, default=0)
    TV = models.TextField(null=True, default=0)
    laundry = models.TextField(null=True, default=0)
    Air_Conditioning = models.TextField(null=True, default=0)
    Fridge = models.TextField(null=True, default=0)
    Hair_dryer = models.TextField(null=True, default=0)
    kitchen_available = models.TextField(null=True, default=0)
    Health_club = models.TextField(null=True, default=0)
    Parking = models.TextField(null=True, default=0)
    Garden = models.TextField(null=True, default=0)
    Desk_and_Lamp = models.TextField(null=True, default=0)
    smoking_possible = models.TextField(null=True, default=0)
    single_room = models.TextField(null=True, default=0)
    double_room = models.TextField(null=True, default=0)
    triple_room = models.TextField(null=True, default=0)
    quadruple_room = models.TextField(null=True, default=0)
    dorm = models.TextField(null=True, default=0)
    #hetero
    minday =models.IntegerField(default=0)
    maxday =models.IntegerField(default=0)
    welcome_irrelevant = models.TextField(null=True, default=0)
    welcome_males = models.TextField(null=True, default=0)
    welcome_females = models.TextField(null=True, default=0)
    welcome_couples = models.TextField(null=True, default=0)
    welcome_families = models.TextField(null=True, default=0)
    welcome_students = models.TextField(null=True, default=0)
    Computer = models.TextField(null=True, default=0)
    Smoke_alarm = models.TextField(null=True, default=0)
    Dresser_Drawers = models.TextField(null=True, default=0)
    Closet_Wardrobe = models.TextField(null=True, default=0)
    Wheelchair_Accessible = models.TextField(null=True, default=0)
    Barbecue= models.TextField(null=True, default=0)
    Bikes_for_use= models.TextField(null=True, default=0)
    Patio= models.TextField(null=True, default=0)
    Gym_at_home= models.TextField(null=True, default=0 )
    Bedside_Locker_Nightstand= models.TextField(null=True, default=0)
    Radio= models.TextField(null=True, default=0)
    telephone= models.TextField(null=True, default=0)
    Carpet_Moquette= models.TextField(null=True, default=0)
    fax= models.TextField(null=True, default=0)
    Mirror= models.TextField(null=True, default=0)
    Shopping_Centre= models.TextField(null=True, default=0)
    Amusement_Park= models.TextField(null=True, default=0)
    Swimming_Pool= models.TextField(null=True, default=0)
    Hospital= models.TextField(null=True, default=0)
    Tennis= models.TextField(null=True, default=0)
    Park= models.TextField(null=True, default=0)
    Gym= models.TextField(null=True, default=0)
    Golf= models.TextField(null=True, default=0)
    Swimming= models.TextField(null=True, default=0)
    Cinema= models.TextField(null=True, default=0)
    Library= models.TextField(null=True, default=0)
    Museum= models.TextField(null=True, default=0)
    Restaurant= models.TextField(null=True, default=0)
    Bowling= models.TextField(null=True, default=0)
    Airport= models.TextField(null=True, default=0)
    Beach= models.TextField(null=True, default=0)
    Fishing= models.TextField(null=True, default=0)
    Sports_arena= models.TextField(null=True, default=0)
    subway_station= models.TextField(null=True, default=0)
    vegetarian= models.TextField(null=True, default=0)
    경상도= models.TextField(null=True, default=0)
    대구광역시= models.TextField(null=True, default=0)
    부산광역시= models.TextField(null=True, default=0)
    인천광역시= models.TextField(null=True, default=0)
    제주도= models.TextField(null=True, default=0)
    충청북도= models.TextField(null=True, default=0)
    울산광역시= models.TextField(null=True, default=0)
    within_a_hour= models.TextField(null=True, default=0)
    within_two_hours= models.TextField(null=True, default=0)
    몇_시간_이내= models.TextField(null=True, default=0)
    하루_이내= models.TextField(null=True, default=0)
    며칠_이내= models.TextField(null=True, default=0)
    강아지= models.TextField(null=True, default=0)
    고양이= models.TextField(null=True, default=0)
    어류= models.TextField(null=True, default=0)
    토끼= models.TextField(null=True, default=0)
    햄스터= models.TextField(null=True, default=0)
    강원도강릉시= models.TextField(null=True, default=0)
    경기도양주시= models.TextField(null=True, default=0)
    경기도의왕시= models.TextField(null=True, default=0)
    경상남도창원시= models.TextField(null=True, default=0)
    경상북도경산시= models.TextField(null=True, default=0)
    대구광역시동구= models.TextField(null=True, default=0)
    대구광역시북구= models.TextField(null=True, default=0)
    부산광역시부산진구= models.TextField(null=True, default=0)
    부산광역시사하구= models.TextField(null=True, default=0)
    부산광역시해운대구= models.TextField(null=True, default=0)
    서울특별시노원구= models.TextField(null=True, default=0)
    서울특별시중랑구= models.TextField(null=True, default=0)
    울산광역시남구= models.TextField(null=True, default=0)
    울산광역시중구= models.TextField(null=True, default=0)
    인천관역시인천= models.TextField(null=True, default=0)
    인천광역시계양구= models.TextField(null=True, default=0)
    인천광역시남동구= models.TextField(null=True, default=0)
    인천광역시부평구= models.TextField(null=True, default=0)
    인천광역시서구= models.TextField(null=True, default=0)
    인천광역시연수구= models.TextField(null=True, default=0)
    인천광역시중구= models.TextField(null=True, default=0)
    제주도서귀포시= models.TextField(null=True, default=0)
    제주도제주시= models.TextField(null=True, default=0)
    충청북도단양군= models.TextField(null=True, default=0)
        
        
        
        

        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        #fields = ["username", "email","password"] 
        fields = ["first_name" ,"last_name" , "username", "email","password"]   


class language(models.Model):
    Korean = models.CharField(null=False , max_length=150)
    English = models.CharField(null=False , max_length=150)
    Japanese = models.CharField(null=False , max_length=150)
    French = models.CharField(null=False , max_length=150)
    Spanish = models.CharField(null=False , max_length=150)
    Chinese = models.CharField(null=False , max_length=150)
    German = models.CharField(null=False , max_length=150)
    Russian = models.CharField(null=False , max_length=150)
    Italian = models.CharField(null=False , max_length=150)
    ArbiC = models.CharField(null=False , max_length=150)
    Portuguese = models.CharField(null=False , max_length=150)
    Malaysian = models.CharField(null=False , max_length=150)
    Indonesia = models.CharField(null=False , max_length=150)
    Hindi = models.CharField(null=False , max_length=150)
    Other = models.CharField(null=False , max_length=150)
    



class Cart(models.Model):
    #장바구니 코드 , 숫자 일련번호
    cart_id= models.AutoField(primary_key = True)
    #사용자 아이디
    userid=models.CharField(null=False, max_length=150)
    product_id=models.IntegerField(default=0)
    amount=models.IntegerField(default=0)
    travel= models.TextField(default='',null=True)
    gas= models.TextField(default='',null=True)
    checkin= models.TextField(default='',null=True)
    checkout= models.TextField(default='',null=True)
    dateinterval=models.TextField(default='',null=True)
    
    
    
    

 
class Board(models.Model):
    idx=models.AutoField(primary_key=True)
    writer=models.CharField(null=False,max_length=50)
    title=models.CharField(null=False,max_length=120)
    hit=models.IntegerField(default=0)
    content=models.TextField(null=False)
    post_date=models.DateTimeField(default=datetime.now,blank=True)
    filename=models.CharField(null=True, blank=True,default="",max_length=500)
    filesize=models.IntegerField(default=0)
    down=models.IntegerField(default=0)
    
    def hit_up(self):
        self.hit += 1
    def down_up(self):
        self.down += 1

class Comment(models.Model):
    idx=models.AutoField(primary_key=True)
    board_idx=models.IntegerField(null=False)
    writer=models.CharField(null=False,max_length=50)
    content=models.TextField(null=False)
    post_date=models.DateTimeField(default=datetime.now,blank=True)
     

class detailinfo(models.Model): 
    sex= models.TextField(default='',null=True)
    location= models.TextField(default='',null=True)
    drop1= models.TextField(default='',null=True)
    drop2= models.TextField(default='',null=True)
    drop3= models.TextField(default='',null=True)
    languageexchangecount= models.TextField(default='',null=True)
    languageexchangeminute= models.TextField(default='',null=True)
    file2=models.CharField(null=True, max_length=150)
    culture= models.TextField(default='',null=True)
    language = models.TextField(default='',null=True)
    username= models.CharField(null=True , max_length=150)
    age= models.TextField(default='',null=True)
    travel= models.TextField(default='',null=True)
    job= models.TextField(default='',null=True)
    gas1= models.TextField(default='',null=True)
    religion= models.TextField(default='',null=True)
    hobby= models.TextField(default='',null=True)
    client= models.TextField(default='',null=True)
    product_id = models.TextField(default='',null=True)
    
    
class culture(models.Model):    
    travel= models.TextField(default='',null=True)
    userid=models.CharField(null=True, max_length=150)

       
    