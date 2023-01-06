# Задание 1. tech support.py

from django.http import JsonResponse
from tech_support.models import Statistic


def statistics(request):
    support_calls = Statistic.objects.all()
    response = []
    for statistic in support_calls:
        response.append({
            "id": statistic.id,
            "author": statistic.author,
            "day": statistic.day,
            "store": statistic.store,
            "reason": statistic.reason,
            "status": statistic.status,
            "timestamp": statistic.timestamp,
        })
    return JsonResponse(response, safe=False)




