from django.core.management.base import BaseCommand

# from companydetails.companyapp.models import *
import pandas as pd

from companyapp.models import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("loading excel......")
        data = pd.read_excel("companyapp/YEARBOOK2019.xls")
        for i in range(len(data)):
            if Company.objects.filter(name=data.iloc[i]["Company Name"]).exists():
                pass
            else:
                instance = Company.objects.create(
                    name=data.iloc[i]["Company Name"],
                    type=data.iloc[i]["Type of Company"],
                    indian_presence=data.iloc[i]["Presence in India"],
                    services=data.iloc[i]["Services"],
                    remarks=data.iloc[i]["Remarks"],
                )
                phone_num = str(data.iloc[i]["Phone Number"])
                if Phone.objects.filter(phone=phone_num).exists() | pd.isna(phone_num):
                    pass
                elif phone_num.find("/") == -1:
                    phone = Phone.objects.create(phone=phone_num, phone_owner=instance)
                else:
                    print(phone_num)
                    ph_list = phone_num.split("/")
                    res = []
                    for h in ph_list:
                        res.append(h.replace("\n", ""))
                    uniq_list = pd.unique(res)
                    print(uniq_list)
                    for k in range(len(uniq_list)):
                        phone = Phone.objects.create(
                            phone=uniq_list[k], phone_owner=instance
                        )
                Web_address = data.iloc[i]["Website"]
                if Website.objects.filter(website=Web_address).exists() | pd.isna(
                    Web_address
                ):
                    pass
                elif Web_address.find("|") == -1:
                    web = Website.objects.create(
                        website=Web_address, website_owner=instance
                    )
                else:
                    web_list = Web_address.split("|")
                    print(web_list)
                    uniq_list1 = pd.unique(web_list)
                    print(uniq_list1)
                    for k in range(len(uniq_list1)):
                        web = Website.objects.create(
                            website=uniq_list1[k], website_owner=instance
                        )
                Email_address = data.iloc[i]["Mail"]
                if Email.objects.filter(email=Email_address).exists() | pd.isna(
                    Email_address
                ):
                    pass
                elif Email_address.find("|") == -1:
                    mail = Email.objects.create(
                        email=Email_address, email_owner=instance
                    )
                else:
                    email_list = Email_address.split("|")
                    uniq_list2 = pd.unique(email_list)
                    for k in range(len(uniq_list2)):
                        mail = Email.objects.create(
                            email=uniq_list2[k], email_owner=instance
                        )
                Address_location = data.iloc[i]["Address"]
                if Address.objects.filter(address=Address_location).exists() | pd.isna(
                    Address_location
                ):
                    pass
                elif Address_location.find("/") == -1:
                    address = Address.objects.create(
                        address=Address_location, address_owner=instance
                    )
                else:
                    address_list = Address_location.split("/")
                    uniq_list3 = pd.unique(address_list)
                    for k in range(len(uniq_list3)):
                        address = Address.objects.create(
                            address=uniq_list3[k], address_owner=instance
                        )
                linkedin_profile = data.iloc[i]["Linkedin Profile"]
                if Linkedin.objects.filter(
                    linkedin=linkedin_profile
                ).exists() | pd.isna(linkedin_profile):
                    pass
                elif linkedin_profile.find("|") == -1:
                    linkedin = Linkedin.objects.create(
                        linkedin=linkedin_profile, linkedin_owner=instance
                    )
                else:
                    linkedin_list = linkedin_profile.split("|")
                    uniq_list4 = pd.unique(linkedin_list)
                    for k in range(len(uniq_list4)):
                        linkedin = Linkedin.objects.create(
                            linkedin=uniq_list4[k], linkedin_owner=instance
                        )
                whatsapp = data.iloc[i]["Whatsapp Number"]
                if Whatsapp.objects.filter(whatsapp=whatsapp).exists() | pd.isna(
                    whatsapp
                ):
                    pass
                elif whatsapp.find("/") == -1:
                    whatsapp = Whatsapp.objects.create(
                        whatsapp=whatsapp, whatsapp_owner=instance
                    )
                else:
                    whatsap_list = whatsapp.split("/")
                    uniq_list5 = pd.unique(whatsap_list)
                    for k in range(len(uniq_list5)):
                        whatsapp = Whatsapp.objects.create(
                            whatsapp=uniq_list5[k], whatsapp_owner=instance
                        )
                faxx = data.iloc[i][" Fax"]
                if Fax.objects.filter(fax=faxx).exists() | pd.isna(faxx):
                    pass
                elif faxx.find("/") == -1:
                    fax = Fax.objects.create(fax=faxx, fax_owner=instance)
                else:
                    fax_list = faxx.split("/")
                    uniq_list6 = pd.unique(fax_list)
                    for k in range(len(uniq_list6)):
                        fax = Fax.objects.create(fax=uniq_list6[k], fax_owner=instance)
