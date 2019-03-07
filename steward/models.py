# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=128)
    customer_address = models.CharField(max_length=128)
    customer_link_man = models.CharField(max_length=20, blank=True, null=True)
    customer_tel = models.CharField(max_length=128, blank=True, null=True)
    customer_principal = models.IntegerField()
    customer_remark = models.CharField(max_length=128, blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    row_status = models.IntegerField(blank=True, null=True)
    eid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customer'
        verbose_name = "客户"
        verbose_name_plural = "客户"


class Enterprise(models.Model):
    eid = models.AutoField(primary_key=True)
    enterprise_name = models.CharField(max_length=50)
    enterprise_link_man = models.CharField(max_length=20, blank=True, null=True)
    enterprise_link_tel = models.CharField(max_length=128, blank=True, null=True)
    enterprise_juridical = models.CharField(max_length=20, blank=True, null=True)
    enterprise_logo = models.CharField(max_length=128, blank=True, null=True)
    enterprise_type = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)
    row_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enterprise'
        verbose_name = "企业"
        verbose_name_plural = "企业"


class EnterpriseDepartment(models.Model):
    dept_id = models.CharField(primary_key=True, max_length=20)
    dept_name = models.CharField(max_length=20)
    dept_remark = models.CharField(max_length=128, blank=True, null=True)
    eid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'enterprise_department'
        verbose_name = "企业部门"
        verbose_name_plural = "企业部门"


class Order(models.Model):
    order_id = models.CharField(primary_key=True, max_length=20)
    order_type = models.IntegerField()
    order_money = models.DecimalField(max_digits=10, decimal_places=5)
    order_review_status = models.IntegerField()
    order_reviewer = models.IntegerField(blank=True, null=True)
    order_review_time = models.DateTimeField(blank=True, null=True)
    order_remark = models.CharField(max_length=128, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    order_status = models.IntegerField()
    eid = models.IntegerField()
    row_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order'
        verbose_name = "订单"
        verbose_name_plural = "订单"


class OrderDetails(models.Model):
    od_id = models.CharField(primary_key=True, max_length=25)
    storage_stock_id = models.IntegerField()
    num = models.DecimalField(max_digits=10, decimal_places=5)
    price = models.DecimalField(max_digits=10, decimal_places=5)
    sum = models.DecimalField(max_digits=10, decimal_places=5)
    remark = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_details'
        verbose_name = "订单详情"
        verbose_name_plural = "订单详情"


class OrderReturned(models.Model):
    order_id = models.CharField(max_length=20)
    or_id = models.CharField(primary_key=True, max_length=20)
    returned_reviewer = models.IntegerField(blank=True, null=True)
    returned_money = models.DecimalField(max_digits=10, decimal_places=5)
    returned_review_status = models.IntegerField()
    remark = models.CharField(max_length=128, blank=True, null=True)
    renturned_review_time = models.DateTimeField(blank=True, null=True)
    create_uid = models.IntegerField()
    create_time = models.DateTimeField()
    returned_status = models.IntegerField()
    eid = models.IntegerField()
    row_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_returned'
        verbose_name = "退货单"
        verbose_name_plural = "退货单"


class OrderReturnedDetails(models.Model):
    rd_id = models.CharField(primary_key=True, max_length=25)
    storage_stock_id = models.IntegerField()
    num = models.DecimalField(max_digits=10, decimal_places=0)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    sum = models.DecimalField(max_digits=10, decimal_places=0)
    remark = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_returned_details'
        verbose_name = "退货单详情"
        verbose_name_plural = "退货单详情"


class Prodcut(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=128)
    product_class = models.IntegerField()
    product_describe = models.CharField(max_length=500, blank=True, null=True)
    product_remark = models.CharField(max_length=128, blank=True, null=True)
    create_uid = models.IntegerField()
    create_time = models.DateTimeField()
    update_uid = models.IntegerField()
    update_time = models.DateTimeField()
    eid = models.IntegerField()
    row_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prodcut'
        verbose_name = "产品详情"
        verbose_name_plural = "产品详情"


class ProductClass(models.Model):
    pc_id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=128)
    class_fid = models.IntegerField()
    class_remakr = models.CharField(max_length=128, blank=True, null=True)
    create_time = models.DateTimeField()
    create_uid = models.IntegerField()
    update_time = models.DateTimeField()
    update_uid = models.IntegerField()
    eid = models.IntegerField()
    row_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_class'
        verbose_name = "产品分类"
        verbose_name_plural = "产品分类"


class ProductDetails(models.Model):
    pd_id = models.AutoField(primary_key=True)
    pd_unit = models.IntegerField()
    pd_standard = models.IntegerField()
    pd_price = models.DecimalField(max_digits=10, decimal_places=5)
    pd_remark = models.CharField(max_length=128)
    create_time = models.DateTimeField()
    create_uid = models.IntegerField()
    update_time = models.DateTimeField()
    update_uid = models.IntegerField()
    eid = models.IntegerField()
    row_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_details'
        verbose_name = "产品详情"
        verbose_name_plural = "产品详情"


class ProductStandard(models.Model):
    ps_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    standard_name = models.CharField(max_length=30)
    create_time = models.DateTimeField()
    create_uid = models.IntegerField()
    eid = models.IntegerField()
    row_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_standard'
        verbose_name = "产品规格"
        verbose_name_plural = "产品规格"


class ProductUnit(models.Model):
    unit_id = models.AutoField(primary_key=True)
    unit_name = models.CharField(max_length=20)
    create_uid = models.IntegerField()
    create_time = models.DateTimeField()
    unit_remark = models.CharField(max_length=128, blank=True, null=True)
    eid = models.IntegerField()
    row_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_unit'
        verbose_name = "产品单位"
        verbose_name_plural = "产品单位"


class Storage(models.Model):
    storage_id = models.CharField(primary_key=True, max_length=20)
    storage_name = models.CharField(max_length=50)
    storage_address = models.CharField(max_length=128)
    storage_principal = models.IntegerField()
    create_time = models.DateTimeField()
    eid = models.IntegerField()
    row_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'storage'
        verbose_name = "仓库"
        verbose_name_plural = "仓库"


class StorageStock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    storage_location = models.CharField(max_length=20)
    storage_id = models.IntegerField()
    product_id = models.IntegerField()
    stock_num = models.DecimalField(max_digits=10, decimal_places=5)
    unit_id = models.IntegerField()
    supplier_id = models.IntegerField()
    first_in = models.DateTimeField(blank=True, null=True)
    last_out = models.DateTimeField(blank=True, null=True)
    eid = models.IntegerField(blank=True, null=True)
    row_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'storage_stock'
        verbose_name = "库存"
        verbose_name_plural = "库存"


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=20)
    supplier_address = models.CharField(max_length=128)
    supplier_phone = models.CharField(max_length=50, blank=True, null=True)
    supplier_fax = models.CharField(max_length=50, blank=True, null=True)
    supplier_link_man = models.CharField(max_length=20, blank=True, null=True)
    supplier_remark = models.CharField(max_length=128, blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)
    row_status = models.IntegerField(blank=True, null=True)
    eid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'supplier'
        verbose_name = "供应商"
        verbose_name_plural = "供应商"


class UserLoginHistory(models.Model):
    history_id = models.AutoField(primary_key=True, verbose_name="记录id")
    token = models.CharField(max_length=128, verbose_name="令牌")
    ip = models.CharField(max_length=50, verbose_name="ip")
    create_time = models.DateTimeField(blank=True, null=True, verbose_name="创建时间")
    remember = models.IntegerField(verbose_name="记住我")
    uid = models.IntegerField(verbose_name="用户id")

    class Meta:
        managed = False
        db_table = 'user_login_history'
        verbose_name = "用户登录历史"
        verbose_name_plural = "用户登录历史数据"
