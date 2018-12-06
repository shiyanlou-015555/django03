from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import render
class Person(object):
    def __init__(self,username,age):
        self.username = username
        self.age = age
def index(request):
    #html = render_to_string("index.html")
    #return HttpResponse(html)
    #
    contex = {
        'person' : {
            'username':112233

        }
    }
    return render(request,"index.html",context=contex)