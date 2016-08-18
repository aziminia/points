from django.db import models


class Guilds(models.Model):
    g_id = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)


class Knots(models.Model):
    k_id = models.IntegerField(null=True, blank=True)


class Logo(models.Model):
    full_size = models.TextField(null=True, blank=True)
    small = models.TextField(null=True, blank=True)


class Rates(models.Model):
    count = models.IntegerField(null=True, blank=True)
    credibility = models.IntegerField(null=True, blank=True)
    popularity = models.IntegerField(null=True, blank=True)
    reliability = models.IntegerField(null=True, blank=True)


class Filters(models.Model):
    doc_count = models.IntegerField(null=True, blank=True)
    key = models.CharField(max_length=500, null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)


class Points(models.Model):
    address = models.TextField(null=True, blank=True)
    guilds = models.ManyToManyField(Guilds)
    has_active_contract = models.BooleanField(default=False)
    point_id = models.IntegerField(null=True, blank=True)
    knots = models.ManyToManyField(Knots)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    logo = models.OneToOneField(Logo, null=True, blank=True)
    rates = models.OneToOneField(Rates, null=True, blank=True)
    slogan = models.CharField(max_length=500, null=True, blank=True)
    slugged_title = models.CharField(max_length=500, null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    tel_1 = models.CharField(max_length=20, null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    uuid = models.CharField(max_length=200, null=True, blank=True)
