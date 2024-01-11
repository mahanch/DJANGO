from django.urls import path
from article_module import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name='article_list'),
    path('cat/<str:category>', views.ArticleList.as_view(), name='article_category_list_filter'),
    path('<pk>', views.ArticleDetailView.as_view(), name='article_detail_page')
]
