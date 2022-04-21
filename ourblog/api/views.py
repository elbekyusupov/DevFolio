from rest_framework import generics
from . import serializer, filters
from .. import models

# Get All
class CommentView(generics.ListAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializer.CommentSerializer
# Post
class  CommentCreateView(generics.CreateAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializer.CommentSerializer
# Get all and Pos
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializer.CommentSerializer
# Get once
class CommentRetrieveView(generics.RetrieveAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializer.CommentSerializer
# Put
class CommentUpdateView(generics.UpdateAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializer.CommentSerializer

# Get and Put
class CommentRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializer.CommentSerializer
# Delete
class CommentDestroyView(generics.DestroyAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializer.CommentSerializer
# Get and Delete
class CommentRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializer.CommentSerializer

class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializer.CommentSerializer

class BlogsView(generics.ListAPIView):
    queryset = models.Blog.objects.all().order_by('-id')
    serializer_class = serializer.BlogSerializer
    filter_class = filters.BlogFilter
    # def get_queryset(self):
    #     return  models.Blog.objects.filter(id__gte=10)


class ReplysView(generics.ListAPIView):
    queryset = models.Reply.objects.all()
    serializer_class = serializer.ReplySerializer
    filter_class = filters.ReplyFilter

class CatsView(generics.ListAPIView):
    queryset = models.Cat.objects.all()
    serializer_class = serializer.CatSerializer
    filter_class = filters.CatFilter
    
    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     return qs.filter(id__gte = 10)
