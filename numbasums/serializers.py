from rest_framework import serializers

from numbasums.models import Numbasum


class NumbasumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numbasum
        read_only_fields = ("id", "numba_sum")
        fields = "__all__"

    first_numba = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False)
    second_numba = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False)
    numba_sum = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False, read_only=True)