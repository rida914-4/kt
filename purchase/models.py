from __future__ import unicode_literals
from django.db import models


class Company(models.Model):
    comp_id = models.CharField(primary_key=True, max_length=2)
    comp_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phones = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    fax = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    stax_no = models.CharField(max_length=17, blank=True, null=True)
    add_line1 = models.CharField(max_length=50, blank=True, null=True)
    add_line2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    production = models.CharField(max_length=1, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    ntn = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class Party(models.Model):
    emp_id = models.CharField(max_length=8, blank=True, null=True)
    party_id = models.CharField(primary_key=True, max_length=4)
    party_name = models.CharField(max_length=50)
    stax_no = models.CharField(max_length=25, blank=True, null=True)
    add_line1 = models.CharField(max_length=50, blank=True, null=True)
    add_line2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    m_add_line1 = models.CharField(max_length=50, blank=True, null=True)
    m_add_line2 = models.CharField(max_length=50, blank=True, null=True)
    m_city = models.CharField(max_length=50, blank=True, null=True)
    icpl_code = models.CharField(max_length=4, blank=True, null=True)
    phones = models.CharField(max_length=50, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)
    o_bal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    party_type = models.CharField(max_length=1)
    party_abbr = models.CharField(max_length=10, blank=True, null=True)
    reg = models.ForeignKey('Regions', models.DO_NOTHING)
    itax_ded = models.CharField(max_length=1, blank=True, null=True)
    comp_id = models.CharField(max_length=2)
    acct_id_cs = models.CharField(max_length=10, blank=True, null=True)
    ntn = models.CharField(max_length=30, blank=True, null=True)
    cnic = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party'


class Regions(models.Model):
    reg_id = models.CharField(primary_key=True, max_length=4)
    reg_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'regions'


class TVPAl(models.Model):
    party_id = models.CharField(primary_key=True, max_length=4, blank=True, null=True)
    inv_id = models.CharField(max_length=8, blank=True, null=True)
    inv_date = models.DateField(blank=True, null=True)
    particulars = models.CharField(max_length=153, blank=True, null=True)
    db = models.FloatField(blank=True, null=True)
    cr = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_p_al'