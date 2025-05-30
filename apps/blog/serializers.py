from rest_framework import serializers
from .models import ListPostModel



class ListPostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()

    class Meta:
        model = ListPostModel
        fields = [
        'id',
        'image',
        'title',
        'content',
        'author',
        'created_at',
        'updated_at',
        ]

    def get_author(self, obj):
        return obj.author.username


    def get_created_at(self, obj):
        formatted_time = obj.created_at.strftime("%b %d, %Y %H:%M")
        return formatted_time

    def get_updated_at(self, obj):
        formatted_time = obj.updated_at.strftime("%b %d, %Y %H:%M")
        return formatted_time

    def get_content(self, obj):
        return f'{obj.content[:50]} ....'




class ListPostDetailSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = ListPostModel
        fields = [
            'id',
            'image',
            'title',
            'content',
            'author',
            'created_at',
            'updated_at',
        ]

    def get_author(self, obj):
        return obj.author.username

    def get_created_at(self, obj):
        formatted_time = obj.created_at.strftime("%b %d, %Y %H:%M")
        return formatted_time

    def get_updated_at(self, obj):
        formatted_time = obj.updated_at.strftime("%b %d, %Y %H:%M")
        return formatted_time



