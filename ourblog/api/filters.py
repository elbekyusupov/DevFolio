import django_filters
from ..models import Cat, Reply, Blog, Personal
from account.models import User


class CatFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Cat
        # fields = ['name', 'parent', 'status']
        fields = {
            'name': ['icontains'],
            'parent': ['exact'],
            'status': ['exact'],
            'price': ['lt', 'gt']
        }

class ReplyFilter(django_filters.FilterSet):
    response = django_filters.CharFilter(lookup_expr='icontains')
    comment__id_min = django_filters.NumberFilter(field_name='comment__id', lookup_expr = 'gte')
    id_max = django_filters.NumberFilter(field_name='id', lookup_expr = 'lte')
    created_at__max = django_filters.DateRangeFilter(field_name='created_at')
    # personal = django_filters.ModelChoiceFilter(queryset=Blog.objects.all(),)

    class Meta:
        model = Reply
        fields = '__all__' #['response', 'id_min', 'id_max']

class BlogFilter(django_filters.FilterSet):

    class Meta:
        model = Blog
        fields = {
            'type': ['icontains'],
            'title': [ 'icontains'],
            'desc': ['exact', 'icontains']
        }