from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import CourseModelForm
from .models import Course
# BASED VIEW CLASS = VIEW

#  A mixin allows us to extend a class-based view with some new code
class CourseObjectMixin(object):
    model = Course
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj =get_object_or_404(self.model, id=id)
        return obj

class CourseDeleteView(CourseObjectMixin, View):
    template_name = "courses/course_delete.html" 
    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context) 

    def post(self, request, id=None, *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
           obj.delete()
           context['object'] = None
           return redirect('/courses/')
        return render(request, self.template_name, context)


class CourseUpdateView(CourseObjectMixin, View): 
    template_name = "courses/course_update.html"
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id=id)
           
        return obj

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context) 

    def post(self, request, *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context) 
        
# When you create sth yo need to accept two methods: GET & POST 
# we can reduce the amount of code we have by creating our own mixin
class CourseCreateView(View):
    template_name = "courses/course_create.html" 
    def get(self, request, *args, **kwargs):
        # GET method
        form = CourseModelForm()
        context = {"form" : form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POST method
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm() # limpia el form
        context = {"form" : form}
        return render(request, self.template_name, context)

class CourseListView(View):
    template_name = 'Courses/course_list.html'
    queryset = Course.objects.all()

    def get_quesryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)

class CourseView(CourseObjectMixin, View):
    template_name = "courses/course_detail.html" # DetailView

    def get(self, request, id=None, *args, **kwargs):
        # id=None means the id is no longer required
        # GET method
        context = {'object':self.get_object()}
        return render(request, self.template_name, context)

    # def post(request, *args, **kwargs):
    #     return render(request, 'about.html', {})

# Http methods
# This is a standard funcion based view. All it does is render a template
def my_fbv(request, *args, **kwargs):
    return render(request, 'about.html', {})
