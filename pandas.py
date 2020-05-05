import telebot
from telebot import types

TOKEN = '1183668096:AAG7fnt7w2iT_JYENQeQrFklFfwA3SuRBgg'  #токен

PARSE_SUBWAY = {'class_all_teg': 'div',
    'class_all' : "restaurant-card",
    'class_address_teg' : 'a',
    'class_address': 'restaurant-card__name',
    'URL' : 'https://www.subway.ru/stores/?q=Иркутск&fullY=52.287054&fullX=104.281047',
    'HEADERS': {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; '
               'x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                '80.0.3987.163 Safari/537.36 OPR/67.0.3575.137',
                'accept': '*/*'}}

PARSE_KFC_KUPON = {'class_all_teg': 'div',
    'class_all' : "row no-gutters",
    'class_kupon_teg' : 'h3',
    'class_kupon': 'card-title',
    'class_price_teg':'span',
    'class_price': 'font-size: 1.5rem;',
    'class_doprice_teg': 'span',
    'class_doprice': 'text-muted',
    'class_skidka_teg': 'div',
    'class_skidka': 'd-inline-block mb-3',
    'class_info_teg':'div',
    'class_info': 'd-block mb-2',
    'class_img_teg': 'img',
    'img_get':'data-src',
    'URL' : 'https://kfccpn.ru',
    'HEADERS': {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; '
               'x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                '80.0.3987.163 Safari/537.36 OPR/67.0.3575.137',
                'accept': '*/*'}}

PARSE_KING_KUPON={
    'class_all_teg': 'figure',
    'class_all' : "wp-caption aligncenter",
    'class_kupon_teg' : 'strong',
    'class_img_teg':'img',
    'class_img_get': 'src',
    'URL':'https://courier-yandex-eda.ru/akcii-i-kupony-burger-king-na-konec-2019-goda',
    'HEADERS':{'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; '
               'x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                '80.0.3987.163 Safari/537.36 OPR/67.0.3575.137',
                'accept': '*/*'}}

FASTFOOD = ({
            'title': 'KFC ТЦ «Снегирь»',
            'lat': 52.254119,
            'lon': 104.248907,
            'address': 'г.Иркутск, ул. Улан-Баторская, 16'
            },{
            'title': 'ТРЦ «Сильвер Молл» food-cord\n(KFC, BurgerKing, Subway)',
            'lat': 52.265124,
            'lon': 104.226868,
            'address': 'г.Иркутск, ул. Сергеева, 3/5'
            }, {
            'title': 'Subway',
            'lat': 52.248178,
            'lon': 104.269071,
            'address': 'г.Иркутск, ул. Лермонтова, 267/3'
            }, {
            'title': 'Subway',
            'lat': 52.271704,
            'lon': 104.258378,
            'address': 'г.Иркутск, ул. Гоголя, 67'
            }, {
            'title': 'Subway',
            'lat': 52.262779,
            'lon': 104.259408,
            'address': 'г.Иркутск, ул. Лермонтова, 90/1'
            }, {
            'title': 'ТРЦ «Модный квартал» food-cord\n(KFC, BurgerKing, Subway)',
            'lat': 52.273099,
            'lon': 104.290915,
            'address': 'г.Иркутск, ул. 3 Июля, 25'
            }, {
            'title': 'KFC',
            'lat': 52.276122,
            'lon': 104.304933,
            'address': 'г.Иркутск, Советская ул., 58/1'
            }, {
            'title': 'Subway',
            'lat': 52.283048,
            'lon': 104.310861,
            'address': 'г.Иркутск, ул. Декабрьских Событий, 103'
            }, {
            'title': 'Subway',
            'lat': 52.278397,
            'lon': 104.318014,
            'address': 'г.Иркутск, Советская ул., 98А'
            }, {
            'title': 'KFC',
            'lat': 52.284714,
            'lon': 104.290202,
            'address': 'г.Иркутск, ул. Урицкого, 5/7'
            }, {
            'title': 'ТРЦ «Яркомолл» food-cord\n(KFC, BurgerKing, Subway)',
            'lat': 52.267578,
            'lon': 104.289312,
            'address': 'г.Иркутск, ул. Верхняя Набережная, д. 10'
            },{
            'title': 'ТРЦ «Карамель» food-cord\n(KFC, Subway)',
            'lat': 52.279395,
            'lon': 104.302393,
            'address': 'г.Иркутск, Партизанская ул., д.36'
            }, {
            'title': 'KFC',
            'lat': 52.312000,
            'lon': 104.235561,
            'address': 'г.Иркутск, Трактовая ул., 3'
            }, {
            'title': 'Subway',
            'lat': 52.263457,
            'lon': 104.311959,
            'address': 'г.Иркутск, Байкальская ул., 130/1'
            }, {
            'title': 'Subway',
            'lat': 52.249112,
            'lon': 104.356925,
            'address': 'г.Иркутск, пр. Маршала Жукова, 11/2'
            }, {
            'title': 'Subway',
            'lat': 52.272828,
            'lon': 104.353584,
            'address': 'г.Иркутск, ул. Ширямова, 13Б'
            }, {
            'title': 'Subway',
            'lat': 52.276721,
            'lon': 104.286032,
            'address': 'г.Иркутск, ул. Ленина, 25'
            }, {
            'title': 'Subway',
            'lat': 52.281858,
            'lon': 104.258968,
            'address': 'г.Иркутск, ул. Терешковой, 2Б'
            }
            )

info = 'Приветствую тебя на главной странице.\n' \
       'Под сообщением есть кнопки, можете ими пользоваться\n' \
       'Также команда /help покажет список команд бота.\n' \
                                            #Начальная информация
text_inform =   'Немного расскажу про своего создателя. ' \
                'Мой создатель самый лучший человек в мире, ' \
                'он работал надо мной около месяца, ' \
                'и надеюсь его старания не были напрасны.\n' \
                'Если вы хотите внести какой вклад в разработку, то пишите:\n' \
                'Tele: @markgregr\n'\
                'inst:_markgregr_ https://www.instagram.com/_markgregr_/\n'\
                'Вк: Марк Гревцов - https://vk.com/markgregr' \

command = 'Список команд\n' \
          '/help - Список команд\n' \
          '/kfc_kup - Купоны KFC\n' \
          '/king_kup - Купоны Burger King\n' \
          '/location - Ближайший Fastfood\n'
                                                #текст информации
button1 = types.KeyboardButton('Отправь свой контакт', request_contact=True) #кнопки контактов и локации
button2 = types.KeyboardButton('Отправь свою геолокацию', request_location=True)

button_menu = types.InlineKeyboardButton('Главное меню', callback_data='get_menu')
button_info = types.InlineKeyboardButton('Информация', callback_data='get_info')     #кнопки главного меню
button_buy = types.InlineKeyboardButton('Акции', callback_data='get_buy')
button_loc = types.InlineKeyboardButton('Ближайший ресторан-fastfood', callback_data='get_loc')
button_kup_kfc = types.InlineKeyboardButton('Купоны KFC',callback_data='get_kup_kfc')
button_all_kfc = types.InlineKeyboardButton('Все купоны', callback_data='get_all_kfc')
button_kup_king = types.InlineKeyboardButton('Купоны Burger King',callback_data='get_kup_king')
button_all_king = types.InlineKeyboardButton('Все купоны', callback_data='get_all_king')
button_loc_back = types.InlineKeyboardButton('Главное меню', callback_data='get_loc_back')
button_kup_back_kfc = types.InlineKeyboardButton('Вернуться к купонам', callback_data='get_kup_back_kfc')
button_kup_back_king = types.InlineKeyboardButton('Вернуться к купонам', callback_data='get_kup_back_king')
button_kupon = types.InlineKeyboardButton('Fastfood Купоны', callback_data='get_kupon')

markup_menu = types.InlineKeyboardMarkup()
markup_menu.row(button_info, button_kupon)      #маркап меню
markup_menu.row(button_loc)

markup_kupon = types.InlineKeyboardMarkup()
markup_kupon.row(button_kup_kfc, button_kup_king)
markup_kupon.add(button_menu)

markup_info = types.InlineKeyboardMarkup()
markup_info.row(button_menu)

markup_loc = types.ReplyKeyboardMarkup(resize_keyboard=1)
markup_loc.add(button2)

markup_buy = types.InlineKeyboardMarkup()

markup_loc_back= types.InlineKeyboardMarkup()
markup_loc_back.add(button_loc_back)

markup_kup_kfc = types.InlineKeyboardMarkup()

markup_kup_king = types.InlineKeyboardMarkup()

markup_kup_back_kfc = types.InlineKeyboardMarkup()
markup_kup_back_kfc.row(button_loc_back, button_kup_back_kfc)

markup_kup_back_king = types.InlineKeyboardMarkup()
markup_kup_back_king.row(button_loc_back, button_kup_back_king)





'''@bot.callback_query_handler(func=lambda c: c.data == 'get_info')
def procces_callbaack_button_info(callback_query: types.CallbackQuery):
    markup_info = types.InlineKeyboardMarkup()
    markup_info.row(pandas.button_menu)
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, pandas.text_inform,
                     reply_markup=markup_info)'''