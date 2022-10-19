from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import Selection
from ads.permissions import IsCreatedBy
from ads.serializers import SelectionSerializer, SelectionCreateSerializer, SelectionUpdateSerializer


class SelectionListView(ListAPIView):
    """Display all selections"""
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer


class SelectionDetailView(RetrieveAPIView):
    """Display selection by id"""
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer


class SelectionCreateView(CreateAPIView):
    """Create new selection"""
    queryset = Selection.objects.all()
    serializer_class = SelectionCreateSerializer
    permission_classes = [IsAuthenticated]


class SelectionUpdateView(UpdateAPIView):
    """Update add by id"""
    queryset = Selection.objects.all()
    serializer_class = SelectionUpdateSerializer
    permission_classes = [IsAuthenticated, IsCreatedBy]


class SelectionDeleteView(DestroyAPIView):
    """Delete selection by id"""
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [IsAuthenticated, IsCreatedBy]
