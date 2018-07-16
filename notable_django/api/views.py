# Create your views here.
import os
from django.shortcuts import render
from django.http import HttpResponse
from api.models import Profile
from api.forms import ProfileForm
from django.conf import settings
import api.clean_method as cm

# Create your views here.


def hello(request):
   # text = """<h1>welcome to my app !</h1>"""
   # return HttpResponse(text)
   return render(request, "/home/arv/notable_django/api/try2.html", {})

def cal(request):
    print ("Hello")
    return HttpResponse(" hgy")

def hel(request):
	if request.method == "POST":
		print("username", request.POST.get("first_name"))

	return HttpResponse("dgfnkd gf")	

def handle_uploaded_file(f):
    with open('/home/arv/Desktop/media', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def perform_comparison():
	os.system("spark-submit parallel.py")
	return HttpResponse("kuch toh hua")



def upload_file(request):
	if request.method == "POST":
		# save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', request.FILES['picture'])
		# path = default_storage.save(save_path, request.FILES['picture'])
		# return default_storage.path(path)
		MyProfileform = ProfileForm(request.POST,request.FILES)
		print(MyProfileform.is_valid())
		if MyProfileform.is_valid():
			print("yes")
			#handle_uploaded_file(request.FILES)
			
			profile = Profile()
			profile.name = MyProfileform.cleaned_data["name"]
			profile.picture = MyProfileform.cleaned_data["picture"]
			profile.save()
			saved = True
			cm.main(profile.picture)
			perform_comparison()
	else:
		MyProfileform = ProfileForm()
	return HttpResponse(" hdvdgdggy")		


