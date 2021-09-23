from rest_framework.views import APIView
from rest_framework import viewsets, filters
from api import models, permissions, forms
from rest_framework.settings import api_settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from threading import Thread 
from rest_framework.authtoken.models import Token
from generate import generate

# Starting threads 
class StartThread(Thread):
    def __init__(self, group = None, target = None, name = None, args = (), kwargs = {}, Verbose = None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)
    def join(self):
        Thread.join(self)
        return self._return

# Developer Profile Viewset
class DeveloperProfileViewSet(viewsets.ModelViewSet):
    serializer_class = forms.DeveloperProfileForm
    queryset = models.DeveloperProfile.objects.all()
    permission_classes = (permissions.UpdateDeveloperProfile,)
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_backends = ('name', 'email', 'organisation')
    def perform_create(self, form):
        form.save()
    def make_create(self, request):
        form = self.serializer_class(data = request.data, context={'request': request})
        if form.is_valid():
            email = form.validated_data['email']
            name = form.validated_data['name']
            organisation = form.validated_data['organisation']
            t1 = StartThread(target = self.perform_create, args = (form,))
            t1.setDaemon(True)
            t1.start()
            return Response({
                'message': "New user is sucessfully created",
                'email': email,
                'name': name,
                'organisation': organisation
            })
        else:
            return Response(
                form.errors,
                status = status.HTTP_400_BAD_REQUEST,
            )
    def create(self, request):
        t = StartThread(target = self.make_create, args = (request,))
        t.setDaemon(True)
        t.start()
        new_response = t.join()
        return new_response

# Developer login apis functions and how it works
class DeveloperLoginApiView(ObtainAuthToken):
    serializer_class = forms.AccessTokenForm
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    def make_post(self, request):
        form = self.serializer_class(data = request.data, context={'request': request})
        if form.is_valid():
            developer = form.validated_data['user']
            token, check = Token.objects.get_or_create(user = developer)
            return Response({
                'token': token.key,
                'is_staff': developer.is_staff,
                'first_time_generated': check 
            })
        else:
            return Response(
                form.errors,
                status = status.HTTP_400_BAD_REQUEST,
            )
    def post(self, request):
        t = StartThread(target = self.make_post, args = (request,))
        t.setDaemon(True)
        t.start()
        new_response = t.join()
        return new_response

# Our main music py viewset
class MusicReportViewSet(viewsets.ModelViewSet):
    serializer_class = forms.MusicReportForm
    queryset = models.MusicReportModel.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnReport, IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_backends = ('timing', 'developer_profile', 'parsed_text')

    def perform_create(self, form, report = None, parsed_music = None):
        form.save(developer_profile = self.request.user, report = report, parsed_music = parsed_music)

    def make_create(self, request):
        form = self.serializer_class(data = request.data)
        if form.is_valid():
            data = form.validated_data['parsed_text']
            data = 'generated_music/' + data + '.mid'
            report = generate(data)
            parsed_music =  data
            t2 = StartThread(target = self.perform_create, args = (form, report, parsed_music))
            t2.setDaemon(True)
            t2.start()
            return Response({'report': report})
        else:
            return Response(
                form.errors,
                status = status.HTTP_400_BAD_REQUEST,
            )
    def create(self, request):
        t = StartThread(target = self.make_create, args = (request,))
        t.setDaemon(True)
        t.start()
        new_response = t.join()
        return new_response