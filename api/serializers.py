from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import permissions
from django.db.models import Q
from django.core.exceptions import ValidationError

# class LibraryMemberSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = LibraryMember
#         fields = ['id', 'user', 'membership_id', 'address', 'phone_number', 'password']

#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         instance = self.Meta.model(**validated_data)
#         if password is not None:
#             instance.set_password(password)
#         instance.save()
#         return instance

class LibraryMemberSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = User.objects.create(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance



class LibraryStaffMemberSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        validated_data['is_staff'] = True
        instance = User.objects.create(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    



class IsStaffUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff']




# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id', 'name', 'description']


class BookSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    class Meta:
        model = Book
        fields = '__all__'

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = "__all__"
    def validate(self, attrs):
        book = attrs['book']
        library_member = attrs['library_member']

        try:
            Issue.objects.get(book=book, library_member=library_member)
            raise serializers.ValidationError({
                'non_field_errors': ['This book has already been issued to this library member.']
            })
        except Issue.DoesNotExist:
            pass

        return attrs
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)

    #     if instance.cover_picture:
    #         format, imgstr = instance.cover_picture.split(';base64,')
    #         ext = format.split('/')[-1]
    #         representation['cover_ picture'] = ContentFile(base64.b64decode(imgstr), name='cover_picture.' + ext)
    #     return representation
    

class ReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Return
        fields = '__all__'

    def create(self, validated_data):
        book = validated_data.get('book')
        library_member = validated_data.get('library_member')
        try:
            issue = Issue.objects.get(book=book, library_member=library_member)
        except Issue.DoesNotExist:
            raise serializers.ValidationError({'error': 'The book must be issued before it can be returned.'})
        return_instance = super().create(validated_data)
        return return_instance

 
 
 

class RenewalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Renewal
        fields = '__all__'
    
    def create(self, validated_data):
        book = validated_data.get('book')
        library_member = validated_data.get('library_member')
        try:
            issue = Issue.objects.get(book=book, library_member=library_member)
        except Issue.DoesNotExist:
            raise serializers.ValidationError({'error': 'The book must be issued before it can be renewed.'})
        issue.due_date = validated_data['due_date']
        issue.save()
        renewal_instance = super().create(validated_data)
        return renewal_instance
        
        




class UserSerializer(serializers.ModelSerializer):
    issues = serializers.SerializerMethodField()
    returns = serializers.SerializerMethodField()
    renewals = serializers.SerializerMethodField()
    # book = BookSerializer()
    # issues = IssueSerializer(many=True)
    # category = CategorySerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff','issues','returns', 'renewals',]
    
    def get_issues(self, user):
        issues = Issue.objects.filter(library_member=user)
        return IssueSerializer(issues, many=True).data

    def get_returns(self, user):
            returns = Return.objects.filter(library_member=user)
            return ReturnSerializer(returns, many=True).data

    def get_renewals(self, user):
        renewals = Renewal.objects.filter(library_member=user)
        return RenewalSerializer(renewals, many=True).data









# Search

class BookSearchSerializer(serializers.Serializer):
    query = serializers.CharField()

# class BookSearchSerializer(serializers.Serializer):
#     query = serializers.CharField()
#     def search(self):
#         query = self.validated_data['query']
#         books = Book.objects.filter(
#             Q(title__icontains=query) |
#             Q(author__icontains=query) |
#             Q(ISBN__icontains=query)
#         )
        
#         return BookSerializer(books, many=True).data