from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Reviews, Quries
# Create your views here.
@login_required(login_url='login')
def searchQuery(request):
	if request.method == 'POST':
		if request.POST.get('query'):
			query = request.POST.get('query')
			reviews = Reviews.objects.raw(query)
			context = {
				'reviews':reviews,
				'searchQuery':query			
			}
			return render(request,"SearchApp/home.html",context)
		elif request.POST.get('searchByFilterQuery'):
			query = request.POST.get('searchByFilterQuery')
			reviews = Reviews.objects.raw(query)
			context = {
				'reviews':reviews,
				'searchQuery':query			
			}
			return render(request,"SearchApp/home.html",context)
	reviews = Reviews.objects.all()
	context = {
			'reviews':reviews
		}
	return render(request,"SearchApp/home.html",context)

# SELECT * From searchapp_reviews WHERE pillar="pillar1"
# SELECT * From searchapp_reviews WHERE pillar="pillar1" AND Market = "Market1"

# SELECT * From searchapp_reviews WHERE created_at BETWEEN '2022-01-05' AND '2022-01-06'

@login_required(login_url='login')
def saveQuery(request):
	if request.method == 'POST':
		query = request.POST.get('saveQuery')
		q = Quries(user=request.user, query=query, name=request.POST.get('queryName'))
		q.save()
	quries = Quries.objects.filter(user=request.user)
	context = {
			'quries':quries
		}
	return render(request,"SearchApp/listOfQueries.html",context)

@login_required(login_url='login')
def editQuery(request, pk):
	q = Quries.objects.get(id=pk)
	reviews = Reviews.objects.raw(q.query)
	context = {
		'reviews':reviews,
		'searchQuery':q.query,
		'searchQueryID':q.id		
	}
	return render(request,"SearchApp/editQuery.html",context)

@login_required(login_url='login')
def update(request):
	if request.method == 'POST':
		query = request.POST.get('query')
		queryID = request.POST.get('queryID')
		q = Quries.objects.get(id=queryID)
		q.query = query
		q.save()
		return redirect('saveQuery')
