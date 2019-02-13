from django.http import HttpResponse
from django.shortcuts import render # this is here by default

# Create your views here.
def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs) # print the arguments, refresh django server page and see the terminal
    print(request.user) # you can request a user for authentication, loggin in your users, how your views can access that
    # see the users (in the terminal) that are logged in
    # if you open the page in incognito google, the user is anonymous user, it is somebody that is not actually logged in
    # return HttpResponse("<h1>Hello World</h1>") # This is not html, it is a string of HTML code
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact Page</h1>")
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "title" : "abc This is about me",
        "this_is_true" : True,
        "my_number" : 123,
        "my_list" : [456,789, 0, 123, "abc"],
        "my_html" : "<h1>Hello World</h1>"
    }
    return render(request, "about.html", my_context)
    
def social_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Social Page</h1>")
    return render(request, "social.html", {})