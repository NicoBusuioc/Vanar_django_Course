from rest_framework import serializers
from .models import Women

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

class WomenSerializer(serializers.ModelSerializer):    # original
    ## the line below is used by creation of new users to hide the option "Polizovateli" and choose by default the current user
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Women
        # fields = ('title', 'content', 'cat')
        fields = "__all__"


# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()

#     def create(self, validated_data):
#         return Women.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title          = validated_data.get("title", instance.title)
#         instance.content        = validated_data.get("content", instance.content)
#         instance.time_update    = validated_data.get("time_update", instance.time_update)
#         instance.is_published   = validated_data.get("is_published", instance.is_published)
#         instance.cat_id         = validated_data.get("cat_id", instance.cat_id)
#         instance.save()
#         return instance
    