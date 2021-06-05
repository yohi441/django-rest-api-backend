from django.db.models import fields
from rest_framework import serializers
from main.models import Product, ProductTag
from django.contrib.auth.models import User



class UserSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = User
        fields = [
            'url',
            'id',
            'username'
        ]


class ProductSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Product
        fields = [
            'url',
            'id',
            'name',
            'description',
            'price',
            'slug',
            'active',
            'in_stock',
            'date_updated'

        ]

class ProductTagSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = ProductTag
        fields = [
            'url',
            'id',
            'products',
            'name',
            'slug',
            'description',
            'active'
        ]