import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
import pandas
import telebot
from telebot import types
from geopy.distance import vincenty
def get_html(url, HEADERS, params=None):
    html_text = requests.get(url, headers=HEADERS, params=params)
    return html_text

def get_content_address(html, class_all_teg,
                class_all, class_address_teg,
                class_address):
    soup = BeautifulSoup(html.text, 'html.parser')
    items = soup.find_all(class_all_teg, class_=class_all)
    restoran = []
    for item in items:
        restoran.append({
            'address': item.find(class_address_teg, class_=class_address).get_text()
        })
    return restoran

def parse(URL, HEADERS, class_all_teg,
          class_all, class_address_teg,
          class_address, params=None):
    html = get_html(URL,
                    HEADERS,
                    params=None)
    if html.status_code == 200:
        get_content_address(html,
                    class_all_teg,
                    class_all,
                class_address_teg,
                    class_address)
    else:
       print('Error')

def parse_content_kupon(html, class_all_teg,
class_all, class_kupon_teg, class_kupon, class_price_teg,
class_price, class_doprice_teg,
class_doprice, class_skidka_teg, class_skidka, class_info_teg,
                        class_info, class_img_teg, img_get):
    soup = BeautifulSoup(html.text, 'html.parser')
    items = soup.find_all(class_all_teg, class_=class_all)
    KUPON = []
    for item in items:
        KUPON.append({
            'kupon': item.find(class_kupon_teg, class_=class_kupon).get_text(),
            'price': item.find(class_price_teg, style=class_price).get_text(),
            'doprice': item.find(class_doprice_teg, class_=class_doprice).get_text(),
            'skidka': item.find(class_skidka_teg, class_=class_skidka).get_text().replace('%', ' % '),
            'info': item.find(class_info_teg, class_=class_info).get_text(),
            'img': item.find(class_img_teg).get(img_get)
        })
    return KUPON

def parse_king_content(html, class_all_teg, class_all,
                       class_kupon_teg, class_img_teg, class_img_get):
    soup = BeautifulSoup(html.text, 'html.parser')
    items = soup.find_all(class_all_teg, class_=class_all)
    result = []
    for item in items:
        result.append({
            'title': item.find(class_kupon_teg).get_text().replace('Ð\x9aÐ\x9eÐ\x94', 'КУПОН').replace('/','|'),
            'img': item.find(class_img_teg).get(class_img_get)})
    return result

def parse_kfc_kupon():
    html = get_html(pandas.PARSE_KFC_KUPON['URL'],
                    pandas.PARSE_KFC_KUPON['HEADERS'], params=None)
    CONTENT = parse_content_kupon(html, pandas.PARSE_KFC_KUPON['class_all_teg'],
              pandas.PARSE_KFC_KUPON['class_all'], pandas.PARSE_KFC_KUPON['class_kupon_teg'],
              pandas.PARSE_KFC_KUPON['class_kupon'], pandas.PARSE_KFC_KUPON['class_price_teg'],
              pandas.PARSE_KFC_KUPON['class_price'], pandas.PARSE_KFC_KUPON['class_doprice_teg'],
              pandas.PARSE_KFC_KUPON['class_doprice'], pandas.PARSE_KFC_KUPON['class_skidka_teg'],
              pandas.PARSE_KFC_KUPON['class_skidka'], pandas.PARSE_KFC_KUPON['class_info_teg'],
              pandas.PARSE_KFC_KUPON['class_info'],pandas.PARSE_KFC_KUPON['class_img_teg'], pandas.PARSE_KFC_KUPON['img_get'])
    return CONTENT

def parse_burger_king_kupon():
    html = get_html(pandas.PARSE_KING_KUPON['URL'],
                    pandas.PARSE_KING_KUPON['HEADERS'], params=None)
    CONTENT = parse_king_content(html, pandas.PARSE_KING_KUPON['class_all_teg'],
              pandas.PARSE_KING_KUPON['class_all'], pandas.PARSE_KING_KUPON['class_kupon_teg'],
                                 pandas.PARSE_KING_KUPON['class_img_teg'], pandas.PARSE_KING_KUPON['class_img_get'])
    return CONTENT

def subway_parse():
    SUBWAY = []

    parse(pandas.PARSE_SUBWAY['URL'],
          pandas.PARSE_SUBWAY['HEADERS'],
          pandas.PARSE_SUBWAY['class_all_teg'],
          pandas.PARSE_SUBWAY['class_all'],
          pandas.PARSE_SUBWAY['class_address_teg'],
          pandas.PARSE_SUBWAY['class_address'],
          params=None)

    html = get_html(pandas.PARSE_SUBWAY['URL'], pandas.PARSE_SUBWAY['HEADERS'], params=None)
    CONTENT = get_content_address(html, pandas.PARSE_SUBWAY['class_all_teg'],
                          pandas.PARSE_SUBWAY['class_all'],
                          pandas.PARSE_SUBWAY['class_address_teg'],
                          pandas.PARSE_SUBWAY['class_address'])
    del CONTENT[8]
    del CONTENT[8]
    for i in CONTENT:
        geolocator = Nominatim(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; '
               'x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                '80.0.3987.163 Safari/537.36 OPR/67.0.3575.137', timeout=3)
        repl = i['address']
        repl = repl.replace('дом', 'д').replace('ул', '').replace('строение 1', '').replace('/2', '').replace('пр.', '').replace('/3','')
        adrs = repl + ', Иркутск'
        loc = geolocator.geocode(adrs)
        rus = (loc.latitude, loc.longitude)
        SUBWAY.append({'title': 'Subway',
                       'lat': loc.latitude,
                       'lon': loc.longitude,
                       'address': adrs})
    return SUBWAY


KFC_KUPON = parse_kfc_kupon()
index_kfc = 0
pandas.markup_kup_kfc.add(pandas.button_all_kfc)
for i in range(len(KFC_KUPON)):
    if len(KFC_KUPON)-1>=index_kfc:
        button_kifuch1 = types.InlineKeyboardButton(KFC_KUPON[index_kfc]['kupon']
                            + '' + KFC_KUPON[index_kfc]['price'].replace('Цена -', ''),
                                                    callback_data='get_kfc_' + str(index_kfc))
        button_kifuch2 = types.InlineKeyboardButton(KFC_KUPON[index_kfc+1]['kupon']
                            + ' ' + KFC_KUPON[index_kfc+1]['price'].replace('Цена -', ''),
                                                    callback_data='get_kfc_' + str(index_kfc+1))
        pandas.markup_kup_kfc.row(button_kifuch1, button_kifuch2)
        index_kfc+=2
    else:
        button_kifuch1 = types.InlineKeyboardButton(KFC_KUPON[i]['kupon'] +
                            ' ' + KFC_KUPON[i]['price'].replace('Цена -', ''),
                                            callback_data='get_kfc_' + str(index_kfc))
pandas.markup_kup_kfc.add(pandas.button_menu)

BURGER_KING_KUPON= parse_burger_king_kupon()
index_king = 0
pandas.markup_kup_king.add(pandas.button_all_king)
for i in range(len(BURGER_KING_KUPON)):
    if len(BURGER_KING_KUPON)-1>index_king:
        button_king1 = types.InlineKeyboardButton(BURGER_KING_KUPON[index_king]['title'],
                                                    callback_data='get_king_' + str(index_king))
        button_king2 = types.InlineKeyboardButton(BURGER_KING_KUPON[index_king+1]['title'],
                                                    callback_data='get_king_' + str(index_king+1))
        pandas.markup_kup_king.row(button_king1, button_king2)
        index_king+=2
    else:
        button_king1 = types.InlineKeyboardButton(BURGER_KING_KUPON[i]['title'],
                                            callback_data='get_king_' + str(index_king))
        pandas.markup_kup_king.row(button_king1)
        break;
pandas.markup_kup_king.add(pandas.button_menu)

bot = telebot.TeleBot(pandas.TOKEN)

@bot.message_handler(commands=['start'])
def start_start(message):
    bot.send_message(message.chat.id, pandas.info,
                     reply_markup=pandas.markup_menu)
@bot.message_handler(commands=['kfc_kup'])
def start_start(message):
    bot.send_message(message.chat.id,'Выбирете купон', reply_markup=pandas.markup_kup_kfc)
@bot.message_handler(commands=['king_kup'])
def start_start(message):
    bot.send_message(message.chat.id, 'Выбирете купон', reply_markup=pandas.markup_kup_king)

@bot.message_handler(commands=['location'])
def start_start(message):
    bot.send_message(message.chat.id, 'Отправьте свою геолокацию', reply_markup=pandas.markup_loc)
@bot.message_handler(commands=['help'])
def start_start(message):
    bot.send_message(message.chat.id, pandas.command, reply_markup=pandas.markup_info)

@bot.callback_query_handler(func=lambda call:True)
def procces_callback_button_cont(call):
    if call.data == 'get_info':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, pandas.text_inform, reply_markup=pandas.markup_info)
    if call.data == 'get_kupon':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Выберите ресторан', reply_markup=pandas.markup_kupon)
    if call.data == 'get_loc':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Отправьте свою геолокацию', reply_markup=pandas.markup_loc)
    if call.data == 'get_loc_back':
        bot.send_message(call.message.chat.id, pandas.info, reply_markup=pandas.markup_menu)
    if call.data == 'get_menu':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, pandas.info, reply_markup=pandas.markup_menu)
    if call.data == 'get_kup_back_kfc':
        bot.send_message(call.message.chat.id, 'Выбирете купон', reply_markup=pandas.markup_kup_kfc)
    if call.data == 'get_kup_back_king':
        bot.send_message(call.message.chat.id, 'Выбирете купон', reply_markup=pandas.markup_kup_king)
    if call.data == 'get_buy':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Скоро будут купоны и акции', reply_markup=pandas.markup_buy)
    if call.data == 'get_kup_kfc':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id,'Выбирете купон', reply_markup=pandas.markup_kup_kfc)

    if call.data == 'get_all_kfc':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        for i in KFC_KUPON:
            bot.send_message(call.message.chat.id, i['kupon']+'\n'+i['price']+'\n'+'Цена без скидки - ' + i['doprice']
                             +'\n'+i['skidka']+'\n'+i['info'])
            bot.send_photo(call.message.chat.id, i['img'], reply_markup=pandas.markup_loc_back)
    if call.data == 'get_all_king':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        for i in BURGER_KING_KUPON:
            bot.send_message(call.message.chat.id,
                             i['title'])
            bot.send_photo(call.message.chat.id, i['img'], reply_markup=pandas.markup_loc_back)

    if call.data == 'get_kup_king':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Выбирете купон', reply_markup=pandas.markup_kup_king)

    for i in range(index_kfc):
        if call.data == 'get_kfc_'+str(i):
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id,
                             KFC_KUPON[i]['kupon'] + '\n' + KFC_KUPON[i]['price'] + '\n' +
                             'Цена без скидки - ' + KFC_KUPON[i]['doprice']
                             + '\n' + KFC_KUPON[i]['skidka'] + '\n' + KFC_KUPON[i]['info'])
            bot.send_photo(call.message.chat.id, KFC_KUPON[i]['img'], reply_markup=pandas.markup_kup_back_kfc)

    for i in range(index_king):
        if call.data == 'get_king_'+str(i):
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id,
                             BURGER_KING_KUPON[i]['title'])
            bot.send_photo(call.message.chat.id, BURGER_KING_KUPON[i]['img'], reply_markup=pandas.markup_kup_back_king)



@bot.message_handler(func=lambda message: True, content_types=['location'])
def magazin_location(message):
    bot.send_message(message.chat.id, 'Ищу в своих архивах твое местоположение')
    bot.send_message(message.chat.id, 'Это займет буквально 15 секунд')
    lat = message.location.latitude
    lon = message.location.longitude
    distance = []
    SUBWAY = subway_parse()
    SUBWAY = SUBWAY + list(pandas.FASTFOOD)
    for m in SUBWAY:
        result = vincenty((m['lat'], m['lon']), (lat, lon)).kilometers
        distance.append(result)
    index = distance.index(min(distance))
    bot.send_message(message.chat.id, 'Ближайший к вам \n ресторан быстрого питания')
    bot.send_venue(message.chat.id,
                     SUBWAY[index]['lat'],
                     SUBWAY[index]['lon'],
                     SUBWAY[index]['title'],
                     SUBWAY[index]['address'], reply_markup=pandas.markup_loc_back)

bot.polling()




