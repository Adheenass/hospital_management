from rest_framework.decorators import api_view
from rest_framework.response import Response



from .models import person
from home.serializers import peopleserializer


@api_view(['GET' , 'POST'  , 'PUT'])
def index(request):
    courses = {
        'course-name' : 'python',
        'learn' : ['flask' , 'django' , 'tornado','fastapi'],
        'course_provider' : 'scaler'
        }
    # return Response(courses)
    if request.method == 'GET':
        print(request.GET.get('search'))
        print('YOU HIT A GET METHOD')
        return Response(courses)
    elif request.method == 'POST':
        data = request.data
        print('**********')
        print(data)
        print(data['name'])
        print('**********')
        print('YOU HIT A POST METHOD')
        return Response(courses)
    elif request.method == 'PUT':
        print('YOU HIT A PUT METHOD')
        return Response(courses)




@api_view(['GET', 'POST'])
def person(request):
    if request.method == 'GET':
        objs = person.objects.all()
        serializer = peopleserializer(objs, many = True)
        return Response(serializer.data)
    else:
        data = request.data
        serializer = peopleserializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)