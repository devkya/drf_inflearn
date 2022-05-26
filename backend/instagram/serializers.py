from .models import Post
from rest_framework.serializers import ModelSerializer, ReadOnlyField

class PostSerializer(ModelSerializer):
    username = ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = [
            'pk',
            'username',
            'message',
            'created_at',
            'updated_at',
        ]
        