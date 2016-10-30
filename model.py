# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AcctType(models.Model):
    acct_type = models.CharField(primary_key=True, max_length=4)
    type_name = models.CharField(max_length=50)
    debit_name = models.CharField(max_length=30)
    credit_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'acct_type'


class AppMod(models.Model):
    voucher_type = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'app_mod'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=160, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=510, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=256, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=300, blank=True, null=True)
    first_name = models.CharField(max_length=60, blank=True, null=True)
    last_name = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=508, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class City(models.Model):
    city_id = models.CharField(primary_key=True, max_length=2)
    city_name = models.CharField(max_length=30)
    acct_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'


class ClosingDates(models.Model):
    voucher_type = models.CharField(primary_key=True, max_length=2)
    date_closing = models.DateField()

    class Meta:
        managed = False
        db_table = 'closing_dates'


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


class Currency(models.Model):
    cur_id = models.CharField(primary_key=True, max_length=2)
    cur_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'currency'


class Division(models.Model):
    div_id = models.CharField(primary_key=True, max_length=2)
    div_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'division'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=400, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=200, blank=True, null=True)
    model = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=510, blank=True, null=True)
    name = models.CharField(max_length=510, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=80)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Expense(models.Model):
    exp_id = models.CharField(primary_key=True, max_length=7)
    exp_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'expense'


class FinYears(models.Model):
    year_id = models.CharField(primary_key=True, max_length=2)
    year_name = models.CharField(unique=True, max_length=10)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    date_closing_cp = models.DateField(blank=True, null=True)
    date_closing_bp = models.DateField(blank=True, null=True)
    date_closing_cr = models.DateField(blank=True, null=True)
    date_closing_br = models.DateField(blank=True, null=True)
    date_closing_jv = models.DateField(blank=True, null=True)
    date_closing_sl = models.DateField(blank=True, null=True)
    date_closing_sr = models.DateField(blank=True, null=True)
    date_closing_rtn = models.DateField(blank=True, null=True)
    date_closing_pl = models.DateField(blank=True, null=True)
    date_closing_pp = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_years'


class Grn(models.Model):
    grn_id = models.CharField(primary_key=True, max_length=5)
    grn_date = models.DateField()
    party_id = models.CharField(max_length=7)
    comp_id = models.CharField(max_length=2)
    emp_id = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grn'


class Grndet(models.Model):
    grn_id = models.CharField(max_length=6)
    lineitem = models.CharField(max_length=3)
    prod_id = models.CharField(max_length=4)
    rec_qty = models.DecimalField(max_digits=13, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'grndet'
        unique_together = (('grn_id', 'lineitem'),)


class Locations(models.Model):
    loc_id = models.CharField(primary_key=True, max_length=2)
    loc_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'locations'


class Lots(models.Model):
    lot_id = models.CharField(primary_key=True, max_length=5)
    lot_date = models.DateField()
    close_date = models.DateField(blank=True, null=True)
    comp_id = models.CharField(max_length=2)
    year_id = models.CharField(max_length=2)
    emp_id = models.CharField(max_length=8)
    loc_id = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'lots'


class MVoucher(models.Model):
    voucher_id = models.CharField(max_length=13, blank=True, null=True)
    voucher_date = models.DateField(blank=True, null=True)
    post_date = models.DateField(blank=True, null=True)
    acct_id = models.CharField(max_length=10, blank=True, null=True)
    particulars = models.CharField(max_length=200, blank=True, null=True)
    emp_id = models.CharField(max_length=20, blank=True, null=True)
    posted = models.CharField(max_length=2, blank=True, null=True)
    jv_no = models.CharField(max_length=4, blank=True, null=True)
    expense = models.CharField(max_length=1, blank=True, null=True)
    comp_id = models.CharField(max_length=2, blank=True, null=True)
    year_id = models.CharField(max_length=2, blank=True, null=True)
    chq_no = models.CharField(max_length=30, blank=True, null=True)
    upd_date = models.DateField(blank=True, null=True)
    upd_emp_id = models.CharField(max_length=8, blank=True, null=True)
    acct_id_cs_1 = models.CharField(max_length=10, blank=True, null=True)
    acct_id_cs_2 = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_voucher'


class MVoucherdet(models.Model):
    voucher_id = models.CharField(max_length=13, blank=True, null=True)
    lineitem = models.CharField(max_length=6, blank=True, null=True)
    acct_id = models.CharField(max_length=10, blank=True, null=True)
    particulars = models.CharField(max_length=200, blank=True, null=True)
    debit = models.FloatField(blank=True, null=True)
    credit = models.FloatField(blank=True, null=True)
    emp_id = models.CharField(max_length=20, blank=True, null=True)
    exp_id = models.CharField(max_length=7, blank=True, null=True)
    sp_exp_id = models.CharField(max_length=10, blank=True, null=True)
    comp_id = models.CharField(max_length=2, blank=True, null=True)
    year_id = models.CharField(max_length=2, blank=True, null=True)
    acct_id_cs = models.CharField(max_length=10, blank=True, null=True)
    v_no = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_voucherdet'


class Nom(models.Model):
    acct_id = models.CharField(primary_key=True, max_length=10)
    acct_name = models.CharField(max_length=50)
    o_bal = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    acct_type = models.ForeignKey(AcctType, models.DO_NOTHING, db_column='acct_type', blank=True, null=True)
    fs_type = models.CharField(max_length=1, blank=True, null=True)
    sub = models.CharField(max_length=1, blank=True, null=True)
    emp_id = models.CharField(max_length=8, blank=True, null=True)
    test_name = models.CharField(max_length=50, blank=True, null=True)
    comp_id = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nom'


class NomLc(models.Model):
    acct = models.ForeignKey(Nom, models.DO_NOTHING, primary_key=True)
    open_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'nom_lc'


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


class PartyAdd(models.Model):
    party = models.ForeignKey(Party, models.DO_NOTHING)
    add_id = models.IntegerField()
    add_line1 = models.CharField(max_length=50, blank=True, null=True)
    add_line2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_add'
        unique_together = (('party', 'add_id'),)


class PartyProduct(models.Model):
    party_id = models.CharField(max_length=4)
    prod_id = models.CharField(max_length=4)
    unit_rate = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    discp = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    s_discp = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    p_rate = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    lineitem = models.IntegerField(blank=True, null=True)
    comp_id = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'party_product'
        unique_together = (('party_id', 'prod_id'),)


class PayMode(models.Model):
    mode_id = models.CharField(max_length=2)
    mode_name = models.CharField(max_length=20)
    cash_bank = models.CharField(max_length=1, blank=True, null=True)
    comp = models.ForeignKey(Company, models.DO_NOTHING)
    disb = models.CharField(max_length=1, blank=True, null=True)
    acct = models.ForeignKey(Nom, models.DO_NOTHING, blank=True, null=True)
    inhand_acct = models.ForeignKey(Nom, models.DO_NOTHING, blank=True, null=True)
    collect_acct = models.ForeignKey(Nom, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pay_mode'
        unique_together = (('comp', 'mode_id'),)


class PlInvoice(models.Model):
    inv_id = models.CharField(max_length=6)
    inv_date = models.DateField()
    emp_id = models.CharField(max_length=8, blank=True, null=True)
    inv_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    st_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dc_amt = models.IntegerField(blank=True, null=True)
    party = models.ForeignKey(Party, models.DO_NOTHING)
    inv_no = models.CharField(unique=True, max_length=5, blank=True, null=True)
    posted = models.CharField(max_length=1)
    po_no = models.CharField(max_length=30, blank=True, null=True)
    po_date = models.DateField(blank=True, null=True)
    disc_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    do_no = models.CharField(max_length=5, blank=True, null=True)
    do_date = models.DateField(blank=True, null=True)
    sin_no = models.CharField(max_length=11, blank=True, null=True)
    sin_date = models.DateField(blank=True, null=True)
    dc_no = models.CharField(max_length=5, blank=True, null=True)
    dc_date = models.DateField(blank=True, null=True)
    wo_id = models.CharField(max_length=5)
    do_desc = models.CharField(max_length=50, blank=True, null=True)
    sin_desc = models.CharField(max_length=50, blank=True, null=True)
    dc_desc = models.CharField(max_length=50, blank=True, null=True)
    add_id = models.IntegerField(blank=True, null=True)
    ut = models.CharField(max_length=1, blank=True, null=True)
    comp = models.ForeignKey('Po', models.DO_NOTHING)
    year = models.ForeignKey('Po', models.DO_NOTHING)
    loc_id = models.CharField(max_length=2)
    dc_acct_id = models.CharField(max_length=10, blank=True, null=True)
    veh_no = models.CharField(max_length=30, blank=True, null=True)
    po = models.ForeignKey('Po', models.DO_NOTHING, blank=True, null=True)
    particulars = models.CharField(max_length=100, blank=True, null=True)
    bill_no = models.CharField(max_length=30, blank=True, null=True)
    bill_date = models.DateField(blank=True, null=True)
    production = models.CharField(max_length=1)
    lot_id = models.CharField(max_length=5, blank=True, null=True)
    stax = models.CharField(max_length=1, blank=True, null=True)
    stax_refund = models.CharField(max_length=1, blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)
    sp_id = models.CharField(max_length=10, blank=True, null=True)
    hand_exp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    clear_exp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cur_id = models.CharField(max_length=2, blank=True, null=True)
    cur_rate = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    credit_days = models.IntegerField(blank=True, null=True)
    acct_id_cs = models.CharField(max_length=10, blank=True, null=True)
    freight_acct_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pl_invoice'
        unique_together = (('comp', 'year', 'inv_id'),)


class PlInvoicedet(models.Model):
    inv_id = models.CharField(max_length=6)
    lineitem = models.CharField(max_length=2)
    prod = models.ForeignKey('SlProduct', models.DO_NOTHING)
    pack_no = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    pack_qty = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    unit_qty = models.DecimalField(max_digits=10, decimal_places=3)
    unit_rate = models.DecimalField(max_digits=10, decimal_places=3)
    staxp = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    stax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    add_staxp = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    itemtot = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    comp_id = models.CharField(max_length=2)
    year_id = models.CharField(max_length=2)
    particulars = models.CharField(max_length=30, blank=True, null=True)
    sale_id = models.IntegerField(blank=True, null=True)
    pack_rate = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    hand_exp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    clear_exp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discp = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    s_discp = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    s_discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    c_duty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    add_stax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    itax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sedp = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    sed = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pl_invoicedet'
        unique_together = (('comp_id', 'year_id', 'inv_id', 'lineitem'),)


class PlInvoicedetapp(models.Model):
    inv_id = models.CharField(max_length=5)
    lineitem = models.IntegerField()
    prod_id = models.CharField(max_length=4)
    pack_no = models.IntegerField()
    pack_qty = models.DecimalField(max_digits=10, decimal_places=3)
    unit_qty = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'pl_invoicedetapp'


class PlReceipt(models.Model):
    rec_id = models.CharField(max_length=6)
    rec_date = models.DateField()
    posted = models.CharField(max_length=1)
    comp_id = models.CharField(max_length=2)
    year_id = models.CharField(max_length=2)
    emp_id = models.CharField(max_length=8, blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)
    production = models.CharField(max_length=1)
    cur_id = models.CharField(max_length=2, blank=True, null=True)
    cur_rate = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pl_receipt'
        unique_together = (('comp_id', 'year_id', 'rec_id'),)


class PlReceiptdet(models.Model):
    rec = models.ForeignKey(PlReceipt, models.DO_NOTHING)
    lineitem = models.CharField(max_length=3)
    r_no = models.CharField(max_length=10, blank=True, null=True)
    v_no = models.CharField(max_length=10, blank=True, null=True)
    party = models.ForeignKey(Party, models.DO_NOTHING)
    particulars = models.CharField(max_length=100, blank=True, null=True)
    r_date = models.DateField(blank=True, null=True)
    acct_id = models.CharField(max_length=10, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    comp = models.ForeignKey(PlReceipt, models.DO_NOTHING)
    year = models.ForeignKey(PlReceipt, models.DO_NOTHING)
    acct_id_cs = models.CharField(max_length=10, blank=True, null=True)
    f1 = models.CharField(max_length=10, blank=True, null=True)
    o_bal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pl_receiptdet'
        unique_together = (('comp', 'year', 'rec', 'lineitem'),)


class PlReceiptdetAcct(models.Model):
    rec = models.ForeignKey(PlReceiptdet, models.DO_NOTHING)
    lineitem = models.ForeignKey(PlReceiptdet, models.DO_NOTHING, db_column='lineitem')
    ser_no = models.CharField(max_length=2)
    particulars = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    mode_id = models.CharField(max_length=2, blank=True, null=True)
    chq_no = models.CharField(max_length=20, blank=True, null=True)
    chq_date = models.DateField(blank=True, null=True)
    acct_date = models.DateField(blank=True, null=True)
    comp = models.ForeignKey(PlReceiptdet, models.DO_NOTHING)
    slip_no = models.CharField(max_length=30, blank=True, null=True)
    wo_id = models.CharField(max_length=5, blank=True, null=True)
    o_bal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    year = models.ForeignKey(PlReceiptdet, models.DO_NOTHING)
    sp_id = models.CharField(max_length=4, blank=True, null=True)
    clear_date = models.DateField(blank=True, null=True)
    inhand_acct_id = models.CharField(max_length=10, blank=True, null=True)
    collect_acct_id = models.CharField(max_length=10, blank=True, null=True)
    bounce_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)
    emp_id = models.CharField(max_length=8, blank=True, null=True)
    amount_fc = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cur = models.ForeignKey(Currency, models.DO_NOTHING, blank=True, null=True)
    cur_rate = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    acct_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pl_receiptdet_acct'
        unique_together = (('comp', 'year', 'rec', 'lineitem', 'ser_no'),)


class PlReceiptdetInv(models.Model):
    rec = models.ForeignKey(PlReceiptdet, models.DO_NOTHING)
    lineitem = models.ForeignKey(PlReceiptdet, models.DO_NOTHING, db_column='lineitem')
    inv_id = models.CharField(max_length=7)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comp = models.ForeignKey(PlReceiptdet, models.DO_NOTHING)
    year = models.ForeignKey(PlReceiptdet, models.DO_NOTHING)
    line_item = models.CharField(max_length=2)
    amount_fc = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    ser_no = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pl_receiptdet_inv'
        unique_together = (('comp', 'year', 'rec', 'lineitem', 'line_item'),)


class Po(models.Model):
    po_id = models.CharField(max_length=5)
    po_date = models.DateField()
    party_id = models.CharField(max_length=7)
    comp_id = models.CharField(max_length=2)
    emp_id = models.CharField(max_length=8, blank=True, null=True)
    year_id = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'po'
        unique_together = (('comp_id', 'year_id', 'po_id'),)


class Podet(models.Model):
    po_id = models.CharField(max_length=6)
    lineitem = models.CharField(max_length=3)
    prod_id = models.CharField(max_length=4)
    unit_qty = models.DecimalField(max_digits=13, decimal_places=3)
    unit_rate = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    dmd_lineitem = models.IntegerField(blank=True, null=True)
    dmd_no = models.CharField(max_length=6, blank=True, null=True)
    rec_qty = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    rej_qty = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    comp_id = models.CharField(max_length=2)
    year_id = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'podet'
        unique_together = (('comp_id', 'year_id', 'po_id', 'lineitem'),)


class Prod(models.Model):
    p_id = models.CharField(max_length=6)
    p_date = models.DateField()
    prod = models.ForeignKey('SlProduct', models.DO_NOTHING, blank=True, null=True)
    qty = models.DecimalField(max_digits=13, decimal_places=3)
    rejected = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    d_lot_no = models.CharField(max_length=10, blank=True, null=True)
    target = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    work_nos = models.IntegerField(blank=True, null=True)
    work_time = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    std_time = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    comp_id = models.CharField(max_length=2)
    year_id = models.CharField(max_length=2)
    emp_id = models.CharField(max_length=8)
    loc_id = models.CharField(max_length=2)
    posted = models.CharField(max_length=1)
    particulars = models.CharField(max_length=100, blank=True, null=True)
    f1 = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prod'
        unique_together = (('comp_id', 'year_id', 'p_id'),)


class ProdCat(models.Model):
    cat_id = models.CharField(primary_key=True, max_length=6)
    cat_name = models.CharField(max_length=30)
    acct_id_cs = models.ForeignKey(Nom, models.DO_NOTHING, db_column='acct_id_cs', blank=True, null=True)
    acct_id = models.CharField(max_length=10, blank=True, null=True)
    grp_id = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prod_cat'


class ProdGrp(models.Model):
    grp_id = models.CharField(primary_key=True, max_length=2)
    grp_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'prod_grp'


class ProdType(models.Model):
    cat_id = models.CharField(max_length=2)
    type_id = models.CharField(max_length=2)
    type_name = models.CharField(max_length=30)
    wastep = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prod_type'
        unique_together = (('cat_id', 'type_id'),)


class Proddet(models.Model):
    p = models.ForeignKey(Prod, models.DO_NOTHING)
    lineitem = models.CharField(max_length=2)
    prod = models.ForeignKey('SlProduct', models.DO_NOTHING)
    qty = models.DecimalField(max_digits=13, decimal_places=3)
    rate = models.DecimalField(max_digits=13, decimal_places=6, blank=True, null=True)
    itemtot = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    comp = models.ForeignKey(Prod, models.DO_NOTHING)
    year = models.ForeignKey(Prod, models.DO_NOTHING)
    pur_id = models.CharField(max_length=7, blank=True, null=True)
    avg_rate = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True)
    formula = models.CharField(max_length=1, blank=True, null=True)
    con_qty = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    req_qty = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    rej_qty = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    f1 = models.CharField(max_length=4, blank=True, null=True)
    f2 = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proddet'
        unique_together = (('comp', 'year', 'p', 'lineitem'),)


class Regions(models.Model):
    reg_id = models.CharField(primary_key=True, max_length=4)
    reg_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'regions'


class Report(models.Model):
    rec_id = models.IntegerField(blank=True, null=True)
    date_from = models.DateField()
    date_to = models.DateField()
    cust_id_from = models.IntegerField(blank=True, null=True)
    cust_id_to = models.IntegerField(blank=True, null=True)
    acct_id = models.CharField(max_length=10, blank=True, null=True)
    supplier_id = models.CharField(max_length=4, blank=True, null=True)
    cash_code = models.CharField(max_length=7, blank=True, null=True)
    bank_code = models.CharField(max_length=7, blank=True, null=True)
    brand_id_from = models.IntegerField(blank=True, null=True)
    brand_id_to = models.IntegerField(blank=True, null=True)
    emp_id = models.CharField(max_length=6, blank=True, null=True)
    voucher_type = models.CharField(max_length=13, blank=True, null=True)
    inv_id_from = models.CharField(max_length=5, blank=True, null=True)
    inv_id_to = models.CharField(max_length=5, blank=True, null=True)
    posted = models.CharField(max_length=9)
    party_id = models.CharField(max_length=4, blank=True, null=True)
    sp_id = models.CharField(max_length=4, blank=True, null=True)
    prod_id = models.CharField(max_length=4, blank=True, null=True)
    comp_id = models.CharField(max_length=2, blank=True, null=True)
    loc_id = models.CharField(max_length=2, blank=True, null=True)
    year_id = models.CharField(max_length=2, blank=True, null=True)
    party_type = models.CharField(max_length=1, blank=True, null=True)
    cat_id = models.CharField(max_length=2, blank=True, null=True)
    order_by = models.CharField(max_length=20, blank=True, null=True)
    acct_id_cs = models.CharField(max_length=10, blank=True, null=True)
    currency = models.CharField(max_length=1, blank=True, null=True)
    sale_rate = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report'


class ReportCat(models.Model):
    cat_id = models.CharField(primary_key=True, max_length=2)

    class Meta:
        managed = False
        db_table = 'report_cat'


class ReportComp(models.Model):
    comp_id = models.CharField(primary_key=True, max_length=2)

    class Meta:
        managed = False
        db_table = 'report_comp'


class ReportCs(models.Model):
    acct_id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'report_cs'


class ReportDiv(models.Model):
    div_id = models.CharField(primary_key=True, max_length=2)

    class Meta:
        managed = False
        db_table = 'report_div'


class ReportParty(models.Model):
    party_id = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_party'


class ReportSp(models.Model):
    sp_id = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_sp'


class Reports(models.Model):
    file_name = models.CharField(max_length=50)
    report_name = models.CharField(max_length=100)
    cat = models.BooleanField()
    landscape = models.CharField(max_length=1)
    rep_id = models.CharField(primary_key=True, max_length=3)

    class Meta:
        managed = False
        db_table = 'reports'


class SlDc(models.Model):
    inv_id = models.CharField(max_length=6)
    inv_date = models.DateField()
    emp_id = models.CharField(max_length=8, blank=True, null=True)
    inv_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    st_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dc_amt = models.IntegerField(blank=True, null=True)
    party = models.ForeignKey(Party, models.DO_NOTHING)
    inv_no = models.CharField(max_length=10, blank=True, null=True)
    posted = models.CharField(max_length=1)
    po_no = models.CharField(max_length=30, blank=True, null=True)
    po_date = models.DateField(blank=True, null=True)
    disc_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    do_no = models.CharField(max_length=5, blank=True, null=True)
    do_date = models.DateField(blank=True, null=True)
    sin_no = models.CharField(max_length=11, blank=True, null=True)
    sin_date = models.DateField(blank=True, null=True)
    dc_no = models.CharField(max_length=5, blank=True, null=True)
    dc_date = models.DateField(blank=True, null=True)
    wo_id = models.CharField(max_length=5, blank=True, null=True)
    do_desc = models.CharField(max_length=50, blank=True, null=True)
    sin_desc = models.CharField(max_length=50, blank=True, null=True)
    dc_desc = models.CharField(max_length=50, blank=True, null=True)
    add = models.ForeignKey(PartyAdd, models.DO_NOTHING, blank=True, null=True)
    ut = models.CharField(max_length=1, blank=True, null=True)
    particulars = models.CharField(max_length=100, blank=True, null=True)
    comp = models.ForeignKey('SlPo', models.DO_NOTHING)
    year = models.ForeignKey('SlPo', models.DO_NOTHING)
    loc_id = models.CharField(max_length=2)
    dc_acct_id = models.CharField(max_length=10, blank=True, null=True)
    veh_no = models.CharField(max_length=30, blank=True, null=True)
    production = models.CharField(max_length=1, blank=True, null=True)
    lot_id = models.CharField(max_length=5, blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)
    sp_id = models.CharField(max_length=4)
    po = models.ForeignKey('SlPo', models.DO_NOTHING, blank=True, null=True)
    credit_days = models.IntegerField(blank=True, null=True)
    insert_date = models.DateField()
    status = models.CharField(max_length=1)
    sin_no_lhr = models.CharField(max_length=11, blank=True, null=True)
    sin_date_lhr = models.DateField(blank=True, null=True)
    sin_desc_lhr = models.CharField(max_length=50, blank=True, null=True)
    discp = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    sup_id = models.CharField(max_length=4, blank=True, null=True)
    acct_id_cs = models.CharField(max_length=10, blank=True, null=True)
    net_payable = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    adv_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    acct_id_cs_1 = models.CharField(max_length=10, blank=True, null=True)
    acct_id_cs_2 = models.CharField(max_length=10, blank=True, null=True)
    dc_acct_name = models.CharField(max_length=200, blank=True, null=True)
    receiver_name = models.CharField(max_length=100, blank=True, null=True)
    dc_to = models.CharField(max_length=100, blank=True, null=True)
    ogp_no = models.CharField(max_length=10, blank=True, null=True)
    vehicle = models.ForeignKey('VehicleType', models.DO_NOTHING, blank=True, null=True)
    bilty_no = models.CharField(unique=True, max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sl_dc'
        unique_together = (('comp', 'year', 'inv_id'),)


class SlDcdet(models.Model):
    inv_id = models.CharField(max_length=6)
    lineitem = models.CharField(max_length=2)
    prod = models.ForeignKey('SlProduct', models.DO_NOTHING, blank=True, null=True)
    pack_no = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    pack_qty = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    unit_qty = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    unit_rate = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    staxp = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    stax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    add_staxp = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    itemtot = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    comp_id = models.CharField(max_length=2)
    year_id = models.CharField(max_length=2)
    pur_id = models.CharField(max_length=7, blank=True, null=True)
    sale_id = models.IntegerField(blank=True, null=True)
    particulars = models.CharField(max_length=30, blank=True, null=True)
    discp = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    s_discp = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    s_discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pack_rate = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    avg_rate = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True)
    loc = models.ForeignKey(Locations, models.DO_NOTHING)
    inclusive = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sedp = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    sed = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    acct_id_cs = models.ForeignKey(Nom, models.DO_NOTHING, db_column='acct_id_cs', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sl_dcdet'
        unique_together = (('comp_id', 'year_id', 'inv_id', 'lineitem'),)


class SlInvoice(models.Model):
    inv_id = models.CharField(max_length=6)
    inv_date = models.DateField()
    emp_id = models.CharField(max_length=8, blank=True, null=True)
    inv_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    st_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dc_amt = models.IntegerField(blank=True, null=True)
    party = models.ForeignKey(Party, models.DO_NOTHING)
    inv_no = models.CharField(max_length=10, blank=True, null=True)
    posted = models.CharField(max_length=1)
    po_no = models.CharField(max_length=30, blank=True, null=True)
    po_date = models.DateField(blank=True, null=True)
    disc_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    do_no = models.CharField(max_length=5, blank=True, null=True)
    do_date = models.DateField(blank=True, null=True)
    sin_no = models.CharField(max_length=11, blank=True, null=True)
    sin_date = models.DateField(blank=True, null=True)
    dc_no = models.CharField(max_length=5, blank=True, null=True)
    dc_date = models.DateField(blank=True, null=True)
    wo_id = models.CharField(max_length=5, blank=True, null=True)
    do_desc = models.CharField(max_length=50, blank=True, null=True)
    sin_desc = models.CharField(max_length=50, blank=True, null=True)
    dc_desc = models.CharField(max_length=50, blank=True, null=True)
    add = models.ForeignKey(PartyAdd, models.DO_NOTHING, blank=True, null=True)
    ut = models.CharField(max_length=1, blank=True, null=True)
    particulars = models.CharField(max_length=100, blank=True, null=True)
    comp = models.ForeignKey('SlPo', models.DO_NOTHING)
    year = models.ForeignKey('SlPo', models.DO_NOTHING)
    loc_id = models.CharField(max_length=2)
    dc_acct_id = models.CharField(max_length=10, blank=True, null=True)
    veh_no = models.CharField(max_length=30, blank=True, null=True)
    production = models.CharField(max_length=1, blank=True, null=True)
    lot_id = models.CharField(max_length=5, blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)
    sp_id = models.CharField(max_length=4)
    po = models.ForeignKey('SlPo', models.DO_NOTHING, blank=True, null=True)
    credit_days = models.IntegerField(blank=True, null=True)
    insert_date = models.DateField()
    status = models.CharField(max_length=1)
    sin_no_lhr = models.CharField(max_length=11, blank=True, null=True)
    sin_date_lhr = models.DateField(blank=True, null=True)
    sin_desc_lhr = models.CharField(max_length=50, blank=True, null=True)
    discp = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    sup = models.ForeignKey(Party, models.DO_NOTHING, blank=True, null=True)
    acct_id_cs = models.CharField(max_length=10, blank=True, null=True)
    net_payable = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    adv_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    acct_id_cs_1 = models.CharField(max_length=10, blank=True, null=True)
    acct_id_cs_2 = models.CharField(max_length=10, blank=True, null=True)
    dc_acct_name = models.CharField(max_length=200, blank=True, null=True)
    staxp = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    bilty_no = models.CharField(max_length=10, blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sl_invoice'
        unique_together = (('comp', 'year', 'inv_id'),)


class SlInvoiceDc(models.Model):
    inv_id = models.CharField(max_length=6)
    inv_amt = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.ForeignKey(SlDc, models.DO_NOTHING)
    comp = models.ForeignKey(SlDc, models.DO_NOTHING)
    lineitem = models.CharField(max_length=3)
    dc = models.ForeignKey(SlDc, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sl_invoice_dc'
        unique_together = (('comp', 'year', 'inv_id', 'lineitem'),)


class SlInvoiceRec(models.Model):
    rec_id = models.CharField(max_length=7)
    lineitem = models.CharField(max_length=2)
    inv_id = models.CharField(max_length=5)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comp = models.ForeignKey(Company, models.DO_NOTHING)
    year = models.ForeignKey(FinYears, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sl_invoice_rec'
        unique_together = (('comp', 'year', 'inv_id', 'lineitem'),)


class SlInvoicedet(models.Model):
    inv_id = models.CharField(max_length=6)
    lineitem = models.CharField(max_length=2)
    prod = models.ForeignKey('SlProduct', models.DO_NOTHING, blank=True, null=True)
    pack_no = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    pack_qty = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    unit_qty = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    unit_rate = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    staxp = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    stax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    add_staxp = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    itemtot = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    comp_id = models.CharField(max_length=2)
    year_id = models.CharField(max_length=2)
    pur_id = models.CharField(max_length=7, blank=True, null=True)
    sale_id = models.IntegerField(blank=True, null=True)
    particulars = models.CharField(max_length=30, blank=True, null=True)
    discp = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    s_discp = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    s_discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pack_rate = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    avg_rate = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True)
    loc = models.ForeignKey(Locations, models.DO_NOTHING)
    inclusive = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sedp = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    sed = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    acct_id_cs = models.ForeignKey(Nom, models.DO_NOTHING, db_column='acct_id_cs', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sl_invoicedet'
        unique_together = (('comp_id', 'year_id', 'inv_id', 'lineitem'),)


class SlInvoicedetBon(models.Model):
    comp = models.ForeignKey(SlInvoicedet, models.DO_NOTHING)
    year = models.ForeignKey(SlInvoicedet, models.DO_NOTHING)
    inv = models.ForeignKey(SlInvoicedet, models.DO_NOTHING)
    lineitem = models.ForeignKey(SlInvoicedet, models.DO_NOTHING, db_column='lineitem')
    ser_no = models.CharField(max_length=2)
    unit_qty = models.DecimalField(max_digits=10, decimal_places=3)
    particulars = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sl_invoicedet_bon'
        unique_together = (('comp', 'year', 'inv', 'lineitem', 'ser_no'),)


class SlInvoicedetapp(models.Model):
    inv_id = models.CharField(max_length=5)
    lineitem = models.IntegerField()
    prod_id = models.CharField(max_length=4)
    pack_no = models.IntegerField()
    pack_qty = models.DecimalField(max_digits=10, decimal_places=3)
    unit_qty = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'sl_invoicedetapp'


class SlPartyAdd(models.Model):
    party_id = models.CharField(max_length=4)
    add_id = models.IntegerField()
    add_line1 = models.CharField(max_length=50, blank=True, null=True)
    add_line2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sl_party_add'
        unique_together = (('party_id', 'add_id'),)


class SlPo(models.Model):
    po_id = models.CharField(max_length=5)
    po_date = models.DateField()
    emp_id = models.CharField(max_length=8, blank=True, null=True)
    inv_amt = models.DecimalField(max_digits=10, decimal_places=2)
    st_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dc_amt = models.IntegerField(blank=True, null=True)
    party = models.ForeignKey(Party, models.DO_NOTHING)
    posted = models.CharField(max_length=1)
    po_no = models.CharField(max_length=30, blank=True, null=True)
    disc_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    particulars = models.CharField(max_length=100, blank=True, null=True)
    comp_id = models.CharField(max_length=2)
    year_id = models.CharField(max_length=2)
    loc_id = models.CharField(max_length=2)
    dc_acct_id = models.CharField(max_length=10, blank=True, null=True)
    veh_no = models.CharField(max_length=30, blank=True, null=True)
    lot_id = models.CharField(max_length=5, blank=True, null=True)
    sp_id = models.CharField(max_length=4)
    credit_days = models.IntegerField(blank=True, null=True)
    add_id = models.IntegerField(blank=True, null=True)
    wo = models.ForeignKey('SlWo', models.DO_NOTHING, blank=True, null=True)
    discp = models.IntegerField(blank=True, null=True)
    sup = models.ForeignKey(Party, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sl_po'
        unique_together = (('comp_id', 'year_id', 'po_id'),)


class SlPodet(models.Model):
    po = models.ForeignKey(SlPo, models.DO_NOTHING)
    lineitem = models.CharField(max_length=2)
    prod = models.ForeignKey('SlProduct', models.DO_NOTHING)
    unit_qty = models.DecimalField(max_digits=10, decimal_places=3)
    unit_rate = models.DecimalField(max_digits=10, decimal_places=3)
    staxp = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    stax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    add_staxp = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    itemtot = models.DecimalField(max_digits=13, decimal_places=2)
    comp = models.ForeignKey(SlPo, models.DO_NOTHING)
    year = models.ForeignKey(SlPo, models.DO_NOTHING)
    pur_id = models.CharField(max_length=7, blank=True, null=True)
    sale_id = models.IntegerField(blank=True, null=True)
    particulars = models.CharField(max_length=30, blank=True, null=True)
    discp = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    s_discp = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    s_discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pack_rate = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    avg_rate = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True)
    pack_no = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    pack_qty = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sl_podet'
        unique_together = (('comp', 'year', 'po', 'lineitem'),)


class SlPodetBon(models.Model):
    comp = models.ForeignKey(SlPodet, models.DO_NOTHING)
    year = models.ForeignKey(SlPodet, models.DO_NOTHING)
    po = models.ForeignKey(SlPodet, models.DO_NOTHING)
    lineitem = models.ForeignKey(SlPodet, models.DO_NOTHING, db_column='lineitem')
    ser_no = models.CharField(max_length=2)
    unit_qty = models.DecimalField(max_digits=10, decimal_places=3)
    particulars = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sl_podet_bon'
        unique_together = (('comp', 'year', 'po', 'lineitem', 'ser_no'),)


class SlProduct(models.Model):
    prod_id = models.CharField(primary_key=True, max_length=4)
    prod_name = models.CharField(max_length=50)
    unit = models.CharField(max_length=10)
    unit_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    staxp = models.DecimalField(max_digits=6, decimal_places=2)
    o_qty = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    o_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cat = models.ForeignKey(ProdCat, models.DO_NOTHING)
    type = models.ForeignKey(ProdType, models.DO_NOTHING)
    batchwise = models.CharField(max_length=1)
    reg_no = models.CharField(max_length=10, blank=True, null=True)
    pack_size = models.CharField(max_length=10, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    p_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    type_grp = models.CharField(max_length=1)
    pack_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    all_cust = models.CharField(max_length=1, blank=True, null=True)
    discp = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    s_discp = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    comp_id = models.CharField(max_length=2)
    mol_qty = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    grp_id = models.CharField(max_length=2, blank=True, null=True)
    mol = models.CharField(max_length=1, blank=True, null=True)
    std_wt = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sl_product'


class SlProductBrand(models.Model):
    prod_id = models.CharField(max_length=4)
    lineitem = models.IntegerField()
    prod_name = models.CharField(max_length=50)
    comp_id = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'sl_product_brand'
        unique_together = (('prod_id', 'lineitem'),)


class SlProductRm(models.Model):
    prod_id = models.CharField(max_length=4)
    prod_fac = models.DecimalField(max_digits=13, decimal_places=6)
    lineitem = models.IntegerField()
    rm_id = models.CharField(max_length=4)
    comp_id = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'sl_product_rm'
        unique_together = (('prod_id', 'lineitem'),)


class SlProductsLog(models.Model):
    prod_id = models.CharField(primary_key=True, max_length=4)
    prod_name = models.CharField(max_length=50)
    unit = models.CharField(max_length=10)
    unit_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    staxp = models.DecimalField(max_digits=6, decimal_places=2)
    post_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'sl_products_log'


class SlQuote(models.Model):
    inv_id = models.CharField(max_length=5)
    inv_date = models.DateField()
    emp_id = models.CharField(max_length=8, blank=True, null=True)
    inv_amt = models.DecimalField(max_digits=10, decimal_places=2)
    st_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dc_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    party_id = models.CharField(max_length=4)
    inv_no = models.CharField(unique=True, max_length=5, blank=True, null=True)
    posted = models.CharField(max_length=1)
    po_no = models.CharField(max_length=30, blank=True, null=True)
    po_date = models.DateField(blank=True, null=True)
    disc_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    do_no = models.CharField(max_length=5, blank=True, null=True)
    do_date = models.DateField(blank=True, null=True)
    sin_no = models.CharField(max_length=11, blank=True, null=True)
    sin_date = models.DateField(blank=True, null=True)
    dc_no = models.CharField(max_length=5, blank=True, null=True)
    dc_date = models.DateField(blank=True, null=True)
    wo_id = models.CharField(max_length=5)
    do_desc = models.CharField(max_length=50, blank=True, null=True)
    sin_desc = models.CharField(max_length=50, blank=True, null=True)
    dc_desc = models.CharField(max_length=50, blank=True, null=True)
    add_id = models.IntegerField(blank=True, null=True)
    ut = models.CharField(max_length=1, blank=True, null=True)
    particulars = models.CharField(max_length=100, blank=True, null=True)
    comp_id = models.CharField(max_length=2)
    year_id = models.CharField(max_length=2)
    loc_id = models.CharField(max_length=2)
    dc_acct_id = models.CharField(max_length=10, blank=True, null=True)
    veh_no = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sl_quote'
        unique_together = (('comp_id', 'year_id', 'inv_id'),)


class SlQuotedet(models.Model):
    inv_id = models.CharField(max_length=5)
    lineitem = models.CharField(max_length=3)
    prod_id = models.CharField(max_length=4)
    pack_no = models.DecimalField(max_digits=10, decimal_places=3)
    pack_qty = models.DecimalField(max_digits=10, decimal_places=3)
    unit_qty = models.DecimalField(max_digits=10, decimal_places=3)
    unit_rate = models.DecimalField(max_digits=10, decimal_places=3)
    staxp = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    stax = models.IntegerField(blank=True, null=True)
    add_staxp = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    itemtot = models.DecimalField(max_digits=13, decimal_places=2)
    comp_id = models.CharField(max_length=2)
    year_id = models.CharField(max_length=2)
    pur_id = models.CharField(max_length=7, blank=True, null=True)
    sale_id = models.IntegerField(blank=True, null=True)
    particulars = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sl_quotedet'
        unique_together = (('comp_id', 'year_id', 'inv_id', 'lineitem'),)


class SlReceipt(models.Model):
    rec_id = models.CharField(max_length=6)
    rec_date = models.DateField()
    posted = models.CharField(max_length=1)
    comp_id = models.CharField(max_length=2)
    year_id = models.CharField(max_length=2)
    emp_id = models.CharField(max_length=8, blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)
    production = models.CharField(max_length=1)
    insert_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'sl_receipt'
        unique_together = (('comp_id', 'year_id', 'rec_id'),)


class SlReceiptBak(models.Model):
    rec_id = models.CharField(max_length=5)
    rec_date = models.DateField()
    posted = models.CharField(max_length=1)
    comp_id = models.CharField(max_length=2)
    year_id = models.CharField(max_length=2)
    emp_id = models.CharField(max_length=8)
    sort_order = models.IntegerField(blank=True, null=True)
    production = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'sl_receipt_bak'


class SlReceiptdet(models.Model):
    rec = models.ForeignKey(SlReceipt, models.DO_NOTHING)
    lineitem = models.CharField(max_length=3)
    r_no = models.CharField(max_length=10, blank=True, null=True)
    v_no = models.CharField(max_length=10, blank=True, null=True)
    party = models.ForeignKey(Party, models.DO_NOTHING)
    particulars = models.CharField(max_length=100, blank=True, null=True)
    r_date = models.DateField(blank=True, null=True)
    acct = models.ForeignKey(Nom, models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    inv_no = models.CharField(max_length=5, blank=True, null=True)
    comp = models.ForeignKey(SlReceipt, models.DO_NOTHING)
    year = models.ForeignKey(SlReceipt, models.DO_NOTHING)
    insert_date = models.DateField()
    o_bal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    acct_id_cs = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sl_receiptdet'
        unique_together = (('comp', 'year', 'rec', 'lineitem'),)


class SlReceiptdetAcct(models.Model):
    rec_id = models.CharField(max_length=6)
    lineitem = models.CharField(max_length=3)
    ser_no = models.CharField(max_length=2, blank=True, null=True)
    particulars = models.CharField(max_length=50, blank=True, null=True)
    amount = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    mode_id = models.CharField(max_length=2, blank=True, null=True)
    chq_no = models.CharField(max_length=20, blank=True, null=True)
    chq_date = models.DateField(blank=True, null=True)
    acct = models.ForeignKey(Nom, models.DO_NOTHING)
    acct_date = models.DateField(blank=True, null=True)
    comp_id = models.CharField(max_length=2)
    slip_no = models.CharField(max_length=30, blank=True, null=True)
    wo = models.ForeignKey('SlWo', models.DO_NOTHING, blank=True, null=True)
    o_bal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    year_id = models.CharField(max_length=2)
    sp = models.ForeignKey('Sp', models.DO_NOTHING, blank=True, null=True)
    clear_date = models.DateField(blank=True, null=True)
    inhand_acct = models.ForeignKey(Nom, models.DO_NOTHING, blank=True, null=True)
    collect_acct = models.ForeignKey(Nom, models.DO_NOTHING, blank=True, null=True)
    bounce_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sl_receiptdet_acct'


class SlReceiptdetAcctLog(models.Model):
    rec_id = models.CharField(max_length=6)
    lineitem = models.CharField(max_length=3)
    ser_no = models.CharField(max_length=2)
    post_date = models.DateField()
    acct_date = models.DateField(blank=True, null=True)
    clear_date = models.DateField(blank=True, null=True)
    bounce_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)
    comp_id = models.CharField(max_length=2)
    year_id = models.CharField(max_length=2)
    particulars = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sl_receiptdet_acct_log'


class SlReceiptdetBak(models.Model):
    rec_id = models.CharField(max_length=5)
    lineitem = models.CharField(max_length=2)
    r_no = models.CharField(max_length=10, blank=True, null=True)
    v_no = models.CharField(max_length=10, blank=True, null=True)
    party_id = models.CharField(max_length=10)
    particulars = models.CharField(max_length=100, blank=True, null=True)
    r_date = models.DateField(blank=True, null=True)
    acct_id = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    inv_no = models.CharField(max_length=5, blank=True, null=True)
    comp_id = models.CharField(max_length=2)
    year_id = models.CharField(max_length=2)
    insert_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'sl_receiptdet_bak'


class SlReceiptdetDisb(models.Model):
    comp_id = models.CharField(max_length=2, blank=True, null=True)
    year_id = models.CharField(max_length=2, blank=True, null=True)
    rec_id = models.CharField(max_length=6, blank=True, null=True)
    lineitem = models.CharField(max_length=2, blank=True, null=True)
    ser_no = models.CharField(max_length=1, blank=True, null=True)
    acct_id = models.CharField(max_length=10, blank=True, null=True)
    particulars = models.CharField(max_length=50, blank=True, null=True)
    amount = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    rec_no = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'sl_receiptdet_disb'


class SlReceiptdetInv(models.Model):
    rec_id = models.CharField(max_length=6)
    lineitem = models.CharField(max_length=3)
    inv_id = models.CharField(max_length=5)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comp = models.ForeignKey(Company, models.DO_NOTHING)
    year = models.ForeignKey(FinYears, models.DO_NOTHING)
    line_item = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'sl_receiptdet_inv'
        unique_together = (('comp', 'year', 'rec_id', 'lineitem', 'line_item'),)


class SlReceiptdetItax(models.Model):
    comp_id = models.CharField(max_length=2)
    year_id = models.CharField(max_length=2)
    rec_id = models.CharField(max_length=6)
    lineitem = models.CharField(max_length=2)
    ser_no = models.CharField(max_length=1)
    rec_no = models.CharField(max_length=1)
    line_item = models.CharField(max_length=1)
    ch_date = models.DateField()
    ch_amt = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'sl_receiptdet_itax'


class SlReturn(models.Model):
    inv_id = models.CharField(max_length=5)
    inv_date = models.DateField()
    emp_id = models.CharField(max_length=8, blank=True, null=True)
    inv_amt = models.IntegerField(blank=True, null=True)
    st_amt = models.IntegerField(blank=True, null=True)
    dc_amt = models.IntegerField(blank=True, null=True)
    party_id = models.CharField(max_length=4)
    old_party = models.CharField(max_length=10, blank=True, null=True)
    inv_no = models.CharField(max_length=5, blank=True, null=True)
    posted = models.CharField(max_length=1)
    po_no = models.CharField(max_length=30, blank=True, null=True)
    po_date = models.DateField(blank=True, null=True)
    disc_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    do_no = models.CharField(max_length=5, blank=True, null=True)
    do_date = models.DateField(blank=True, null=True)
    sin_no = models.CharField(max_length=11, blank=True, null=True)
    sin_date = models.DateField(blank=True, null=True)
    dc_no = models.CharField(max_length=5, blank=True, null=True)
    dc_date = models.DateField(blank=True, null=True)
    wo_id = models.CharField(max_length=5, blank=True, null=True)
    do_desc = models.CharField(max_length=50, blank=True, null=True)
    sin_desc = models.CharField(max_length=50, blank=True, null=True)
    dc_desc = models.CharField(max_length=50, blank=True, null=True)
    sin_no_lhr = models.CharField(max_length=11, blank=True, null=True)
    sin_date_lhr = models.DateField(blank=True, null=True)
    sin_desc_lhr = models.CharField(max_length=50, blank=True, null=True)
    inv_id_rtn = models.CharField(max_length=5)
    stax_exp_acct = models.CharField(max_length=1)
    ut = models.CharField(max_length=1, blank=True, null=True)
    comp_id = models.CharField(max_length=2)
    year_id = models.CharField(max_length=2)
    loc_id = models.CharField(max_length=2)
    production = models.CharField(max_length=1, blank=True, null=True)
    particulars = models.CharField(max_length=100, blank=True, null=True)
    through = models.CharField(max_length=100, blank=True, null=True)
    lot_id = models.CharField(max_length=5, blank=True, null=True)
    dc_acct_id = models.CharField(max_length=10, blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)
    sp = models.ForeignKey('Sp', models.DO_NOTHING, blank=True, null=True)
    veh_no = models.CharField(max_length=30, blank=True, null=True)
    add_id = models.IntegerField(blank=True, null=True)
    insert_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'sl_return'
        unique_together = (('comp_id', 'year_id', 'inv_id'),)


class SlReturndet(models.Model):
    inv_id = models.CharField(max_length=5)
    lineitem = models.CharField(max_length=2)
    prod_id = models.CharField(max_length=4)
    pack_no = models.IntegerField(blank=True, null=True)
    pack_qty = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    unit_qty = models.DecimalField(max_digits=10, decimal_places=3)
    unit_rate = models.DecimalField(max_digits=10, decimal_places=3)
    staxp = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    stax = models.IntegerField(blank=True, null=True)
    add_staxp = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    itemtot = models.BigIntegerField()
    comp_id = models.CharField(max_length=2)
    year_id = models.CharField(max_length=2)
    discp = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    s_discp = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    s_discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    particulars = models.CharField(max_length=30, blank=True, null=True)
    damaged = models.CharField(max_length=1, blank=True, null=True)
    avg_rate = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sl_returndet'
        unique_together = (('comp_id', 'year_id', 'inv_id', 'lineitem'),)


class SlSa(models.Model):
    sa_id = models.CharField(max_length=5)
    sa_date = models.DateField()
    posted = models.CharField(max_length=1)
    comp_id = models.CharField(max_length=2)
    year_id = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'sl_sa'
        unique_together = (('comp_id', 'year_id', 'sa_id'),)


class SlSadet(models.Model):
    sa_id = models.CharField(max_length=5)
    lineitem = models.IntegerField()
    party_id = models.CharField(max_length=4)
    acct_id = models.CharField(max_length=10)
    particulars = models.CharField(max_length=30, blank=True, null=True)
    amount = models.IntegerField()
    sp_id = models.CharField(max_length=4)
    div_id = models.CharField(max_length=2)
    city_id = models.CharField(max_length=2)
    wo_id = models.CharField(max_length=5)
    comp_id = models.CharField(max_length=2)
    year_id = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'sl_sadet'
        unique_together = (('comp_id', 'year_id', 'sa_id', 'lineitem'),)


class SlWo(models.Model):
    wo_id = models.CharField(primary_key=True, max_length=5)
    wo_date = models.DateField()
    particulars = models.CharField(max_length=100, blank=True, null=True)
    party = models.ForeignKey(Party, models.DO_NOTHING)
    sp_id = models.CharField(max_length=4, blank=True, null=True)
    o_bal = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    wo_name = models.CharField(max_length=50, blank=True, null=True)
    div = models.ForeignKey(Division, models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sl_wo'


class So(models.Model):
    so_id = models.CharField(primary_key=True, max_length=5)
    so_date = models.DateField()
    party_id = models.CharField(max_length=7)
    comp_id = models.CharField(max_length=2)
    emp_id = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'so'


class Sodet(models.Model):
    so_id = models.CharField(max_length=6)
    lineitem = models.CharField(max_length=3)
    prod_id = models.CharField(max_length=4)
    ord_qty = models.DecimalField(max_digits=13, decimal_places=3)
    ord_rate = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sodet'
        unique_together = (('so_id', 'lineitem'),)


class Sp(models.Model):
    emp_id = models.CharField(max_length=6)
    sp_id = models.CharField(primary_key=True, max_length=4)
    sp_name = models.CharField(max_length=50, blank=True, null=True)
    div_id = models.CharField(max_length=2, blank=True, null=True)
    city_id = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp'


class SpBak(models.Model):
    emp_id = models.CharField(max_length=6, blank=True, null=True)
    sp_id = models.CharField(max_length=4)
    sp_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_bak'


class SpParty(models.Model):
    sp_id = models.CharField(max_length=4)
    lineitem = models.IntegerField()
    party = models.ForeignKey(Party, models.DO_NOTHING)
    emp_id = models.CharField(max_length=8, blank=True, null=True)
    o_bal = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    inactive_sl = models.CharField(max_length=1, blank=True, null=True)
    inactive_sr = models.CharField(max_length=1, blank=True, null=True)
    inactive_sa = models.CharField(max_length=1, blank=True, null=True)
    inactive_rtn = models.CharField(max_length=1, blank=True, null=True)
    comp_id = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'sp_party'
        unique_together = (('sp_id', 'party'),)


class StaxRem(models.Model):
    staxp_name = models.CharField(max_length=50)
    staxp = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'stax_rem'


class System(models.Model):
    duty_bl = models.CharField(max_length=7, blank=True, null=True)
    duty_pl = models.CharField(max_length=7, blank=True, null=True)
    app_path = models.CharField(max_length=50, blank=True, null=True)
    cash = models.CharField(max_length=7, blank=True, null=True)
    creditors = models.CharField(max_length=10, blank=True, null=True)
    lc_margin = models.CharField(max_length=10, blank=True, null=True)
    debtors = models.CharField(max_length=10, blank=True, null=True)
    sales_tax = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    add_sales_tax = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    sl_rebate = models.CharField(max_length=7, blank=True, null=True)
    freight = models.CharField(max_length=7, blank=True, null=True)
    app_title = models.CharField(max_length=50, blank=True, null=True)
    date_from = models.DateField()
    date_to = models.DateField()
    inactive = models.CharField(max_length=1, blank=True, null=True)
    date_closing_cp = models.DateField()
    date_closing_cr = models.DateField()
    date_closing_bp = models.DateField()
    date_closing_br = models.DateField()
    date_closing_jv = models.DateField()
    date_closing_bj = models.DateField()
    date_closing_sl = models.DateField()
    date_closing_sr = models.DateField()
    bp = models.DateField(blank=True, null=True)
    date_closing_sa = models.DateField()
    date_closing_rtn = models.DateField()
    date_closing_pl = models.DateField(blank=True, null=True)
    date_closing_ft = models.DateField(blank=True, null=True)
    comp_id = models.CharField(max_length=2, blank=True, null=True)
    year_id = models.CharField(max_length=2, blank=True, null=True)
    date_closing_fg = models.DateField()
    date_closing_pc = models.DateField()
    app_type = models.CharField(max_length=1, blank=True, null=True)
    date_closing_pp = models.DateField()
    lock_prod_supp = models.CharField(max_length=1, blank=True, null=True)
    stax_exp_acct_id = models.CharField(max_length=10, blank=True, null=True)
    stax_pay_acct_id = models.CharField(max_length=10, blank=True, null=True)
    dc_acct_id = models.CharField(max_length=10, blank=True, null=True)
    disc_acct_id = models.CharField(max_length=10, blank=True, null=True)
    sales_acct_id = models.CharField(max_length=10, blank=True, null=True)
    pack_size = models.CharField(max_length=1)
    cogs_acct_id = models.CharField(max_length=10, blank=True, null=True)
    app_cust = models.CharField(max_length=10, blank=True, null=True)
    rtn_acct_id = models.CharField(max_length=10, blank=True, null=True)
    stock_acct_id = models.CharField(max_length=10, blank=True, null=True)
    rptsrv = models.CharField(max_length=30)
    cash_acct_id = models.CharField(max_length=10, blank=True, null=True)
    bank_acct_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system'


class TVPAl(models.Model):
    party_id = models.CharField(max_length=4, blank=True, null=True)
    inv_id = models.CharField(max_length=8, blank=True, null=True)
    inv_date = models.DateField(blank=True, null=True)
    particulars = models.CharField(max_length=153, blank=True, null=True)
    db = models.FloatField(blank=True, null=True)
    cr = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_v_p_al'


class Users(models.Model):
    emp_id = models.CharField(primary_key=True, max_length=20)
    emp_name = models.CharField(max_length=40)
    password = models.CharField(max_length=20, blank=True, null=True)
    auth_id = models.CharField(max_length=1, blank=True, null=True)
    use_form = models.CharField(max_length=1, blank=True, null=True)
    use_rep = models.CharField(max_length=1, blank=True, null=True)
    logged = models.CharField(max_length=1, blank=True, null=True)
    comp_id = models.CharField(max_length=2, blank=True, null=True)
    year_id = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class UsersComp(models.Model):
    emp = models.ForeignKey(Users, models.DO_NOTHING)
    comp = models.ForeignKey(Company, models.DO_NOTHING)
    logged = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_comp'
        unique_together = (('emp', 'comp'),)


class UsersMod(models.Model):
    emp_id = models.CharField(max_length=20)
    voucher_type = models.ForeignKey(AppMod, models.DO_NOTHING, db_column='voucher_type')

    class Meta:
        managed = False
        db_table = 'users_mod'
        unique_together = (('emp_id', 'voucher_type'),)


class UsersRep(models.Model):
    emp = models.ForeignKey(Users, models.DO_NOTHING)
    rep = models.ForeignKey(Reports, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_rep'
        unique_together = (('emp', 'rep'),)


class VehicleType(models.Model):
    vehicle_id = models.CharField(primary_key=True, max_length=4)
    vehicle_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle_type'


class Voucher(models.Model):
    voucher_id = models.CharField(max_length=13)
    voucher_date = models.DateField(blank=True, null=True)
    post_date = models.DateField(blank=True, null=True)
    acct = models.ForeignKey(Nom, models.DO_NOTHING, blank=True, null=True)
    particulars = models.CharField(max_length=200, blank=True, null=True)
    emp_id = models.CharField(max_length=20, blank=True, null=True)
    posted = models.CharField(max_length=1, blank=True, null=True)
    jv_no = models.CharField(max_length=4, blank=True, null=True)
    expense = models.CharField(max_length=1, blank=True, null=True)
    comp_id = models.CharField(max_length=2)
    year_id = models.CharField(max_length=2)
    chq_no = models.CharField(max_length=30, blank=True, null=True)
    upd_date = models.DateField(blank=True, null=True)
    upd_emp_id = models.CharField(max_length=8, blank=True, null=True)
    acct_id_cs_1 = models.ForeignKey(Nom, models.DO_NOTHING, db_column='acct_id_cs_1', blank=True, null=True)
    acct_id_cs_2 = models.ForeignKey(Nom, models.DO_NOTHING, db_column='acct_id_cs_2', blank=True, null=True)
    bilty_no = models.ForeignKey(SlDc, models.DO_NOTHING, db_column='bilty_no', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voucher'
        unique_together = (('comp_id', 'year_id', 'voucher_id'),)


class Voucherdet(models.Model):
    voucher = models.ForeignKey(Voucher, models.DO_NOTHING)
    lineitem = models.CharField(max_length=6)
    acct = models.ForeignKey(Nom, models.DO_NOTHING, blank=True, null=True)
    particulars = models.CharField(max_length=200, blank=True, null=True)
    debit = models.FloatField(blank=True, null=True)
    credit = models.FloatField(blank=True, null=True)
    emp_id = models.CharField(max_length=20, blank=True, null=True)
    exp_id = models.CharField(max_length=7, blank=True, null=True)
    sp_exp_id = models.CharField(max_length=10, blank=True, null=True)
    comp = models.ForeignKey(Voucher, models.DO_NOTHING)
    year = models.ForeignKey(Voucher, models.DO_NOTHING)
    acct_id_cs = models.ForeignKey(Nom, models.DO_NOTHING, db_column='acct_id_cs', blank=True, null=True)
    chasis_no = models.CharField(max_length=50, blank=True, null=True)
    v_no = models.CharField(max_length=10, blank=True, null=True)
    usd = models.CharField(max_length=1, blank=True, null=True)
    er = models.FloatField(blank=True, null=True)
    unit_rate = models.FloatField(blank=True, null=True)
    tt_no = models.CharField(max_length=30, blank=True, null=True)
    reg_no = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voucherdet'
        unique_together = (('comp', 'year', 'voucher', 'lineitem'),)
