from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse


def test_view(request):
    a = request.GET.get("a", None)
    b = request.GET.get("b", None)

    if b is None:
        return JsonResponse(
            {
                "error_code": "1",
                "error_message": "Parameter 'b' is missing",
                "reference": "None",
            }
        )

    response_data = {"error_code": "0", "error_message": "success", "reference": "111"}

    return JsonResponse(response_data)
