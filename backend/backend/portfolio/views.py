from .models import Introduction, AccountLinks, Projects, Timeline
from .serializer import (IntroductionSerializer, 
                        AccountLinksSerializer, 
                        ProjectsSerializer, 
                        TimelineSerializer)
from drf_multiple_model.views import ObjectMultipleModelAPIView
from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination

class LimitPagination(MultipleModelLimitOffsetPagination):
    default_limit = 4


class ObjectLimitPaginationView(ObjectMultipleModelAPIView):
    pagination_class = LimitPagination
    querylist = (
        {'queryset': Introduction.objects.all(), 
        'serializer_class': IntroductionSerializer},

        {'queryset': AccountLinks.objects.all(), 
        'serializer_class': AccountLinksSerializer},

        {'queryset': Projects.objects.all(), 
        'serializer_class': ProjectsSerializer},

        {'queryset': Timeline.objects.all(), 
        'serializer_class': TimelineSerializer},
    )