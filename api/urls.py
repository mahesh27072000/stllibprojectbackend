from django.urls import path
from .views import *


urlpatterns = [
    # Login
    path('login/', LoginAPI.as_view(), name='login'),
    # Users
    path('library-members/', LibraryMemberCreateView.as_view(), name='library-member-create'),
    path('library-staff-members/', LibraryStaffMemberCreateView.as_view(), name='library-staff-member-create'),
    path('user_list/', UserList.as_view(), name='user_list'),
    path('user/<int:pk>/', UserDestroyAPIView.as_view(), name='user-retrieve-update-delete'),
    # Category
    # path('categories/', CategoryListCreateAPIView.as_view(), name='category-list'),
    # path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-update'),
   
   # Books
    path('books/', BookListAPIView.as_view(), name='book-list'),
    path('books/add/', BookCreateAPIView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-retrieve-update-delete'),

    # Search
    path('books/search/', BookSearchView.as_view(), name='book-search'),


    path('issues/', IssueListCreateAPIView.as_view(), name='issue-create-list'),
    path('returns/', ReturnListCreateAPIView.as_view(), name='return-create-list'),
    path('renewals/', RenewalListCreateAPIView.as_view(), name='renewal-create-list'),
    
    # retrieve-update-delete

    path('issues/<int:pk>/', IssueRetrieveUpdateDestroyAPIView.as_view(), name='issue-retrieve-update-delete'),
    path('returns/<int:pk>/', ReturnRetrieveUpdateDestroyAPIView.as_view(), name='return-retrieve-update-delete'),
    path('renewals/<int:pk>/', RenewalRetrieveUpdateDestroyAPIView.as_view(), name='renewal-retrieve-update-delete'),


    
]
