import urllib
import urllib2
import json
import datetime as dt
from datetime import datetime
from models import CrmInfo

#date conversions for limelight query, start variable defines how far back to search for an account
end = dt.date.today()
end_search = end.strftime('%m/%d/%Y')
start = end - dt.timedelta(days=120)
start_search = start.strftime('%m/%d/%Y')


class CrmData:
    def __int__(self, **kwargs):
        pass


# Query the crm for data about a customer using the phone number
def crm_query(account, phone):
    url = account.url
    values = {"username": account.user_name,
              "password": account.pswd,
              "method": "order_find",
              "campaign_id": "all",
              "start_date": start_search,
              "end_date": end_search,
              "search_type": "any",
              "return_type": "order_view",
              #"criteria": "phone=2036486406"}
              "criteria": 'phone=' + phone}
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    # check for valid response code
    errorcheck = the_page.split('&')
    if errorcheck[0] == 'response_code=100':
        print 'response ok!'
    elif errorcheck[0] == 'response_code=333':
        print 'no orders found'
    else:
        print 'responser error - ' + errorcheck[0]
    return the_page


# format json notes strings to print nicely
def format_json_notes(note):
    parse = note.split('+')
    s = str()
    for i in parse:
        s += i + ' '
    return s


# process order data json response
def order_data_json(data):
    parse_response = data.split('data=')
    json_data = json.loads(parse_response[1])
    # get order numbers
    parse_orders = data.split('order_ids=')
    orders = str(parse_orders[1]).split('&')
    # temp fix order numbers into list, was showing each char as order not seperating by comma
    split_orders = orders[0].split(",")
    order_list = []
    order_info = []
    for i in split_orders:
        order_list.append(i)

    for order in order_list:
        # parse and structure the json data
        try:
            display_ob = CrmData()
            display_ob.s_notes = []
            display_ob.e_notes = []
            display_ob.first_name = json_data[order]['first_name']
            display_ob.last_name = json_data[order]['last_name']
            display_ob.customer_id = json_data[order]['customer_id']
            display_ob.email = json_data[order]['email_address']
            display_ob.order_id = order
            display_ob.recurring = json_data[order]['is_recurring']
            display_ob.recurring_date = json_data[order]['recurring_date']
            display_ob.street = format_json_notes(json_data[order]['shipping_street_address'])
            display_ob.city = json_data[order]['shipping_city']
            display_ob.state = json_data[order]['shipping_state_id']
            display_ob.zip = json_data[order]['shipping_postcode']
            display_ob.phone = json_data[order]['customers_telephone']
            display_ob.main_prod_id = json_data[order]['main_product_id']
            display_ob.main_prod_qty = json_data[order]['main_product_quantity']
            display_ob.upsell_prod_id = json_data[order]['upsell_product_id']
            display_ob.upsell_prod_qty = json_data[order]['upsell_product_quantity']
            display_ob.order_total = json_data[order]['order_total']
            display_ob.tracking_number = json_data[order]['tracking_number']
            display_ob.camp_id = json_data[order]['campaign_id']  # need to double check
            display_ob.chargeback = json_data[order]['is_chargeback']
            display_ob.rma = json_data[order]['is_rma']
            # todo need better formatting of system notes - unicode?
            c = 0
            for x in range(0, 20):
                try:
                    if json_data[order]['systemNotes['+str(c)+']']:
                        display_ob.s_notes.append(format_json_notes(json_data[order]['systemNotes['+str(c)+']']))
                        c += 1
                except (KeyError, ValueError):
                    # todo add better error handling
                    print 'key or value error system notes'
            e = 0
            for x in range(0, 20):
                try:
                    if json_data[order]['employeeNotes['+str(e)+']']:
                        display_ob.e_notes.append(format_json_notes(json_data[order]['employeeNotes['+str(e)+']']))
                        e += 1
                except (KeyError, ValueError):
                    # todo add better error handling
                    print 'key or value error employee notes'
            order_info.append(display_ob)

        except (KeyError, ValueError):
            # todo add error handling
            print 'Key or Value Error json data'
    return order_info


# add crm to the database
def add_crm_info(name, url, user, pwd):
    crm = CrmInfo(name=name, url=url, user_name=user, password=pwd)
    crm.save()


# retrieve crm credentials
def get_crm_info(request):
    camp = request.user.first_name
    creds = CrmInfo.objects.get(name=camp)
    return creds
