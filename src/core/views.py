from django.shortcuts import render
from django.http import JsonResponse

#Third party imports
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PostSerializer
from .models import Post


class TestView(APIView):

    permission_classes = (IsAuthenticated, )
    def get(self, request, *args, **kwargs):
      qa = Post.objects.all()
      post = qa.first()
    #  serializer = PostSerializer(qa, many=True)
      serializer = PostSerializer(post)
      return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, *args, **kwargs):
        qs = Post.objects.all()
        post = qs.delete()
        return Response({'message': 'Data deleted successfully'})


# Create your views here.
# def test_veiw(request):
#    data = {
#        'name': 'john',
#        'age': 23
#    }
#    return JsonResponse(data)

