from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('scripts/', views.scripts, name='scripts'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('sell/', views.sell, name='sell scripts'),
    path('sell', views.sell, name='sell scripts'),
    path('professionals/', views.professionals, name='professionals'),
    path('about/', views.about, name='about us'),
    path('terms/', views.terms, name='terms of service'),
    path('becomeprofessional', views.becomeprofessional, name='professionals'),
    path('<str:pk>/', views.scriptdetail, name='script details'),
    path('scripts/<str:pk>/', views.scriptdetail, name='script details'),
    path('<str:pk>/', views.professionaldetail, name='professional details'),
    path('professionals/<str:pk>/', views.professionaldetail, name='professional details'),
    #path('<str:pk>', views.catdetail, name='categories'),
    path('like-post', views.like_post, name='like-post'),
    path('hireprofessional', views.hire_professional, name='hire professional'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('blog', views.blog, name='News and updates'),
    path('blog/<str:pk>', views.blog_details, name="news details")
]

