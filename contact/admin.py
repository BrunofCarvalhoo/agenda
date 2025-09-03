from django.contrib import admin
from contact import models
# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','first_name','last_name','phone','show', # no Django admin vai aparecer esses campos
    ordering = '-id', # ordenar por id de forma decrescente
    #list_filter = 'created_date',
    search_fields = 'id','first_name','last_name', # serve para fazer buscas
    list_per_page = 10 # exibir apenas 10 contatos por pagina
    list_max_show_all = 200 # so vai aparecer o 'mostrar tudo' se tiver com menos de 200 contatos
    list_editable = 'first_name','last_name','show', # esses campos podem ser editados diretamente na listagem
    list_display_links = 'id', 'phone', # esses campos vão ser links para editar o contato

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name', 
    ordering = '-id', 
    