from django.urls import path

from box_app.views import home_page, SignUpView, LoginView, ParentCabinetView, ChildCabinetView, LogoutView

urlpatterns = [
    path('', home_page, name='home'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('parent_cabinet/', ParentCabinetView.as_view(), name='parent_cabinet'),
    path('child_cabinet/', ChildCabinetView.as_view(), name='child_cabinet'),
]
