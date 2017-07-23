# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.
from bugdemo.models import (SideA, ABLink)

from adminsortable2.admin import (
    SortableAdminMixin, SortableInlineAdminMixin)


class ABLinkInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ABLink
    extra = 0

class SideAAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [ABLinkInline]

admin.site.register(SideA, SideAAdmin)

# Register your models here.
