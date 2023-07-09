from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('rowNum',
        'opnSfTeamCode',
        'mgtNo',
        'opnSvcId',
        'updateGbn',
        'updateDt',
        'opnSvcNm',
        'bplcNm',
        'sitePostNo',
        'siteWhlAddr',
        'rdnPostNo',
        'rdnWhlAddr',
        'siteArea',
        'apvPermYmd',
        'apvCancelYmd',
        'dcbYmd',
        'clgStdt',
        'clgEnddt',
        'ropnYmd',
        'trdStateGbn',
        'dtlStateGbn',
        'dtlStateNm',
        'x',
        'y',
        'lastModTs',
        'uptaeNm',
        'siteTel')
