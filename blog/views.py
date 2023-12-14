from django.shortcuts import render
# from django.http import HttpResponse

posts = [
    {
        'author': 'James Etole',
        'title': 'My First Blog Post',
        'content': 'A smooth refresher on the new components of Django(Part 1)',
        'date_posted': 'December 1, 2023' 
    },
    {
        'author': 'Anne Wamaitha',
        'title': 'My Trip to Paris',
        'content': 'The best thing that has ever happened in my life',
        'date_posted': 'December 2, 2023' 
    },
    {
        'author': 'James Etole',
        'title': 'My Second Blog Post',
        'content': 'A smooth refresher on the new components of Django(Part 2)',
        'date_posted': 'December 3, 2023' 
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', { 'title': 'About'})

#Example with HttpResponse
# def about(request):
#     return HttpResponse("<h1>Jemmo's About Page</h1>")
