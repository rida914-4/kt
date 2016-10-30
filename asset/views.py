from django.shortcuts import render, render_to_response, HttpResponse, HttpResponseRedirect, redirect, get_object_or_404, RequestContext
from models import *
import logging
from reportlab.pdfgen import canvas
from .forms import *
from django.views.generic.edit import FormView
from .forms import FileFieldForm
from django.core.mail import send_mail
from models import Item
from django.forms.models import inlineformset_factory
from django.forms.models import modelformset_factory
from django.forms import formset_factory, BaseFormSet
from django.contrib import auth, messages
from django.core.context_processors import csrf


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
media_path = os.path.join(BASE_DIR, 'media')
static_path = os.path.join(BASE_DIR, 'static')


from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied

@login_required
def edit_user(request, pk):
    user = Users.objects.get(pk=pk)
    user_form = UserProfileForm(instance=user)

    ProfileInlineFormset = inlineformset_factory(Users, UserProfile, fields=('website', 'bio', 'phone', 'city', 'country', 'organization'))
    formset = ProfileInlineFormset(instance=user)

    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == "POST":
            user_form = UserProfileForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('/accounts/profile/')

        return render(request, "account_update.html", {
            "noodle": pk,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied
# *************************************************** #
#                   Index                             #
# *************************************************** #
def index(request):
    logger.info('Launching pgc')

    return render_to_response('index.html')


# *************************************************** #
#                   Invoice                           #
# *************************************************** #
# def invoice(request):
#     asset_db = VPlInvoice.objects.all()
#
#     context = {
#         'assets': asset_db
#     }
#
#     return render_to_response('asset.html', context)
#
#
# def purchase(request, voucher_id):
#     # logger.info('First purchase method %s', voucher_id)
#     master_dic = dict()
#     context = dict()
#     # if len(request.body.split('=')) > 0:
#     #     voucher_id = request.body.split('=')[0]
#     # else:
#     #     voucher_id = ''
#     # logger.info('Getting voucher id from post request %s', voucher_id)
#     imagelib_path = os.path.join(static_path, 'asset/lib', voucher_id)
#     imagefront_path = os.path.join('asset/lib', voucher_id, voucher_id + '_0000')
#     imagebill_path = os.path.join(static_path, 'asset/bills', voucher_id)
#     imagespecs_path = os.path.join(static_path, 'asset/specs', voucher_id)
#
#     invoice_data = VPlInvoicedet.objects.all().filter(voucher_id=voucher_id)
#
#     for a in invoice_data:
#         # logger.info('acct_id %s--------------------------------------------,', a.acct_id)
#         master_dic['acct_id'] = a.acct_id
#         master_dic['stock_name'] = a.stock_name
#         master_dic['voucher_date'] = a.voucher_date
#         master_dic['particulars'] = a.particulars
#         master_dic['stock_code'] = a.stock_code
#     # logger.info('master dic done')
#     if request.method == "GET":
#         context = {
#             'voucher_id': voucher_id,
#             'invoice_data': invoice_data,
#             'acct_id': master_dic['acct_id'],
#             'stock_name': master_dic['stock_name'],
#             'voucher_date': master_dic['voucher_date'],
#             'particulars': master_dic['particulars'],
#             'imagelib_count': len(listdir(imagelib_path)),
#             'imagelib_path': imagelib_path,
#             'imagelib_list': listdir(imagelib_path),
#             'imagebill_list': listdir(imagebill_path),
#             'imagefront_path': imagefront_path,
#             'imagespecs_list': listdir(imagespecs_path),
#         }
#         # logger.info(context)
#         # logger.info('front path %s', imagefront_path)
#         return render(request, 'purchase_invoice.html', context)
#     else:
#
#         return render(request, 'purchase_invoice.html', context)
#
#
# def item_list():
#     item_list = []
#     items = Item.objects.values('description')
#     for item in items:
#         item_list.append(item['description'])
#     return item_list
#
#
# def pos_dic():
#     item_dic = dict()
#     items = Positions.objects.values('pos_code', 'description')
#     for item in items:
#         item_dic[item['description']] = item['pos_code']
#     return item_dic
#
#
# def cust_list():
#     item_list = []
#     items = Custodian.objects.values('description')
#     for item in items:
#         item_list.append(item['description'])
#     return item_list
#
#
# def new_invoice(request):
#     logger.info('FORM INFO ----------------------------------------------')
#     form = TmpForm()
#
#     def get_next_voucher():
#         temp_vid = TmpPlInvoice.objects.order_by().values_list("voucher_id", flat=True).distinct()
#         logger.info('Voucher ID already present %s', temp_vid)
#         if not temp_vid:
#             voucher_id = str(1).zfill(4)
#         else:
#             voucher_id = str(int(max(temp_vid)) + 1).zfill(4)
#         return voucher_id
#
#     voucher_id = get_next_voucher()
#     QuestionFormSet = formset_factory(TmpFormDetForm, extra=1)
#     QuestionFormSet_one = formset_factory(TmpFormDetForm, extra=1)
#
#     if request.method == 'POST':
#         logger.info('Method is POST')
#         form = TmpForm(request.POST or None)
#
#         if form.is_valid():
#             logger.info('FORM INFO')
#             logger.info('*' * 50)
#             # logger.info('form  is %s ', form)
#             # logger.info('formset is %s ', formset.cleaned_data)
#             voucher_id_f = form.cleaned_data['voucher_id']
#
#             form_ins = form.save(commit=False)
#             print 'the voucher id is as foloows u btta', voucher_id_f
#
#             # formset = TmpFormDetForm(request.POST, v_id=voucher_id, initial={'voucher': voucher_id})
#             formset = QuestionFormSet(request.POST, instance=form_ins)
#             if formset.is_valid():
#                 form.save()
#                 # formset_ins = formset.save(commit=False)
#                 # formset_ins.student = form_ins
#                 formset.save()
#                 logger.info('saved formset')
#             else:
#                 logger.error('formset not working %s', formset.errors)
#             logger.info('*' * 50)
#             return HttpResponseRedirect('/new/')
#
#         else:
#             message = "wrong"
#             logger.error('Form is invalid. Errors are %s', form.errors)
#         return render_to_response('test1.html',
#                                   {'formset': QuestionFormSet(), 'form': form, 'formset_single': QuestionFormSet_one},
#                                   context_instance=RequestContext(request))
#     else:
#         logger.info('Method is GET')
#         form = TmpForm()
#         formset = QuestionFormSet(initial={'voucher': voucher_id})
#         # logger.info('Formset from GET is %s', formset)
#         return render_to_response('test1.html',
#                                   {'formset': QuestionFormSet(), 'form': form, 'formset_single': QuestionFormSet_one},
#                                   context_instance=RequestContext(request))
#
#
# def new_invoiceee(request):
#     logger.info('FORM INFO ----------------------------------------------')
#     temp_vid = TmpPlInvoice.objects.order_by().values_list("voucher_id", flat=True).distinct()
#     logger.info('Voucher ID already present %s', temp_vid)
#     if not temp_vid:
#         voucher_id = str(1).zfill(4)
#     else:
#         voucher_id = str(int(max(temp_vid)) + 1).zfill(4)
#     QuestionFormSet = formset_factory(TmpFormDetForm, extra=1)
#     QuestionFormSet_one = formset_factory(TmpFormDetForm, extra=1)
#
#     form = TmpFor(voucher_id=voucher_id, initial={'voucher_id': voucher_id})
#     formset = TmpFormDetForm()
#     if request.method == 'POST':
#         logger.info('Method is POST')
#         form = TmpFor(request.POST, voucher_id=voucher_id, initial={'voucher_id': voucher_id})
#         if form.is_valid():
#             logger.info('FORM INFO')
#             logger.info('*' * 50)
#             inst = form.save()
#
#             formset = TmpFormDetForm(request.POST or None)
#
#             if formset.is_valid():
#                 formset.save(commit=False)
#
#             else:
#                 logger.error('errors in formset %s', formset.errors)
#             logger.info('*' * 50)
#             return HttpResponseRedirect('/new/')
#
#         else:
#             logger.error('Master Form is invalid. Errors are %s', form.errors)
#             return render_to_response('new_invoice.html', {'formset': QuestionFormSet(), 'form': form, 'formset_single': QuestionFormSet_one},
#                                   context_instance=RequestContext(request))
#     else:
#         logger.info('Method is GET')
#         formset = TmpFormDetForm()
#         return render_to_response('new_invoice.html', {'formset': QuestionFormSet(), 'form': form, 'formset_single': QuestionFormSet_one},
#                                   context_instance=RequestContext(request))
#
#
# def new_invoic(request):
#     logger.info('FORM INFO ----------------------------------------------')
#     temp_vid = TmpPlInvoice.objects.order_by().values_list("voucher_id", flat=True).distinct()
#     logger.info('Voucher ID already present %s', temp_vid)
#     if not temp_vid:
#         voucher_id = str(1).zfill(4)
#     else:
#         voucher_id = str(int(max(temp_vid)) + 1).zfill(4)
#     QuestionFormSet = formset_factory(TmpFormDetForm, extra=1)
#     QuestionFormSet_one = formset_factory(TmpFormDetForm, extra=1)
#
#
#     form = TmpFor(voucher_id=voucher_id, initial={'voucher_id': voucher_id})
#     formset = TmpFormDetForm()
#     if request.method == 'POST':
#         logger.info('Method is POST')
#         AuthorFormSet = modelformset_factory(TmpPlInvoicedet, fields=("qty",))
#         # form = TmpFor(request.POST, voucher_id=voucher_id, initial={'voucher_id': voucher_id})
#         if form.is_valid():
#             formset = AuthorFormSet(queryset=TmpPlInvoice.objects.filter(voucher_id=voucher_id))
#             inst = form.save()
#
#             # formset = TmpFormDetForm(request.POST or None)
#
#             if formset.is_valid():
#                 formset.save(commit=False)
#
#             else:
#                 logger.error('errors in formset %s', formset.errors)
#             logger.info('*' * 50)
#             return HttpResponseRedirect('/new/')
#
#         else:
#             logger.error('Master Form is invalid. Errors are %s', form.errors)
#             return render_to_response('new_invoice.html', {'formset': QuestionFormSet(), 'form': form, 'formset_single': QuestionFormSet_one},
#                                   context_instance=RequestContext(request))
#     else:
#         logger.info('Method is GET')
#         formset = TmpFormDetForm()
#         return render_to_response('new_invoice.html', {'formset': QuestionFormSet(), 'form': form, 'formset_single': QuestionFormSet_one},
#                                   context_instance=RequestContext(request))
#
# # *************************************************** #
# #                  Reports                            #
# # *************************************************** #
#
#
# def reports(request):
#     acct_names = Reports.objects.filter(cat=1).order_by('report_name')
#     sales_names = Reports.objects.filter(cat=2).order_by('report_name')
#     purchase_names = Reports.objects.filter(cat=3).order_by('report_name')
#     stock_names = Reports.objects.filter(cat=4).order_by('report_name')
#     party_names = Reports.objects.filter(cat=5).order_by('report_name')
#     group_names = ''
#     audit_names = ''
#     for a in purchase_names:
#         logger.info('reports %s', a.report_name)
#     logger.info('-----------------------------------------')
#     context = {
#         'acct_names': acct_names,
#         'sales_names': sales_names,
#         'purchase_names': purchase_names,
#         'stock_names': stock_names,
#         'party_names': party_names
#     }
#     return render_to_response('reports.html', context)
#
#
# def pf_pl_invoicedet(request, file_name):
#     logger.info('In PF PL')
#     form = PForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             data = form.cleaned_data
#             logger.info('*' * 50)
#             items = list(Item.objects.all().values_list('cat_id', 'description'))
#             logger.info('type of item %s', type(items))
#             combo_final = ([('', 'Select One')])
#             logger.info('type of combo %s', type(combo_final))
#             combo_final.extend(items)
#             logger.info('type of final %s', type(combo_final))
#             logger.info('final %s', combo_final)
#             from_date = str(data['from_date'].strftime('%d-%m-%y')).replace('-', '.')
#             to_date = str(data['to_date'].strftime('%d-%m-%y')).replace('-', '.')
#             vid = str(data['vid'])
#             location = str(data['loc_combo'])
#             custodian = str(data['cus_combo'])
#             assets = str(data['item_combo'])
#             category = str(data['cat_combo'])
#             logger.info(from_date)
#             logger.info(to_date)
#             logger.info(vid)
#             logger.info('from location %s', location)
#             logger.info(custodian)
#             logger.info(assets)
#             logger.info(category)
#             logger.info('*' * 50)
#             url = 'http://192.168.100.3:7001/reports/rwservlet?server=RptSrvCS+report=s:\\apps\\Django\\pgc\\am\\' \
#                   'reports\\pl_invoicedet.jsp+userid=pgc_am/pass@psm+desformat=pdf+DESTYPE=cache+p_date_from=' \
#                   + from_date + '+p_date_to=' + to_date + '+p_voucher_id=' + vid + '+p_pos_code=' + location + '+p_cust_id=' \
#                   + custodian + '+p_cat_id=' + category + '+p_acct_id=' + assets
#             logger.info(url)
#             reports_download(url, file_name)
#             pdf_name = "report" + file_name
#             image_data = open(pdf_name, 'rb').read()
#
#             context = {
#                 'file_name': file_name,
#                 'url': url,
#                 'form': form
#             }
#             return HttpResponse(image_data, content_type='application/pdf')
#         else:
#             logger.info('Not valid')
#             logger.error(form.error)
#     return render(request, 'pf_pl_invoicedet.html', context={'form': form})
#
#
# def reports_download(report_url, file_name):
#     logger.info('report download')
#     pdf_name = "report" + file_name
#     urllib.urlretrieve(report_url, pdf_name)
#
#
# # *********************************************#
# #               Working  image upload
# # *********************************************#
#
#
# def upload(request):
#     if request.method == "POST":
#         logger.info('Upload start ' + '*' * 25)
#         form = UploadFileForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             # logger.info('files --> %s', request.FILES.getlist("files"))
#             files_to_upload = request.FILES.getlist("files")
#             # logger.info('files to be uploaded type %s', files_to_upload)
#
#             folder_type = str(request.POST['folder_type']).replace("_", "/").replace("-", "/")
#             # logger.info('folder type %s', folder_type)
#
#             voucher_id = request.POST.get("voucher_id")
#             # logger.info('v %s', voucher_id)
#             folder_path = os.path.join(static_path, voucher_id)
#             folder_count = len(listdir(folder_path))
#             # logger.info('New folder count %s in %s', folder_count, folder_path)
#             logger.info('folder path ->> %s', folder_path)
#
#             # check the count in static. Do not want to overwrite
#
#             for count, x in enumerate(files_to_upload):
#                 def process(f):
#                     sub_file = os.path.join(folder_path, voucher_id + '_' + str(count))
#
#                     with open(sub_file, 'wb+') as destination:
#                         for chunk in f.chunks():
#                             destination.write(chunk)
#
#                 if folder_count > 0:
#                     count += folder_count
#                     process(x)
#                     count += 1
#                 else:
#                     process(x)
#             copy_uploaded_images(str(voucher_id), str(folder_type))
#             # logger.info('New folder count %s in %s', folder_count, folder_path)
#
#         else:
#             # form = UploadFileForm()
#             logger.error('Form does not seem valid %s', form.errors)
#
#         return HttpResponseRedirect(voucher_id)
#     else:
#         voucher_id = ''
#         logger.error('NOT A VALID POST REQUEST')
#         # form = UploadFileForm()
#         # logger.error('Not a POST REQUEST %s', form.errors)
#         # return render(request, 'purchase_invoice.html', {'form': form})
#         return HttpResponse(voucher_id)
#
#
# # *********************************************#
# #                Helper views
# # *********************************************#
#
#
# def create(request):
#     logger.info(request.method)
#     # itemform = ItemComboForm(request.POST or None)
#     # posform = PformsetomboForm(request.POST or None)
#     # cusform = CusComboForm(request.POST or None)
#     itemform = ''
#     posform = ''
#     cusform = ''
#     tmpform = TmpForm(request.POST or None)
#     tmpformdet = TmpFormDetForm(request.POST or None)
#     if request.method == "POST":
#         # if itemform.is_valid() and posform.is_valid() and cusform.is_valid():
#         if tmpformdet.is_valid():
#             logger.info('*' * 50)
#             # logger.info(itemform.cleaned_data)
#             # logger.info(posform.cleaned_data)
#             # logger.info(cusform.cleaned_data)
#             # logger.info(tmpform.cleaned_data)
#             logger.info(tmpformdet.cleaned_data)
#             logger.info('*' * 50)
#             # itemform.save()
#             # posform.save()
#             # cusform.save()
#             # tmpform.save()
#             tmpformdet.save()
#             return render_to_response('test1.html',
#                                   {'form': tmpform, 'det': tmpformdet}, context_instance=RequestContext(request))
#         else:
#             logger.info('This form is not valid')
#             return render_to_response('test1.html',
#                                   {'form': tmpform, 'det': tmpformdet}, context_instance=RequestContext(request))
#     else:
#         logger.info('This form is GET')
#         tmpformdet = TmpPlInvoicedet()
#         return render_to_response('test1.html',
#                                   {'form': tmpform, 'det': tmpformdet}, context_instance=RequestContext(request))
#
#
# def copy_of_upload(request):
#     if request.method == "POST":
#         logger.info('Upload start')
#         form = UploadFileForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             files_to_upload = request.FILES.getlist("files")
#             logger.info('folder type %s', files_to_upload)
#             folder_type = str(request.POST['folder_type']).replace("_", "/").replace("-", "/")
#             # logger.info('folder type %s', folder_type)
#             voucher_id = request.POST.get("voucher_id")
#             # logger.info('folder type %s', folder_type)
#             folder_path = os.path.join(static_path, folder_type, voucher_id)
#             mfolder_path = os.path.join(media_path, folder_type, voucher_id)
#             folder_count = len(listdir(folder_path))
#             listdir(mfolder_path)
#
#             # check the count in static. Do not want to overwrite
#             for count, x in enumerate(files_to_upload, 1):
#                 def process(f):
#                     sub_file = os.path.join(mfolder_path, '{}_{}'.format(voucher_id, str(count)))
#                     # for front pic name will be different.
#                     if 'front' in folder_path:
#                         checkfrontpic(folder_path, voucher_id)
#                         sub_file = os.path.join(mfolder_path.replace('front', ''), '{}_0'.format(voucher_id))
#                     logger.info('sub file %s', sub_file)
#                     with open(sub_file, 'wb+') as destination:
#                         for chunk in f.chunks():
#                             destination.write(chunk)
#
#                 if folder_count > 0:
#                     count += folder_count
#                     process(x)
#                     count += 1
#                 else:
#                     process(x)
#             logger.info('v %s fol %s', voucher_id, folder_type)
#             copy_uploaded_images(str(voucher_id), str(folder_type))
#             logger.info('New folder count %s in %s', folder_count, folder_path)
#
#         else:
#             # form = UploadFileForm()
#             logger.error('Form does not seem valid %s', form.errors)
#
#         return HttpResponseRedirect(voucher_id)
#     else:
#         voucher_id = ''
#         # form = UploadFileForm()
#         # logger.error('Not a POST REQUEST %s', form.errors)
#         # return render(request, 'purchase_invoice.html', {'form': form})
#         return HttpResponse(voucher_id)
#
#
# def stable_of_upload(request):
#     if request.method == "POST":
#         logger.info('Upload start')
#         form = UploadFileForm(request.POST, request.FILES)
#
#         if form.is_valid():
#
#             files_to_upload = request.FILES.getlist("files")
#             logger.info('folder type %s', files_to_upload)
#             folder_type = str(request.POST['folder_type']).replace("_", "/").replace("-", "/")
#             logger.info('folder type %s', folder_type)
#             voucher_id = request.POST.get("voucher_id")
#             logger.info('folder type %s', folder_type)
#             folder_path = os.path.join(static_path, folder_type, voucher_id)
#             mfolder_path = os.path.join(media_path, folder_type, voucher_id)
#             folder_count = len(listdir(folder_path))
#             listdir(mfolder_path)
#             logger.info('New folder count %s in %s', folder_count, folder_path)
#
#             # check the count in static. Donot want to overwrite
#
#             for count, x in enumerate(files_to_upload):
#
#                 def process(f):
#                     sub_file = os.path.join(mfolder_path, voucher_id + '_' + str(count))
#                     with open(sub_file, 'wb+') as destination:
#                         for chunk in f.chunks():
#                             destination.write(chunk)
#
#                 if folder_count > 0:
#                     count += folder_count
#                     process(x)
#                     count += 1
#                 else:
#                     process(x)
#             logger.info('v %s fol %s', voucher_id, folder_type)
#             copy_uploaded_images(str(voucher_id), str(folder_type))
#             logger.info('New folder count %s in %s', folder_count, folder_path)
#
#         else:
#             # form = UploadFileForm()
#             logger.error('Form does not seem valid %s', form.errors)
#
#         return HttpResponseRedirect(voucher_id)
#     else:
#         voucher_id = ''
#         # form = UploadFileForm()
#         # logger.error('Not a POST REQUEST %s', form.errors)
#         # return render(request, 'purchase_invoice.html', {'form': form})
#         return HttpResponse(voucher_id)
#
#
# def handle_uploaded_file(f, folder_path):
#     with open(folder_path + '/t', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
#     logger.info('Upload complete!')
#
#
# def upload_file(request):
#     if request.method == 'POST':
#         logger.info('Upload start')
#         form = UploadFileForm(request.POST, request.FILES)
#
#         logger.info(' | request value ---> %s :', request.POST.get("your_name"))
#         # voucher_id = re.findall(r'PL[0-9]+_[a-z0-9-]+', request.POST.get('value'), re.I)
#         # logger.info('voucher id %s', voucher_id)
#         # logger.info('request files with name %s :', request.FILES[voucher_id[0]])
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['files'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload.html', {'form': form})
#
#
# class FileFieldView(FormView):
#     form_class = FileFieldForm
#     template_name = 'upload.html'  # Replace with your template.
#     success_url = '...'  # Replace with your URL or reverse().
#
#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         files = request.FILES.getlist('file_field')
#         if form.is_valid():
#             for f in files:
#                 logger.info(f)
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
#
#
# def pdf_report(request):
#     # Create the HttpResponse object with the appropriate PDF headers.
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="sample.pdf"'
#
#     # Create the PDF object, using the response object as its "file."
#     p = canvas.Canvas(response)
#
#     # Draw things on the PDF. Here's where the PDF generation happens.
#     # See the ReportLab documentation for the full list of functionality.
#     p.drawString(100, 100, "Hello world.")
#
#     # Close the PDF object cleanly, and we're done.
#     p.showPage()
#     p.save()
#     return response
#
#
# def test(request):
#     return render(request, 'test1.html')
#
#
# def working_form_django(request):
#     logger.info('FORM INFO ----------------------------------------------')
#     if request.method == 'POST':
#         form = NameForm(request.POST)
#
#         if form.is_valid():
#             data = form.cleaned_data
#             logger.info('FORM INFO')
#             logger.info('form info date is %s ', data)
#             new_date = form.cleaned_data['new_date']
#             new_parc = form.cleaned_data['new_date']
#             item_combo = form.cleaned_data['item_combo']
#             table_parc = form.cleaned_data['table_parc']
#             table_qty = form.cleaned_data['table_qty']
#             logger.info('form info date is %s ', data)
#             # return HttpResponseRedirect('/thanks/')
#             return render(request, 'new_invoice.html', {'form': form})
#         else:
#             logger.error('Form is invalid. Errors are %s', form.errors)
#     else:
#         form = NameForm()
#         logger.error('Form has GET request. Errors are %s', form.errors)
#
#     return render(request, 'new_invoice.html', {'form': form})
#
#
# def copy_of_get_name(request):
#     logger.info('FORM INFO ----------------------------------------------')
#     if request.method == 'POST':
#         form = NameForm(request.POST)
#
#         if form.is_valid():
#             data = form.cleaned_data
#             logger.info('FORM INFO')
#             logger.info('*' * 50)
#             logger.info('form info date is %s ', data.cleaned_data['new_date'])
#             logger.info('*' * 50)
#             new_date = form.cleaned_data['new_date']
#             new_parc = form.cleaned_data['new_date']
#             item_combo = form.cleaned_data['item_combo']
#             table_parc = form.cleaned_data['table_parc']
#             table_qty = form.cleaned_data['table_qty']
#             # logger.info('form info date is %s ', data)
#             # return HttpResponseRedirect('/thanks/')
#             return render(request, 'new_invoice.html', {'form': form})
#         else:
#             logger.error('Form is invalid. Errors are %s', form.errors)
#     else:
#         form = NameForm()
#         logger.error('Form has GET request. Errors are %s', form.errors)
#
#     return render(request, 'new_invoice.html', {'form': form})
#
#
# def Form(request):
#     context = {
#         'rida': 'PL564646'
#     }
#     return render(request, 'formm.html', context)
#
#
# def new_invoice_copy(request):
#     logger.info('FORM INFO ----------------------------------------------')
#     QuestionFormSet = formset_factory(AddRowsForm, extra=5)
#     QuestionFormSet_one = formset_factory(AddRowsForm, extra=1)
#
#     if request.method == 'POST':
#         form = NameForm(request.POST)
#         logger.info('Method is POST')
#         formset = QuestionFormSet(request.POST)
#         temp_vid = TmpPlInvoice.objects.order_by().values_list("voucher_id", flat=True).distinct()
#         items = Item.objects.all().values_list('stock_code', 'description')
#
#         # logger.info('abug type >>>>>>>>>>>>>>>>>>>>>>>> %s', items)
#         if form.is_valid():
#             data = form.cleaned_data
#             logger.info('FORM INFO')
#             new_date = data['new_date']
#             new_parc = data['new_parc']
#             new_vid = data['new_vid']
#
#             item_combo = data['item_combo']
#             pos_combo = data['pos_combo']
#             cus_combo = data['cus_combo']
#
#             # logger.info('form new date is %s ', new_date)
#             # logger.info('form new parc is %s ', new_parc)
#             # logger.info('form new vid is %s ', new_vid)
#             # logger.info('form item combo is %s ', item_combo)
#             # logger.info('form pos combo is %s ', pos_combo)
#             # logger.info('form cus combo is%sthis ', cus_combo)
#             # logger.info('form type cus combo is %s ', type(cus_combo))
#
#             # form save procedure
#             if not temp_vid:
#                 voucher_id = 0
#                 voucher_id += 1
#                 logger.info('new voucher id %s', voucher_id)
#             else:
#                 logger.info('MAX voucher id %s', max(temp_vid))
#                 voucher_id = str(int(max(temp_vid)) + 1).zfill(4)
#                 logger.info('voucher id %s', voucher_id)
#                 # form.save()
#                 # formset.save()
#
#             tmpPlInvoice_save = TmpPlInvoice.objects.create(voucher_date=new_date,
#                                                             voucher_id=new_vid,
#                                                             acct_id=item_combo,
#                                                             particulars=new_parc,
#                                                             pos_code=pos_combo,
#                                                             cust_id=cus_combo
#                                                             )
#
#             tmpPlInvoice_save.save()
#             for detail in enumerate(formset.cleaned_data, 1):
#                 logger.info('SROCK CODE %s', detail[1]['StockCode'])
#                 logger.info('qty CODE %s', type(int(detail[1]['Rate'])))
#                 logger.info('rate CODE %s', type(int(detail[1]['Quantity'])))
#                 tmpPlInvoicedet_save = TmpPlInvoicedet.objects.create(
#                     voucher_id=TmpPlInvoicedet.objects.all().filter(voucher_id=voucher_id),
#                     lineitem=detail[0],
#                     particulars=detail[1]['Rate'],
#                     qty=detail[1]['Quantity'],
#                     rate=detail[1]['Rate'],
#                     itemtot=int(detail[1]['Rate']) * int(detail[1]['Quantity']),
#                     stock_code=detail[1]['StockCode']
#                 )
#                 tmpPlInvoicedet_save.save()
#             message = "Thank you"
#             # return render(request, 'new_invoice.html', {'form': form})
#
#         else:
#             message = "wrong"
#             logger.error('Form is invalid. Errors are %s', form.errors)
#         return render_to_response('new_invoice.html',
#                                   {'formset': QuestionFormSet(), 'form': form, 'formset_single': QuestionFormSet_one},
#                                   context_instance=RequestContext(request))
#     else:
#         logger.info('Method is GET')
#         form = NameForm()
#         formset = QuestionFormSet()
#         # logger.info('Formset from GET is %s', formset)
#         return render_to_response('new_invoice.html',
#                                   {'formset': QuestionFormSet(), 'form': form, 'formset_single': QuestionFormSet_one},
#                                   context_instance=RequestContext(request))
#
#
#
#
#
#
#
#
#
#
#
# ############################################
#             # MASter detaill view
# def get_max_voucher_id():
#     temp_vid = TmpPlInvoice.objects.order_by().values_list("voucher_id", flat=True).distinct()
#     if not temp_vid:
#         voucher_id = str(1).zfill(4)
#     else:
#         voucher_id = str(int(max(temp_vid))).zfill(4)
#     logger.info('max voucher id %s', voucher_id)
#     logger.info(temp_vid)
#     return voucher_id
#
#
# def get_listof_voucher_id():
#     temp_vid = TmpPlInvoice.objects.order_by().values_list("voucher_id", flat=True).distinct()
#     return temp_vid
#
#
# def get_min_voucher_id():
#     temp_vid = TmpPlInvoice.objects.order_by().values_list("voucher_id", flat=True).distinct()
#     if not temp_vid:
#         voucher_id = str(1).zfill(4)
#     else:
#         voucher_id = str(int(min(temp_vid))).zfill(4)
#     logger.info('min voucher id %s', voucher_id)
#     return voucher_id
#
#
# def check_exists_voucher_id(id):
#     temp_vid = TmpPlInvoice.objects.order_by().values_list("voucher_id", flat=True).distinct()
#     if id in temp_vid:
#         return True, temp_vid
#     else:
#         return False, temp_vid
#
#
# def get_incremented_voucher_id(voucher_id):
#     vid_exists, vidu_list = check_exists_voucher_id(voucher_id)
#     if not vid_exists:
#         logger.info('This voucher_id %s does not exists. Finding higher.', voucher_id)
#         vid_list = map(int, [x.encode('UTF8') for x in vidu_list])
#         while voucher_id <= int(get_max_voucher_id()):
#             if int(voucher_id) in vid_list:
#                 logger.info('Found a higher voucher_id %s.', voucher_id)
#                 break
#             voucher_id = int(voucher_id) + 1
#             logger.info('Incrementing voucher_id %s ', voucher_id)
#     return str(voucher_id).zfill(4)
#
#
# def get_decremented_voucher_id(voucher_id):
#     vid_exists, vidu_list = check_exists_voucher_id(voucher_id)
#     if not vid_exists:
#         logger.info('This voucher_id %s does not exists. Finding lower.', voucher_id)
#         vid_list = map(int, [x.encode('UTF8') for x in vidu_list])
#         while int(voucher_id) >= int(get_min_voucher_id()):
#             if int(voucher_id) in vid_list:
#                 logger.info('Found a lower voucher_id %s!!', voucher_id)
#                 break
#             voucher_id = int(voucher_id) - 1
#             logger.info('Decrementing voucher_id %s ', voucher_id)
#
#     return str(voucher_id).zfill(4)
#
#
# def master_detail(request):
#     def get_new_voucher_id():
#         temp_vid = TmpPlInvoice.objects.order_by().values_list("voucher_id", flat=True).distinct()
#         if not temp_vid:
#             voucher_id = str(1).zfill(4)
#         else:
#             voucher_id = str(int(max(temp_vid)) + 1).zfill(4)
#         return voucher_id
#
#     author_form = TmpForm()
#     author = TmpPlInvoice()
#     BookFormSet = inlineformset_factory(TmpPlInvoice, TmpPlInvoicedet, exclude=('emp_id', 'voucher', 'lineitem', 'id',),
#                                         form=TmpFormDetForm, extra=10)
#     formset = BookFormSet(instance=author)
#     totalform = TmpFormTotal()
#     postform = CheckPostedForm(instance=author)
#     if request.method == 'POST':
#         logger.info('*'*50)
#         voucher_id = get_new_voucher_id()
#         logger.info('VOUCHER %s', voucher_id)
#         author = TmpForm(request.POST)
#         if author.is_valid():
#             logger.info('Data for Author is %s', author.cleaned_data)
#             created_author = author.save(commit=False)
#             created_author.voucher_id = voucher_id
#             created_author.save()
#
#             formset = BookFormSet(request.POST, instance=created_author)
#             if formset.is_valid():
#                 logger.info('Data for Book is %s', formset.cleaned_data)
#                 formset.save()
#             else:
#                 logger.info('Formset errors %s', formset.errors)
#
#             totalform = TmpFormTotal(request.POST, instance=created_author)
#
#             if totalform.is_valid():
#                 logger.info('Formset errors %s', totalform)
#                 totalform.save()
#         else:
#             logger.info('Master form  errors %s', author.errors)
#         logger.info('*'*50)
#         return render_to_response('new_invoice.html',
#                                   {'form': author_form, 'formset': formset, 'formtotal': totalform},
#                                   context_instance=RequestContext(request))
#
#     else:
#         logger.info('Formset from GET is')
#
#         logger.info('Formset errors %s', totalform)
#         return render_to_response('new_invoice.html',
#                                   {'form': author_form, 'formset': formset, 'formtotal': totalform, 'postform': postform},
#                                   context_instance=RequestContext(request))
#
#
# def main_master_detail(request):
#     def get_new_voucher_id():
#         temp_vid = TmpPlInvoice.objects.order_by().values_list("voucher_id", flat=True).distinct()
#         if not temp_vid:
#             voucher_id = str(1).zfill(4)
#         else:
#             voucher_id = str(int(max(temp_vid)) + 1).zfill(4)
#         return voucher_id
#
#     def get_current_voucher_id():
#         temp_vid = TmpPlInvoice.objects.order_by().values_list("voucher_id", flat=True).distinct()
#         voucher_id = str(int(max(temp_vid))).zfill(4)
#         return voucher_id
#
#     ''' If we post data'''
#     if request.method == 'POST':
#         logger.info('*'*50)
#         author = TmpForm()
#         if request.POST['voucher_id']:
#             voucher_id = request.POST['voucher_id']
#             author = TmpPlInvoice.objects.get(voucher_id=voucher_id)
#             author = TmpForm(request.POST, instance=author)
#         else:
#             voucher_id = get_new_voucher_id()
#             author = TmpForm(request.POST)
#
#         if author.is_valid():
#             logger.info('Data for Author is %s', author.cleaned_data)
#             created_author = author.save(commit=False)
#             created_author.voucher_id = voucher_id
#             created_author.save()
#
#             formset = TmpFormDetForm(request.POST, instance=created_author)
#             logger.info('This is the posted form %s', instance.posted)
#             postform = CheckPostedForm(request.POST, instance=created_author, posted=created_author.posted)
#             if formset.is_valid():
#                 logger.info('Data for Book is %s', formset.cleaned_data)
#                 formset.save()
#             else:
#                 logger.info('voucher %s', created_author.voucher_id)
#
#             totalform = TmpFormTotal(request.POST, instance=created_author)
#
#             if totalform.is_valid():
#                 logger.info('amount Formset is valid %s', totalform.cleaned_data)
#                 totalform.save()
#             if postform.is_valid():
#                 logger.info('amount postform is valid %s', totalform.cleaned_data)
#                 totalform.save()
#
#         return render_to_response('main.html',
#                                   {'form': author_form, 'formset': formset, 'formtotal': totalform, 'postform': postform},
#                                   context_instance=RequestContext(request))
#
#     ''' If there are no records in the table'''
#     if len(get_listof_voucher_id()) == 0:
#         author = TmpPlInvoice()
#         author_form = TmpForm()
#         BookFormSet = inlineformset_factory(TmpPlInvoice, TmpPlInvoicedet,
#                                             exclude=('emp_id', 'voucher', 'lineitem', 'id',),
#                                             form=TmpFormDetForm, )
#         formset = BookFormSet(instance=author)
#         totalform = TmpFormTotal(instance=author)
#         postform = CheckPostedForm(instance=author, posted=author)
#         return render_to_response('main.html',
#                                   {'form': author_form, 'formset': formset, 'formtotal': totalform, 'postform': postform},
#                                   context_instance=RequestContext(request))
#
#     else:
#         ''' We want to show the current id'''
#         voucher_id = get_current_voucher_id()
#
#         ''' Define the three forms here'''
#         author = TmpPlInvoice.objects.get(voucher_id=voucher_id)
#         author_form = TmpForm(instance=author)
#         BookFormSet = inlineformset_factory(TmpPlInvoice, TmpPlInvoicedet,
#                                             exclude=('emp_id', 'voucher', 'lineitem', 'id',),
#                                             form=TmpFormDetForm, )
#         formset = BookFormSet(instance=author)
#         totalform = TmpFormTotal(instance=author)
#         logger.info('pos GET %s', str(author.posted))
#         print 'pos GET %s', str(author.posted)
#         postform = CheckPostedForm(instance=author, posted=str(author.posted))
#         logger.info('Main master detail form')
#         return render_to_response('main.html',
#                                   {'form': author_form, 'formset': formset, 'formtotal': totalform, 'postform': postform},
#                                   context_instance=RequestContext(request))
#
#
# def master_detail_save(request):
#     def get_new_voucher_id():
#         temp_vid = TmpPlInvoice.objects.order_by().values_list("voucher_id", flat=True).distinct()
#         if not temp_vid:
#             voucher_id = str(1).zfill(4)
#         else:
#             voucher_id = str(int(max(temp_vid)) + 1).zfill(4)
#         return voucher_id
#
#     def get_current_voucher_id():
#         temp_vid = TmpPlInvoice.objects.order_by().values_list("voucher_id", flat=True).distinct()
#         voucher_id = str(int(max(temp_vid))).zfill(4)
#         return voucher_id
#
#     ''' Define the three forms here'''
#     logger.info('This is how we live!!!!!!!!!!!!!!!!!!')
#     author_form = TmpForm()
#     author = TmpPlInvoice()
#     BookFormSet = inlineformset_factory(TmpPlInvoice, TmpPlInvoicedet, exclude=('emp_id', 'voucher', 'lineitem', 'id',),
#                                         form=TmpFormDetForm, extra=2)
#     formset = BookFormSet(instance=author)
#     totalform = TmpFormTotal()
#     postform = CheckPostedForm(instance=author)
#
#     ''' Decide what we want to show'''
#     if request.method == 'POST':
#         logger.info('*'*50)
#         voucher_id = get_new_voucher_id()
#         logger.info('VOUCHER %s', voucher_id)
#         author = TmpForm(request.POST)
#         if author.is_valid():
#             logger.info('Data for Author is %s', author.cleaned_data)
#             created_author = author.save(commit=False)
#             created_author.voucher_id = voucher_id
#             created_author.save()
#
#             formset = BookFormSet(request.POST, instance=created_author)
#             if formset.is_valid():
#                 logger.info('Data for Book is %s', formset.cleaned_data)
#                 formset.save()
#             else:
#                 logger.info('Formset errors %s', formset.errors)
#             if postform.is_valid():
#                 logger.info('Data for Book is %s', postform.cleaned_data)
#                 postform.save()
#             else:
#                 logger.info('Formset errors %s', postform.errors)
#
#             totalform = TmpFormTotal(request.POST, instance=created_author)
#
#             if totalform.is_valid():
#                 logger.info('amount Formset is valid %s', totalform.cleaned_data)
#                 totalform.save()
#         else:
#             logger.info('Master form  errors %s', author.errors)
#         logger.info('*'*50)
#         return render_to_response('main.html',
#                                   {'form': author_form, 'formset': formset, 'formtotal': totalform, 'postform': postform},
#                                   context_instance=RequestContext(request))
#
#     else:
#         ''' We want to show the current id'''
#         voucher_id = get_current_voucher_id()
#
#         ''' Define the three forms here'''
#         author = TmpPlInvoice.objects.get(voucher_id=voucher_id)
#         author_form = TmpForm(instance=author)
#
#         BookFormSet = inlineformset_factory(TmpPlInvoice, TmpPlInvoicedet,
#                                             exclude=('emp_id', 'voucher', 'lineitem', 'id',),
#                                             form=TmpFormDetForm, )
#         formset = BookFormSet(instance=author)
#         totalform = TmpFormTotal(instance=author)
#         postform = CheckPostedForm(instance=author)
#         logger.info('Main master detail form')
#         return render_to_response('main.html',
#                                   {'form': author_form, 'formset': formset, 'formtotal': totalform, 'postform': postform},
#                                   context_instance=RequestContext(request))
#
#
# def master_detail_next(request):
#     def decrement_voucher_id(form_id):
#         voucher_id = str(int(form_id) - 1).zfill(4)
#         return voucher_id
#
#     if request.method == 'POST':
#         logger.info('*'*50)
#         logger.info(request.POST)
#         form_id = request.POST['voucher_id']
#         logger.info('Data request for voucher_id %s ', form_id)
#         voucher_id = decrement_voucher_id(form_id)
#         voucher_id = get_decremented_voucher_id(voucher_id)
#         logger.info(voucher_id)
#     else:
#         voucher_id = ''
#
#     author = TmpPlInvoice.objects.get(voucher_id=voucher_id)
#     author_form = TmpForm(instance=author)
#
#     BookFormSet = inlineformset_factory(TmpPlInvoice, TmpPlInvoicedet,
#                                         exclude=('emp_id', 'voucher', 'lineitem', 'id',),
#                                         form=TmpFormDetForm, )
#     formset = BookFormSet(instance=author)
#     totalform = TmpFormTotal(instance=author)
#     postform = CheckPostedForm(instance=author, posted=author.posted)
#     logger.info(postform)
#     logger.info('*'*50)
#     return render_to_response('form.html', {'form': author_form, 'formset': formset, 'formtotal': totalform, 'postform': postform},
#                                   context_instance=RequestContext(request))
#
#
# def master_detail_previous(request):
#     def increment_voucher_id(form_id):
#         voucher_id = str(int(form_id) + 1).zfill(4)
#         return voucher_id
#
#     if request.method == 'POST':
#         logger.info('*'*50)
#         logger.info(request.POST)
#         form_id = request.POST['voucher_id']
#         logger.info('Data request for voucher_id %s ', form_id)
#         voucher_id = increment_voucher_id(form_id)
#         voucher_id = get_incremented_voucher_id(voucher_id)
#         logger.info('Final voucher id %s', voucher_id)
#     else:
#         voucher_id = ''
#
#     try:
#         author = TmpPlInvoice.objects.get(voucher_id=voucher_id)
#     except:
#         author = TmpPlInvoice.objects.get(voucher_id=get_max_voucher_id())
#
#     author_form = TmpForm(instance=author)
#
#     BookFormSet = inlineformset_factory(TmpPlInvoice, TmpPlInvoicedet,
#                                         exclude=('emp_id', 'voucher', 'lineitem', 'id',),
#                                         form=TmpFormDetForm, )
#     formset = BookFormSet(instance=author)
#     totalform = TmpFormTotal(instance=author)
#     postform = CheckPostedForm(instance=author)
#     logger.info('*'*50)
#     return render_to_response('form.html', {'form': author_form, 'formset': formset, 'formtotal': totalform, 'postform': postform},
#                                   context_instance=RequestContext(request))
#
#
# def master_detail_first(request):
#     voucher_id = get_min_voucher_id()
#     if request.method == 'POST':
#         logger.info('*'*50)
#     else:
#         voucher_id = ''
#     logger.info('First voucher %s', voucher_id)
#     author = TmpPlInvoice.objects.get(voucher_id=voucher_id)
#     author_form = TmpForm(instance=author)
#     BookFormSet = inlineformset_factory(TmpPlInvoice, TmpPlInvoicedet,
#                                         exclude=('emp_id', 'voucher', 'lineitem', 'id',),
#                                         form=TmpFormDetForm, )
#     formset = BookFormSet(instance=author)
#     totalform = TmpFormTotal(instance=author)
#     postform = CheckPostedForm(instance=author)
#     logger.info('*'*50)
#     return render_to_response('form.html', {'form': author_form, 'formset': formset, 'formtotal': totalform, 'postform': postform},
#                                   context_instance=RequestContext(request))
#
#
# def master_detail_last(request):
#     voucher_id = get_max_voucher_id()
#     if request.method == 'POST':
#         logger.info('*'*50)
#     else:
#         voucher_id = ''
#     logger.info('Last voucher %s', voucher_id)
#     author = TmpPlInvoice.objects.get(voucher_id=voucher_id)
#     author_form = TmpForm(instance=author)
#     BookFormSet = inlineformset_factory(TmpPlInvoice, TmpPlInvoicedet,
#                                         exclude=('emp_id', 'voucher', 'lineitem', 'id',),
#                                         form=TmpFormDetForm, )
#     formset = BookFormSet(instance=author)
#     totalform = TmpFormTotal(instance=author)
#     postform = CheckPostedForm(instance=author)
#     logger.info('*'*50)
#     return render_to_response('form.html', {'form': author_form, 'formset': formset, 'formtotal': totalform, 'postform': postform},
#                                   context_instance=RequestContext(request))
#
#
# def search_master_detail(request):
#
#     if request.method == 'POST':
#         logger.info('*'*50)
#         logger.info(request.POST)
#         voucher_id = request.POST['voucher_id']
#         logger.info(voucher_id)
#         thisinstance = TmpPlInvoice.objects.get(voucher_id=voucher_id)
#         form = TmpForm(instance=thisinstance)
#     else:
#         voucher_id = ''
#
#     author = TmpPlInvoice.objects.get(voucher_id=voucher_id)
#     author_form = TmpForm(instance=author)
#
#     BookFormSet = inlineformset_factory(TmpPlInvoice, TmpPlInvoicedet,
#                                         exclude=('emp_id', 'voucher', 'lineitem', 'id',),
#                                         form=TmpFormDetForm, )
#     formset = BookFormSet(instance=author)
#     totalform = TmpFormTotal(instance=author)
#     postform = CheckPostedForm(instance=author)
#
#     logger.info('*'*50)
#     return render_to_response('form.html',
#                                   {'form': author_form, 'formset': formset, 'formtotal': totalform, 'postform': postform},
#                                   context_instance=RequestContext(request))
#
#
# def master_detail_new(request):
#     author = TmpPlInvoice()
#     author_form = TmpForm(instance=author)
#     BookFormSet = inlineformset_factory(TmpPlInvoice, TmpPlInvoicedet,
#                                         exclude=('emp_id', 'voucher', 'lineitem', 'id',),
#                                         form=TmpFormDetForm, )
#     formset = BookFormSet(instance=author)
#     totalform = TmpFormTotal(instance=author)
#     postform = CheckPostedForm(instance=author)
#     return render_to_response('form.html', {'form': author_form, 'formset': formset, 'formtotal': totalform, 'postform': postform},
#                                   context_instance=RequestContext(request))
#
#
#
# def master_detail_del(request):
#     if request.method == 'POST':
#         logger.info('*'*50)
#         voucher_id = request.POST['voucher_id']
#         logger.info('VOUCHER %s', voucher_id)
#         instance = TmpPlInvoicedet.objects.filter(voucher_id=voucher_id)
#         for a in instance:
#             a.delete()
#         messages.success(request, 'Deleted')
#         instance = TmpPlInvoice.objects.get(voucher_id=voucher_id)
#         instance.delete()
#         logger.info('Create new instance with voucher id %s', get_decremented_voucher_id(voucher_id))
#         author = TmpPlInvoice.objects.get(voucher_id=get_decremented_voucher_id(voucher_id))
#
#     else:
#         logger.info('GET')
#         logger.info('Create new instance with voucher id %s', get_max_voucher_id())
#         author = TmpPlInvoice.objects.get(voucher_id=get_max_voucher_id())
#
#     author_form = TmpForm(instance=author)
#     BookFormSet = inlineformset_factory(TmpPlInvoice, TmpPlInvoicedet,
#                                         exclude=('emp_id', 'voucher', 'lineitem', 'id',),
#                                         form=TmpFormDetForm, )
#     formset = BookFormSet(instance=author)
#     totalform = TmpFormTotal(instance=author)
#     postform = CheckPostedForm(instance=author)
#
#     logger.info('*'*50)
#     return render_to_response('form.html', {'form': author_form, 'formset': formset, 'formtotal': totalform, 'postform': postform},
#                                   context_instance=RequestContext(request))
#
#
# def Copy_master_detail(request):
#     def get_new_voucher_id():
#         temp_vid = TmpPlInvoice.objects.order_by().values_list("voucher_id", flat=True).distinct()
#         logger.info('Voucher ID already present %s', temp_vid)
#         if not temp_vid:
#             voucher_id = str(1).zfill(4)
#         else:
#             voucher_id = str(int(max(temp_vid)) + 1).zfill(4)
#         return voucher_id
#
#     voucher_id = get_new_voucher_id()
#     author_form = TmpForm(initial={'voucher_id': voucher_id})
#     author = TmpPlInvoice()
#     BookFormSet = inlineformset_factory(TmpPlInvoice, TmpPlInvoicedet, exclude=('emp_id', 'voucher', 'lineitem', 'id',),
#                                         form=TmpFormDetForm, extra=10)
#     formset = BookFormSet(instance=author)
#     totalform = TmpFormTotal()
#
#     if request.method == 'POST':
#         logger.info('*'*50)
#         author = TmpForm(request.POST, initial={'voucher_id': voucher_id})
#         if author.is_valid():
#             logger.info('Data for Author is %s', author.cleaned_data)
#             created_author = author.save()
#
#             formset = BookFormSet(request.POST, instance=created_author)
#             if formset.is_valid():
#                 logger.info('Data for Book is %s', formset.cleaned_data)
#                 formset.save()
#             else:
#                 logger.info('Formset errors %s', formset.errors)
#
#             totalform = TmpFormTotal(request.POST, instance=created_author)
#
#             if totalform.is_valid():
#                 logger.info('Formset errors %s', totalform)
#                 totalform.save()
#         else:
#             logger.info('Master form  errors %s', author.errors)
#         logger.info('*'*50)
#         return render_to_response('new_invoice.html',
#                                   {'form': author_form, 'formset': formset, 'formtotal': totalform},
#                                   context_instance=RequestContext(request))
#
#     else:
#         logger.info('Formset from GET is')
#
#         logger.info('Formset errors %s', totalform)
#         return render_to_response('new_invoice.html',
#                                   {'form': author_form, 'formset': formset, 'formtotal': totalform},
#                                   context_instance=RequestContext(request))
#
#
# def master_detail_post(request):
#     ''' Decide what we want to show'''
#     if request.method == 'POST':
#         logger.info('*'*50)
#         if request.POST['voucher_id']:
#             voucher_id = request.POST['voucher_id']
#             author = TmpPlInvoice.objects.get(voucher_id=voucher_id)
#             author = TmpForm(request.POST, instance=author)
#         else:
#             voucher_id = get_new_voucher_id()
#             author = TmpForm(request.POST)
#
#         logger.info('VOUCHER %s', voucher_id)
#
#         if author.is_valid():
#             logger.info('Data for Author is %s', author.cleaned_data)
#             created_author = author.save(commit=False)
#             created_author.voucher_id = voucher_id
#             created_author.save()
#
#             formset = BookFormSet(request.POST, instance=created_author)
#             if formset.is_valid():
#                 logger.info('Data for Book is %s', formset.cleaned_data)
#                 formset.save()
#             else:
#                 logger.info('voucher %s', created_author.voucher_id)
#                 logger.info('Formset errors %s', formset.errors)
#                 # logger.info('Formset errors %s', formset)
#             if postform.is_valid():
#                 logger.info('Data for post form is %s', postform.cleaned_data)
#                 postform.save()
#             else:
#                 logger.info('POstFormset errors %s', postform.errors)
#
#             totalform = TmpFormTotal(request.POST, instance=created_author)
#
#             if totalform.is_valid():
#                 logger.info('amount Formset is valid %s', totalform.cleaned_data)
#                 totalform.save()
#         else:
#             logger.info('Master form  errors %s', author.errors)
#         logger.info('*'*50)
#         return render_to_response('main.html',
#                                   {'form': author_form, 'formset': formset, 'formtotal': totalform, 'postform': postform},
#                                   context_instance=RequestContext(request))
#
#     elif len(get_listof_voucher_id()) == 0:
#         author = TmpPlInvoice()
#         author_form = TmpForm()
#         BookFormSet = inlineformset_factory(TmpPlInvoice, TmpPlInvoicedet,
#                                             exclude=('emp_id', 'voucher', 'lineitem', 'id',),
#                                             form=TmpFormDetForm, )
#         formset = BookFormSet(instance=author)
#         totalform = TmpFormTotal(instance=author)
#         postform = CheckPostedForm(instance=author)
#         return render_to_response('main.html',
#                                   {'form': author_form, 'formset': formset, 'formtotal': totalform, 'postform': postform},
#                                   context_instance=RequestContext(request))
#
#     else:
#         ''' We want to show the current id'''
#         voucher_id = get_current_voucher_id()
#
#         ''' Define the three forms here'''
#         author = TmpPlInvoice.objects.get(voucher_id=voucher_id)
#         author_form = TmpForm(instance=author)
#
#         BookFormSet = inlineformset_factory(TmpPlInvoice, TmpPlInvoicedet,
#                                             exclude=('emp_id', 'voucher', 'lineitem', 'id',),
#                                             form=TmpFormDetForm, )
#         formset = BookFormSet(instance=author)
#         totalform = TmpFormTotal(instance=author)
#         postform = CheckPostedForm(instance=author)
#         logger.info('Main master detail form')
#         return render_to_response('main.html',
#                                   {'form': author_form, 'formset': formset, 'formtotal': totalform, 'postform': postform},
#                                   context_instance=RequestContext(request))
#
#
