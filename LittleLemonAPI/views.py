from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Category, MenuItem
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.decorators import api_view 
from .serializers import MenuItemSerializer


# Create your views here.
@api_view(["GET", "POST"])
def menu_items(request):
	if request.method == "GET":
		items = get_list_or_404(MenuItem)
		# items = MenuItem.objects.select_related('category').all()
		serialized_item = MenuItemSerializer(items, many=True)
		return Response(serialized_item.data)


	elif request.method == "POST":
		serialized_item = MenuItemSerializer(data=request.data)
		serialized_item.is_valid(raise_exception=True)
		serialized_item.save()
		return Response(serialized_item.data, status.HTTP_201_CREATED)
	

@api_view(["GET", "PUT", "DELETE"])
def menu_detail(request, id):
	item = get_object_or_404(MenuItem, pk=id)

	if request.method == "GET":
		serialized_item = MenuItemSerializer(item, many=False)
		return Response(serialized_item.data)


	elif request.method == "PUT":
		serialized_item = MenuItemSerializer(item, data=request.data)
		serialized_item.is_valid(raise_exception=True)
		serialized_item.save()
		return Response(serialized_item.data, status.HTTP_201_CREATED)
	
	elif request.method == "DELETE":
		item.delete()
		return Response(status.HTTP_204_NO_CONTENT)
		
		

	


