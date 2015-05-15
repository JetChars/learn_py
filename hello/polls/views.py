from django.shortcuts import render_to_response
from django.http import HttpResponse
import os, sys, subprocess
# Create your views here.


def index(req, id):
    hello = 'helloworlder'
    #return HttpResponse('<h1>helloworld!</h1>')
    os.system('pwd > /Users/JetChars/github/learn_py/hello/test.txt')
    p = subprocess.Popen('for i in `ls`; do [[ -d $i ]]&&echo $i;done', stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    return render_to_response('index.html',{'hello':hello, 'tid':output, 'output':output.split()})
    
