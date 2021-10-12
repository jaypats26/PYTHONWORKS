from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse

from .models import Posts
# Create your views here.
def index(request):
    return render(request, "posts/index.html")

def posts(request):
    # Get start and end points
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))

    posts=Posts.objects.order_by('id')[start:end].all()
    sendpost=[]
    for post in posts:
    	abc={
		"id":post.id,
		"title":post.title,
		"shortdesc":post.shortdesc,
        "imageurl":post.image.url
		}
    	sendpost.append(abc)
    # Generate list of posts
    # Return list of posts
    return JsonResponse({
        "posts": sendpost
    })

def detailposts(request):
	postid = int(request.GET.get("postid") or 0)
	post=Posts.objects.get(pk=postid)
	return render(request,"posts/detpost.html",{
		"post":post,
        "imageurl":post.image.url
		})



# def flight(request,flight_id):
# 	flight=Flight.objects.get(pk=flight_id)
# 	return render(request,"flights/flight.html",{
# 		"flight":flight,
# 		"Passengers":flight.Passengers.all(),
# 		"non_passengers":Passenger.objects.exclude(flights=flight).all()
# 		})	
# def book(request,flight_id):
# 	if request.method=="POST":
# 		flight = Flight.objects.get(pk=flight_id)
# 		passenger=Passenger.objects.get(pk=int(request.POST["passenger"]))
# 		passenger.flights.add(flight)
# 		return HttpResponseRedirect(reverse("flights:flight", args=(flight_id,)))
