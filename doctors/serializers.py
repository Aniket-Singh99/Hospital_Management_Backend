from rest_framework import serializers

from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            "id", "name", "specialization", "email", "phone",
            "experience_years", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_phone(self, value):
        if not value.isdigit() or len(value) < 10:
            raise serializers.ValidationError("Enter a valid phone number (digits only, min 10).")
        return value

    def validate_experience_years(self, value):
        if value > 70:
            raise serializers.ValidationError("Experience looks too high, please check.")
        return value
