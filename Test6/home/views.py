import math
import os
import numpy as np
import pandas as pd
from pprint import pprint
from django.shortcuts import render, render_to_response,redirect ,HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from .forms import UserForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout,
)
from django.views.decorators.csrf import csrf_exempt
from home.models import Product, Cart
from home.models import language,Board
from home.models import detailinfo,Comment
from home.models import culture
from django.db.models import Q
from django.contrib.staticfiles.storage import staticfiles_storage
import pickle
from django.conf import settings
from django.utils.http import urlquote
from django.db import connections
from numba.tests import true_div_usecase
#문화교류
import requests as r
import json
import geopy
from geopy.geocoders import Nominatim
from django.views.generic import View
from dsft.dsft import DSFT
# from django.contrib.formtools.wizard.views import SessionWizardView
import datetime
import scipy
import sys
from _ast import Try

#상품 이미지를 업로드할 데렉토리
UPLOAD_DIR = "C:/codesquard/workspace/Test6/home/static/images/"



def about(request):
    return render_to_response('about.html')


def blog(request):
    return render_to_response("blog.html")


def booking(request):
    return render_to_response("booking.html")
 

def contact(request):
    return render_to_response("contact.html")


def elements(request):
    return render_to_response("elements.html")



def mypage(request):
    if not request.user.is_authenticated:
        data = {"username": request.user,
                "is_authenticated": request.user.is_authenticated}
    else:
        data = {"last_login": request.user.last_login ,
                "username": request.user.username,
                "password": request.user.password,
                "is_authenticated": request.user.is_authenticated,
                
                
                }
    return render(request, "mypage.html", context={"data": data})




def home(request):
    if not request.user.is_authenticated:
        data = {"username": request.user,
                "is_authenticated": request.user.is_authenticated}
    else:
        data = {"last_login": request.user.last_login ,
                "username": request.user.username,
                "password": request.user.password,
                "is_authenticated": request.user.is_authenticated}
    return render(request, "index.html", context={"data": data})



def product_list1(request):
#     uid = request.session.get("userid")
#     productList = Product.objects.filter(username=uid)
#     return render_to_response("product_list.html", {"productList": productList }) 
    uid = request.session.get("userid")
#     id=request.POST.get("product_id")
#     obj = Product.objects.filter(product_id=id)
#     pid=request.POST.get("product_id","no")
    productList = Product.objects.filter(username=uid)
    fp=open("C:\\model_test.sav","rb")
    model = pickle.load(fp)
#     a= Product.objects.values('welcome_irrelevant','welcome_males','welcome_couples','welcome_families','internet','kitchen_available','Parking','Air_Conditioning','Computer','Smoke_alarm','Desk_and_Lamp','Dresser_Drawers','Closet_Wardrobe','Hair_dryer','Garden','Wheelchair_Accessible','Barbecue','Bikes_for_use','Gym_at_home','Bedside_Locker_Nightstand').order_by('-product_id')[0]    
#     host_allinfo= Product.objects.filter(username = uid).order_by("-pid").values()
    host_allinfo= Product.objects.filter(username = uid).order_by("-product_id").values()     #'product_name', flat= True
    print(host_allinfo)
    allinfo = []
    try:
        
        for k,v in host_allinfo[0].items():
            allinfo.append(v)
             
    #     print(allinfo)
        aaaa = allinfo[8:28]
        bbbb = []
        for i in aaaa:
            
            bbbb.append(int(i))
        priceTips = model.predict([bbbb])[0]             
        real_price1 = np.expm1(priceTips)
        real_price=int(round(real_price1))
        return render_to_response("product_list.html", {"productList": productList,'real_price':real_price })
    except:
        return render_to_response("product_list.html", {"productList": productList})
    fp.close()


@csrf_exempt
def product_list(request):
    uid = request.session.get("userid")
    productList = Product.objects.filter(username=uid)
    fp=open("C:\\model_weekday.sav","rb")
    f2=open("C:\\matrix_CZ.sav","rb")
    f3=open("C:\\y_pred.sav","rb")
    f4=open("C:\\y_tar.sav","rb")
    f5=open("C:\\dsft.sav","rb")
 
    y_pred = pickle.load(f3)
    y_tar = pickle.load(f4)
    model = pickle.load(fp)
    CZ = pickle.load(f2)
    dsft= pickle.load(f5)
    
    host_allinfo= Product.objects.filter(username = uid).order_by("-product_id").values()     #'product_name', flat= True
    print(host_allinfo)
    allinfo = []
    try:
        
        for k,v in host_allinfo[0].items():
            allinfo.append(v)
        print(allinfo)     
        aaaa = allinfo[18:68]
        print(aaaa)
        bbbb =  allinfo[68:]
        print(bbbb)
        
        X_homo = []
        X_hetero = []
        
        for i in aaaa:
            
            X_homo.append(int(i))
        print(X_homo)    
            
        for j in bbbb:
            
            
            X_hetero.append(int(j))
        print(X_hetero) 
            

        X_homo = np.array(X_homo)
        X_homo = np.dot(X_homo, CZ)
        X_hetero = np.array(X_hetero)
        
        try:     
            X_test = dsft.make_homogeneous_feature(X_homo, X_hetero, True)
             
        except Exception as e:
            print(e)

    
        print(X_test)
        priceTips = model.predict([X_test])[0]
        print(priceTips)


        y_tar1 = np.expm1(y_tar)
        y_pred1 = np.expm1(y_pred)
        real_price1 = np.expm1(priceTips)
        real_price = int(round(real_price1,-2))
        
        print(real_price)
    
        sum_errs = sum((y_tar1 - y_pred1)**2)
        stdev = math.sqrt(1/(len(y_tar1)-2) * sum_errs)
        sigma = 0.2 * stdev
        min_price1, max_price1 = real_price - sigma, real_price + sigma
        
        min_price = int(round(min_price1,-2))
        max_price = int(round(max_price1,-2))
        
        return render_to_response("product_list.html", {"productList": productList ,'real_price':real_price, "min_price":min_price, "max_price":max_price })
    
    except Exception as e:
        print(e)
        return render_to_response("product_list.html", {"productList": productList})
    fp.close()


@csrf_exempt
def room_listAll(request):   
    count = Product.objects.count()
    productList=Product.objects.all() 
    detailinfoList=detailinfo.objects.all()   

        
     
    try:
        search_option=request.POST["search_option"]
    except:
        search_option=""
        
    try:
        search=request.POST["search"]
    except:
        search=""
        
    #필드명__contains = 검색어  name__contains=""
    if search_option=="all":
        count = Product.objects.filter(Q(product_name__contains=search) | Q(language__contains=search)| Q(culture__contains=search)).count()
    elif search_option=="product_name":
        count = Product.objects.filter(product_name = search).count()
    elif search_option=="language":
        count = Product.objects.filter(language = search).count()
    elif search_option=="culture":
        count = Product.objects.filter(culture = search).count()
         
         
    if search_option=="all":
        productList = Product.objects.filter(Q(product_name__contains=search) | Q(language__contains=search)| Q(culture__contains=search))
    elif search_option=="product_name":
        productList = Product.objects.filter(product_name__contains = search)
    elif search_option=="language":
        productList = Product.objects.filter(language__contains = search)
    elif search_option=="culture":
        productList = Product.objects.filter(culture__contains = search) 
        
    location = request.GET.get('location', '')
    culture = request.GET.get('culture', '')
    language = request.GET.get('language', '')
    room = request.GET.get('room', '')
    bed = request.GET.get('bed', '')
    bathroom = request.GET.get('bathroom', '')
    family = request.GET.get('family', '')
    pet = request.GET.get('pet', '')
    religion = request.GET.get('religion', '')
    drop1 = request.GET.get('drop1', '') 

    print("BLABLA", request.GET)
    
    if location: # q가 있으면
        productList =productList.filter(location__icontains=location)
        #return render(request, 'room_listAll.html', {'productList' : productList})
    
    elif culture: 
        
        productList =productList.filter(culture__icontains=culture) 
        #return render(request, 'room_listAll.html', {'productList' : productList})
        
    elif language:
        productList =productList.filter(language__icontains=language) 
        print(language)    
        
    elif room:
        productList =productList.filter(room__contains=room)        
        
    elif bed:
        productList =productList.filter(bed__contains=bed)    
            
    elif bathroom:
        productList =productList.filter(bathroom__contains=bathroom)   
             
    elif family:
        productList =productList.filter(family__contains=family) 
        
    elif pet:
        productList =productList.filter(pet__contains=pet)          
                                                                                    
    elif drop1:
        detailinfoList= detailinfoList.filter(drop1__contains=drop1)
        
    elif religion:
        detailinfoList= detailinfoList.filter(religion__contains=religion)  
        
        
    try:
        id=request.GET["host"]
        print(id)
        host=productList.filter(username=id)
        return render_to_response("room_listAll.html", {"productList": host, "count": count, "search_option":search_option, "search": search,'detailinfoList':detailinfoList ,"location" : location, "drop1":drop1,"culture":culture,"language":language,   "room":room,  "bed":bed,  "bathroom":bathroom, "family":family,"pet":pet,"religion":religion  })
    except:
        return render_to_response("room_listAll.html", {"productList": productList, "count": count, "search_option":search_option, "search": search,'detailinfoList':detailinfoList ,"location" : location, "drop1":drop1,"culture":culture,"language":language,   "room":room,  "bed":bed,  "bathroom":bathroom, "family":family,"pet":pet,"religion":religion  })
        
        





def product_listAll(request):
    count = Product.objects.count()
    productList=Product.objects.order_by("product_name")
    return render_to_response("product_listAll.html" , {"productList":productList, "count":count})


def product_detail(request):
    uid = request.session.get("userid")
    pid=request.GET["product_id"]
    dto=Product.objects.get(product_id=pid)
    dto2=detailinfo.objects.get(product_id=pid)
    return render_to_response("product_detail.html", {"dto":dto, "dto2":dto2 , "range":range(1,11) })


@csrf_exempt
def cart_insert(request):
    uid=request.session.get("userid","")
    gas = request.GET.get("gas")
    print(gas)
    if uid!="": #로그인한 상태
        dto=Cart(userid=uid,
                 product_id=request.POST.get("product_id","0"),
                 travel=request.POST.get("travel","0"),
                 checkin=request.POST.get("checkin","0"),
                 checkout=request.POST.get("checkout","0"),
                 
#                  real_price=request.POST.get("real_price", "0"),
                 amount=request.POST.get("amount","0"),)

        dto.save()
        return redirect("/cart_list?pid="+request.POST.get("product_id","0")+"&gas="+gas, {"dto": dto})
    else: #로그인하지 않은 상태
        return redirect("/login")
    
            
def login_check(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        name= request.POST["username"]
        pwd = request.POST["password"]
        user=authenticate(username=name, password=pwd)
        if user is not None:
            django_login(request, user)
            request.session["userid"] = name #세션변수 저장
            print(request.session["userid"])
            return redirect("/")
        else:
            return render_to_response("index.html", {"msg": "로그인 문제....다시 시도해 보세요."})
    else: #get 방식의 경우
        form=LoginForm()
        return render(request, "login1.html", {"form": form})
    
    
    
    
@csrf_exempt  
def join(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user=User.objects.create_user(**form.cleaned_data)
            django_login(request, new_user)
            return redirect("/mypage")
        else:
            return render_to_response("index.html", {"msg":"회원가입 실패.... 다시시도해보세요."})
    else:
        form=UserForm()
        return render(request, "join2.html", {"form": form })
    return render(request, "index.html")





def logout(request):
    django_logout(request)
    for sesskey in request.session.keys():
        del request.session[sesskey]
    return redirect("/")


def cart_list(request):
    uid= request.session.get("userid","")
    print(request.GET)
#     pid=request.GET["pid"]
    pid=request.GET.get("pid")
    gas=request.GET.get("gas")
    print(pid,gas)

    if uid != "":
        nom = Nominatim()
        location_list= Product.objects.filter(product_id = pid).values()
        print(location_list)
        location = []
        destination_list= Cart.objects.filter(userid = uid).values()
        destination = []
        gas_list=Product.objects.filter(gas = gas).values()
        print(gas_list)
        gas = []
    
            
        try:
            for a,b in location_list[0].items():
                location.append(b)    
            mainlocation = location[11]
            start = location[10]
            print("sssssss ",start)
            startgeocode = nom.geocode(start , timeout=5)
            startlat = str(startgeocode.latitude)
            startlng = str(startgeocode.longitude)
         
            for c,d in destination_list[0].items():
                destination.append(d)    
            end = destination[4]
            print(end)
            endgeocode = nom.geocode(end ,timeout=5)
            endlat = str(endgeocode.latitude)       
            endlng = str(endgeocode.longitude)
    
            
            for e,f in gas_list[0].items():
                gas.append(f)    
            kind_of_oil = gas[8]
    
                                                                              
            search_distance_url_base = "https://map.naver.com/spirra/findCarRoute.nhn?route=route3&output=json&result=web3&coord_type=naver&search=2&car=0&mileage=12.4&start=" +startlng+ "," +startlat+","+start+"&destination="+endlng+ ","+endlat+","+end
            
            friending_price =  GET_INFO(mainlocation, search_distance_url_base, start, end, kind_of_oil)
            print('FRIENDING PRICE:', friending_price)
    
            print('LOOK AT ME')
    
        except Exception as e:
            print("error") 
            print(e)
            
        try:        
            date_list= Cart.objects.filter(userid = uid).values()
            date=[]
            print(date_list)
            for g,h in date_list[0].items():
                date.append(h)    
            checkin1 = date[6]
            checkout1 = date[7]
            
            checkin=datetime.datetime.strptime(checkin1,'%m/%d/%Y')
            checkout=datetime.datetime.strptime(checkout1,'%m/%d/%Y')
    #         print(checkin)
    #         print(checkout)
            dateinterval2=checkout-checkin
            dateinterval=(dateinterval2.days)
        
        except:
            return redirect("/")
        
                   
        cartCount = Cart.objects.count()
        cartList = Cart.objects.raw("""
select cart_id, userid, amount, c.product_id , product_name, real_price, amount*real_price money, dateinterval
from home_cart c, home_product p
where c.product_id=p.product_id and userid='{0}' """.format(uid))
        sumMoney=0
        fee=0
        sum=0
        if cartCount > 0 :
            sumRow = Cart.objects.raw("""
        select sum(amount*real_price) cart_id
        from home_cart c, home_product p
        where c.product_id=p.product_id and userid='{0}'
            """.format(uid))
            sumMoney=sumRow[0].cart_id
            if  sumMoney != None and sumMoney > 10000:
                fee=0
            else:
                fee=2500
                    
            if sumMoney != None:
#                 sum=sumMoney+fee+friending_price
                sum=(sumMoney+fee)*dateinterval+friending_price
            else:
                sumMoney=0
                sum=0        
         
        return render_to_response("cart_list.html", {"cartList": cartList,"cartCount": cartCount,"sumMoney": sumMoney,"fee": fee,"sum": sum ,"friending_price":friending_price,"dateinterval":dateinterval })
    else:
        return redirect("/login")

    
def cart_update(request):
    uid=request.session.get("userid","")
    if uid!= "":
        amt=request.POST.getlist("amount")
        cid=request.POST.getlist("cart_id")
        pid=request.POST.getlist("product_id")
        for idx in range(len(cid)):
            dto=Cart(cart_id=cid[idx],
                     userid=uid,
                     product_id=pid[idx],
                     amount=amt[idx])
            dto.save();
        return render_to_response("/cart_list")
    else:
        return redirect("/login")


def cart_del(request):
    #print(request.GET)
    Cart.objects.get(cart_id=request.GET["cart_id"]).delete()
    return redirect("/cart_list")



def cart_del_all(request):
    uid=request.session.get("userid","")
    if uid!="":
        Cart.objects.filter(userid=uid).delete()
        return redirect("/cart_list")
    else:
        return redirect("/login")
    
    
def price_write(request): 
    uid=request.session.get("userid","")   
    return render_to_response("price_list.html")

#상품등록 페이지로 이동    
def product_write(request):
    uid=request.session.get("userid","")
    return render_to_response("product_write.html",{"uid":uid})



@csrf_exempt    
def product_insert(request):
    #첨부파일이 있는 경우
    if "file1" in request.FILES:
        file=request.FILES["file1"]
        file_name=file._name
        fp=open("%s%s" % (UPLOAD_DIR, file_name), "wb")
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()
    else:
        file_name="-"
        
    dto = Product( product_name=request.POST["product_name"],
                    description=request.POST["description"],
#                     price=request.POST["price"],
                    username=request.POST["username"],
                    locate=request.POST["locate"],
                    location=request.POST["location"],
                    picture_url=file_name,
#                     priceTips=request.get("priceTips"),
                    language=request.POST.get("language", "no"),
                    culture=request.POST.get("culture", "no"),
                    house=request.POST.get("house", "no"),
                    room=request.POST.get("room", "no"),
                    bed=request.POST.get("bed", "no"),
                    bathroom=request.POST.get("bathroom", "no"),
                    family=request.POST.get("family", "no"),
                    pet=request.POST.get("pet", "no"),
                    gas=request.POST.get("gas", "no"),
                                            공용화장실=request.POST.get("공용화장실", "0"),
                                            객실내화장실=request.POST.get("객실내화장실", "0"),
                                            객실밖화장실=request.POST.get("객실밖화장실", "0"),
                                           경기도고양시=request.POST.get("경기도고양시", "0"),
                                            경기도광주시 = request.POST.get("경기도광주시", "0"),
                                            경기도김포시 =request.POST.get("경기도김포시", "0"),
                                            경기도부천시 = request.POST.get("경기도부천시", "0"),
                                            경기도성남시 =request.POST.get("경기도성남시", "0"),
                                            경기도수원시  =request.POST.get("경기도수원시", "0"),
                                            경기도안양시  =request.POST.get("경기도안양시", "0"),
                                            경기도양평군  =request.POST.get("경기도양평군", "0"),
                                            경기도오산시   =request.POST.get("경기도오산시", "0"),
                                            경기도용인시=request.POST.get("경기도용인시", "0"),
                                            경기도이천시=request.POST.get("경기도이천시", "0"),
                                            경기도파주시 =request.POST.get("경기도파주시", "0"),
                                            서울특별시강남구 =request.POST.get("서울특별시강남구", "0"),
                                            서울특별시강동구 = request.POST.get("서울특별시강동구", "0"),
                                            서울특별시강북구 = request.POST.get("서울특별시강북구", "0"),
                                            서울특별시강서구 =request.POST.get("서울특별시강서구", "0"),
                                            서울특별시구로구 =request.POST.get("서울특별시구로구", "0"),
                                            서울특별시도봉구 = request.POST.get("서울특별시도봉구", "0"),
                                            서울특별시동대문구 =  request.POST.get("서울특별시동대문구", "0"),
                                            서울특별시동작구 =  request.POST.get("서울특별시동작구", "0"),
                                            서울특별시마포구 = request.POST.get("서울특별시마포구", "0"),
                                            서울특별시서대문구 = request.POST.get("서울특별시서대문구", "0"),
                                            서울특별시서초구 = request.POST.get("서울특별시서초구", "0"),
                                            서울특별시성북구 = request.POST.get("서울특별시성북구", "0"),
                                            서울특별시송파구 = request.POST.get("서울특별시송파구", "0"),
                                            서울특별시양천구 = request.POST.get("서울특별시양천구", "0"),
                                            서울특별시영등포구 = request.POST.get("서울특별시영등포구", "0"),
                                            서울특별시용산구 = request.POST.get("서울특별시용산구", "0"),
                                            서울특별시종로구 =request.POST.get("서울특별시종로구", "0"),
                                            서울특별시중구 = request.POST.get("서울특별시중구", "0"),
                    internet =request.POST.get("internet", "0"),
                    TV = request.POST.get("TV", "0"),
                    laundry = request.POST.get("laundry", "0"),
                    Air_Conditioning = request.POST.get("Air_Conditioning", "0"),
                    Fridge = request.POST.get("Fridge", "0"),
                    Hair_dryer = request.POST.get("Hair_dryer", "0"),
                    kitchen_available = request.POST.get("kitchen_available", "0"),
                    Health_club =  request.POST.get("Health_club", "0"),
                    Parking = request.POST.get("Parking", "0"),
                    Garden =request.POST.get("Garden", "0"),
                    Desk_and_Lamp = request.POST.get("Desk_and_Lamp", "0"),
                    smoking_possible = request.POST.get("smoking_possible", "0"),
                    single_room =  request.POST.get("single_room", "0"),
                    double_room =request.POST.get("double_room", "0"),
                    triple_room = request.POST.get("triple_room", "0"),
                    quadruple_room = request.POST.get("quadruple_room", "0"),
                    dorm =request.POST.get("dorm", "0"),
                    #hetero
                    minday =request.POST.get("minday", "0"),
                    maxday =request.POST.get("maxday", "0"),
                    welcome_irrelevant = request.POST.get("welcome_irrelevant", "0"),
                    welcome_males = request.POST.get("welcome_iwelcome_malesrrelevant", "0"),
                    welcome_females = request.POST.get("welcome_females", "0"),
                    welcome_couples = request.POST.get("welcome_couples", "0"),
                    welcome_families = request.POST.get("welcome_families", "0"),
                    welcome_students = request.POST.get("welcome_students", "0"),
                    Computer = request.POST.get("Computer", "0"),
                    Smoke_alarm = request.POST.get("Smoke_alarm", "0"),
                    Dresser_Drawers = request.POST.get("Dresser_Drawers", "0"),
                    Closet_Wardrobe = request.POST.get("Closet_Wardrobe", "0"),
                    Wheelchair_Accessible =request.POST.get("Wheelchair_Accessible", "0"),
                    Barbecue =request.POST.get("Barbecue", "0"),
                    Bikes_for_use=request.POST.get("Bikes_for_use", "0"),
                    Patio=request.POST.get("Patio", "0"),
                    Gym_at_home=request.POST.get("Gym_at_home", "0"),
                    Bedside_Locker_Nightstand=request.POST.get("Bedside_Locker_Nightstand", "0"),
                    Radio=request.POST.get("Radio", "0"),
                    telephone=request.POST.get("telephone", "0"),
                    Carpet_Moquette=request.POST.get("Carpet_Moquette", "0"),
                    fax=request.POST.get("fax", "0"),
                    Mirror=request.POST.get("Mirror", "0"),
                    Shopping_Centre=request.POST.get("Shopping_Centre", "0"),
                    Amusement_Park=request.POST.get("Amusement_Park", "0"),
                    Swimming_Pool=request.POST.get("Swimming_Pool", "0"),
                    Hospital=request.POST.get("Hospital", "0"),
                    Tennis=request.POST.get("Tennis", "0"),
                    Park=request.POST.get("Park", "0"),
                    Gym=request.POST.get("Gym", "0"),
                    Golf=request.POST.get("Golf", "0"),
                    Swimming=request.POST.get("Swimming", "0"),
                    Cinema=request.POST.get("Cinema", "0"),
                    Library=request.POST.get("Library", "0"),
                    Museum=request.POST.get("Museum", "0"),
                    Restaurant=request.POST.get("Restaurant", "0"),
                    Bowling=request.POST.get("Bowling", "0"),
                    Airport=request.POST.get("Airport", "0"),
                    Beach=request.POST.get("Beach", "0"),
                    Fishing=request.POST.get("Fishing", "0"),
                    Sports_arena=request.POST.get("Sports_arena", "0"),
                    subway_station= request.POST.get("subway_station", "0"),
                    vegetarian= request.POST.get("vegetarian", "0"),
                                            경상도= request.POST.get("경상도", "0"),
                                            대구광역시= request.POST.get("대구광역시", "0"),
                                            부산광역시= request.POST.get("부산광역시", "0"),
                                            인천광역시= request.POST.get("인천광역시", "0"),
                                            제주도= request.POST.get("제주도", "0"),
                                            충청북도= request.POST.get("충청북도", "0"),
                                            울산광역시=request.POST.get("울산광역시", "0"),
                    within_a_hour=request.POST.get("within_a_hour", "0"),
                    within_two_hours= request.POST.get("within_two_hours", "0"),
                                            몇_시간_이내= request.POST.get("몇_시간_이내", "0"),
                                            하루_이내= request.POST.get("하루_이내", "0"),
                                            며칠_이내= request.POST.get("며칠_이내", "0"),
                                            강아지= request.POST.get("강아지", "0"),
                                            고양이= request.POST.get("고양이", "0"),
                                            어류= request.POST.get("어류", "0"),
                                            토끼= request.POST.get("토끼", "0"),
                                            햄스터=request.POST.get("햄스터", "0"),
                                            강원도강릉시= request.POST.get("강원도강릉시", "0"),
                                            경기도양주시=request.POST.get("경기도양주시", "0"),
                                            경기도의왕시= request.POST.get("경기도의왕시", "0"),
                                            경상남도창원시= request.POST.get("경상남도창원시", "0"),
                                            경상북도경산시=request.POST.get("경상북도경산시", "0"),
                                            대구광역시동구=request.POST.get("대구광역시동구", "0"),
                                            대구광역시북구= request.POST.get("대구광역시북구", "0"),
                                            부산광역시부산진구=request.POST.get("부산광역시부산진구", "0"),
                                            부산광역시사하구= request.POST.get("부산광역시사하구", "0"),
                                            부산광역시해운대구= request.POST.get("부산광역시해운대구", "0"),
                                            서울특별시노원구= request.POST.get("서울특별시노원구", "0"),
                                            서울특별시중랑구= request.POST.get("서울특별시중랑구", "0"),
                                            울산광역시남구= request.POST.get("울산광역시남구", "0"),
                                            울산광역시중구= request.POST.get("울산광역시중구", "0"),
                                            인천관역시인천= request.POST.get("인천관역시인천", "0"),
                                            인천광역시계양구= request.POST.get("인천광역시계양구", "0"),
                                            인천광역시남동구= request.POST.get("인천광역시남동구", "0"),
                                            인천광역시부평구= request.POST.get("인천광역시부평구", "0"),
                                            인천광역시서구= request.POST.get("인천광역시서구", "0"),
                                            인천광역시연수구= request.POST.get("인천광역시연수구", "0"),
                                            인천광역시중구=request.POST.get("인천광역시중구", "0"),
                                            제주도서귀포시= request.POST.get("제주도서귀포시", "0"),
                                            제주도제주시= request.POST.get("제주도제주시", "0"),
                                            충청북도단양군= request.POST.get("충청북도단양군", "0")                                    
 
#                     welcome_irrelevant=request.POST.get("welcome_irrelevant", "0"),
#                     welcome_males=request.POST.get("welcome_males", "0"),
#                     welcome_couples=request.POST.get("welcome_couples","0"),
#                     welcome_families=request.POST.get("welcome_families", "0"),
#                     internet=request.POST.get("internet", "0"),
#                     kitchen_available=request.POST.get("kitchen_available", "0"),
#                     Parking=request.POST.get("Parking", "0"),
#                     Air_Conditioning=request.POST.get("Air_Conditioning", "0"),
#                     Computer=request.POST.get("Computer", "0"),
#                     Smoke_alarm=request.POST.get("Smoke_alarm", "0"),
#                     Desk_and_Lamp=request.POST.get("Desk_and_Lamp", "0"),
#                     Dresser_Drawers=request.POST.get("Dresser_Drawers", "0"),
#                     Closet_Wardrobe=request.POST.get("Closet_Wardrobe", "0"),
#                     Hair_dryer=request.POST.get("Hair_dryer", "0"),
#                     Garden=request.POST.get("Garden", "0"),
#                     Wheelchair_Accessible=request.POST.get("Wheelchair_Accessible", "0"),
#                     Barbecue=request.POST.get("Barbecue", "0"),
#                     Bikes_for_use=request.POST.get("Bikes_for_use", "0"),
#                     Gym_at_home=request.POST.get("Gym_at_home", "0"),
#                     Bedside_Locker_Nightstand=request.POST.get("Bedside_Locker_Nightstand", "0"),
                
                    )
    dto.save()
             
    return redirect("/product_list")

    


def product_edit(request):
    pid=request.GET["product_id"]
    dto=Product.objects.get(product_id=pid)
    return render_to_response("product_edit.html",{"dto":dto})
#     uid=request.session.get("userid","")
#     if uid=="admin":
#         pid=request.GET["product_id"]
#         dto=Product.objects.get(product_id=pid)
#         return render_to_response("product_edit.html",{"dto":dto})
#     #관리자 계정이 아닌 경우
#     else:
#         return redirect("/login")
 
def detailinfo_edit(request):
    pid=request.GET["id"]
    dto=detailinfo.objects.get(id=pid)
    return render_to_response("detailinfo_edit.html",{"dto":dto})

    
@csrf_exempt    
def product_update(request):
    id=request.POST['product_id']
    dto_src=Product.objects.get(product_id=id)
    p_url = dto_src.picture_url
    if "file1" in request.FILES:
        file=request.FILES["file1"]
        p_url = file._name
        fp=open("%s%s" % (UPLOAD_DIR, p_url), 'wb')
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()
    dto_new = Product( product_id=id,
                       username=request.session["userid"],
                       product_name=request.POST["product_name"],
                       description=request.POST["description"],
                       location= request.POST.get("location", "0"),
                       locate= request.POST.get("locate", "0"),
                       house= request.POST.get("house", "0"), 
                       room= request.POST.get("room", "0"),
                       bed= request.POST.get("bed", "0"),  
                       bathroom= request.POST.get("bathroom", "0"), 
                       pet= request.POST.get("pet", "0"),
                       language= request.POST.get("language", "0"),
                       culture= request.POST.get("culture", "0"),
                       family= request.POST.get("family", "2"),
                       gas= request.POST.get("gas", "1"),       
                       picture_url=p_url )
    dto_new.save()
    return redirect("/product_list")




@csrf_exempt 
def product_delete(request):
    Product.objects.get( product_id=request.POST["product_id"]).delete()
    return redirect("/product_list")



@csrf_exempt
def detail_infowrite(request):
    uid=request.session.get("userid","")
    pid=request.GET.get("product_id")
    print(pid)
    return render_to_response("detail_infowrite.html",{"uid":uid,"pid":pid})


@csrf_exempt    
def detailinfo_insert(request):
    #첨부파일이 있는 경우
    if "file2" in request.FILES:
        file=request.FILES["file2"]
        file_name=file._name
        fp=open("%s%s" % (UPLOAD_DIR, file_name), "wb")
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()
    else:
        file_name="-"
           
    dto = detailinfo(sex=request.POST.get("sex", "no"),
                location=request.POST.get("location", "no"),
                drop1=request.POST.get("drop1", "no"),
                drop2=request.POST.get("drop2", "no"),
                drop3=request.POST.get("drop3", "no"),
                religion=request.POST.get("religion", "no"),
                hobby=request.POST.get("hobby", "no"),               
                languageexchangecount=request.POST.get("languageexchangecount", "no"),
                languageexchangeminute=request.POST.get("languageexchangeminute", "no"),
                file2=file_name,
                language=request.POST.get("language", "no"),
                culture=request.POST.get("culture", "no"),
#                 username=request.POST["username"],
                username=request.POST.get("username", "no"),
                age=request.POST.get("age", "no"),
                travel=request.POST.get("travel", "no"),
                job=request.POST.get("job", "no"),
                gas1=request.POST.get("gas1", "no"),
                client=request.POST.get("client", "no"),
                product_id=request.POST.get("product_id", "no")
            )
    dto.save()
        
    return redirect("/detailinfo_list")


def detailinfo_list(request):
    uid = request.session.get("userid")
    detailinfoList = detailinfo.objects.filter(username=uid)
#     detailinfoList = detailinfo.objects.all()
    return render_to_response("detailinfo_list.html", {"detailinfoList": detailinfoList})

@csrf_exempt
def list(request):
    boardCount = Board.objects.count();
    boardList = Board.objects.all().order_by("-idx")
    return render_to_response("list.html", {"boardList":boardList, "boardCount": boardCount})

def write(request):
    return render_to_response("write.html")

@csrf_exempt
def insert(request):
    fname = ""
    fsize = 0
    if "file" in request.FILES:
        file=request.FILES["file"]
        fname = file._name
        #fsize=os.path.getsize(UPLOAD_DIR+fname)
        #wb :이전파일 쓰기 모드
        fp=open("%s%s" % (UPLOAD_DIR, fname), "wb")
        for chunk in file.chunks():
            fp.writer(chunk)
        fp.close()
        
        #첨부파일의 크기(업로드 완료후 계산하기)
        fsize=os.path.getsize(UPLOAD_DIR+fname)
    dto = Board( writer=request.POST["writer"],
                      title=request.POST["title"],
                      content=request.POST["content"],
                      filename=fname,
                      filesize=fsize )
    dto.save()
    print(dto)
    return redirect("/list")

def download(request):
    id=request.GET['idx']
    dto=Board.objects.get(idx=id)
    path = UPLOAD_DIR+dto.filename
    print("path:", path)
    filename= os.path.basename(path)
    filename= urlquote(filename)
    print("pfilename:" , os.path.basename(path))
    #파일오픈
    with open(path, 'rb') as file:
        response = HttpResponse(file.read(), context_type="applications/octet-stream")
        response["Content-Disposition"] = "attachment; filename*=UTF-8''{0}".format(filename)
        dto.down_up()
        dto.save()
        return response
    
    
def detail(request):
    id=request.GET["idx"]
    dto=Board.objects.get(idx=id)
    dto.hit_up()
    dto.save()
    filesize='%.2f' % (dto.filesize/ 1024)
    commentList=Comment.objects.filter(board_idx=id).order_by("idx")
    return render_to_response("detail.html", {"dto": dto, "filesize":filesize, "commentList":commentList})

@csrf_exempt    
def reply_insert(request):
    id=request.POST["idx"]
    dto=Comment(board_idx=id, writer=request.POST["writer"], content=request.POST["content"])
    dto.save()
    return HttpResponseRedirect("detail?idx="+id)

@csrf_exempt 
def update(request):
    id=request.POST['idx'] 
    dto_src=Board.objects.get(idx=id)
    fname = dto_src.filename
    fsize = dto_src.filesize
    if "file" in request.FILES:
       file=request.FILES["file"]
       fname = file._name
       fp=open("%s%s" % (UPLOAD_DIR, fname), "wb")
       for chunk in file.chunks():
           fp.write(chunk)
       fp.close()
       fsize=os.path.getsize(UPLOAD_DIR+fname)
    dto_new = Board( idx=id, writer=request.POST["writer"],
                     title=request.POST["title"],
                     content=request.POST["content"],
                     filename=fname, filesize=fsize)
    dto_new.save()
    return redirect("/list")
      
      
        
@csrf_exempt   
def delete(request):
    id=request.POST["idx"]
    Board.objects.get(idx=id).delete()
    #시작페이지로 이동
    return redirect("/list")


@csrf_exempt    
def detailinfo_update(request):
    id=request.POST['id']
    dto_src=detailinfo.objects.get(id=id)
    p_url = dto_src.file2
    if "file2" in request.FILES:
        file=request.FILES["file2"]
        p_url = file._name
        fp=open("%s%s" % (UPLOAD_DIR, p_url), 'wb')
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()
    dto_new = detailinfo( id=id,
                       sex=request.POST["sex"],
                       username=request.session["userid"],
                       location=request.POST["location"],
                       drop1=request.POST["drop1"],
                       drop2=request.POST["drop2"],
                       drop3=request.POST["drop3"],
                       languageexchangecount=request.POST["languageexchangecount"],
                       languageexchangeminute=request.POST["languageexchangeminute"],
                       culture=request.POST["culture"],
                       language=request.POST["language"],
                       age=request.POST["age"],
                       travel=request.GET.get("travel"),
                       job=request.POST["job"],
                       gas1=request.POST.get("gas1","1"),
                       religion=request.POST["religion"],
                       hobby=request.POST.get("hobby",""),
                       client=request.POST.get("client","guest"),
                       file2=p_url )
    dto_new.save()
    return redirect("/detailinfo_list")


@csrf_exempt 
def detailinfo_delete(request):
    detailinfo.objects.get( id=request.POST["id"]).delete()
    return redirect("/detailinfo_list")



def price_list(request):
    uid=request.session.get("userid","")
    product_id=request.POST.get("product_id", False)
    real_price=float(request.GET['real_price'])
    min_price=float(request.GET['min_price'])
    max_price=float(request.GET['max_price'])
#     min_price=request.GET.get("min_price")
    print(min_price)
#     max_price=request.GET.get("max_price")
    
    return render_to_response("price_list.html",{"real_price":real_price,"product_id":product_id,"min_price":min_price,"max_price":max_price} )


@csrf_exempt    
def price_update(request):
    uid=request.session.get("userid","")
    real_price = float(request.POST['real_price'])
    id=request.GET["product_id"]
    obj = Product.objects.get(product_id=id)
    obj.real_price = real_price
    obj.save()
    return redirect("/product_list")  




def SEARCH_DISTANCE_URL(search_distance_url_base, start_point, end_point):
    return search_distance_url_base+'&start={}&destination={}'.format(start_point, end_point)

def SEARCH_POINT_URL(mainlocation, q):
    return 'https://m.map.naver.com/apis/search/poi?query='+mainlocation+'&page=1'.format(q)                                                                              
    
def GET_END_POINT(mainlocation, q):
    session = r.Session()
    res = session.get(SEARCH_POINT_URL(mainlocation, q)).text
    res_dict = json.loads(res)
    x = res_dict['result']['address']['list'][0]['x']
    y = res_dict['result']['address']['list'][0]['y']
    name = res_dict['result']['address']['list'][0]['name']
    return '{},{},{}'.format(x, y, name)

def GET_INFO(mainlocation, search_distance_url_base, start, end, kind_of_oil):
    start_point = GET_END_POINT(mainlocation, start)
    end_point = GET_END_POINT(mainlocation, end)
    
    session = r.Session()

    res = session.get(SEARCH_DISTANCE_URL(search_distance_url_base, start_point, end_point=end_point), headers={'User-Agent':'Mozilla/5.0'}).text
    print("RES HEREEEEE", SEARCH_DISTANCE_URL(search_distance_url_base, start_point, end_point=end_point))
    print(SEARCH_DISTANCE_URL(search_distance_url_base, start_point, end_point=end_point))
    print(res)
    res_dict = json.loads(res)
    
    target = res_dict['routes'][0]['summary']
    distance = target['distance']
    sec = target['duration']
    taxi_fare = target['taxi_fare']
    tollgate_fare = target["toll"][0:4]
    gasoline_fare = (distance/1000*1500/12.4)
    diesel_fare = (distance/1000*1400/12.4)
    LPG_fare = (distance/1000*850/12.4)
    
    print('검색완료')
    print('출발지: {}, 도착지: {}'.format(start, end))
    print('예상 이동거리: {}km'.format(distance/1000))
    print('예상 소요시간: {}분'.format(round(sec/60)))
    print('예상 택시요금: {}원'.format(taxi_fare))
    
    if tollgate_fare == "0,0,":
        print("통행료 : 0원")
    else:
        print("통행료 : {}원".format(tollgate_fare))
    print("")
    
    print("예상 휘발유 주유비: {}원".format(round(distance/1000*1500/12.4)))
    print("예상 경유 주유비: {}원".format(round(distance/1000*1400/12.4)))
    print("예상 LPG 주유비: {}원".format(round(distance/1000*850/12.4)))
    print("")
    
    
    #print("Friending culture price: {}원".format(int(taxi_fare)-3800)) #예상택시비에서 기본요금 뺀것

    if tollgate_fare == "0,0,":  #톨비까지 계산
        if kind_of_oil == "1":
            friending_culture_price = 3800+round(gasoline_fare)
            print("Friending culture price2: {}원".format(3800+round(gasoline_fare)))#택시 기본 요금에 휘발유주유비 더한 것
        elif kind_of_oil == "2":
            friending_culture_price = 3800+round(diesel_fare)
            print("Friending culture price2: {}원".format(3800+round(diesel_fare)))#택시 기본 요금에 경유주유비 더한 것
        elif kind_of_oil == "3":
            friending_culture_price = 3800+round(LPG_fare)
            print("Friending culture price2: {}원".format(3800+round(LPG_fare)))#택시 기본 요금에 LPG주유비 더한 것
            
    else:
        if kind_of_oil == "1":
            friending_culture_price = 3800+round(gasoline_fare)+int(tollgate_fare)
            print("Friending culture price2: {}원".format(3800+round(gasoline_fare)+int(tollgate_fare)))#택시 기본 +주유비 + 톨비
        elif kind_of_oil == "2":
            friending_culture_price = 3800+round(diesel_fare)+int(tollgate_fare)
            print("Friending culture price2: {}원".format(3800+round(diesel_fare)+int(tollgate_fare)))#택시 기본 요금에 경유주유비 더한 것
        elif kind_of_oil == "3":
            friending_culture_price = 3800+round(LPG_fare)+int(tollgate_fare)
            print("Friending culture price2: {}원".format(3800+round(LPG_fare)+int(tollgate_fare)))#택시 기본 요금에 LPG주유비 더한 것
    
    return friending_culture_price
    #print("Friending culture price3: {}원".format()  #

def culture1(request):
    
    uid= request.session.get("userid","")
    nom = Nominatim()
    pid=request.GET["pid"]
    location_list= Product.objects.filter(product_id = pid).values()
    print("TIRED",location_list)
    location = []
    destination_list= Cart.objects.filter(userid = uid).values()
    print("TIRED",destination_list)
    destination = []
    gas_list=detailinfo.objects.filter(username = uid).values()
    gas = []
    
#     try:
    for a,b in location_list[0].items():
        location.append(b)    
    mainlocation = location[10]
    print(mainlocation)
    start = location[9]
    print(start)
    startgeocode = nom.geocode(start)
    startlat = str(startgeocode.latitude)
    startlng = str(startgeocode.longitude)
    
    for c,d in destination_list[0].items():
        destination.append(d)    
    end = destination[4]
    endgeocode = nom.geocode(end)
    endlat = str(endgeocode.latitude)       
    endlng = str(endgeocode.longitude)
    
    for e,f in gas_list[0].items():
        gas.append(f)    
    kind_of_oil = gas[15]
                                                                      
    search_distance_url_base = "https://map.naver.com/spirra/findCarRoute.nhn?route=route3&output=json&result=web3&coord_type=naver&search=2&car=0&mileage=12.4&start=" +startlng+ "," +startlat+","+start+"&destination="+endlng+ ","+endlat+","+end
    
    GET_INFO(mainlocation, search_distance_url_base, start, end, kind_of_oil)
    
#     except Exception as e:
#         print("error") 
#         print(e)                 
          
    return redirect("/test",{"mainlocation":mainlocation, "start":start,"end":end,"kind_of_oil":kind_of_oil})       
#     return redirect("/test",{"mainlocation":mainlocation, "start":start,"end":end,"kind_of_oil":kind_of_oil}) 


def test1(request): 
    uid = request.session.get("userid")
    
    productList = Product.objects.filter(username=uid)
    return render_to_response("test1.html")



from operator import itemgetter



def detailinfo_matching(request):
    uid = request.session.get("userid")
#     detailinfoList = detailinfo.objects.all()  
    GuestList = detailinfo.objects.filter(username=uid)
    Guestinfo= detailinfo.objects.filter(username = uid).values()
    guestlanguage1 = Guestinfo.values_list('username','drop1','drop2','drop3','hobby','religion')
    print('aaaa',guestlanguage1)
    kk=()
    for j in guestlanguage1:
        print(j)
        kk=j
    print("j2",j)
    print("kk",kk)
    allGuestinfo=[]
    
    for k,v in Guestinfo[0].items():
        allGuestinfo.append(v)     
    guest_language = allGuestinfo[3:6]
#     guest_language = Guestinfo.values_list('drop1','drop2','drop3')
#     a=list(guest_language.values())
#     print(a)
    print(guest_language)
    
    host_list = detailinfo.objects.filter(client="host").values()
    host_info=[]
#     print(host_list)   
    host_language = host_list.values_list('username','drop1','drop2','drop3','hobby','religion')
#     b= host_language.values()
#     print(b)
#         
    a=len(host_language)

    match=0
    d=[]
    for i in host_language:
        match=0
        print(i)
        intersection = set(i) & set(kk)
        print(intersection)
        if len(intersection) != 0:
            match = len(intersection)
        score=match/(len(i)-1)
        
        if (score >= 0.4):
            c=i[0]
            
#             for c in host_language:
            info = {
                'host': c,
                'score': score
                }
            d.append(info)
#     
#             print(c)
   
    print(d) 
    print(match)
    print(score)
    
    d = sorted(d, key=itemgetter('score'), reverse=True)
    return render_to_response("detailinfo_matching.html",{"GuestList":GuestList,"d":d }) 
    



    

   
