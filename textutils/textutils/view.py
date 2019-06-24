from django.http import HttpResponse

def index(request):
    return HttpResponse('''<h1>Abhishek<br></h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Django code with harry</a><br>
    
     <a href="https://www.facebook.com/">Facebook</a>''')