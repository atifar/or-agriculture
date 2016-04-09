# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Metadata(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    table_name = models.CharField(max_length=64, blank=True, null=True)
    unit = models.CharField(max_length=64, blank=True, null=True)
    field = models.CharField(max_length=64, blank=True, null=True)
    source_name = models.CharField(max_length=256, blank=True, null=True)
    source_link = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metadata'


class NassAnimalsInventory(models.Model):
    commodity = models.CharField(max_length=64, blank=True, null=True)
    year = models.SmallIntegerField(blank=True, null=True)
    fips = models.IntegerField(blank=True, null=True)
    animals = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nass_animals_inventory'


class NassAnimalsSales(models.Model):
    commodity = models.CharField(max_length=64, blank=True, null=True)
    year = models.SmallIntegerField(blank=True, null=True)
    fips = models.IntegerField(blank=True, null=True)
    animals = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nass_animals_sales'


class NassCommodityArea(models.Model):
    commodity = models.CharField(max_length=64, blank=True, null=True)
    year = models.SmallIntegerField(blank=True, null=True)
    fips = models.IntegerField(blank=True, null=True)
    acres = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # id = models.AutoField()

    class Meta:
        managed = False
        db_table = 'nass_commodity_area'


class NassCommodityFarms(models.Model):
    commodity = models.CharField(max_length=64, blank=True, null=True)
    year = models.SmallIntegerField(blank=True, null=True)
    fips = models.IntegerField(blank=True, null=True)
    farms = models.IntegerField(blank=True, null=True)
    # id = models.AutoField()

    class Meta:
        managed = False
        db_table = 'nass_commodity_farms'


class OainHarvestAcres(models.Model):
    commodity = models.CharField(max_length=64, blank=True, null=True)
    year = models.SmallIntegerField(blank=True, null=True)
    fips = models.IntegerField(blank=True, null=True)
    harvested_acres = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oain_harvest_acres'


# class Orfipsonly(models.Model):
#     gid = models.AutoField(primary_key=True)
#     fips = models.IntegerField(blank=True, null=True)
#     geom = models.TextField(blank=True, null=True)  # This field type is a guess.
#
#     class Meta:
#         managed = False
#         db_table = 'orfipsonly'
#
#
# class RawNassCensusData(models.Model):
#     source_desc = models.CharField(max_length=32, blank=True, null=True)
#     sector_desc = models.CharField(max_length=32, blank=True, null=True)
#     group_desc = models.CharField(max_length=64, blank=True, null=True)
#     commodity_desc = models.CharField(max_length=64, blank=True, null=True)
#     class_desc = models.CharField(max_length=128, blank=True, null=True)
#     production_practice_desc = models.CharField(max_length=64, blank=True, null=True)
#     util_practice_desc = models.CharField(max_length=32, blank=True, null=True)
#     statistical_category_desc = models.CharField(max_length=64, blank=True, null=True)
#     unit_desc = models.CharField(max_length=32, blank=True, null=True)
#     domain_desc = models.CharField(max_length=64, blank=True, null=True)
#     domain_category_description = models.CharField(max_length=128, blank=True, null=True)
#     data_item = models.CharField(max_length=256, blank=True, null=True)
#     aggregation_level_desc = models.CharField(max_length=32, blank=True, null=True)
#     state_ansi = models.CharField(max_length=16, blank=True, null=True)
#     state_fips_code = models.IntegerField(blank=True, null=True)
#     state_alpha = models.CharField(max_length=2, blank=True, null=True)
#     state_name = models.CharField(max_length=16, blank=True, null=True)
#     asd_code = models.IntegerField(blank=True, null=True)
#     asd_desc = models.CharField(max_length=16, blank=True, null=True)
#     county_ansi = models.IntegerField(blank=True, null=True)
#     county_code = models.IntegerField(blank=True, null=True)
#     county_name = models.CharField(max_length=32, blank=True, null=True)
#     region_desc = models.CharField(max_length=64, blank=True, null=True)
#     zip_5 = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
#     watershed_code = models.IntegerField(blank=True, null=True)
#     watershed_desc = models.CharField(max_length=64, blank=True, null=True)
#     congr_district_code = models.IntegerField(blank=True, null=True)
#     country_code = models.IntegerField(blank=True, null=True)
#     country_name = models.CharField(max_length=64, blank=True, null=True)
#     location_desc = models.CharField(max_length=256, blank=True, null=True)
#     year = models.IntegerField(blank=True, null=True)
#     frequency_desc = models.CharField(max_length=16, blank=True, null=True)
#     begin_code = models.IntegerField(blank=True, null=True)
#     end_code = models.IntegerField(blank=True, null=True)
#     reference_period_desc = models.CharField(max_length=16, blank=True, null=True)
#     week_ending = models.DateField(blank=True, null=True)
#     load_time = models.DateTimeField(blank=True, null=True)
#     value = models.CharField(max_length=64, blank=True, null=True)
#     cv = models.CharField(max_length=16, blank=True, null=True)
#     value_num = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'raw_nass_census_data'
#
#
# class RawOainData(models.Model):
#     commodity = models.CharField(max_length=128, blank=True, null=True)
#     county = models.CharField(max_length=64, blank=True, null=True)
#     year = models.IntegerField(blank=True, null=True)
#     harvest_units = models.IntegerField(blank=True, null=True)
#     yield_unit = models.CharField(max_length=32, blank=True, null=True)
#     production_unit = models.IntegerField(blank=True, null=True)
#     price_unit = models.CharField(max_length=32, blank=True, null=True)
#     value_produced = models.CharField(max_length=64, blank=True, null=True)
#     percent_sold = models.IntegerField(blank=True, null=True)
#     value_sales = models.CharField(max_length=64, blank=True, null=True)
#     harvest_unit_of_measure = models.CharField(max_length=32, blank=True, null=True)
#     yield_unit_of_measure = models.CharField(max_length=32, blank=True, null=True)
#     production_unit_of_measure = models.CharField(max_length=32, blank=True, null=True)
#     price_unit_of_measure = models.CharField(max_length=32, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'raw_oain_data'
#
#
# class RawSubsidyData(models.Model):
#     rank = models.IntegerField(blank=True, null=True)
#     program = models.CharField(max_length=64, blank=True, null=True)
#     fips = models.IntegerField(blank=True, null=True)
#     number_of_recipients = models.IntegerField(blank=True, null=True)
#     year = models.SmallIntegerField(blank=True, null=True)
#     subsidy_total = models.IntegerField(blank=True, null=True)
#     crop = models.CharField(max_length=64, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'raw_subsidy_data'


class RegionLookup(models.Model):
    st_code = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    co_code = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    region = models.CharField(max_length=90, blank=True, null=True)
    fips = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'region_lookup'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class SubsidyDollars(models.Model):
    commodity = models.CharField(max_length=64, blank=True, null=True)
    year = models.SmallIntegerField(blank=True, null=True)
    fips = models.IntegerField(blank=True, null=True)
    subsidy_dollars = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subsidy_dollars'


class SubsidyRecipients(models.Model):
    commodity = models.CharField(max_length=64, blank=True, null=True)
    year = models.SmallIntegerField(blank=True, null=True)
    fips = models.IntegerField(blank=True, null=True)
    subsidy_recipients = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subsidy_recipients'
