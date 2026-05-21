from django.shortcuts import render, redirect
from .models import Example, CalculatorSession


def get_current_session(request):
    if not request.session.session_key:
        request.session.create()

    session_key = request.session.session_key

    calculator_session, created = CalculatorSession.objects.get_or_create(
        session_key=session_key
    )

    return calculator_session


def home(request):
    result = ""
    calculator_session = get_current_session(request)

    if request.method == "POST":
        expr = request.POST.get("expr")

        try:
            result = eval(expr)

            Example.objects.create(
                text=expr,
                result=str(result),
                session=calculator_session
            )

        except:
            result = "Ошибка"

    return render(request, "calc/home.html", {
        "result": result
    })


def history_page(request):
    calculator_session = get_current_session(request)

    history = Example.objects.filter(
        session=calculator_session
    )

    return render(request, "calc/history.html", {
        "history": history
    })


def about_page(request):
    return render(request, "calc/about.html")


def clear_history(request):
    calculator_session = get_current_session(request)

    Example.objects.filter(
        session=calculator_session
    ).delete()

    return redirect("history")