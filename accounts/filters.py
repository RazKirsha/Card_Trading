import django_filters
from trading.models import Card


class CardFilter(django_filters.FilterSet):
    class Meta:
        model = Card
        fields = {'name': ['icontains'],
                  'power': ['gt', 'lt'],
                  'type': ['exact'],
                  }
