from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Women, Category
from .serializers import WomenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework.decorators import action
from rest_framework.permissions import *
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsOwnerOrReadOnly, )  

class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly, )  # only admin can delete entries


###########################
### CODE TO LEARN BELOW ###   
###########################

# class WomenViewSet(viewsets.ModelViewSet):
#    # queryset = Women.objects.all() #this line is not anymore needed because i overwrote the methos get_queryset, 
#    # dont forget to add in the router.register the attribute: basename='women'

#     serializer_class = WomenSerializer    

#     ## cu ajutorul la decorator action am adaugat un nou link: http://127.0.0.1:8000/api/v1/women/category/
#     ## la link-ul de baza http://127.0.0.1:8000/api/v1/women/ s-a adaugat denumirea functiei date, adica 'category'
#     @action(methods=['get'], detail=False)
#     def category(self, request):
#         cats = Category.objects.all()
#         return Response({'cats': [c.name for c in cats]})
    
#     ##
#     ## Method overwrite to get only first 3 items
#     def get_queryset(self):
#         pk = self.kwargs.get("pk")

#         if not pk:
#             # return Women.objects.all()[:3]
#             return Women.objects.all()[:3]
        
#         return Women.objects.filter(pk=pk)



# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer






###########################
### CODE TO LEARN BELOW ###   
###########################

# class WomenAPIView(APIView):
#     def get(self, request):
#         # print(type(Women.objects.all()))    # QuerySet
#         # lst = Women.objects.all().values()  # in order to get values from a QuerySet use .values() method

#         w = Women.objects.all()
#         return Response({'posts': WomenSerializer(w, many=True).data})
    
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({'post': serializer.data})

#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
        
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exist"})
        
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
    
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
        
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exist"})
        
#         instance.delete()
#         return Response({"post": "deleted post " + str(pk)})