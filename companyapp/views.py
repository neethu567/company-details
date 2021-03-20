from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.views.generic.edit import FormView

from companyapp.models import *
from .forms import *


def Table_generation_listview(request):
    table_header = [
        "Company Name",
        "Type of Company",
        "Indian Presence",
        "Services",
        "Remarks",
    ]

    company_list = Company.objects.all()
    Email_list = Email.objects.all()
    Address_list = Address.objects.all()
    Website_list = Website.objects.all()
    Whatsapp_list = Whatsapp.objects.all()
    Fax_list = Fax.objects.all()
    Phone_list = Phone.objects.all()
    Linkedin_list = Linkedin.objects.all()
    # Linkedin_list=Linkedin.objects.all()
    paginator = Paginator(company_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "company_list": company_list,
        "table_headers": table_header,
        "page_obj": page_obj,
        "Email_list": Email_list,
        "Address_list": Address_list,
        "Website_list": Website_list,
        "Whatsapp_list": Whatsapp_list,
        "Fax_list": Fax_list,
        "Phone_list": Phone_list,
        "Linkedin_list": Linkedin_list,
    }
    return render(request, "companyapp/home.html", context)


def CompanyDetailView(request, id):

    company = Company.objects.get(id=id)
    print(company, "##")
    form = CompanyForm(instance=company)
    # form = TCompanyForm(instance=company)

    if request.method == "POST":
        print("neethu")
        form = CompanyForm(request.POST, instance=company)
        print(form)
        if form.is_valid():
            print("antony")
            form.save()

    return render(request, "companyapp/EditForm.html", context={"companylist": form})


def Addnew_details(request):
    form = CompanyForm(request.POST)
    # company = Company.objects.get(id=pk)
    company_instnace = None

    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data.get("name")
            type = form.cleaned_data.get("type")
            indian_presence = form.cleaned_data.get("indian_presence")
            services = form.cleaned_data.get("services")
            remarks = form.cleaned_data.get("remarks")
            if not form.data["name"]:
                messages.info(request, "Enter a valid Company Name !")
                return redirect("/addnew")
            elif Company.objects.filter(name=name).exists():
                messages.info(request, "Company With same name already exist!")
                return redirect("/addnew")
            else:
                company_instnace = form.save(commit=False)
                company_instnace.save()
                messages.info(
                    request, "Company Details Sucessfullay Saved.Go for next Step!"
                )
                print(company_instnace.id)
                # return redirect("/addnew")
            if company_instnace:
                return render(
                    request,
                    "companyapp/addnew.html",
                    context={"companylist": form, "company_instnace": company_instnace},
                )
            return redirect("address/", contenct=company_instnace.id)
    # company_instance = form.save()
    # print(company_instance.id)

    return render(
        request,
        "companyapp/addnew.html",
        context={"companylist": form, "company_instnace": company_instnace},
    )


# class IndexView(FormView):
#     # template_name = 'companyapp/addnew.html'
#     form = TCompanyForm
#     # success_url = '/addnew/'
#     print(TCompanyForm)
#
#         # def form_valid(self, form):
#             # This method is called when valid form data has been POSTed.
#             # It should return an HttpResponse.
#             # form.send_email()
#             # return super().form_valid(form)


def Add_address(request, pk=id, *args):
    company = Company.objects.get(id=pk)
    print(company)
    count = 0
    if request.method == "POST":
        print("aaa", request.POST)
        for key in request.POST:
            count += 1
            if count == 1:
                pass
            else:
                add = request.POST[key]
                print(request.POST[key])
                Address.objects.create(address=add, address_owner=company)
                print(company.id)
        # return redirect("address/"+str(company.id))
        return redirect("/"+str(company.id))
    return render(request, "companyapp/address_update.html",)

def Add_email(request):

    return render(request, "companyapp/add_email.html", )