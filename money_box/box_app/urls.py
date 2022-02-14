from django.urls import path

from box_app.views import home_page, SignUpView, LoginView, ParentCabinetView, ChildCabinetView, LogoutView, \
    AddChildView, first_child_page, second_child_page, third_child_page, forth_child_page, fifth_child_page

urlpatterns = [
    path('', home_page, name='home'),
    path('child_page1', first_child_page, name='child_page1'),
    path('child_page2', second_child_page, name='child_page2'),
    path('child_page3', third_child_page, name='child_page3'),
    path('child_page4', forth_child_page, name='child_page4'),
    path('child_page5', fifth_child_page, name='child_page5'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('parent_cabinet/', ParentCabinetView.as_view(), name='parent_cabinet'),
    path('child_cabinet/', ChildCabinetView.as_view(), name='child_cabinet'),
    path('add_child/', AddChildView.as_view(), name='add_child')
]
