

from rest_framework import serializers

from posts.models import Forum, Comments,


class ForumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Forum
        fields = ('id','title', 'content', 'created', 'author')
        read_only_fields = ['author']

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
