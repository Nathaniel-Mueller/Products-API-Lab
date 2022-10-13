from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def productsList(request):
     
    
    
    return Response('ok')