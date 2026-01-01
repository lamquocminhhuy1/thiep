from django.db import models

class WeddingInfo(models.Model):
    groom_name = models.CharField(max_length=100, default='Nguyễn Phước Hải')
    bride_name = models.CharField(max_length=100, default='Dương Hà Giang')
    
    groom_parents_dad = models.CharField(max_length=100, default='Ông Nguyễn Văn Học')
    groom_parents_mom = models.CharField(max_length=100, default='Bà Phùng Thị Bạch Yến')
    groom_address = models.CharField(max_length=255, default='131 Rạch Ông Kinh, P. Long Tuyền, TP. Cần Thơ')
    
    bride_parents_dad = models.CharField(max_length=100, default='Ông Dương Huy Thu')
    bride_parents_mom = models.CharField(max_length=100, default='Bà Nguyễn Thị Hoa')
    bride_address = models.CharField(max_length=255, default='240 Lê Duẩn, Thôn 12, Xã Ea Knốp, H. Ea Kar, T. Đắk Lắk')
    
    ceremony_date = models.DateTimeField(null=True, blank=True)
    ceremony_time_str = models.CharField(max_length=50, default='08:00')
    ceremony_date_str = models.CharField(max_length=100, default='Thứ Năm, 29/01/2026')
    ceremony_location = models.CharField(max_length=255, default='Tại tư gia nhà trai')
    ceremony_address = models.CharField(max_length=255, default='131 Rạch Ông Kinh, P. Long Tuyền, TP. Cần Thơ')
    ceremony_lunar_date = models.CharField(max_length=100, default='(Tức ngày 11 tháng 12 năm Ất Tỵ)')
    
    reception_date = models.DateTimeField(null=True, blank=True)
    reception_time_str = models.CharField(max_length=50, default='10:30')
    reception_date_str = models.CharField(max_length=100, default='CHỦ NHẬT | 31 | THÁNG 08')
    reception_location = models.CharField(max_length=255, default='Queen Plaza Kỳ Hòa')
    reception_address = models.CharField(max_length=255, default='Queen Plaza Kỳ Hòa, 16A Lê Hồng Phong, Phường 12, Quận 10, TP. Hồ Chí Minh')
    reception_lunar_date = models.CharField(max_length=100, default='(Tức ngày 09/07 Ất Tỵ)')
    
    google_map_link = models.URLField(max_length=500, blank=True, default='https://maps.app.goo.gl/somewhere')
    
    # Photos
    groom_photo = models.ImageField(upload_to='couple/', blank=True, null=True, help_text="Upload groom's photo (square ratio recommended)")
    bride_photo = models.ImageField(upload_to='couple/', blank=True, null=True, help_text="Upload bride's photo (square ratio recommended)")

    def __str__(self):
        return f"{self.groom_name} & {self.bride_name}"

    class Meta:
        verbose_name_plural = "Wedding Info"


class WeddingAlbumPhoto(models.Model):
    wedding_info = models.ForeignKey(WeddingInfo, related_name='album_photos', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='album/')
    caption = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo {self.id} for {self.wedding_info}"

