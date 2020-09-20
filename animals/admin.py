from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()

admin.site.unregister(User)

# @admin.register(UserProfile)
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ['user', 'date_of_birth', ]


class UserProfileInline(admin.TabularInline):
    model = UserProfile


# UserProfile registers in User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [UserProfileInline]


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'slug', 'animal_type', 'description', 'date_of_birth', 'like', 'photo']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(AnimalType)
class AnimalTypeAdmin(admin.ModelAdmin):
    list_display = ('type_animal', )


@admin.register(ImageAnimal)
class ImageAnimalAdmin(admin.ModelAdmin):
    list_display = ('user', 'photo', 'description', 'animal')


