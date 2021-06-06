
from rest_framework import serializers
from main.models import Product, ProductTag
from django.contrib.auth.models import User



class UserSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = User
        fields = '__all__',


class ProductSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Product
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
       
       

class ProductTagSerializer(serializers.HyperlinkedModelSerializer): 
    products = serializers.HyperlinkedRelatedField(many=True, view_name='producttag-detail', read_only=True)



    class Meta:
        model = ProductTag
        fields = '__all__'
        
        