from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as loginUser, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from keyapp.forms import BookForm
from keyapp.models import Book
from django.contrib.auth.decorators import login_required


@login_required(login_url='login') # Django login required function used to secure views
def home(req):
    if req.user.is_authenticated:
        user = req.user
        form = BookForm()
        books = Book.objects.filter(user=user)
        return render(req, 'home.html', {'form': form, 'books': books})


def login(req):
    if req.method == 'GET':
        form1 = AuthenticationForm()
        return render(req, 'login.html', {"form": form1})
    else:
        form = AuthenticationForm(data=req.POST)
        # print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                loginUser(req, user)
                return redirect('home')
        else:
            return render(req, 'login.html', {"form": form})


def signup(req):
    if req.method == 'GET':
        form = UserCreationForm()
        return render(req, 'signup.html', {"form": form})
    else:
        print(req.POST)
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            # print(user)
            if user is not None:
                return redirect('/login/')
        else:
            return render(req, 'signup.html', {"form": form})


@login_required(login_url='login')
def add_book(req):
    if req.user.is_authenticated:
        user = req.user
        # print(user)
        form = BookForm(req.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            book = form.save(commit=False)
            book.user = user
            book.save()
            # print(book)
            return redirect("home")
        else:
            return render(req, 'home.html', {'form': form})


def delete_book(req, id):
    # print(id)
    Book.objects.get(pk=id).delete()
    return redirect('home')


def change_book(req, id):
    book = Book.objects.get(pk=id)
    book.save()
    return redirect('home')


def Signout(req):
    logout(req)
    return redirect('login')


def StudentView(req):
    books = Book.objects.all()
    return render(req, 'library.html', {'books': books})
