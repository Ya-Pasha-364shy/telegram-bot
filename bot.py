import config
import telebot
from telebot import types

import random
import demoji
import pyowm

# Если ты хочешь порабоать на полной версии бота - напиши мне на почту
# If you want to work on the full version of the bot - write me an email
# pv-chernov2000@yandex.ru  or  pv.chernov2000@gmal.com

bot = telebot.TeleBot(config.token)

owm = pyowm.OWM('токен с сайта https://openweathermap.org', language="ru")
demoji.download_codes()


path = 'Path_to_your_stickers'


# Обработка команды для старта
@bot.message_handler(commands=['go', 'start'])
def welcome(message):
    sti = open(path+'stiker.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item3 = types.KeyboardButton("Приложения 🌏")
    item2 = types.KeyboardButton("Мероприятия 🍔")
    item1 = types.KeyboardButton('О нас 🎯')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\n\nЯ - <b>{1.first_name}</b>, бот команды Projector в НГТУ, "
                     "создан для того, "
                     "чтобы помочь Вам влиться в нашу команду,"
                     "просто узнать что-то о нас или же просто пообщаться и весело провести время.\n\n"
                     "<i>Have a nice time</i>🌈".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


# Обработка команды для выхода
@bot.message_handler(commands=['stop'])
def bye(message):
    bye_Sti = open(path+'byeMorty.tgs', 'rb')

    hideBoard = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id,
                     "Досвидания, {0.first_name}!\nМы, команда <b>{1.first_name}</b>, надеемся, что ты хорошо провел(а) время 🌈✨\n\n"
                     "Присоединяйся к нашей команде в <a href='https://vk.com/projector_neti'>vk</a>\n"
                     "Наш <a href='https://instagram.com/projector_neti'>inst</a>\n\n"
                     "Напиши Координатору проектов (<a href='https://vk.com/nikyats'>Никите Яцию</a>) и задай интересующие тебя вопросы по <i>проектной деятельности</i>\n\n"
                     "Надеемся, что тебе ответят очень скоро 💫\n\n"
                     "<u>Don't be ill and have a nice day</u> 🦠\n\n\n"
                     "P.S.: Если есть какие-то пожелания или вопросы по боту, то напиши <a href='https://vk.com/setmyaddresspls'>мне</a>".format(
                         message.from_user, bot.get_me()), parse_mode='html', reply_markup=hideBoard)
    exit()


# Обработка стикеров
@bot.message_handler(content_types=["sticker"])
def my_send_sticker(message):
    sti_1 = open(path+'AnimatedSticker.tgs', 'rb')
    sti_2 = open(path+'girlEngine.tgs', 'rb')
    sti_3 = open(path+'thinkingPatric.tgs', 'rb')
    sti_4 = open(path+'thinkingGirl.tgs', 'rb')
    sti_5 = open(path+'wowPatric.tgs', 'rb')
    bot.send_sticker(message.chat.id, random.choice([sti_4, sti_5, sti_3, sti_2, sti_1]))


@bot.callback_query_handler(func=lambda call: call.data in ['good', 'bad'])  # Как дела ?
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':  # Ответ на "хорошо"
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':  # Ответ на "не очень"
                bot.send_message(call.message.chat.id, 'Всё будет хорошо, я уверен ❤️\n'
                                                       'А чтобы никогда не грустить - \n'
                                                       'присоединяйся к нам 📈')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" А твои?",
                                  reply_markup=None)  # Как дела у юзера ?
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="ЭТО ТЕСТОВОЕ "
                                                                                        "УВЕДОМЛЕНИЕ!!11!1!11")

    except Exception as e:
        print(repr(e))


@bot.callback_query_handler(func=lambda call: call.data in ['about1', 'about2', 'about3', 'about4', 'about5', 'about6'])  # О нас
def callback_inline_two(call):
    try:
        if call.message:
            if call.data == "about1":
                bot.send_message(call.message.chat.id,
                                 'В НГТУ, наряду с другими университетами, большое внимание уделяется проектной деятельности обучающихся,\n'
                                 'развивается система мотивации и повышения восприимчивости научно-исследовательской и инновационной деятельностей у обучающихся.\n\n'
                                 'На данный момент наблюдается недостаточная включенность обучающихся в проектную деятельность университета,\n'
                                 'а также несвоевременная и недостаточная информированность о возможностях и актуальных мероприятиях проектной деятельности.\n'
                                 'Поэтому сформирован проект "Лаборатория "Projector" для предприимчивых обучающихся" (далее - Projector),\n'
                                 'который сформирован по методике программы Межвузовского центра Новосибирской области "Университет предпринимателя",\n'
                                 'поддержанного Министерством экономического развития РФ.\n\n'
                                 'Деятельность Projector направлена на активизацию проектной и научно-исследовательской работы обучающихся,\n'
                                 'информирование об актуальных мероприятиях, предоставляемых возможностях и повышению степени восприимчивости инновационной деятельности.\n'
                                 'Проект "Projector" – комплекс взаимосвязанных направлений деятельности, объединенных общей целью и координируемых совместно в целях повышения общей результативности и управляемости.\n'
                                 'Цель: мотивация и формирование базовых компетенций проектной, инновационной и предпринимательской деятельности обучающихся; распространение знаний в области технологического предпринимательства.\n')

            elif call.data == 'about2':
                bot.send_message(call.message.chat.id, 'Мы занимаемся автоматизацией разработки проектов,\n'
                                                       'с нами ты сможешь сделать <u>свой собственный проект</u>\n '
                                                       'или вступить в уже существующий и достичь любых целей,\n'
                                                       'было бы желание!', parse_mode='html')
            elif call.data == 'about3':
                bot.send_message(call.message.chat.id, '2 корпус, ауд. None')
            elif call.data == 'about4':

                form_markup = types.InlineKeyboardMarkup(row_width=2)
                im1 = types.InlineKeyboardButton(text="Написать Никите",
                                                 url='https://vk.com/id8970990')

                im2 = types.InlineKeyboardButton(text="Подать заявку на сайте ПД",
                                                 url='https://project-study.nstu.ru/project?id=612')
                form_markup.add(im1, im2)

                bot.send_message(call.message.chat.id,
                                 'Напиши координатору проекта - <a href="https://vk.com/nikyats">Никите</a>\n'
                                 'или перейди на <strong>сайт проектной деятельности</strong>,\n'
                                 'найди проект номер 612 и подай заявку\n'
                                 '(или просто нажми <a href="https://project-study.nstu.ru/project?id=612">сюда</a>)',
                                 parse_mode="html", reply_markup=form_markup)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Удачи !",
                                      reply_markup=None)

                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                          text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ !")
            elif call.data == 'about5':
                bot.send_message(call.message.chat.id,
                                 'Вот наши контакты, надеемся, что тебе ответят в ближайшее время!\n\n'
                                 'Сайт: SOON\n'
                                 'Наша <a href="https://vk.com/projector_neti">группа Вконтакте</a>\n'
                                 'Мы есть <a href="https://instagram.com/projector_neti">в Instagram</a>\n',
                                 parse_mode="html")
            elif call.data == 'about6':
                form_markup = types.InlineKeyboardMarkup(row_width=2)
                im1 = types.InlineKeyboardButton(text="Задать вопрос/Написать руководителю",
                                                 url='https://vk.com/id8970990')
                form_markup.add(im1)

                bot.send_message(call.message.chat.id, 'У тебя есть возможность написать сообщение\n'
                                                       'нашему Руководителю проекта 👇',
                                 parse_mode="html",
                                 reply_markup=form_markup)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Удачи !",
                                      reply_markup=None)

                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                          text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ !")

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Спасибо за обратную связь ☺️",
                                  reply_markup=None)

            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы потрясающий(ая) !")

    except Exception as e:
        print(repr(e))


@bot.callback_query_handler(func=lambda call: call.data in ['good2', 'bad4'])  # Приложения
def callback_inline_three(call):
    try:
        if call.message:
            if call.data == 'good2':  # Рандомное число
                bot.send_message(call.message.chat.id, "Твоё число: " + str(random.randint(0, 100)))

            elif call.data == 'bad4':  # Как дела ?
                an_markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
                item2 = types.InlineKeyboardButton('Не очень', callback_data='bad')
                an_markup.add(item1, item2)

                bot.send_message(call.message.chat.id, 'Отлично, сам(а) как ?', reply_markup=an_markup)

            # Remove buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Хороший выбор 🍀",
                                  reply_markup=None)
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11!1!11")

    except Exception as e:
        print(repr(e))


@bot.callback_query_handler(func=lambda call: call.data in ['one', 'two', 'three', 'fourth', 'five'])  # Мероприятия
def callback_inline_one(call):
    try:
        if call.message:
            if call.data == 'one':  # Ближайшие мероприятия
                bot.send_message(call.message.chat.id,
                                 "Итак,<b>ближайшие мероприятия</b>:\n\n"  # Здесь будут ссылки ещё
                                 "Форум «Байкал»\n"
                                 "Конкурс «Цифровой ветер»\n"
                                 "PRONETI", parse_mode="html")
            elif call.data == 'two':  # Проведённые мероприятия
                bot.send_message(call.message.chat.id, "Вот список <b>проведённых мероприятий</b>:\n\n"
                                                       "МНТК\n"
                                                       "Семинары по проектной деятельности\n"
                                                       "Встреча с представителями предприятий", parse_mode="html")
            elif call.data == 'three':

                form_markup = types.InlineKeyboardMarkup(row_width=3)
                im1 = types.InlineKeyboardButton(text="Заполнить анкету",
                                                 url='https://docs.google.com/forms/d/e/1FAIpQLSewfT5dQ0kF9cKOJqmTTKPEm9dSllFRAfxH3zTK2cnSNPwhGA/viewform')
                form_markup.add(im1)

                bot.send_message(call.message.chat.id, "По поводу этого критерия напиши "
                                                       "<u><a href='https://vk.com/ki1337ki'>Илье</a></u>\n"
                                                       "А также, ты можешь заполнить анкету, благодаря которой,\n"
                                                       "с тобой лично свяжется один из руководителей направления\nили "
                                                       "<u><a href='https://vk.com/nikyats'>координатор проекта</a></u> :",
                                 parse_mode="html",
                                 reply_markup=form_markup)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Удачи с анкетой !",
                                      reply_markup=None)

                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                          text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ !")

            elif call.data == 'fourth':
                bot.send_message(call.message.chat.id,
                                 "Отлично!\nВсю информацию ты можешь"
                                 " <u><a href='https://project-study.nstu.ru'>узнать здесь</a></u> 👇",
                                 parse_mode="html")
            elif call.data == 'five':
                f_markup = types.InlineKeyboardMarkup(row_width=3)
                im1 = types.InlineKeyboardButton(text="Сайт 📶",
                                                 url='http://nauka-nso.ru/news/')
                f_markup.add(im1)

                bot.send_message(call.message.chat.id, "Подробнее можно узнать"
                                                       "<u><a href='http://nauka-nso.ru/news/'> на сайте</a></u> 👇",
                                 parse_mode="html", reply_markup=f_markup)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Надеюсь, ты найдешь полезную информацию для себя !",
                                      reply_markup=None)

                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                          text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ !")

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Спасибо за обратную связь ☺️",
                                  reply_markup=None)

            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы потрясающий(ая) !")

    except Exception as e:
        print(repr(e))


@bot.message_handler(content_types=["text"])
def go_send_messages(message):
    if message.chat.type == 'private':
        if message.text == 'Приложения 🌏':

            keyboard = types.InlineKeyboardMarkup(row_width=1)
            itemboo = types.InlineKeyboardButton(text="Тыщ на кнопку и ты уже в Google ✔️", url="https://www.google.ru")
            itemboo1 = types.InlineKeyboardButton('Рандомное число 🎲', callback_data='good2')
            itemboo4 = types.InlineKeyboardButton("Как твои дела ? 🤔", callback_data='bad4')

            keyboard.add(itemboo, itemboo1, itemboo4)

            bot.send_message(message.chat.id,
                             "{0.first_name}, окей, смотри, что у нас есть тут:\n".format(message.from_user),
                             reply_markup=keyboard)

        elif message.text == "Мероприятия 🍔":
            one_markup = types.InlineKeyboardMarkup(row_width=1)
            ite1 = types.InlineKeyboardButton("Ближайшие мероприятия 🌅", callback_data="one")
            ite2 = types.InlineKeyboardButton("Проведенные мероприятия 🗿", callback_data="two")
            ite3 = types.InlineKeyboardButton("Волонтерство на мероприятие 💸", callback_data="three")
            ite4 = types.InlineKeyboardButton("Действующие проекты в НГТУ 🏛", callback_data="fourth")
            ite5 = types.InlineKeyboardButton("Мероприятия Межвузовского центра 🏛", callback_data="five")
            one_markup.add(ite1, ite2, ite3, ite4, ite5)
            bot.send_message(message.chat.id, "{0.first_name}, у нас <u>ежемесячно</u> проводится множество "
                                              "мероприятий,\nмы постарались разбить их на следующие составляющие:".format(
                message.from_user), parse_mode="html", reply_markup=one_markup)

        elif message.text == 'О нас 🎯':
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            itembtn1 = types.InlineKeyboardButton('Основная информация 🔋', callback_data='about1')
            itembtn2 = types.InlineKeyboardButton('Чем мы занимаемся ❓', callback_data='about2')
            itembtn3 = types.InlineKeyboardButton('Где мы находимся ❓', callback_data='about3')
            itembtn4 = types.InlineKeyboardButton('Как попасть в команду 📈', callback_data='about4')
            itembtn5 = types.InlineKeyboardButton('Контакты 📒', callback_data='about5')
            itembtn6 = types.InlineKeyboardButton('Задать вопрос руководителю проекта 👤', callback_data='about6')
            markup1.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)

            bot.send_message(message.chat.id,
                             "Хочешь узнать немного о проекте  🧩\n"
                             "Выбери нужную категорию: ".format(message.from_user, bot.get_me()),
                             reply_markup=markup1)

        elif message.text.lower() == 'привет':
            bot.send_message(message.chat.id, 'Да-да, я тут ')
        elif message.text.lower() == 'пока':
            bye_Sti = open('C:/Users/user/PycharmProjects/My_Python/venv/Lib/site-packages/telebot/static/byeMorty.tgs',
                           'rb')
            hideBoard = types.ReplyKeyboardRemove()  # if sent as reply_markup, will hide the keyboard
            bot.send_message(message.chat.id, 'Надеюсь, я помог тебе!\nДо встречи 👋🏻', reply_markup=hideBoard)
            bot.send_sticker(message.chat.id, bye_Sti)
            exit()
        else:
            a = demoji.findall(message.text)
            if len(a) != 0:
                sti_1 = open(
                    path+'AnimatedSticker.tgs',
                    'rb')
                sti_2 = open(
                    path+'girlEngine.tgs',
                    'rb')
                sti_3 = open(
                    path+'thinkingPatric.tgs',
                    'rb')
                sti_4 = open(
                    path+'thinkingGirl.tgs',
                    'rb')
                sti_5 = open(
                    path+'wowPatric.tgs', 'rb')
                bot.send_sticker(message.chat.id, random.choice([sti_4, sti_5, sti_3, sti_2, sti_1]))
            else:
                bot.send_message(message.chat.id, 'Не понимаю тебя 🌚')


# RUN
if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except ConnectionError as e:
        print('Ошибка соединения: ', e)
    except Exception as r:
        print("Непридвиденная ошибка: ", r)
    finally:
        print("Здесь всё закончилось")
