from django.shortcuts import render
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
