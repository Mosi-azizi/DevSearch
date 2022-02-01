from django.http import  JsonResponse


def getRoutes(request):
    routes = [
        {'GET': 'api/projects'},
        {'GET': 'api/projects/id'},
        {'Get': 'api/projects/id/vote'},

        {'GET': 'api/users/token'},
        {'GET': 'api/users/token/refresh'}
    ]
    return JsonResponse(routes, safe=False)