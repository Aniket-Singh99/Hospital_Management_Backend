from rest_framework import serializers

from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            "id", "name", "age", "gender", "phone",
            "address", "medical_history", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_age(self, value):
        if value < 1 or value > 120:
            raise serializers.ValidationError("Age must be between 1 and 120.")
        return value

    def validate_phone(self, value):
        if not value.isdigit() or len(value) < 10:
            raise serializers.ValidationError("Enter a valid phone number (digits only, min 10).")
        return value
