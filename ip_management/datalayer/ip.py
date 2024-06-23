from django.utils import timezone

from ip_management.models import IP


class IPDatalayer(object):

    @classmethod
    def filter_ip(cls, id=None, ip=None, label=None, start_date=None, end_date=None, created_by=None):

        queryset = IP.objects.all()

        if id:
            queryset = queryset.filter(id=id)

        if ip:
            queryset = queryset.filter(ip__exact=ip)

        if label:
            queryset = queryset.filter(label__icontains=label)

        if start_date and end_date:
            queryset = queryset.filter(create_time__date__range=[start_date, end_date])

        if created_by:
            queryset = queryset.filter(created_by__iexact=created_by)

        return queryset


    @classmethod
    def create_ip(cls, ip, label, created_by=None):

        ip = IP(
            ip=ip,
            label=label,
            created_by=created_by
        )

        ip.save()

        return 0

    @classmethod
    def update_ip(cls, id, label):

        ip = IP.objects.get(id=id)
        ip.label = label
        ip.update_time = timezone.now()

        ip.save()

        return 0