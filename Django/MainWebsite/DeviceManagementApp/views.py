from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from .models import DeviceInstance
from rest_framework import generics, permissions
from .serializers import DeviceInstanceSerialier
import uuid

# Create your views here.


def testViewFromApp_view(request):
    return render(request, 'DeviceManagementApp/listDevices.html')


class ListDevicesView(ListView):
    model = DeviceInstance
    template_name = 'DeviceManagementApp/listDevices.html'
    # paginate_by = 5

# def ListDevicesView(request):
#     return render(request, 'DeviceManagementApp/test.html')


class AddDeviceView(CreateView):  # book_form.html
    model = DeviceInstance
    fields = '__all__'
    success_url = '/DM/listDevice/'


# class ListDevicesInstancesAPI(generics.ListAPIView):
class ListDevicesInstancesAPI(generics.ListCreateAPIView):
    queryset = DeviceInstance.objects.all()
    serializer_class = DeviceInstanceSerialier
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perfom_create(self, serializer):
        serializer.save(owner = self.request.user, DeviceID = uuid.uuid4, connectionStatus = 'C' )