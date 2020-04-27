import json

from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from main.models import User, Twit


@csrf_exempt
def twit_list(request):
    if request.method == 'GET':
        twits = Twit.objects.all()
        twits_json = [c.to_json() for c in twits]
        return JsonResponse(twits_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        twits = Twit.objects.create(name=data.get('name'))
        return JsonResponse(twits.to_json())

@csrf_exempt
class TwitList(View):
     def get(self, request):
         twits = Twit.objects.all()
         twits_json = [c.to_json() for c in twits]
         return JsonResponse(twits_json, safe=False)

     def post(self, request):
         data = json.loads(request.body)
         twits = Twit.objects.create(name=data.get('name'))
         return JsonResponse(twits.to_json)

@csrf_exempt
def twit_detail(request, twit_id):
    try:
        twit = Twit.objects.get(id=twit_id)
    except Twit.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(twit.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        twit.name = data.get('name', twit.name)
        twit.save()
        return JsonResponse(twit.to_json())
    elif request.method == 'DELETE':
        twit.delete()
        return JsonResponse({'deleted': True})


@csrf_exempt
class TwitDetails(View):
    def get(self, request, twit_id):
        try:
            twit = Twit.objects.get(id=twit_id)
            return JsonResponse(twit.to_json())
        except User.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

    def put(self, request, twit_id):
        try:
            twit = Twit.objects.get(id=twit_id)
            data = json.loads(request.body)
            twit.name = data.get('name', twit.name)
            twit.save()
            return JsonResponse(twit.to_json())
        except User.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

    def delete(self, request, twit_id):
        try:
            twit = Twit.objects.get(id=twit_id)
            twit.delete()
            return JsonResponse({'deleted': True})
        except User.DoesNotExist as e:
            return JsonResponse({'error': str(e)})


@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        users_json = [c.to_json() for c in users]
        return JsonResponse(users_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        users = User.objects.create(name=data.get('name'))
        return JsonResponse(users.to_json())


@csrf_exempt
class UserList(View):
    def get(self, request):
        users = User.objects.all()
        users_json = [c.to_json() for c in users]
        return JsonResponse(users_json, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        users = User.objects.create(name=data.get('name'))
        return JsonResponse(users.to_json)


@csrf_exempt
def user_detail(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(user.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        user.name = data.get('name', user.name)
        user.save()
        return JsonResponse(user.to_json())
    elif request.method == 'DELETE':
        user.delete()
        return JsonResponse({'deleted': True})


@csrf_exempt
class UserDetails(View):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            return JsonResponse(user.to_json())
        except User.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

    def put(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            data = json.loads(request.body)
            user.name = data.get('name', user.name)
            user.save()
            return JsonResponse(user.to_json())
        except User.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

    def delete(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return JsonResponse({'deleted': True})
        except User.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

