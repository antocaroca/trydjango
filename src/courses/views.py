from django.shortcuts import render
from django.views import View

# BASED VIEW CLASS = VIEW

class CourseView(View):
    template_name = "about.html"
    def get(self, request, *args, **kwargs):
        # GET method
        return render(request, self.template_name, {})

    # def post(request, *args, **kwargs):
    #     return render(request, 'about.html', {})

# Http methods
def my_fbv(request, *args, **kwargs):
    return render(request, 'about.html', {})
