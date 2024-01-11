from django.shortcuts import render
from django.views.generic import ListView, DetailView
from article_module import models


# Create your views here.
class ArticleList(ListView):
    model = models.ArticleModel
    paginate_by = 5
    template_name = 'article_module/article_list.html'

    def get_queryset(self):
        query = super(ArticleList, self).get_queryset()
        query = query.filter(is_active=True)
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected_categories__url_title__iexact=category_name)
        return query


def article_category_component(request):
    context = {
        'categories': models.ArticleCategory.objects.filter(is_active=True, parent_id=None)
    }
    return render(request, 'components/article_category_component.html', context)


class ArticleDetailView(DetailView):
    model = models.ArticleModel
    template_name = 'article_module/article_detail.html'
    context_object_name = 'article'
