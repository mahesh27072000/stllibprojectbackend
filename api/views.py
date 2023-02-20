from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.views.generic import ListView, CreateView
from rest_framework import status
# from rest_framework.exceptions import NotFound



class LoginAPI(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            user_serializer = UserSerializer(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": user_serializer.data
                
            })
        else:
            return Response({"error": "Invalid credentials"})




class LibraryMemberCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LibraryMemberSerializer

class LibraryStaffMemberCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LibraryStaffMemberSerializer 

class UserList(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsStaffUser]
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsStaffUser]
    queryset = User.objects.all()
    serializer_class = UserListSerializer

# # Category
# class CategoryListCreateAPIView(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated, IsStaffUser]
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated, IsStaffUser]
#     serializer_class = CategorySerializer


# Book

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookCreateAPIView(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated, IsStaffUser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsStaffUser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Search

class BookSearchView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        search = self.request.query_params.get('search')


        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(author__icontains=search) |
                Q(ISBN__icontains=search) |
                Q(id__icontains=search)
            )

        # if not queryset:
        #     raise NotFound(detail={'message': 'No books found matching the search criteria'})

        return queryset
        


class IssueListCreateAPIView(generics.ListCreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        # include the user details in the response
        user = User.objects.get(id=serializer.data['library_member'])
        user_serializer = UserSerializer(user)
        data = {
            'issue': serializer.data,
            'library_member': user_serializer.data
        }
        
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

class ReturnListCreateAPIView(generics.ListCreateAPIView):
    queryset = Return.objects.all()
    serializer_class = ReturnSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        # include the user details in the response
        user = User.objects.get(id=serializer.data['library_member'])
        user_serializer = UserSerializer(user)
        data = {
            'issue': serializer.data,
            'library_member': user_serializer.data
        }
        
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

class RenewalListCreateAPIView(generics.ListCreateAPIView):
    queryset = Renewal.objects.all()
    serializer_class = RenewalSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        # include the user details in the response
        user = User.objects.get(id=serializer.data['library_member'])
        user_serializer = UserSerializer(user)
        data = {
            'issue': serializer.data,
            'library_member': user_serializer.data
        }
        
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


# retrieve-update-delete

class IssueRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated, IsStaffUser]
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        library_member = instance.library_member
        instance.delete()
        user_serializer = UserSerializer(library_member)
        return Response(user_serializer.data)

        # library_member = instance.library_member
        # instance.delete()
        # user_serializer = UserSerializer(library_member)
        # return Response(user_serializer.data)

class ReturnRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated, IsStaffUser]
    queryset = Return.objects.all()
    serializer_class = ReturnSerializer
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        library_member = instance.library_member
        instance.delete()
        user_serializer = UserSerializer(library_member)
        return Response(user_serializer.data)


class RenewalRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated, IsStaffUser]
    queryset = Renewal.objects.all()
    serializer_class = RenewalSerializer
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        library_member = instance.library_member
        instance.delete()
        user_serializer = UserSerializer(library_member)
        return Response(user_serializer.data)
