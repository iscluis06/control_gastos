from django.contrib.auth.models import User, Group
from control_gastos.serializer import GroupSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework import permissions

# Create your views_classes here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]