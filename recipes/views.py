from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from  . import models

recipes = [{
    'author': 'Автор: Rambutan',
    'title': 'Куриный беф-строганов',
    'description': 'Бефстроганов из курицы - очень нежный и вкусный. И быстро готовится. Готовится так же, как и бефстроганов из говядины, ' \
                'но меньше по времени.',
    'time': 'Время приготовления: 45 мин.',
    'recipe': 'Продукты: Куриное филе – 600 г. '
              'Сметана – 2 ст. ложки '
              'Томатная паста – 1 ст. ложка '
              'Лук репчатый – 2 шт. '
              'Мука – 0,5 стакана. '
              'Масло растительное – 2 ст. ложки. '
              'Бульон (воспользовалась разведенным в воде бульонным кубиком) – 1,5 стакана. '
              'Соль - по вкусу. '
              'Перец черный молотый - по вкусу. '
    },

    {
        'author': 'Автор: anastasiya.panait  ',
        'title': 'Тушёная картошка с мясом, грибами и сметаной',
        'description': 'Картофель, тушенный с мясом и грибами, - популярное блюдо домашней кухни, очень сытное и очень вкусное. '
                       'Небольшой секрет: если в конце приготовления сдобрить всё сметаной, жаркое получится ещё вкуснее. '
                       'Сметана превращается в бархатистый соус с лёгкой кислинкой и сливочным послевкусием и прекрасно объединяет все компоненты.',
        'time': 'Время приготовления: 1 час. ',
        'recipe': 'Продукты: Картофель (крупный, очищенный) - 800 г (5 шт.)'
                   'Свинина (мякоть) - 400 г. '
                   'Шампиньоны - 250 г. '
                   'Лук репчатый - 100 г (1 шт.). '
                   'Сметана жирностью 20% - 140 г. '
                   'Масло подсолнечное - 60 мл (4 ст. ложки). '
                   'Лавровый лист - 1 шт. '
                   'Соль - 1 ч. ложка (по вкусу). '
                   'Перец чёрный молотый - 0,25 ч. ложки (по вкусу). '

    },

    {
            'author': 'Автор: GlebSky',
            'title': 'Спаггети с курицей и помидорами черри',
            'description': 'Простой и вкусный рецепт приготовления пасты с курицей и помидорами черри.',
            'time': 'Время приготовления: 45 мин.',
            'recipe': 'Продукты: Спагетти - 250 г. '
                       'Куриные бедра - 3-4 шт. '
                       'Помидоры черри - 250-300 г. '
                       'Сыр чеддер - 150 г. '
                       'Перец чили, хлопья - 1/2 ч. л. '
                       'Чеснок - 2-3 зубчика. '
                       'Петрушка свежая. '
                       'Перец черный молотый. '
                       'Соль. '

    }
]

# Create your views here.
def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/home.html", context)

class RecipeListView(ListView):
    model = models.Recipe
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'

class RecipeDetailView(DetailView):
    model = models.Recipe

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = models.Recipe
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Recipe
    fields = ['title', 'description']

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('recipes-home')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author


def about(request):
    return render(request, "recipes/about.html", {'title': 'about us page'})
