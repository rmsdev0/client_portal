__author__ = 'ryan schuetz'

from models import *
from datetime import datetime
import datetime as dt
from django.contrib import auth
import csv

today = dt.date.today()
date_today = today.strftime('%Y/%m/%d')
yesterday = today - dt.timedelta(days=1)
week = today - dt.timedelta(days=7)
date_yesterday = yesterday.strftime('%Y/%m/%d')
end_datetime = str(today) + ' 23:59:59'
yesterday_end_datetime = str(yesterday) + ' 23:59:59'


#min_dt = datetime.datetime.combine('2015-07-28', datetime.time.min)
#max_dt = datetime.datetime.combine('2015-07-28', datetime.time.max)


#format date to match bp_sql
def date_format(date):
    string_time = date.strftime('%Y-%m-%d')
    return string_time


#date format for graphs
def graph_date(date):
    graph_time = date.strftime('%d')
    return graph_time


def graph_date_form(date):
    graph_date1 = date.strftime('%Y, %m, %d')
    return graph_date1


#seconds to H:M:S
def seconds_to_hms(seconds):
    time = dt.timedelta(seconds=seconds)
    return time


#seconds to M:S
def seconds_to_ms(seconds):
    ms = '%d:%02d' % (seconds / 60, seconds % 60)
    return ms


week_list = [date_format(yesterday), date_format(today - dt.timedelta(days=2)),
             date_format(today - dt.timedelta(days=3)), date_format(today - dt.timedelta(days=4)),
             date_format(today - dt.timedelta(days=5)), date_format(today - dt.timedelta(days=6)),
             date_format(today - dt.timedelta(days=7)), date_format(today - dt.timedelta(days=8))]
graph_week_list = [graph_date(yesterday), graph_date(today - dt.timedelta(days=2)),
                   graph_date(today - dt.timedelta(days=3)), graph_date(today - dt.timedelta(days=4)),
                   graph_date(today - dt.timedelta(days=5)), graph_date(today - dt.timedelta(days=6)),
                   graph_date(today - dt.timedelta(days=7)), graph_date(today - dt.timedelta(days=8))]
graph_form_list = [graph_date_form(yesterday), graph_date_form(today - dt.timedelta(days=2)),
                   graph_date_form(today - dt.timedelta(days=3)), graph_date_form(today - dt.timedelta(days=4)),
                   graph_date_form(today - dt.timedelta(days=5)), graph_date_form(today - dt.timedelta(days=6)),
                   graph_date_form(today - dt.timedelta(days=7)), graph_date_form(today - dt.timedelta(days=8))]
hour_list = ['00:00:00', '01:00:00', '02:00:00', '03:00:00', '04:00:00', '05:00:00', '06:00:00', '07:00:00', '08:00:00',
             '09:00:00', '10:00:00', '11:00:00', '12:00:00', '13:00:00', '14:00:00', '15:00:00', '16:00:00', '17:00:00',
             '18:00:00', '19:00:00', '20:00:00', '21:00:00', '22:00:00', '23:00:00', '23:59:59']

class DailyMetrics:

    def __init__(self, calls, abandons, saves, wait_time, callback, handle, ref, abn, sl, tt, ht, acw):
        self.calls = calls
        self.abandons = abandons
        self.saves = saves
        self.wait_time = wait_time
        self.callbacks = callback
        self.handle_time = handle
        self.refunds = ref
        self.abandon_rate = abn
        self.service_level = sl
        self.talk_time = tt
        self.hold_time = ht
        self.aftercall = acw


def raw_data(camp_list, start, end):
    metric_data = []
    for camp in camp_list:
        query = CallDetail.objects.using('bp').filter(service_name=camp.campaign_name, start_time__range=(start, end))
        metric_data.append(query)
    return metric_data


# hourly metrics one day ie yesterday
def get_hourly_metrics(camps, date):
    data = []
    for i in range(0, 24, 1):
        try:
            start = str(date) + ' ' + hour_list[i]
            end = str(date) + ' ' + hour_list[i+1]
            camp_data = raw_data(camps, start, end)
            metrics = get_daily_metrics(camp_data)
            data.append((hour_list[i], hour_list[i+1], metrics.service_level, metrics.calls, (metrics.calls - metrics.abandons),
                         metrics.abandons, metrics.wait_time, metrics.handle_time, metrics.talk_time, metrics.hold_time,
                         metrics.aftercall))
        except ZeroDivisionError:
            data.append((hour_list[i], hour_list[i+1], "NA"))
    return data


# hourly metrics today to current time
def get_hourly_metrics_current(camps):
    data = []
    for i in range(0, 24, 1):
        try:
            print data
            start = str(today) + ' ' + hour_list[i]
            end = str(today) + ' ' + hour_list[i+1]
            camp_data = raw_data(camps, start, end)
            metrics = get_daily_metrics(camp_data)
            print metrics.service_level
            data.append((hour_list[i], hour_list[i+1], metrics.service_level, metrics.calls, (metrics.calls - metrics.abandons),
                         metrics.abandons, metrics.wait_time, metrics.handle_time, metrics.talk_time, metrics.hold_time,
                         metrics.aftercall))
        except ZeroDivisionError:
            data.append((hour_list[i], hour_list[i+1], "NA"))
    return data


# get metrics
def get_daily_metrics(camp_data):
    calls, abandons, saves, callbacks, refunds = 0, 0, 0, 0, 0
    wait, q_wait, duration, aftercall, sl_over, talk, hold = [], [], [], [], [], [], []
    for camp in camp_data:
        for i in camp:
            if i.queue_time or i.talk_time and i.disposition != 'SELF_SERVICE':
                calls += 1
                q_wait.append(i.queue_time)
                if i.disposition == 'ABANDONED_QUEUE':
                    abandons += 1
                elif i.disposition == 'CALLBACK_REQUESTED':
                    callbacks += 1
                else:
                    wait.append(i.queue_time)
                    call_duration = i.talk_time + i.acw_time + i.hold_time
                    duration.append(call_duration)
                    talk.append(i.talk_time)
                    hold.append(i.hold_time)
                    aftercall.append(i.acw_time)
                    if i.agent_disposition_name:
                        dispo_split = i.agent_disposition_name.split(' ')
                        if dispo_split[0] == 'SAVE' or dispo_split[0] == 'NEW':
                            saves += 1
                        elif dispo_split[0] == 'REFUND':
                            refunds += 1
            else:
                pass   # todo (error???)
    for x in wait:
        if x < 60:
            sl_over.append(x)
    qwt = sum(q_wait)/calls
    handle = sum(duration)/len(duration)
    abn = (abandons / float(calls - callbacks)) * 100
    abn_rate = str('%.2f' % round(abn, 2)) + '%'
    service_temp = ((len(sl_over) / float(calls)) * 100)
    service_level = str('%.2f' % round(service_temp, 2)) + '%'
    talk_time = sum(talk)/len(talk)
    hold_time = sum(hold)/len(hold)
    acw = sum(aftercall)/len(aftercall)
    metrics = DailyMetrics(calls, abandons, saves, seconds_to_ms(qwt), callbacks, seconds_to_ms(handle), refunds,
                           abn_rate, service_level, seconds_to_ms(talk_time), seconds_to_ms(hold_time), seconds_to_ms(acw))
    return metrics


# last week of raw data
def weekly_raw_data(camp_list):
    metric_data = []
    for camp in camp_list:
        query = CallDetail.objects.using('bp').filter(service_name=camp.campaign_name, start_time__range=(week, yesterday_end_datetime))
        metric_data.append(query)
    return metric_data


# get total calls last 7 days
def get_calls(camp_data):
    # weekly_call_totals [yesterday,2,3,4,5,6,7,]
    weekly_call_totals = [0, 0, 0, 0, 0, 0, 0]
    for camp in camp_data:
        for call in camp:
            call_datetime = call.start_time
            call_date = str(call_datetime).split(' ')
            graph_date_form = call_datetime.strftime('%Y, %m, %d')
            if call_date[0] == week_list[0]:
                weekly_call_totals[0] += 1
            elif call_date[0] == week_list[1]:
                weekly_call_totals[1] += 1
            elif call_date[0] == week_list[2]:
                weekly_call_totals[2] += 1
            elif call_date[0] == week_list[3]:
                weekly_call_totals[3] += 1
            elif call_date[0] == week_list[4]:
                weekly_call_totals[4] += 1
            elif call_date[0] == week_list[5]:
                weekly_call_totals[5] += 1
            elif call_date[0] == week_list[6]:
                weekly_call_totals[6] += 1
    return weekly_call_totals


#get abandons last 7 days
def get_abandons(camp_data):
    weekly_abandon_totals = [0, 0, 0, 0, 0, 0, 0]
    for camp in camp_data:
        for call in camp:
            if call.disposition == 'ABANDONED' or call.disposition =='ABANDONED_QUEUE':
                call_datetime = call.start_time
                call_date = str(call_datetime).split(' ')
                graph_date_form = call_datetime.strftime('%Y, %m, %d')
                if call_date[0] == week_list[0]:
                    weekly_abandon_totals[0] += 1
                elif call_date[0] == week_list[1]:
                    weekly_abandon_totals[1] += 1
                elif call_date[0] == week_list[2]:
                    weekly_abandon_totals[2] += 1
                elif call_date[0] == week_list[3]:
                    weekly_abandon_totals[3] += 1
                elif call_date[0] == week_list[4]:
                    weekly_abandon_totals[4] += 1
                elif call_date[0] == week_list[5]:
                    weekly_abandon_totals[5] += 1
                elif call_date[0] == week_list[6]:
                    weekly_abandon_totals[6] += 1
    return weekly_abandon_totals


#get refunds/saves/cancels last 7 days
def get_saves(camp_data):
    # weekly_save_totals [yesterday,2,3,4,5,6,7,]
    weekly_save_totals = [0, 0, 0, 0, 0, 0, 0]
    for camp in camp_data:
        for call in camp:
            call_datetime = call.start_time
            call_date = str(call_datetime).split(' ')
            if call.agent_disposition_name:
                save = call.agent_disposition_name.split(' ')
                if save[0] == 'SAVE' and call_date[0] == week_list[0]:
                    weekly_save_totals[0] += 1
                elif save[0] == 'SAVE' and call_date[0] == week_list[1]:
                    weekly_save_totals[1] += 1
                elif save[0] == 'SAVE' and call_date[0] == week_list[2]:
                    weekly_save_totals[2] += 1
                elif save[0] == 'SAVE' and call_date[0] == week_list[3]:
                    weekly_save_totals[3] += 1
                elif save[0] == 'SAVE' and call_date[0] == week_list[4]:
                    weekly_save_totals[4] += 1
                elif save[0] == 'SAVE' and call_date[0] == week_list[5]:
                    weekly_save_totals[5] += 1
                elif save[0] == 'SAVE' and call_date[0] == week_list[6]:
                    weekly_save_totals[6] += 1
    return weekly_save_totals


def get_refunds(camp_data):
    # weekly_save_totals [yesterday,2,3,4,5,6,7,]
    weekly_refund_totals = [0, 0, 0, 0, 0, 0, 0]
    for camp in camp_data:
        for call in camp:
            call_datetime = call.start_time
            call_date = str(call_datetime).split(' ')
            if call.agent_disposition_name:
                refund = call.agent_disposition_name.split(' ')
                if refund[0] == 'REFUND' and call_date[0] == week_list[0]:
                    weekly_refund_totals[0] += 1
                elif refund[0] == 'REFUND' and call_date[0] == week_list[1]:
                    weekly_refund_totals[1] += 1
                elif refund[0] == 'REFUND' and call_date[0] == week_list[2]:
                    weekly_refund_totals[2] += 1
                elif refund[0] == 'REFUND' and call_date[0] == week_list[3]:
                    weekly_refund_totals[3] += 1
                elif refund[0] == 'REFUND' and call_date[0] == week_list[4]:
                    weekly_refund_totals[4] += 1
                elif refund[0] == 'REFUND' and call_date[0] == week_list[5]:
                    weekly_refund_totals[5] += 1
                elif refund[0] == 'REFUND' and call_date[0] == week_list[6]:
                    weekly_refund_totals[6] += 1
    return weekly_refund_totals


def get_cancels(camp_data):
    # weekly_save_totals [yesterday,2,3,4,5,6,7,]
    weekly_cancel_totals = [0, 0, 0, 0, 0, 0, 0]
    for camp in camp_data:
        for call in camp:
            call_datetime = call.start_time
            call_date = str(call_datetime).split(' ')
            if call.agent_disposition_name:
                cancel = call.agent_disposition_name.split(' ')
                if cancel[0] == 'PRE' or cancel[0] == 'POST':
                    if call_date[0] == week_list[0]:
                        weekly_cancel_totals[0] += 1
                    elif call_date[0] == week_list[1]:
                        weekly_cancel_totals[1] += 1
                    elif call_date[0] == week_list[2]:
                        weekly_cancel_totals[2] += 1
                    elif call_date[0] == week_list[3]:
                        weekly_cancel_totals[3] += 1
                    elif call_date[0] == week_list[4]:
                        weekly_cancel_totals[4] += 1
                    elif call_date[0] == week_list[5]:
                        weekly_cancel_totals[5] += 1
                    elif call_date[0] == week_list[6]:
                        weekly_cancel_totals[6] += 1
    return weekly_cancel_totals


def get_avg_wait(camp_data):
     # weekly_save_totals [yesterday,2,3,4,5,6,7,]
    averages = []
    weekly_wait_times = [[], [], [], [], [], [], []]
    for camp in camp_data:
        for call in camp:
            call_datetime = call.start_time
            call_date = str(call_datetime).split(' ')
            if call.ivr_time:
                if call_date[0] == week_list[0]:
                    weekly_wait_times[0].append(call.queue_time)
                elif call_date[0] == week_list[1]:
                    weekly_wait_times[1].append(call.queue_time)
                elif call_date[0] == week_list[2]:
                    weekly_wait_times[2].append(call.queue_time)
                elif call_date[0] == week_list[3]:
                    weekly_wait_times[3].append(call.queue_time)
                elif call_date[0] == week_list[4]:
                    weekly_wait_times[4].append(call.queue_time)
                elif call_date[0] == week_list[5]:
                    weekly_wait_times[5].append(call.queue_time)
                elif call_date[0] == week_list[6]:
                    weekly_wait_times[6].append(call.queue_time)
    for i in weekly_wait_times:
        avg = sum(i)/len(i)
        averages.append(avg)
    return averages


class RecentCalls:
    def __init__(self, phone):
        self.phone = phone


# todo convert to show only escalated calls
def get_recent_calls(service):
    query = CallDetail.objects.using('bp').filter(service_name=service, start_time__range=(today, end_datetime))
    calls_temp = []
    for call in query:
        if call.ivr_time and call.agent_disposition_name:
            recent = RecentCalls(call.from_phone)
            dispo_split = call.agent_disposition_name.split(" ")
            if dispo_split[0] == 'ESCALATION':
                recent.disposition = call.agent_disposition_name
                recent.que_time = seconds_to_ms(call.queue_time)
                recent.talk_time = seconds_to_ms(call.talk_time)
                recent.acw = seconds_to_ms(call.acw_time)
                recent.agent = call.callee_login_id
                recent.phone = recent.phone[1:]
                calls_temp.append(recent)
    return calls_temp[-25:]


# get lists of calls, editible for data ranges? eventually replace get_recent_calls()
def get_call_list(service, date):
    date = date
    end_date_time = str(date) + ' 23:59:59'
    query = CallDetail.objects.using('bp').filter(service_name=service, start_time__range=(date, end_date_time))
    calls_temp = []
    for call in query:
        if call.ivr_time and call.disposition != 'ABANDONED' and call.disposition != 'ABANDONED_QUEUE'\
                and call.disposition != 'SYSTEM_DISCONNECTED' and call.disposition != 'SELF_SERVICE':
            recent = RecentCalls(call.from_phone)
            if call.disposition == 'CALLBACK_REQUESTED':
                recent.disposition = 'Callback Requested'
            elif call.agent_disposition_name:
                recent.disposition = call.agent_disposition_name
            else:
                recent.disposition = call.disposition
            recent.que_time = seconds_to_ms(call.queue_time)
            recent.talk_time = seconds_to_ms(call.talk_time)
            recent.acw = seconds_to_ms(call.acw_time)
            recent.agent = call.callee_login_id
            recent.phone = recent.phone[1:]
            calls_temp.append(recent)
    return calls_temp


# search for calls from a specific phone number
def search_call_list(service, number):
    query = CallDetail.objects.using('bp').filter(service=service, from_phone=number)
    calls_temp = []
    for call in query:
        if call.ivr_time:
            recent = RecentCalls(call.from_phone)
            if call.disposition == 'CALLBACK_REQUESTED':
                recent.disposition = 'Callback Requested'
            elif call.agent_disposition_name:
                recent.disposition = call.agent_disposition_name
            else:
                recent.disposition = call.disposition
            recent.que_time = seconds_to_ms(call.queue_time)
            recent.talk_time = seconds_to_ms(call.talk_time)
            recent.acw = seconds_to_ms(call.acw_time)
            recent.agent = call.callee_login_id
            recent.phone = recent.phone[1:]
            calls_temp.append(recent)
    return calls_temp


# ******************* stats for call info
class CallFeb:
    def __init__(self, dn, an, dat, dur):
        self.dnis = dn
        self.ani = an
        self.date_time = dat
        self.duration = dur


def mask_4(num):
    strip = num[:-4]
    masked = strip + '0000'
    return masked

def calls_feb():
    query = CallDetail.objects.using('bp').filter(start_time__range=('2017-02-01', '2017-02-28 23:59:59'))
    calls = []
    for i in query:
        d2 = i.ivr_time + i.hold_time + i.queue_time + i.talk_time
        calls.append(CallFeb(mask_4(i.original_destination_phone), mask_4(i.from_phone), i.start_time, i.duration))

    with open("feb_masked.csv", "wb") as f:
        writer = csv.writer(f)
        for i in calls:
            writer.writerow([i.dnis, i.ani, i.date_time, i.duration])
    return calls
