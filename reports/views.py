from django.shortcuts import render, render_to_response, HttpResponse
from models import Reports, SlProduct
from forms import PForm
import logging
import urllib

# *************************************************** #
#                  Reports                            #
# *************************************************** #

logger = logging.getLogger(__name__)


def reports(request):
    acct_names = Reports.objects.filter(cat=1).order_by('report_name')
    sales_names = Reports.objects.filter(cat=2).order_by('report_name')
    purchase_names = Reports.objects.filter(cat=3).order_by('report_name')
    stock_names = Reports.objects.filter(cat=4).order_by('report_name')
    party_names = Reports.objects.filter(cat=5).order_by('report_name')
    group_names = ''
    audit_names = ''

    # for a in purchase_names:
    logger.info('*'*25 + 'reports' + '*'*25)
    logger.info('reports  %s', purchase_names)
    context = {
        'acct_names': acct_names,
        'sales_names': sales_names,
        'purchase_names': purchase_names,
        'stock_names': stock_names,
        'party_names': party_names
    }
    # logger.info('Context %s', context)
    logger.info('*' * 50)
    return render_to_response('reports.html', context)


def pf_pl_invoicedet(request, file_name):
    logger.info('In PF PL')
    form = PForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            logger.info('*' * 50)
            logger.info(data)
            from_date = str(data['date_from'].strftime('%d-%m-%y').replace('-', '.'))
            to_date = str(data['date_to'].strftime('%d-%m-%y').replace('-', '.'))
            if data['acct_name'] == '0'*20:
                acct_name = 'ALL'
            else:
                acct_name = data['acct_name']
            logger.info('*' * 50)
            url = 'http://42.201.238.170:7001/reports/rwservlet?%20server=RptSrv+report=s:\\apps\\oracle11g\\art\\reports\\ledger.rdf+userid=click_kt/pass@psm+desformat=pdf+DESTYPE=cache+p_date_from=' + from_date + '+p_date_to=' + to_date + '+p_acct_id=' + acct_name

            logger.info(url)
            reports_download(url, file_name)
            pdf_name = "report" + file_name
            image_data = open(pdf_name, 'rb').read()

            context = {
                'file_name': file_name,
                'url': url,
                'form': form
            }
            return HttpResponse(image_data, content_type='application/pdf')
        else:
            logger.info('Not valid')
            logger.error(form.errors)
    else:
        form = PForm()
        logger.info('this is -------- %s', form)
        return render(request, 'pf_pl_invoicedet.html', context={'form': form})


def reports_download(report_url, file_name):
    logger.info('report download')
    pdf_name = "report" + file_name
    urllib.urlretrieve(report_url, pdf_name)
