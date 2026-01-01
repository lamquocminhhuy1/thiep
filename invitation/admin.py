from django.contrib import admin
from .models import WeddingInfo, WeddingAlbumPhoto

class WeddingAlbumPhotoInline(admin.TabularInline):
    model = WeddingAlbumPhoto
    extra = 1

@admin.register(WeddingInfo)
class WeddingInfoAdmin(admin.ModelAdmin):
    inlines = [WeddingAlbumPhotoInline]
    
    # Only allow one instance
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return True
