from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import *
from django.db import connection

def get_user(username, password):
    with connection.cursor() as cursor:
        query = "SELECT * FROM vuln_user WHERE username = ? AND password = ?"
        try:
            cursor.execute(query,(username,password))
            obj = cursor.fetchall()
        except:
            return 0
    if len(obj) == 0:
        return 0
    else:
        return 1

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        res = get_user(username,password)
        if res == 0:
            return JsonResponse({"message":"wrong username or password"})
        else:
            if username == 'admin':
                if res == 1:
                    return render(request,"admin.html")
            else:
                if res == 1:
                    return render(request,"profile.html")
    return render(request,"login.html")


def comment_view(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        content = request.POST.get('content')
        if author and content:
            Comment.objects.create(author=author, content=content)
            return redirect('comment_view')  # Redirect to avoid form resubmission
    comments = Comment.objects.all()
    return render(request, 'comments.html', {'comments': comments})

def delete(request):
    Comment.objects.all().delete()
    return redirect('comment_view')


from django.http import HttpResponse

def set_test_cookie(request):
    response = HttpResponse("Setting a test cookie.")
    response.set_cookie('test_cookie', 'secured_cookie_you_never_now_this', max_age=3600)  # Cookie expires after 1 hour
    return response

'''
def get_user(username,password):
    obj = user.objects.filter(username=username,password=password)
    print(obj)
    # obj is equivalant to select * from user where username = ${username} and password = ${password}
    if len(obj) == 0:
        return 0
    else:
        return 1
'''




'''
def get_user(username):
    obj = user.objects.filter(username=username)
    # obj is equivalant to select * from user where username = ${username}
    if len(obj) == 0:
        return (0,"user not found")
    else:
        user_pass = obj[0].password
        return (1,user_pass)

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        res = get_user(username)
        if res[0] == 0:
            return JsonResponse({"message":res[1]})
        else:
            if username == 'admin':
                if password == res[1]:
                    return render(request,"admin.html")
            else:
                if password == res[1]:
                    return render(request,"profile.html")
    return render(request,"login.html")


'''





# Create your views here.

admin_password = "Ensias@2024_is_secured"

def check_admin(request,passw):
    #print("ugdvfbwejfwejfewjhb")
    if len(passw) != len(admin_password):

        return JsonResponse({"message" : "invalid length"})
    else:
        for i in range(len(passw)):
            if passw[i] != admin_password[i]:
                return JsonResponse({"message" : "invalid password index : " + str(i) })
        return render(request,"admin.html")
