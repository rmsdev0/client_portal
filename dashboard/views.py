from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from models import *
import datetime as dt
import graph_data as gd
from django.views.decorators.csrf import csrf_exempt
import crm_query as cq
# Create your views here.


# test page
def db_test(request):
    return render_to_response('dash.html')


# ***********production dashboard views********************


def prod_dashboard(request):
    cid = request.user.last_name
    service = request.user.first_name
    camps = CampaignList.objects.filter(client_id=cid)
    raw_data = gd.raw_data(camps, gd.today, gd.end_datetime)
    wk_data = gd.weekly_raw_data(camps)
    daily_metrics = gd.get_daily_metrics(raw_data)
    handled = (daily_metrics.calls - daily_metrics.abandons)
    graph1 = gd.graph_form_list
    call_data = gd.get_calls(wk_data)
    call_total = sum(call_data)
    abandon_data = gd.get_abandons(wk_data)
    abandon_totals = sum(abandon_data)
    refund_daily = gd.get_refunds(wk_data)
    refund_total = sum(refund_daily)
    save_daily = gd.get_saves(wk_data)
    save_total = sum(save_daily)
    cancel_daily = gd.get_cancels(wk_data)
    cancel_total = sum(cancel_daily)
    wk_list = gd.week_list
    avg_que = gd.get_avg_wait(wk_data)
    recent = gd.get_recent_calls(service)
    user_name = request.user.username
    return render_to_response('prod_dash.html', {'metrics': daily_metrics,
                                                 'graph1': graph1,
                                                 'abandon': abandon_data,
                                                 'calls': call_data,
                                                 'cancel': cancel_total,
                                                 'refund': refund_total,
                                                 'save': save_total,
                                                 'abandon_tot': abandon_totals,
                                                 'call_tot': call_total,
                                                 'week': wk_list,
                                                 'save_day': save_daily,
                                                 'cancel_day': cancel_daily,
                                                 'refund_day': refund_daily,
                                                 'wait': avg_que,
                                                 'rec_calls': recent,
                                                 'service': service,
                                                 'user': user_name,
                                                 'camp_list': camps,
                                                 'hand': handled})


@csrf_exempt
def prod_dashboard_custom(request):
    cid = request.user.last_name
    service = request.user.first_name
    camps = CampaignList.objects.filter(client_id=cid)
    if request.method == 'POST':
        if request.POST.get('service_name'):
            serv = request.POST.get('service_name')
            camps = [CampaignList(campaign_name=serv, client_id=0)]
            start = gd.today
            end = gd.end_datetime
            end_date = gd.today
            raw_data = gd.raw_data(camps, gd.today, gd.end_datetime)
            wk_data = gd.weekly_raw_data(camps)
            daily_metrics = gd.get_daily_metrics(raw_data)
            handled = (daily_metrics.calls - daily_metrics.abandons)
            graph1 = gd.graph_form_list
            call_data = gd.get_calls(wk_data)
            call_total = sum(call_data)
            abandon_data = gd.get_abandons(wk_data)
            abandon_totals = sum(abandon_data)
            refund_daily = gd.get_refunds(wk_data)
            refund_total = sum(refund_daily)
            save_daily = gd.get_saves(wk_data)
            save_total = sum(save_daily)
            cancel_daily = gd.get_cancels(wk_data)
            cancel_total = sum(cancel_daily)
            dates = (start, end_date)
            wk_list = gd.week_list
            avg_que = gd.get_avg_wait(wk_data)
            recent = gd.get_recent_calls(service)
            user_name = request.user.username
            return render_to_response('prod_dash_custom.html', {'metrics': daily_metrics,
                                                                'graph1': graph1,
                                                                'abandon': abandon_data,
                                                                'calls': call_data,
                                                                'cancel': cancel_total,
                                                                'refund': refund_total,
                                                                'save': save_total,
                                                                'abandon_tot': abandon_totals,
                                                                'call_tot': call_total,
                                                                'date_range': dates,
                                                                'week': wk_list,
                                                                'save_day': save_daily,
                                                                'cancel_day': cancel_daily,
                                                                'refund_day': refund_daily,
                                                                'wait': avg_que,
                                                                'rec_calls': recent,
                                                                'service': service,
                                                                'user': user_name,
                                                                'camp_list': camps,
                                                                'hand': handled})
        else:
            start = request.POST.get('start-date')
            end_date = request.POST.get('end-date')
            end = end_date + ' 23:59:59'
            raw_data = gd.raw_data(camps, start, end)
            wk_data = gd.weekly_raw_data(camps)
            daily_metrics = gd.get_daily_metrics(raw_data)
            handled = (daily_metrics.calls - daily_metrics.abandons)
            graph1 = gd.graph_form_list
            call_data = gd.get_calls(wk_data)
            call_total = sum(call_data)
            abandon_data = gd.get_abandons(wk_data)
            abandon_totals = sum(abandon_data)
            refund_daily = gd.get_refunds(wk_data)
            refund_total = sum(refund_daily)
            save_daily = gd.get_saves(wk_data)
            save_total = sum(save_daily)
            cancel_daily = gd.get_cancels(wk_data)
            cancel_total = sum(cancel_daily)
            dates = (start, end_date)
            wk_list = gd.week_list
            avg_que = gd.get_avg_wait(wk_data)
            recent = gd.get_recent_calls(service)
            user_name = request.user.username
            return render_to_response('prod_dash_custom.html', {'metrics': daily_metrics,
                                                                'graph1': graph1,
                                                                'abandon': abandon_data,
                                                                'calls': call_data,
                                                                'cancel': cancel_total,
                                                                'refund': refund_total,
                                                                'save': save_total,
                                                                'abandon_tot': abandon_totals,
                                                                'call_tot': call_total,
                                                                'date_range': dates,
                                                                'week': wk_list,
                                                                'save_day': save_daily,
                                                                'cancel_day': cancel_daily,
                                                                'refund_day': refund_daily,
                                                                'wait': avg_que,
                                                                'rec_calls': recent,
                                                                'service': service,
                                                                'user': user_name,
                                                                'camp_list': camps,
                                                                'hand': handled})

    else:
        return render_to_response('404.html')


# settings page
def settings(request):
    return render_to_response('settings.html', {'req_data': request})


# handle api credential form response
@csrf_exempt
def api_form_handler(request):
    if request.method == 'POST':
        api_url = request.POST.get('api-url')
        api_user = request.POST.get('api-user-name')
        api_password = request.POST.get('api-password')
        api_name = request.POST.get('serv-name')
        new_api = CrmInfo.objects.create(name=api_name, url=api_url, pswd=api_password, user_name=api_user)
        new_api.save()
        return HttpResponseRedirect('/settings')
    else:
        return render_to_response('404.html')


# inbox view
def inbox(request):
    return render_to_response('inbox.html')


# crm info listing view
@csrf_exempt
def crm_listing(request):
    try:
        crm_acct = request.user.first_name
        num = request.POST.get('phone')
        account = CrmInfo.objects.get(name=crm_acct)
        data = cq.crm_query(account, num)
        info = cq.order_data_json(data)
        return render_to_response('crm_list.html', {'data': info})
    except IndexError:
        return render_to_response('crm-listing-no-data.html')


# call history
@csrf_exempt
def call_history(request):
    service = request.user.first_name
    if request.method == 'POST':
        date = request.POST.get('date')
        recent = gd.get_call_list(service, date)
        return render_to_response('call-history.html', {'rec_calls': recent,
                                                        'display_date': date})
    else:
        today = dt.date.today()
        recent = gd.get_call_list(service, today)
        return render_to_response('call-history.html', {'rec_calls': recent,
                                                        'display_date': today})


# handle phone number call history search and return data to call-history page
def call_history_search(request):
    pass


#get and return hourly data for current day
def hourly_data(request):
    cid = request.user.last_name
    camps = CampaignList.objects.filter(client_id=cid)
    hourly = gd.get_hourly_metrics(camps, gd.today)
    return render_to_response('hourly-stats1.html', {'hour': hourly})


@csrf_exempt
#get and return hourly data for given day
def hourly_data_custom(request):
    if request.method == 'POST':
        search_date = request.POST.get('date')
        cid = request.user.last_name
        camps = CampaignList.objects.filter(client_id=cid)
        hourly = gd.get_hourly_metrics(camps, search_date)
        return render_to_response('hourly-stats1.html', {'hour': hourly})
    else:
        pass  # return 404 error



def test(request):
    calls_data = gd.calls_feb()
    return render_to_response('test.html', {'calls': calls_data})


