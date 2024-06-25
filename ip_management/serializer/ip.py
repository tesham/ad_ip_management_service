
from rest_framework import serializers

import ipaddress
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

    def validate_ip(self, value):

        try:
            ip_obj = ipaddress.ip_address(value)
            if ip_obj.version == 4 or ip_obj.version == 6:
                pass
        except Exception:
            raise Exception('Invalid ip address')

        return value