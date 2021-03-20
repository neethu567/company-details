from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    indian_presence = models.CharField(max_length=1000, blank=True, null=True)
    services = models.CharField(max_length=1000, blank=True, null=True)
    remarks = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name


class Email(models.Model):
    email_owner = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="email"
    )
    email = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.email


class Address(models.Model):
    address_owner = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="address"
    )
    address = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.address


class Website(models.Model):
    website_owner = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="website"
    )
    website = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.website


class Whatsapp(models.Model):
    whatsapp_owner = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="whatsapp"
    )
    whatsapp = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.whatsapp


class Fax(models.Model):
    fax_owner = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="fax")
    fax = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.fax


class Phone(models.Model):
    phone_owner = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="phone"
    )
    phone = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.phone


class Linkedin(models.Model):
    linkedin_owner = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="linkedin"
    )
    linkedin = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.linkedin


class Picupload(models.Model):
    picupload_owner = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="picupload"
    )
    picupload = models.ImageField(upload_to="images/")


import django_tables2 as tables

# class SimpleTable(tables.Table):
#     class Meta:
#         model = Company
