from django.urls import path
from . import views
from django.contrib import admin, auth
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('login/', LoginView.as_view(template_name='polls/login.html')),
	path('logout/', LogoutView.as_view(next_page='/')),
]