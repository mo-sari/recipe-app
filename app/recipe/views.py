"""Views for Recipe API's"""

from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import (
    Recipe,
    Tag,
    Ingredient
)
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
        if self.action == 'upload_image':
            return serializers.RecipeImageSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new Recipe"""
        serializer.save(user=self.request.user)

    @action(methods=['POST'], detail=True, url_path='uploda_image')
    def upload_image(self, request, pk=None):

        recipe = self.gt_object()
        serializer = self.get_serializer(recipe, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_ok)

        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class BaseRecipeAttrViewSet(mixins.UpdateModelMixin,
                            mixins.ListModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet,):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user).order_by('-name')


# in the line below it is important to have GenericViewSet at last
class TagViewSet(BaseRecipeAttrViewSet):

    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class IngredientViewSet(BaseRecipeAttrViewSet):

    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer
