from django.shortcuts import render_to_response

# Create your views here.

from django.http import HttpResponse

def index(req, id):
    hello = 'helloworlder'
    #return HttpResponse('<h1>helloworld!</h1>')
    return render_to_response('index.html',{'hello':hello, 'tid':id})
