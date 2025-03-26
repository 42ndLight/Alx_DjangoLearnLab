from django.shortcuts import render
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from.models import CustomUser
from rest_framework.response import Response 
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer

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
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user': UserSerializer(user).data,
            'token':token.key
                    })

class ProfileUserView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
      
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser.objects.all(), id=user_id)

        if request.user == user_to_follow:
            return Response({"error" : "You cant Follow YourSelf!!"}, status=status.HTTP_400_BAD_REQUEST)
        
        if request.user.following.filter(id=user_id).exists():
            return Response({"status" : "Already Following this user"}, status=status.HTTP_200_OK)
        
        request.user.following.add(user_to_follow)
        return Response({"status" : "Success, You now Follow {user_to_follow.userame}"}, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser.objects.all(), id=user_id)

        if not request.user.following.filter(id=user_id).exists():
            return Response({"error" : "You are not following this user"}, status=status.HTTP_400_BAD_REQUEST)
        
        request.user.following.remove(user_to_unfollow)
        return Response({"status" : "You have Unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)
    

