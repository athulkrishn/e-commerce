from django.shortcuts import render

from crm.models import Review,Product

from crm.forms import AddReview,Addproduct

from django.views.generic import View

class NewReview(View):

    def get(self,request):

        form=AddReview

        return render(request,"addreview.html",{"form":form})
    
    def post(self,request):
        
        form=AddReview(request.POST)

        if form.is_valid():

            Review.objects.create(**form.cleaned_data)

        return render(request,"addreview.html",{"form":form})
    


class NewProduct(View):

    def get(self,request):

        form=Addproduct

        return render(request,"addproduct.html",{"form":form})
    
    def post(self,request):

        form=Addproduct(request.POST)

        if form.is_valid():

            Product.objects.create(**form.cleaned_data)
        
        return render(request,"addproduct.html",{"form":form})
    

class AllReview(View):

    def get(self,request):

        data=Review.objects.all()

        return render(request,"view.html",{"data":data})
    
class DeleteReview(View):

    def get(self,request,**kwargs):

        id=kwargs.get('pk')

        Review.objects.get(id=id).delete()

        return render(request,"index.html")
    

class AvgRating(View):

    def get(self,request):

        data=Product.objects.all()

        return render(request,"avgrating.html",{"data":data})

