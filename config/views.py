from django.http import JsonResponse


def healthcheck_view(request):
    return JsonResponse({"status": "ok"})
