from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log user in with help of from django.contrib.auth import login
            
            login(request, user)
            return redirect('articles:article_list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) #valiation of the user data
        if form.is_valid():
            #log in user 
            user = form.get_user()
            login(request, user)
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            #return redirect(request.POST["next"])
            else:
                return redirect('articles:article_list')
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form':form})


def logout_view(request):
    #post request to log out
    if request.method == 'POST':
        logout(request)
        return redirect('articles:article_list')
        

        
        
        
    