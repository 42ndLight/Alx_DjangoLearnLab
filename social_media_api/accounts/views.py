from django.shortcuts import render
from rest_framework import generics
from .serializers import RegisterSerializer, LoginSerializer

# Create your views here.
class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self,request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user.serializer.save()
        token = Token.objects.get(user=user)
        return Response({
            'user': UserSerializer(user).data,
            'token':token.key
                    }, status.HTTP_201_CREATED)
    
class LoginUserView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.user)
        serializer.is_valid(raise_exception=True)
        user.serializer.save()
        token = Token.objects.get(user=user)
        return Response({
            'user': UserSerializer(user).data,
            'token':token.key
                    })
    

