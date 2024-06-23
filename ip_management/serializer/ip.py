
from rest_framework import serializers

from ip_management.models import IP

#
# class IPSerializer1(serializers.ModelSerializer):
#     class Meta:
#         model = IP
#         fields = '__all__'
#
#     def validate_ip(self, value):
#         return value.upper()
#
#     def create(self, validated_data):
#         print('create')
#
#     def update(self, instance, validated_data):
#         print('update')


class IPSerializer(serializers.Serializer):

    id = serializers.IntegerField(required=False)
    ip = serializers.CharField(max_length=100, required=False)
    label = serializers.CharField(max_length=500, allow_blank=True, allow_null=True)