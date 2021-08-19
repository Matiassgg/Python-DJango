import datetime
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("Buenass con django")


def get_sum(request):
    valor_a = 1
    valor_b = 1
    return HttpResponse(f"Resultado: {valor_a + valor_b}")


def get_date(request):

    actual_date = datetime.datetime.now()
    documento_html = f"""
    <body>
        <bold>
            <h3>
                Fecha y hora : {actual_date}
            <h3>
        <bold>
    <body>
    """
    return HttpResponse(documento_html)


def get_future_age(request, age, year):
    actual_age = age
    periodo = year - 2021
    documento_html = f"""
    <body>
        <bold>
            <h3>
                Tu edad para el año {year} sera de {actual_age + periodo}
            <h3>
        <bold>
    <body>
    """
    return HttpResponse(documento_html)
