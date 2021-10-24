from django.http import JsonResponse


def choose_flight(request):
    return JsonResponse(True)


def get_flight_info(request):
    data = request.body.decode()

    flight_info = {
        "from": "start",
        "to": "destinacija",
        "date": "datum",
        "time": "vrijeme",
        "price": "pare"
    }

    return JsonResponse(flight_info)
