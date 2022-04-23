from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(Catefory)
class CategoriAdmin(admin.ModelAdmin):
    """''' Категории '''"""
    list_display = ('id', 'name', 'url',)
    list_display_links = ('name',)


class ReviewInlines(admin.TabularInline):
    """ Отзывы на странице фильма """
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')

class MoavieShotsInlines(admin.TabularInline):
    """ Кадры из фильма на странице фильма """
    model = MoviesShots
    extra = 1
    readonly_fields = ('get_image', )
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110">')

    get_image.short_description = "Кадры"

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """ Фильмы """
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')
    """поистк по котегории сделать с помощью мени ту мени 
    филд значит вводим название категории из модели фильмы и указываем 
    через двойное подчеркивоние на что ссылаемся"""
    inlines = [MoavieShotsInlines, ReviewInlines]
    save_on_top = True
    save_as = True
    """Для дублирование фильма"""
    list_editable = ('draft',)
    # fields = ('title', ('actors', 'directors','genres'), ) """Уроки Django 3 - настройка админки django - урок 11"""
    readonly_fields = ('get_image', )
    fieldsets = (
        (None, {
            'fields': (('title', 'tagline'),)
        }),
        (None, {
            'fields': ('description',('get_image', 'poster'))
        }),
        (None, {
            'fields': (('year', 'world_premiere', 'country'),)
        }),
        ('Actors', {
            "classes": ('collapse',),
            'fields': (('actors', 'directors', 'genres', 'category'),)
        }),
        (None, {
            'fields': (('budget', 'fess_in_usa', 'fess_in_world'),)
        }),
        ('Options', {
            'fields': (('url', 'draft'),)
        }),
    )


    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110">')

    get_image.short_description = "Постер"

@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    """ Отзывы """
    list_display = ('id', 'name', 'email', 'parent', 'movie',)
    list_display_links = ('name',)
    """Вывести ссылокй поле"""
    readonly_fields = ('name', 'email')
    '''Скрыть поля от редоктирования'''


@admin.register(Genre)
class GanreAdmin(admin.ModelAdmin):
    """ Жанры """
    list_display = ('name', 'url')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """''' Актеры '''"""
    list_display = ('name', 'age', 'get_image')
    readonly_fields = ('get_image', )
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')

    get_image.short_description = "Изоброжение"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """ Рейтигн """
    list_display = ('star', 'ip')


@admin.register(MoviesShots)
class MovieShotAdmin(admin.ModelAdmin):
    """ Кадры из фильма """
    list_display = ('title', 'movie', 'get_image')
    readonly_fields = ('get_image', )
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')

    get_image.short_description = "Изоброжение"

admin.site.register(RatingStar)


admin.site.site_title = 'Django фильмы'
admin.site.site_header = 'Django фильмы'