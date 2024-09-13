from django.shortcuts import render
from rest_framework.views import APIView
from django.db.models import Q
from profileapi.models import Profile

from rest_framework.response import Response


# Create your views here.
class SearchAPIViewlist(APIView):
    def get(self, request):
        # Get search parameters from request
        search_params = request.GET
        # Build query based on search parameters
        query = Q()
        for key, value in search_params.items():
            if key == 'age':
                age_range = value.split('-')
                query &= Q(age__range=(age_range[0], age_range[1]))
            elif key == 'gender':
                query &= Q(gender=value)
            elif key == 'religion':
                # Add a filter for religion
                query &= Q(religion=value)
            elif key == 'bride_or_groom':
                query &= Q(bride_or_groom=value)
            # Add filters for Marital status, Education and Occupation
            elif key == 'marital_status':
                query &= Q(marital_status=value)
            elif key == 'education':
                query &= Q(education=value)
            elif key == 'occupation':
                query &= Q(occupation=value)
            # Add more filters here

        # Execute query and return results
        results = Profile.objects.filter(query)
        return Response(results)
