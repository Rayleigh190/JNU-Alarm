from django.db import models

class Shortcut(models.Model):
  name = models.CharField(max_length=10)
  ios_image_name = models.CharField(max_length=20)
  aos_image_name = models.CharField(max_length=20)
  color_code = models.CharField(max_length=6)
  link = models.URLField()
  is_webview = models.BooleanField()
  is_modal = models.BooleanField()
  is_available = models.BooleanField()

  def __str__(self):
    return self.name

class BannerAd(models.Model):
  name = models.CharField(max_length=50)
  image_url = models.URLField()
  direction_url = models.URLField(blank=True)
  expiry_date = models.DateField()
  is_external_browser = models.BooleanField(default=False)
  is_available = models.BooleanField()

class TopBannerAd(models.Model):
  name = models.CharField(max_length=50)
  image_url = models.URLField()
  direction_url = models.URLField(blank=True)
  expiry_date = models.DateField()
  is_external_browser = models.BooleanField(default=False)
  is_available = models.BooleanField()

class Restaurant(models.Model):
  name = models.CharField(max_length=20)
  road_address = models.CharField(max_length=50)
  jibun_address = models.CharField(max_length=50)
  latitude = models.FloatField()
  longitude = models.FloatField()
  type = models.CharField(max_length=10)
  naver_map_url = models.URLField()
  is_available = models.BooleanField()
