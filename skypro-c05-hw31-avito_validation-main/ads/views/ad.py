from django.db.models import Q
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad
from ads.permissions import IsCreatedByOrAdminOrModerator
from ads.serializers import AdSerializer, AdCreateSerializer, AdUpdateSerializer, AdImageSerializer


class AdListView(ListAPIView):
    """Display all ads"""
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def get(self, request, *args, **kwargs):

        # Filter by category id
        categories = request.GET.getlist('cat', None)
        cat_query = None

        for cat_id in categories:
            if cat_query is None:
                cat_query = Q(category__id__exact=cat_id)
            else:
                cat_query |= Q(category__id__exact=cat_id)

        if cat_query:
            self.queryset = self.queryset.filter(cat_query)

        # Filter by ad text
        ad_name = request.GET.get('text', None)
        if ad_name:
            self.queryset = self.queryset.filter(
                name__icontains=ad_name
            )

        # Filter by user location
        user_location = request.GET.get('location', None)
        if user_location:
            self.queryset = self.queryset.filter(
                author__location__name__icontains=user_location
            )

        # Filter by price
        price_from = request.GET.get('price_from', None)
        price_to = request.GET.get('price_to', None)
        if price_from:
            self.queryset = self.queryset.filter(
                price__gte=price_from
            )
        if price_to:
            self.queryset = self.queryset.filter(
                price__lte=price_to
            )

        return super().get(request, *args, **kwargs)


class AdDetailView(RetrieveAPIView):
    """Display ad by id"""
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]


class AdCreateView(CreateAPIView):
    """Create new add"""
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer


class AdUpdateView(UpdateAPIView):
    """Update add by id"""
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer
    permission_classes = [IsAuthenticated, IsCreatedByOrAdminOrModerator]


class AdImageView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdImageSerializer
    permission_classes = [IsAuthenticated, IsCreatedByOrAdminOrModerator]


class AdDeleteView(DestroyAPIView):
    """Delete ad by id"""
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, IsCreatedByOrAdminOrModerator]
