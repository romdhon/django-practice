from django.shortcuts import render
import sqlite3
from myapp.forms import User

# Create your views here.
def home(request):
    with sqlite3.connect('db.sqlite') as con:
        con.row_factory = sqlite3.Row
        cmd = 'select * from person'
        data = con.execute(cmd)
        dict_data = {'insert':data}    
    return render(request, "home.html", context=dict_data)

def help(request):

    if request.method == 'POST':
        user = User(request.POST)

        if user.is_valid():
            print('Name: '+user.cleaned_data['name'])
            print('Email: '+user.cleaned_data['email'])
            print('URL: '+user.cleaned_data['url'])
            user.save(commit=True)
            return home(request)
        else:
            print('Error: Invalid Form')
    else:
        user = User()
    return render(request, 'myapp/help.html', context={'user':user})