# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    addressid = models.AutoField(db_column='AddressID', primary_key=True, db_comment='Primary key for Address record')  # Field name made lowercase.
    addressline1 = models.CharField(db_column='AddressLine1', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', db_comment='First street address line.')  # Field name made lowercase.
    addressline2 = models.CharField(db_column='AddressLine2', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True, db_comment='Second street address line.')  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', db_comment='Name of the city.')  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', db_comment='Postal code for the street add')  # Field name made lowercase.
    rowguid = models.CharField(unique=True, max_length=36, db_comment='ROWGUIDCOL number uniquely ide')
    modifieddate = models.DateTimeField(db_column='ModifiedDate', db_comment='Date and time the record was l')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Address'
        db_table_comment = 'Street address information for'


class Customer(models.Model):
    customerid = models.AutoField(db_column='CustomerID', primary_key=True, db_comment='Primary key for Customer recor')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True, db_comment='A courtesy title. For example,')  # Field name made lowercase.
    suffix = models.CharField(db_column='Suffix', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True, db_comment='Surname suffix. For example, S')  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True, db_comment="The customer's organization.")  # Field name made lowercase.
    salesperson = models.CharField(db_column='SalesPerson', max_length=256, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True, db_comment="The customer's sales person, a")  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True, db_comment='E-mail address for the person.')  # Field name made lowercase.
    passwordhash = models.CharField(db_column='PasswordHash', max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS', db_comment='Password for the e-mail accoun')  # Field name made lowercase.
    passwordsalt = models.CharField(db_column='PasswordSalt', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', db_comment='Random value concatenated with')  # Field name made lowercase.
    rowguid = models.CharField(unique=True, max_length=36, db_comment='ROWGUIDCOL number uniquely ide')
    modifieddate = models.DateTimeField(db_column='ModifiedDate', db_comment='Date and time the record was l')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Customer'
        db_table_comment = 'Customer information.'


class Customeraddress(models.Model):
    customerid = models.OneToOneField(Customer, models.DO_NOTHING, db_column='CustomerID', primary_key=True, db_comment='Primary key. Foreign key to Cu')  # Field name made lowercase. The composite primary key (CustomerID, AddressID) found, that is not supported. The first column is selected.
    addressid = models.ForeignKey(Address, models.DO_NOTHING, db_column='AddressID', db_comment='Primary key. Foreign key to Ad')  # Field name made lowercase.
    rowguid = models.CharField(unique=True, max_length=36, db_comment='ROWGUIDCOL number uniquely ide')
    modifieddate = models.DateTimeField(db_column='ModifiedDate', db_comment='Date and time the record was l')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CustomerAddress'
        unique_together = (('customerid', 'addressid'),)
        db_table_comment = 'Cross-reference table mapping '


class Product(models.Model):
    productid = models.AutoField(db_column='ProductID', primary_key=True, db_comment='Primary key for Product record')  # Field name made lowercase.
    productnumber = models.CharField(db_column='ProductNumber', unique=True, max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', db_comment='Unique product identification ')  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True, db_comment='Product color.')  # Field name made lowercase.
    standardcost = models.DecimalField(db_column='StandardCost', max_digits=19, decimal_places=4, db_comment='Standard cost of the product.')  # Field name made lowercase.
    listprice = models.DecimalField(db_column='ListPrice', max_digits=19, decimal_places=4, db_comment='Selling price.')  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True, db_comment='Product size.')  # Field name made lowercase.
    weight = models.DecimalField(db_column='Weight', max_digits=8, decimal_places=2, blank=True, null=True, db_comment='Product weight.')  # Field name made lowercase.
    productcategoryid = models.ForeignKey('Productcategory', models.DO_NOTHING, db_column='ProductCategoryID', blank=True, null=True, db_comment='Product is a member of this pr')  # Field name made lowercase.
    productmodelid = models.ForeignKey('Productmodel', models.DO_NOTHING, db_column='ProductModelID', blank=True, null=True, db_comment='Product is a member of this pr')  # Field name made lowercase.
    sellstartdate = models.DateTimeField(db_column='SellStartDate', db_comment='Date the product was available')  # Field name made lowercase.
    sellenddate = models.DateTimeField(db_column='SellEndDate', blank=True, null=True, db_comment='Date the product was no longer')  # Field name made lowercase.
    discontinueddate = models.DateTimeField(db_column='DiscontinuedDate', blank=True, null=True, db_comment='Date the product was discontin')  # Field name made lowercase.
    thumbnailphoto = models.BinaryField(db_column='ThumbNailPhoto', blank=True, null=True, db_comment='Small image of the product.')  # Field name made lowercase.
    thumbnailphotofilename = models.CharField(db_column='ThumbnailPhotoFileName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True, db_comment='Small image file name.')  # Field name made lowercase.
    rowguid = models.CharField(unique=True, max_length=36, db_comment='ROWGUIDCOL number uniquely ide')
    modifieddate = models.DateTimeField(db_column='ModifiedDate', db_comment='Date and time the record was l')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Product'
        db_table_comment = 'Products sold or used in the m'


class Productcategory(models.Model):
    productcategoryid = models.AutoField(db_column='ProductCategoryID', primary_key=True, db_comment='Primary key for ProductCategor')  # Field name made lowercase.
    parentproductcategoryid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentProductCategoryID', blank=True, null=True, db_comment='Product category identificatio')  # Field name made lowercase.
    rowguid = models.CharField(unique=True, max_length=36, db_comment='ROWGUIDCOL number uniquely ide')
    modifieddate = models.DateTimeField(db_column='ModifiedDate', db_comment='Date and time the record was l')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductCategory'
        db_table_comment = 'High-level product categorizat'


class Productdescription(models.Model):
    productdescriptionid = models.AutoField(db_column='ProductDescriptionID', primary_key=True, db_comment='Primary key for ProductDescrip')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=400, db_collation='SQL_Latin1_General_CP1_CI_AS', db_comment='Description of the product.')  # Field name made lowercase.
    rowguid = models.CharField(unique=True, max_length=36, db_comment='ROWGUIDCOL number uniquely ide')
    modifieddate = models.DateTimeField(db_column='ModifiedDate', db_comment='Date and time the record was l')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductDescription'
        db_table_comment = 'Product descriptions in severa'


class Productmodel(models.Model):
    productmodelid = models.AutoField(db_column='ProductModelID', primary_key=True, db_comment='Clustered index created by a p')  # Field name made lowercase.
    catalogdescription = models.TextField(db_column='CatalogDescription', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rowguid = models.CharField(unique=True, max_length=36)
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductModel'


class Productmodelproductdescription(models.Model):
    productmodelid = models.OneToOneField(Productmodel, models.DO_NOTHING, db_column='ProductModelID', primary_key=True, db_comment='Primary key. Foreign key to Pr')  # Field name made lowercase. The composite primary key (ProductModelID, ProductDescriptionID, Culture) found, that is not supported. The first column is selected.
    productdescriptionid = models.ForeignKey(Productdescription, models.DO_NOTHING, db_column='ProductDescriptionID', db_comment='Primary key. Foreign key to Pr')  # Field name made lowercase.
    culture = models.CharField(db_column='Culture', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', db_comment='The culture for which the desc')  # Field name made lowercase.
    rowguid = models.CharField(unique=True, max_length=36)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', db_comment='Date and time the record was l')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductModelProductDescription'
        unique_together = (('productmodelid', 'productdescriptionid', 'culture'),)
        db_table_comment = 'Cross-reference table mapping '


class Salesorderdetail(models.Model):
    salesorderid = models.OneToOneField('Salesorderheader', models.DO_NOTHING, db_column='SalesOrderID', primary_key=True, db_comment='Primary key. Foreign key to Sa')  # Field name made lowercase. The composite primary key (SalesOrderID, SalesOrderDetailID) found, that is not supported. The first column is selected.
    salesorderdetailid = models.AutoField(db_column='SalesOrderDetailID', db_comment='Primary key. One incremental u')  # Field name made lowercase.
    orderqty = models.SmallIntegerField(db_column='OrderQty', db_comment='Quantity ordered per product.')  # Field name made lowercase.
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID', db_comment='Product sold to customer. Fore')  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, db_comment='Selling price of a single prod')  # Field name made lowercase.
    unitpricediscount = models.DecimalField(db_column='UnitPriceDiscount', max_digits=19, decimal_places=4, db_comment='Discount amount.')  # Field name made lowercase.
    linetotal = models.DecimalField(db_column='LineTotal', max_digits=38, decimal_places=6, db_comment='Per product subtotal. Computed')  # Field name made lowercase.
    rowguid = models.CharField(unique=True, max_length=36, db_comment='ROWGUIDCOL number uniquely ide')
    modifieddate = models.DateTimeField(db_column='ModifiedDate', db_comment='Date and time the record was l')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SalesOrderDetail'
        unique_together = (('salesorderid', 'salesorderdetailid'),)
        db_table_comment = 'Individual products associated'


class Salesorderheader(models.Model):
    salesorderid = models.AutoField(db_column='SalesOrderID', primary_key=True, db_comment='Primary key.')  # Field name made lowercase.
    revisionnumber = models.SmallIntegerField(db_column='RevisionNumber', db_comment='Incremental number to track ch')  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='OrderDate', db_comment='Dates the sales order was crea')  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate', db_comment='Date the order is due to the c')  # Field name made lowercase.
    shipdate = models.DateTimeField(db_column='ShipDate', blank=True, null=True, db_comment='Date the order was shipped to ')  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', db_comment='Order current status. 1 = In p')  # Field name made lowercase.
    salesordernumber = models.CharField(db_column='SalesOrderNumber', unique=True, max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', db_comment='Unique sales order identificat')  # Field name made lowercase.
    customerid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CustomerID', db_comment='Customer identification number')  # Field name made lowercase.
    shiptoaddressid = models.ForeignKey(Address, models.DO_NOTHING, db_column='ShipToAddressID', blank=True, null=True, db_comment='The ID of the location to send')  # Field name made lowercase.
    billtoaddressid = models.ForeignKey(Address, models.DO_NOTHING, db_column='BillToAddressID', related_name='salesorderheader_billtoaddressid_set', blank=True, null=True, db_comment='The ID of the location to send')  # Field name made lowercase.
    shipmethod = models.CharField(db_column='ShipMethod', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', db_comment='Shipping method. Foreign key t')  # Field name made lowercase.
    creditcardapprovalcode = models.CharField(db_column='CreditCardApprovalCode', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True, db_comment='Approval code provided by the ')  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=4, db_comment='Sales subtotal. Computed as SU')  # Field name made lowercase.
    taxamt = models.DecimalField(db_column='TaxAmt', max_digits=19, decimal_places=4, db_comment='Tax amount.')  # Field name made lowercase.
    freight = models.DecimalField(db_column='Freight', max_digits=19, decimal_places=4, db_comment='Shipping cost.')  # Field name made lowercase.
    totaldue = models.DecimalField(db_column='TotalDue', max_digits=19, decimal_places=4, db_comment='Total due from customer. Compu')  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True, db_comment='Sales representative comments.')  # Field name made lowercase.
    rowguid = models.CharField(unique=True, max_length=36, db_comment='ROWGUIDCOL number uniquely ide')
    modifieddate = models.DateTimeField(db_column='ModifiedDate', db_comment='Date and time the record was l')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SalesOrderHeader'
        db_table_comment = 'General sales order informatio'
