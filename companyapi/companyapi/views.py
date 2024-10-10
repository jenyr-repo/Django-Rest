from django.http import HttpResponse,JsonResponse
def home_page(request):
    print(" home page requested")
    return HttpResponse("This is the Home Page")

def friend_page(request):
    friends=[
        'ankit',
        'joseph',
        'salim'
    ]
    return JsonResponse(friends,safe=False)