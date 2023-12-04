from django.shortcuts import render

from django.views.generic import View
import math
# Create your views here.

class HelloWorldView(View):
    def get(self,request,*args,**kwargs):
        print("Hello World")
        return render(request,"helloworld.html")
    

class GoodMorningView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"gm.html")
    
class AfternoonView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"an.html")
    
    
class AddView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"add.html")
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)+int(n2)
        print (result)
        return render(request,"add.html",{"out":result})

    

    
class MultiplicationView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"multiplication.html")
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)*int(n2)
        print(result)
        return render(request,"multiplication.html",{"out":result})

    
class DivisionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"div.html")
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)/int(n2)
        print(result)
        return render(request,"div.html",{"out":result})
    
class SubtractionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"sub.html")
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)-int(n2)
        print(result)
        return render(request,"sub.html",{"out":result})
    
class CubeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"cube.html")
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num")
        result=int(n1)**3
        print (result)
        return render(request,"cube.html",{"out":result})
    
class FactorialView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"fact.html")
    
    def post(self,request,*args,**kwargs):
        n=request.POST.get("num")
        n=int(n)
        i=0
        fact=1
        for i in range(1,(n+1),1):
            fact=fact*i
        print(f"Factorial of {n} is {fact}")
        return render(request,"fact.html",{"out":fact})
    
class LeapYearView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"leapyear.html")
    
    def post(self,request,*args,**kwargs):
        year=request.POST.get("year")
        year=int(year)
        if (year%4 ==0 and year%100 !=0) or (year%400==0):
            result=(f"{year} is leap year")
        else:
            result=(f"{year} is not leap year")
        return render(request,"leapyear.html",{"out":result})
    
class OddEvenView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"oddeven.html")
    
    def post(self,request,*args,**kwargs):
        n=request.POST.get("num")
        n=int(n)
        if(n%2==0):
            result=(f"{n} is Even number")
        else:
            result=(f"{n} is odd number")
        return render(request,"oddeven.html",{"out":result})

    
class PrimeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"prime.html")
    def post(self,request,*args,**kwargs):
        n=request.POST.get("num")
        n=int(n)
        is_prime=True
        for i in range(2,n):
            if (n%i==0):
                is_prime=False
            break
        print(is_prime)
        if(is_prime==True):
            result=(f"{n} is prime number")
        else:
            result=(f"{n} is not prime number")
        return render(request,"prime.html",{"out":result})
    

class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")
    
class BmiView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"bmi.html")
    
    def post(self,request,*args,**kwargs):
        weight=int(request.POST.get("weight"))
        height=int(request.POST.get("height"))
        height_m=int(height)/100
        bmi=int(weight)/(height_m**2)
        bmi=round(bmi,2)
        if (bmi<18.5):
            result=("Under weight")
        elif(18.5<= bmi <=24.9):
            result=("Normal weight")
        elif(25.0<= bmi <=29.9):
            result=("Overweight")
        elif(30.0<=bmi<=34.9):
            result=("Obesity (Class I)")
        elif(35.0<=bmi<=39.9):
            result=("Obesity (Class II)")
        elif bmi>40.0:
            result=("Obesity (Class III)")
        return render(request,"bmi.html",{"bmi":bmi,
                                          "result":result})
    

class EmiView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"emi.html")
    
    def post(self,request,*args,**kwargs):
        p=int(request.POST.get("amount"))
        r=int(request.POST.get("interest"))
        n=int(request.POST.get("tenure"))

        r=(r/100)/12
        n=n*12
        emi=p*r*(1+r)**n/((1+r)**n-1)
        emi=round(emi,0)
        total_payable_amount=emi*n
        interest=total_payable_amount-p
        return render(request,"emi.html",{"emi":emi,
                                          "interest":interest,
                                          "total":total_payable_amount})