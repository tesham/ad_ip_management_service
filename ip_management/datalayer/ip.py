from django.utils import timezone

from ip_management.models import IP
from ip_management.rabbitmq_producer import send_message


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
    def create_ip(cls, ip, label, created_by=None, user=None):

        ip_model = IP(
            ip=ip,
            label=label,
            created_by=created_by
        )

        ip_model.save()

        try:
            # sending audit message to consumer after ip create
            message = dict(
                user=user.name if user else '',
                session_id=user.session_id if user else '',
                module='IP',
                label='Create',
                action='IP created: ' + ip,
                ip=ip
            )

            send_message("audit_queue", message)

        except Exception as exe:
            print('RabbitMQ exception in IP Create', str(exe))

        return 0

    @classmethod
    def update_ip(cls, id, label, user=None):

        ip = IP.objects.get(id=id)
        old_label = ip.label
        ip.label = label
        ip.update_time = timezone.now()

        ip.save()

        try:
            # sending audit message to consumer after ip update
            message = dict(
                user=user.name if user else '',
                session_id=user.session_id if user else '',
                module='IP',
                label='Update',
                action=f'label updated from {old_label} to {ip.label} for ip {ip.ip}',
                ip=ip.ip
            )

            send_message("audit_queue", message)
        except Exception as exe:
            print('RabbitMQ exception in IP Update', str(exe))

        return 0