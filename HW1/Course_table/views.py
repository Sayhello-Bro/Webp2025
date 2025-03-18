#from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.core.serializers.json import DjangoJSONEncoder
import json
import logging

from .models import Course_table_Post
logger = logging.getLogger('django')
@api_view(['GET'])
def add_post(request):
    department = request.GET.get('department', '')
    coursetitle = request.GET.get('coursetitle', '')
    instructor = request.GET.get('instructor', '')

    new_post = Course_table_Post()
    new_post.department = department
    new_post.coursetitle = coursetitle
    new_post.instructor = instructor
    new_post.save()
    logger.debug(" ************** myhello_api: " + department)
    if (department and coursetitle and instructor):
        return Response({"data": department + coursetitle + instructor + " insert!"}, status = status.HTTP_200_OK)
    else:
        return Response(
            {"res": "parameter: name is None"},
            status = status.HTTP_400_BAD_REQUEST
        )
@api_view(['GET'])
def list_post(request):
    posts = Course_table_Post.objects.all().values()
    return JsonResponse(list(posts), safe = False)
#    return Response({"data":
#    json.dumps(
#        list(posts),
#        sort_keys = True,
#        indent = 1,
#        cls = DjangoJSONEncoder)},
#        status = status.HTTP_200_OK)

