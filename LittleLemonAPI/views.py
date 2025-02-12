from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Category, MenuItem
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.decorators import api_view 
from .serializers import MenuItemSerializer, CategorySerializer
from urllib.parse import unquote
# from django.db.models import Q



# Create your views here.
@api_view(["GET", "POST"])
def menu_items(request):
	if request.method == "GET":
		# items = get_list_or_404(MenuItem)
		items = MenuItem.objects.select_related('category').all()

		category_name = request.query_params.get("category")
		to_price = request.query_params.get("to_price")
		menu_item = request.query_params.get("menu_item")

		if category_name:
			items = items.filter(category__slug__iexact=category_name)

		if menu_item:
			items = items.filter(title__iexact=menu_item)

		if to_price:
			items = items.filter(price__lte=to_price)

		# Another way to implement category filtering
		# category_name = request.GET.get("category") if request.GET.get("category") != None else ""

		# items = MenuItem.objects.filter(
        # Q(category__title__icontains=category_name))

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
		
		
@api_view(["GET","POST"])
def category_items(request):
	if request.method == "GET":
		category_list = get_list_or_404(Category)
		serialized_list = CategorySerializer(category_list, many=True)
		return Response(serialized_list.data)

	elif request.method == "POST":
		serialized_list = CategorySerializer(data=request.data)
		serialized_list.is_valid(raise_exception=True)
		serialized_list.save()
		return Response(serialized_list.data, status.HTTP_201_CREATED)
	

@api_view(["GET", "PUT", "DELETE"])
def category_detail(request, id):
	category_detail = get_object_or_404(Category, pk=id)

	if request.method == "GET":
		serialized_category_detail = CategorySerializer(category_detail, many=False)
		return Response(serialized_category_detail.data)

	elif request.method == "PUT":
		serialized_category_detail = CategorySerializer(category_detail, data=request.data)
		serialized_category_detail.is_valid(raise_exception=True)
		serialized_category_detail.save()
		return Response(serialized_category_detail.data, status.HTTP_201_CREATED)

	elif request.method == "DELETE":
		category_detail.delete()
		return Response(status.HTTP_204_NO_CONTENT)
	

		
        
		

	


