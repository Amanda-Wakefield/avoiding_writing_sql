from django.contrib import admin

# Register your models here.

from .models import AlloStructure, Protein, Similarities, Structure

# an InLine allows you to view objects with foreign keys
class StructureInline(admin.TabularInline):
    model = Structure


class ProteinAdmin(admin.ModelAdmin):
    inlines = (StructureInline)


class StructureAdmin(admin.ModelAdmin):
    model = Structure


class AlloStructureAdmin(admin.ModelAdmin):
    model = AlloStructure


class SimilaritiesAdmin(admin.ModelAdmin):
    model = Similarities


admin.site.register(Protein, ProteinAdmin)
admin.site.register(Structure, StructureAdmin)
admin.site.register(AlloStructure, AlloStructureAdmin)
admin.site.register(Similarities, SimilaritiesAdmin)