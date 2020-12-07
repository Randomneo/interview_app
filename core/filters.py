from django_filters import FilterSet

from .models import Locode


class LocodeFilter(FilterSet):
    class Meta:
        model = Locode
        fields = ['id', 'name_wo', 'locode']
