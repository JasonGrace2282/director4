# SPDX-License-Identifier: MIT
# (c) 2019 The TJHSST Director 4.0 Development Team & Contributors

from django.contrib import admin

from .models import (
    Action,
    Database,
    DatabaseHost,
    DockerImage,
    DockerImageExtraPackage,
    DockerImageSetupCommand,
    Domain,
    Operation,
    Site,
    SitePendingUser,
    SiteResourceLimits,
)

admin.register(DockerImage)
class DockerImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name', 'description')
    search_fields = ('name', 'friendly_name', 'description')
    ordering = ('parent', 'name', 'friendly_name')

admin.site.register(DockerImageSetupCommand)
admin.site.register(DockerImageExtraPackage)
admin.site.register(Domain)

admin.site.register(DatabaseHost)
admin.site.register(Database)

admin.site.register(Site)
admin.site.register(SitePendingUser)
admin.site.register(SiteResourceLimits)

admin.site.register(Operation)
admin.site.register(Action)
