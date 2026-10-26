from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from patients.models import Patient

from .models import PatientDoctorMapping
from .serializers import MappingSerializer


class MappingListCreateView(APIView):
    def get(self, request):
        mappings = PatientDoctorMapping.objects.filter(
            patient__created_by=request.user
        ).select_related("patient", "doctor")
        serializer = MappingSerializer(mappings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MappingSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MappingDetailView(APIView):
    """
    GET    /api/mappings/<patient_id>/  -> doctors assigned to that patient
    DELETE /api/mappings/<id>/          -> remove a mapping
    """

    def get(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk, created_by=request.user)
        mappings = PatientDoctorMapping.objects.filter(patient=patient).select_related(
            "patient", "doctor"
        )
        serializer = MappingSerializer(mappings, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        mapping = get_object_or_404(
            PatientDoctorMapping, pk=pk, patient__created_by=request.user
        )
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
