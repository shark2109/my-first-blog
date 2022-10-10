from django.http import HttpResponse


def index(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/polls">pollsへ移動</a><br><a href="http://127.0.0.1:8000/admin">管理サイト</a>')

#<br><a href="http://127.0.0.1:8000/worker_list/">managerへ移動</a>