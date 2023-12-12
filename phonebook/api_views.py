from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
from . import serializers

@csrf_exempt
def persone_list(request):
    if request.method == 'GET':
        persons = models.Persone.objects.all()
        serializers = serializers.PersoneSerializers(persons, many=True)
        return JsonResponse(serializers.data, safe=False)
    elif request.method == 'POST':
        persone = request.POST
        serializers = serializers.PersoneSerializers(data=persone)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data, status=201)
