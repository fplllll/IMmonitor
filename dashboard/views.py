from rest_framework import mixins, viewsets, filters
from motors.serializers import MotorsSerializer, RotorSerializer, BearingsSerializer, StatorSerializer, \
    WarningLogSerializer, WeeklyRecordSerializer, MotorTrendSerializer
from django_filters.rest_framework import DjangoFilterBackend
from motors.models import Motor, Rotor, Bearing, Stator, WarningLog, WeeklyRecord
from motors.filters import MotorsFilter, WarninglogFilter, WeeklyRecordFilter
from rest_framework.views import APIView
from rest_framework.response import Response


class MotorsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    list:
        电机列表，搜索，过滤，排序
    retrieve:
        获取电机部分详情
    '''

    queryset = Motor.objects.all().order_by('id')
    serializer_class = MotorsSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = MotorsFilter
    search_fields = ('name', 'sn', 'statu')
    ordering_fields = ('name')


class RotorListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Rotor.objects.all().order_by('id')
    serializer_class = RotorSerializer


class BearingListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Bearing.objects.all().order_by('id')
    serializer_class = BearingsSerializer


class StatorListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Stator.objects.all().order_by('id')
    serializer_class = StatorSerializer


class WarningLogListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = WarningLog.objects.all().order_by('id')
    serializer_class = WarningLogSerializer
    filter_backends = (DjangoFilterBackend,)

    # 设置filter的类为我们自定义的类
    # 过滤
    filter_class = WarninglogFilter


class WeeklyRecordListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = WeeklyRecord.objects.all().order_by('id')
    serializer_class = WeeklyRecordSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = WeeklyRecordFilter


class TreemMapView(APIView):
    def get(self, request, format=None):
        """
        Return a equipment tree map.
        """
        treejson = {'name': 'Induction Motor Monitoring Platform', 'children': []}
        for motor in Motor.objects.all():
            treejson['children'].append({'name': motor.name, 'children': []})
            for bearing in motor.bearings.all():
                treejson['children'][-1]['children'].append({'name': bearing.name})
            for rotor in motor.rotors.all():
                treejson['children'][-1]['children'].append({'name': rotor.name})
            for stator in motor.stators.all():
                treejson['children'][-1]['children'].append({'name': stator.name})
        return Response(treejson)


class MotorTrendRetriveViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Motor.objects.all().order_by('id')
    serializer_class = MotorTrendSerializer


class MotorStatusView(APIView):
    def get(self, request, format=None):
        statistic={}
        for item in Motor.asset_status:
            statistic[item[1]]= Motor.objects.filter(statu=item[0]).count()
        return Response(statistic)
