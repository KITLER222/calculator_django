from django.shortcuts import render
from .models import Example


def home(request):
    res = ""

    if request.method == "POST":
        expr = request.POST.get("expr")

        try:
            res = eval(expr)
            Example.objects.create(text=expr, result=res)
        except:
            res = "Ошибка"

    history = Example.objects.all()

    return render(request, "home.html", {
        "result": res,
        "history": history
    })