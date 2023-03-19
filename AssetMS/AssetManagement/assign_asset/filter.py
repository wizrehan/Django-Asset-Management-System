import django_filters

from .models import *


class AssignedAssetFilter(django_filters.FilterSet):
    class Meta:
        model = AssignAsset
        fields = ['product_id','employee_id', 'status']
        
