from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

from ip_management.datalayer import IPDatalayer
from ip_management.serializer import IPSerializer


class AuthenticatedView(APIView):
    pass


class UnauthenticatedView(APIView):
    permission_classes = ()


class IPAPIView(AuthenticatedView):

    # Fetch IP data
    def get(self, request):
        try:
            id = request.query_params.get('id', None)
            ip = request.query_params.get('ip', None)
            label = request.query_params.get('label', None)
            start_date = request.query_params.get('start_date', None)
            end_date = request.query_params.get('end_date', None)
            queryset = IPDatalayer.filter_ip(id=id, ip=ip, label=label, start_date=start_date, end_date=end_date)

            data = queryset.values()

            return Response(
                data, status=status.HTTP_200_OK
            )

        except Exception as exe:
            return Response(
                dict(
                    message=str(exe)
                ), status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    # Create IP data
    def post(self, request):

        try:
            serializer = IPSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            is_error = IPDatalayer.create_ip(
                ip=serializer.validated_data.get('ip'),
                label=serializer.validated_data.get('label'),
                created_by=request.user.name if request.user else None,
                user=request.user
            )

            return Response(
                dict(is_error=is_error, message='success'), status=status.HTTP_200_OK
            )
        except Exception as exe:
            return Response(
                dict(
                    message=str(exe)
                ), status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    # Update IP data
    def put(self, request):
        try:
            serializer = IPSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            is_error = IPDatalayer.update_ip(
                id=serializer.validated_data.get('id'),
                label=serializer.validated_data.get('label'),
                user=request.user
            )

            return Response(
                dict(is_error=is_error, message='success'), status=status.HTTP_200_OK
            )
        except Exception as exe:
            return Response(
                dict(
                    message=str(exe)
                ), status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
