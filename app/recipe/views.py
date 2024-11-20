"""Views for Recipe API's"""

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe
from recipe import serializers


class RecipeVeiwSet(viewsets.ModelViewSet):
    """View for manage recipe API's"""
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        """Retrieve recipes for authenticated users"""
        return Recipe.objects.filter(user=self.request.user).order_by('id')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.RecipeSerializer

        return self.serializer_class
