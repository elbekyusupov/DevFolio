from rest_framework import serializers
from ..models import Comment, Blog, Reply, Cat


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'type', 'img']


class CommentSerializer(serializers.ModelSerializer):
    # blog = BlogSerializer()
    class Meta:
        model = Comment
        fields = '__all__'#['id', 'personal', 'blog', 'created_at'] #'__all__'
        # depth = 1 bog'langan jadvallarni ham ko'rsatadi malumoti 1 chuqurlik darajasi


class ReplySerializer(serializers.ModelSerializer):
    comment = CommentSerializer()

    class Meta:
        model = Reply
        fields = '__all__'#['id', 'response', 'comment']
        # depth = 2

class CatSerializer(serializers.ModelSerializer):
    childs = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Cat
        fields = '__all__'
        # depth = 5

    def get_childs(self, instance):
        childs = instance.childs.filter(status = True).order_by('id')
        request = self.context.get('request')
        return CatSerializer(childs, many=True, context={'request':request}).data