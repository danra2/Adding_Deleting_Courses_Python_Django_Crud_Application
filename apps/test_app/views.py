from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from . models import Courses

def index(request):
    context = {
    "Courses" : Courses.objects.all()
    }
    return render(request, "test_app/index.html", context)

def courses(request):
    Courses.objects.create(course_name=request.POST['classname'], description=request.POST['description'])
    context = {
    "Courses" : Courses.objects.all()
    }
    print 'chocolate'
    return redirect ('/', context)

def confirm(request, id):
    context = {
    "Courses" : Courses.objects.filter(id=id)
    }
    return render(request, 'test_app/confirm.html', context)

def delete(request, id):
    Courses.objects.get(id=id).delete()
    return redirect('/')

def goback(request):
    return redirect('/')



# def blogs(request):
#     #using ORM
#     print request.POST
#     #Blog is the name of the table referred to within models
#     # You are referring to the title from the table, it's a column a table.
#     #So title is a column within table, = the input within the html form.
#     # So .POST['title'] , title
#     Blog.objects.create(title=request.POST['title'], blog=request.POST['blog'])
#     #insert into blogs(title,blog, created_at, updated_at) values (title,blog, now(), now())
#     return redirect('/')
#
# def comments(request, id):
#     blog = Blog.objects.get(id=id)
#     # 2nd parameter is within the route, and that ID is related to the id in cyan, and the id = in orange within the .get is a paramenter, don't worry about that.
#     #Blog contains the action figure, the action figure ID has a generated ID which protarys which order it was created in, the attributes you fill out in a form, create a new contact, and that contact
#     Comment.objects.create(comment=request.POST['comment'], blog=blog)
#     return redirect('/')
