from django.contrib import admin

from pokemon_crawler.storage.models import Ability, Form, Move, Pokemon, Stat, Type


class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name',)


class StatAdmin(admin.ModelAdmin):
    list_display = ('name',)


class MoveAdmin(admin.ModelAdmin):
    list_display = ('name',)


class FormAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AbilityAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Stat, StatAdmin)
admin.site.register(Move, MoveAdmin)
admin.site.register(Form, FormAdmin)
admin.site.register(Ability, AbilityAdmin)
admin.site.register(Type, TypeAdmin)
