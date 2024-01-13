from rest_framework import viewsets
from django.db import transaction
from rest_framework.exceptions import APIException

from numbasums.models import Numbasum
from numbasums.serializers import NumbasumSerializer
from numbasums.tasks import task_execute


class NumbasumViewSet(viewsets.ModelViewSet):
    serializer_class = NumbasumSerializer
    queryset = Numbasum.objects.all()

    def perform_create(self, serializer):
        try:
            with transaction.atomic():
                instance = serializer.save()

                job_params = {"db_id": instance.id}
                transaction.on_commit(lambda: task_execute.delay(job_params))
        except Exception as e:
            raise APIException(str(e))
