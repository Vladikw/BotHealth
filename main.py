import time
import webbrowser
import random
import telebot
from telebot import types, callback_data
from telebot.types import InlineKeyboardButton

load_dotenv()  # загружаем переменные из .env
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Изучать теорию 🧠', callback_data='2'))
    markup.add(types.InlineKeyboardButton('Высчитать индекс массы тела ➕➖', callback_data='1'))
    markup.add(types.InlineKeyboardButton('Узнать примерный рацион на день 📄', callback_data='day'))
    bot.send_message(message.chat.id, 'Отлично! С чего начнем?', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_message(call):
    if call.data == '1':
        keyboard_new = types.InlineKeyboardMarkup()
        button_new1 = types.InlineKeyboardButton(text='Здесь', callback_data='3')
        button_new2 = types.InlineKeyboardButton(text='На сайте', url='https://el-klinika.ru/kalkulyator-i'
                                                                      'mt-onlajn-s-uchetom-vozrasta-i-pola/')
        keyboard_new.add(button_new1, button_new2, )

        bot.send_message(call.message.chat.id, 'Вы выбрали опцию "Высчитать ИМТ". Где будем высчитывать?',
                         reply_markup=keyboard_new)
    elif call.data == '3':
        bot.send_message(call.message.chat.id, 'Введите ваш вес в килограммах:')
        bot.register_next_step_handler(call.message, process_weight_step)
    elif call.data == 'day':
        bot.send_message(call.message.chat.id, 'Норма калорий рассчитывается индивидуально и зависит от пола, '
                                               'веса, возраста, образа жизни и от физической активности в течение дня. '
                                               '🏃 \n  Для начала укажите ваш <b>вес</b> в килограммах.',
                         parse_mode='HTML')
        bot.register_next_step_handler(call.message, process_ideal)
    elif call.data == '2':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text='Начнем💡', callback_data='start_study'))
        markup.add(types.InlineKeyboardButton(text='Начать с определенного пункта🔍', callback_data='run'))
        markup.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
        bot.send_message(call.message.chat.id, text='Врууум врум врум 🏎🏎🏎 \nТеоретический материал состоит из 2-х '
                                                    'разделов,'
                                                    ' посвященных физической активности и питанию. \n\n<b>'
                                                    '🌟 Физическая активность:</b>'
                                                    ' \n  1. Польза регулярных упражнений для здоровья и благополучия;'
                                                    '\n  2. Рекомендации по количеству и интенсивности физических '
                                                    'нагрузок;'
                                                    '\n  3. Виды физической активности: аэробные упражнения, силовые '
                                                    'тренировки, растяжка и др. \n\n<b>🌟 Питание:</b>'
                                                    '\n  4. Значение сбалансированного питания для здоровья; '
                                                    '\n  5. Основные группы продуктов и их питательная ценность; \n  '
                                                    '6. '
                                                    'Значение воды для организма; \n  7. Cоставление плана питания.',
                         parse_mode='HTML', reply_markup=markup)
    elif call.data == 'start_study':
        text = ('<b>1. Польза регулярных упражнений для здоровья и благополучия </b> \n\n'
                'Регулярные упражнения имеют множество положительных эффектов на здоровье и благополучие. '
                'Вот некоторые из них:\n\n🍏 <b>Улучшение физического здоровья.</b> Регулярные упражнения помогают '
                'укрепить '
                'сердце, легкие, мышцы и кости. Это снижает риск развития сердечно-сосудистых заболеваний, ожирения, '
                'диабета и других заболеваний.\n\n🍏 <b>Повышение настроения и улучшение эмоционального благополучия.'
                '</b> Физическая активность способствует выделению эндорфинов, которые улучшают настроение и снижают '
                'уровень стресса и тревоги. Это также помогает бороться с депрессией. \n\n🍏 <b>Улучшение сна.</b> '
                'Регулярные упражнения могут помочь улучшить качество сна, что в свою очередь положительно '
                'сказывается на общем самочувствии и работоспособности. \n\n🍏 <b>Повышение энергии и выносливости.</b> '
                'Физическая активность способствует улучшению кровообращения и обмена веществ, что помогает повысить '
                'уровень энергии и выносливости. \n\n🍏 <b>Улучшение самооценки и уверенности.</b> Регулярные '
                'тренировки '
                'помогают улучшить физическую форму, что может повысить самооценку и уверенность в себе. '
                '\n\n🍏 <b>Предотвращение различных заболеваний.</b> Физическая активность снижает риск развития '
                'многих хронических заболеваний, таких как рак, артрит, остеопороз и др.')

        bot.send_message(call.message.chat.id, text=text, parse_mode='HTML')

        photo = open('images/polza.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo)
        photo.close()
        keyboard_new = types.InlineKeyboardMarkup()

        button_new1 = types.InlineKeyboardButton(text='Видео📹', url='https://www.youtube.com/watch?v=SPRj4l0I1oo')
        keyboard_new.add(button_new1)

        bot.send_message(call.message.chat.id, 'Можете взглянуть видеоролик на эту тему! Для этого кликните по '
                                               'кнопке снизу!',
                         reply_markup=keyboard_new)

        bot.register_next_step_handler(call.message, study_2)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn = types.KeyboardButton('Дальше')
        markup.add(btn)
        bot.send_message(call.message.chat.id, 'Нажмите на кнопку "Дальше", чтобы продолжить.',
                         reply_markup=markup)
    elif call.data == 'back':
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    elif call.data == 'strt':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn = types.KeyboardButton('Перейти')
        markup.add(btn)
        bot.send_message(call.message.chat.id, 'Для перехода на главную нажмите на кнопку "Перейти"',
                         reply_markup=markup)
        bot.register_next_step_handler(call.message, start)
    elif call.data == 'run':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn2 = types.KeyboardButton('2')
        btn3 = types.KeyboardButton('3')
        btn4 = types.KeyboardButton('4')
        btn5 = types.KeyboardButton('5')
        btn6 = types.KeyboardButton('6')
        btn7 = types.KeyboardButton('7')
        markup.add(btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(call.message.chat.id, 'С какого пункта вы хотите начать?',
                         reply_markup=markup)
        bot.register_next_step_handler(call.message, run_fun)
    elif call.data == 'test1':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn1 = types.KeyboardButton('а')
        btn2 = types.KeyboardButton('б')
        btn3 = types.KeyboardButton('в')
        markup.add(btn1, btn2, btn3)
        bot.send_message(call.message.chat.id, '<b>Вопрос 1.</b>Какой вид активности не '
                                               'относится к аэробным упражнениям?'
                                               '\n\n а - бег'
                                               '\n\n б - поднятие гантелей'
                                               '\n\n в - плавание  ', parse_mode='HTML', reply_markup=markup)
        bot.register_next_step_handler(call.message, test1_2)
    elif call.data == 'next':
        bot.register_next_step_handler(call.message, study_4)
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn = types.KeyboardButton('Дальше')
        marcup.add(btn)
        bot.send_message(call.message.chat.id, 'Нажмите на кнопку "Дальше", чтобы продолжить.', reply_markup=marcup)
    elif call.data == 'FINAL':
        markup = types.InlineKeyboardMarkup()
        btn3 = types.InlineKeyboardButton('Вернуться на главную', callback_data='strt')
        markup.add(btn3)
        bot.send_message(call.message.chat.id, 'Поздравляю с окончанием обучения!', reply_markup=markup)
    elif call.data == 'test2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn1 = types.KeyboardButton('а')
        btn2 = types.KeyboardButton('б')
        btn3 = types.KeyboardButton('в')
        markup.add(btn1, btn2, btn3)
        bot.send_message(call.message.chat.id, '<b>Вопрос 1.</b> Чем НЕ обеспечивает организм '
                                               'сбалансированное питание?'
                                               '\n\n а - кислородом'
                                               '\n\n б - белками'
                                               '\n\n в - углеводами', parse_mode='HTML', reply_markup=markup)
        bot.register_next_step_handler(call.message, test2_2)


def test1_2(message):
    try:
        otvet = str(message.text)
        if otvet == 'б':
            bot.send_message(message.chat.id, 'Правильно!')

        else:
            bot.send_message(message.chat.id, 'Неправильно. Поднятие гантелей - лишнее в списке')
    except ValueError:
        bot.send_message(message.chat.id, 'что то не то')
        bot.register_next_step_handler(message, test1_2)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('а')
    btn2 = types.KeyboardButton('б')
    btn3 = types.KeyboardButton('в')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, '<b>Вопрос </b>2. Сколько минут в неделю нужно '
                                      'уделять на аэробные упражнения средней интенсивности?'
                                      '\n\n а - 75 минут'
                                      '\n\n б - 30 минут'
                                      '\n\n в - 150 минут'
                                      ' ', parse_mode='HTML', reply_markup=markup)
    bot.register_next_step_handler(message, test1_3)


def test1_3(message):
    try:
        otvet = str(message.text)
        if otvet == 'в':
            bot.send_message(message.chat.id, 'Правильно!')
        else:
            bot.send_message(message.chat.id, 'Неправильно! Правильный ответ: 150 минут')
    except ValueError:
        bot.send_message(message.chat.id, 'что то не то')
        bot.register_next_step_handler(message, test1_2)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('а')
    btn2 = types.KeyboardButton('б')
    btn3 = types.KeyboardButton('в')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, '<b>Вопрос 3.</b> Чему равен показатель ЧСС, когда у человека развивается'
                                      ' скорость и сила?'
                                      '\n\n а - 110-130 уд./мин'
                                      '\n\n б - 130-160 уд./мин'
                                      '\n\n в - 160-180 уд./мин', parse_mode='HTML', reply_markup=markup)
    bot.register_next_step_handler(message, test1_4)


def test1_4(message):
    try:
        otvet = str(message.text)
        if otvet == 'в':
            bot.send_message(message.chat.id, 'Правильно!')
        else:
            bot.send_message(message.chat.id, 'Неправильно! 160-180 уд./мин')
    except ValueError:
        bot.send_message(message.chat.id, 'что то не то')
        bot.register_next_step_handler(message, test1_2)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('а')
    btn2 = types.KeyboardButton('б')
    btn3 = types.KeyboardButton('в')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, '<b>Вопрос 4.</b> '
                                      'К какому виду растяжки относятся мягкие "пружинящие" движения, '
                                      'помогающие растянуть мышцы? '
                                      '\n\n а - статическая'
                                      '\n\n б - динамическая'
                                      '\n\n в - равновесная', parse_mode='HTML', reply_markup=markup)
    bot.register_next_step_handler(message, test1_5)


def test1_5(message):
    try:
        otvet = str(message.text)
        if otvet == 'б':
            bot.send_message(message.chat.id, 'Правильно!')
        else:
            bot.send_message(message.chat.id, 'Неправильно! Динамическая растяжка.')
    except ValueError:
        bot.send_message(message.chat.id, 'что то не то')
        bot.register_next_step_handler(message, test1_2)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('а')
    btn2 = types.KeyboardButton('б')
    btn3 = types.KeyboardButton('в')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, '<b>Вопрос 5.</b> Сколько раз в неделю рекомендуется '
                                      'проводить силовые тренировки?'
                                      '\n\n а - 2-3 раза'
                                      '\n\n б - 1 раз'
                                      '\n\n в - 4-5 раз', parse_mode='HTML', reply_markup=markup)
    bot.register_next_step_handler(message, test1_final)


def test1_final(message):
    try:
        otvet = str(message.text)
        if otvet == 'а':
            bot.send_message(message.chat.id, 'Правильно!')
        else:
            bot.send_message(message.chat.id, 'Неправильно! 2-3 раза в неделю.')
    except ValueError:
        bot.send_message(message.chat.id, 'что то не то')
        bot.register_next_step_handler(message, test1_2)
    bot.send_message(message.chat.id, 'Переходим к разделу "Питание"🏃‍♀️')
    bot.register_next_step_handler(message, study_4)
    marcup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn = types.KeyboardButton('Дальше')
    marcup.add(btn)
    bot.send_message(message.chat.id, 'Нажмите на кнопку "Дальше", чтобы продолжить.', reply_markup=marcup)


def test2_2(message):
    try:
        otvet = str(message.text)
        if otvet == 'а':
            bot.send_message(message.chat.id, 'Правильно!')

        else:
            bot.send_message(message.chat.id, 'Неправильно. Правильный ответ: кислородом')
    except ValueError:
        bot.send_message(message.chat.id, 'что то не то')
        bot.register_next_step_handler(message, test1_2)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('а')
    btn2 = types.KeyboardButton('б')
    btn3 = types.KeyboardButton('в')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, '<b>Вопрос 2.</b>Какой витамин важен для свертываемости крови и '
                                      'здоровья костей?'
                                      '\n\n а - К'
                                      '\n\n б - А'
                                      '\n\n в - С', parse_mode='HTML', reply_markup=markup)
    bot.register_next_step_handler(message, test2_3)


def test2_3(message):
    try:
        otvet = str(message.text)
        if otvet == 'а':
            bot.send_message(message.chat.id, 'Правильно!')
        else:
            bot.send_message(message.chat.id, 'Неправильно. Витамин К.')
    except ValueError:
        bot.send_message(message.chat.id, 'что то не то')
        bot.register_next_step_handler(message, test1_2)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('а')
    btn2 = types.KeyboardButton('б')
    btn3 = types.KeyboardButton('в')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, '<b>Вопрос 3.</b> '
                                      'В каком продукте в основном находятся пищевые волокна?'
                                      '\n\n а - мясо'
                                      '\n\n б - рыба'
                                      '\n\n в - фрукты', parse_mode='HTML', reply_markup=markup)
    bot.register_next_step_handler(message, test2_4)


def test2_4(message):
    try:
        otvet = str(message.text)
        if otvet == 'в':
            bot.send_message(message.chat.id, 'Правильно!')
        else:
            bot.send_message(message.chat.id, 'Неправильно. Во фруктах.')
    except ValueError:
        bot.send_message(message.chat.id, 'что то не то')
        bot.register_next_step_handler(message, test1_2)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('а')
    btn2 = types.KeyboardButton('б')
    btn3 = types.KeyboardButton('в')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, '<b>Вопрос 4.</b> Что НЕ относится к '
                                      'ключевым значениям воды для организма?'
                                      '\n\n а - развитие выносливости'
                                      '\n\n б - поддержка здоровья кожи'
                                      '\n\n в - участие в терморегуляции ', parse_mode='HTML', reply_markup=markup)
    bot.register_next_step_handler(message, test2_5)


def test2_5(message):
    try:
        otvet = str(message.text)
        if otvet == 'а':
            bot.send_message(message.chat.id, 'Правильно!')
        else:
            bot.send_message(message.chat.id, 'Неправильно. Развитие выносливости здесь лишнее.')
    except ValueError:
        bot.send_message(message.chat.id, 'что то не то')
        bot.register_next_step_handler(message, test1_2)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('а')
    btn2 = types.KeyboardButton('б')
    btn3 = types.KeyboardButton('в')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, '<b>Вопрос 5.</b> Что такое калорийность?'
                                      ''
                                      '\n\n а - способность организма к продолжительному выполнению какой-либо '
                                      'работы без заметного снижения работоспособности'
                                      '\n\n б - количество тепловой энергии, которая вырабатывается'
                                      ' организмом при усвоении съеденных продуктов '
                                      '\n\n в - группа низкомолекулярных биологически активных веществ органического '
                                      'происхождения, которые принимают участие в ряде биохимических процессов в '
                                      'организме человека. ', parse_mode='HTML', reply_markup=markup)
    bot.register_next_step_handler(message, test2_final)


def test2_final(message):
    try:
        otvet = str(message.text)
        if otvet == 'a':
            bot.send_message(message.chat.id, 'Правильно!')
        else:
            bot.send_message(message.chat.id, 'Неправильно! Количество тепловой энергии, которая вырабатывается'
                                              ' организмом при усвоении съеденных продуктов')
    except ValueError:
        bot.send_message(message.chat.id, 'что то не то')
        bot.register_next_step_handler(message, test1_2)

    markup = types.InlineKeyboardMarkup()

    btn3 = types.InlineKeyboardButton('Вернуться на главную⏮', callback_data='strt')
    markup.add(btn3)
    bot.send_message(message.chat.id, 'Тест по разделу "Питание" окончен! Вы большой молодец, что дошли до конца!'
                                      ' Поздравляшки!🎉🎉🎉', reply_markup=markup)


def study_2(message):
    text = ('<b>2. Рекомендации по количеству и интенсивности физических нагрузок</b>'
            '\n\nРекомендации по количеству и интенсивности физических нагрузок могут зависеть от ваших целей, '
            'текущего уровня физической подготовки и общего состояния здоровья. Вот некоторые общие рекомендации:'
            '\n\n 🏃‍♀️ Аэробные упражнения: \n\n - Для поддержания общего здоровья рекомендуется проводить '
            'аэробные упражнения (бег, ходьба, плавание, велосипед и др.) в течение 150 минут в неделю умеренной '
            'интенсивности или 75 минут высокой интенсивности; \n - Если вашей целью является потеря веса, '
            'можно увеличить количество времени и интенсивность тренировок. \n\n 🏃‍♀️ Силовые тренировки:'
            '\n\n - Рекомендуется проводить силовые тренировки 2-3 раза в неделю. Это поможет укрепить мышцы, '
            'улучшить общую физическую форму и метаболизм. \n - Необходимо подбирать нагрузку так, чтобы выполнение '
            'упражнений было безопасным и эффективным. \n\n 🏃‍♀️ Гибкость и растяжка: \n\n - Важно также уделять '
            'внимание гибкости и растяжке. Регулярные упражнения на растяжку помогут улучшить подвижность суставов '
            'и предотвратить травмы.\n\n 🏃‍♀️ Отдых:\n\n - Не забывайте об отдыхе. Регулярные выходные дни помогут '
            'вашему организму восстановиться после тренировок. \n\nВажно учитывать свои индивидуальные особенности, '
            'цели и ограничения при планировании программы физических нагрузок.')
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')
    photo = open('images/fiz_nagruzzzka.jpg', 'rb')
    bot.send_photo(chat_id=message.chat.id, photo=photo)
    photo.close()

    bot.register_next_step_handler(message, study_3)
    marcup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn = types.KeyboardButton('Дальше')
    marcup.add(btn)
    bot.send_message(message.chat.id, 'Нажмите на кнопку "Дальше", чтобы продолжить.', reply_markup=marcup)


def study_3(message):
    text1 = ('<b>3. Виды физической активности: аэробные упражнения, силовые тренировки, растяжка и др.</b>'
             '\n\n Примеры каждого из видов упражнений: \n\n 🏃 <b>Аэробные упражнения: </b>\n\n - Бег на улице или '
             'беговой дорожке;\n - Быстрая ходьба на открытом воздухе или на тренажёре;\n - Плавание в бассейне или '
             'открытой воде;\n - Езда на велосипеде как на открытом воздухе, так и на тренажёре;\n - '
             'Групповые занятия по аэробике с музыкой и хореографией.\n\n📹Видеоролик с примером аэробных упражнений:\n'
             'https://youtu.be/CKPgb-a9khg?si=2fDx-s47p8kwnQ9E')
    bot.send_message(message.chat.id, text=text1, parse_mode='HTML')
    photo3 = open('images/aerob_upr.jpeg.jpg', 'rb')
    bot.send_photo(chat_id=message.chat.id, photo=photo3, caption='Упражнения аэробного характера')
    photo3.close()
    time.sleep(3)
    text2 = ('\n\n 🏃 <b>Силовые тренировки:</b>'
             '\n\n - Подъёмы тяжестей: подъём гантелей или упражнения на тренажёрах для различных групп мышц;'
             '\n - Отжимания: классические отжимания, отжимания с узким хватом, отжимания на брусьях и другие '
             'варианты; \n - Приседания: классические приседания, приседания с гантелями, приседания на одной ноге '
             'и '
             'другие варианты. \n\n 📹<em>Видеоролики с силовыми тренировками для дома и тренажерного зала:</em>\n'
             '1) https://youtu.be/ZFXsJ5e6Wpc?si=44vR6XLBjwEwZaP1 \n'
             '2) https://youtu.be/pOuhwvXiRlw?si=xwLTJlXOdaeIQazi')
    bot.send_message(message.chat.id, text2, parse_mode='HTML')
    photo1 = open('images/sil_tr.jpg', 'rb')
    bot.send_photo(chat_id=message.chat.id, photo=photo1)
    photo2 = open('images/sil_tr2.jpg', 'rb')
    bot.send_photo(chat_id=message.chat.id, photo=photo2)
    photo1.close()
    photo2.close()

    time.sleep(3)
    text3 = ('🏃 <b>Растяжка и упражнения на гибкость:</b> \n\n - Статическая растяжка: длительное удержание позы '
             'на уровне максимального растяжения мышц на продолжительный период времени \n<em>Видеоролик с примерами'
             ' упражнений на данный вид растяжки:</em>'
             '\n📹https://youtu.be/WqJssgfUuOQ?si=C557agThsQj9gPxk'
             '\n\n - Динамическая растяжка - мягкие "пружинящие" движения, помогающие растянуть мышцы \n'
             '<em>Также видеоролик с примерами'
             ' упражнений на данный вид растяжки:</em>\n📹https://youtu.be/a9nLNNfinac'
             '\n\n - Йога: совокупность различных духовных, психических и физических практик,'
             ' направленные на гибкость и укрепление тела. \n<em>Пример тренировки с йогой:</em> \n'
             '📹https://youtu.be/hj1_a7umGNI?si=HpcPk_n9q8pixkzK'
             '\n\n - Пилатес: комплекс гимнастических упражнений, направленный на подтяжку мышц тела'
             '\n<em>Тренировка-пилатес: </em>\n'
             '📹https://youtu.be/N24r0jLelZ0?si=Cy6zx0M1sS-waXGB')
    bot.send_message(message.chat.id, text3, parse_mode='HTML')
    bot.send_message(message.chat.id, 'Материал, посвященный разделу "Физическая активность" окончен!🎇',
                     parse_mode='HTML')
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Тест по разделу "Физическая активность"🔤', callback_data='test1'))
    btn2 = types.InlineKeyboardButton('К следующему разделу⏭', callback_data='next')
    btn3 = types.InlineKeyboardButton('Вернуться на главную⏮', callback_data='strt')
    markup.add(btn3, btn2)
    bot.send_message(message.chat.id, 'Что дальше?', reply_markup=markup)


def study_4(message):
    text = ('4.<b> Значение сбалансированного питания для здоровья;</b>\n\nСбалансированное питание играет '
            'важную роль в обеспечении здоровья и благополучия. Вот несколько ключевых преимуществ '
            'сбалансированного питания: \n\n🥑 Сбалансированное '
            'питание обеспечивает организм всеми необходимыми витаминами, минералами, белками, углеводами и жирами, '
            'которые необходимы для поддержания здоровья. \n\n🥑 Правильно сбалансированное питание помогает '
            'контролировать вес, предотвращая избыточный набор или потерю веса. \n\n🥑 Правильное питание связано '
            'с снижением риска развития различных заболеваний, таких как сердечно-сосудистые заболевания, диабет, '
            'ожирение и определенные виды рака. \n\n🥑 Сбалансированное питание может оказать положительное влияние '
            'на психическое здоровье, уровень энергии и общее самочувствие.  \n\n Ну и конечно же, видеоролик '
            'на данную тему: \n📹 https://youtu.be/2kT_MoMevBM?si=P6dummvE71vox738')
    bot.send_message(message.chat.id, text, parse_mode='HTML')
    photo = open('images/сбалансированное_питание.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)
    photo.close()

    bot.register_next_step_handler(message, study_5)
    marcup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn = types.KeyboardButton('Дальше')
    marcup.add(btn)
    bot.send_message(message.chat.id, 'Нажмите на кнопку "Дальше", чтобы продолжить.', reply_markup=marcup)


def study_5(message):
    text = ('<b>5. Основные группы продуктов и их питательная ценность </b>\n\nСуществует несколько основных групп '
            'продуктов, каждая из которых вносит свой вклад в общую питательную ценность рациона. Вот некоторые из '
            'них и их ключевые питательные составляющие: \n\n 🍓<b>Белки: </b> \n - Продукты: мясо, птица, рыба, '
            'молочные продукты, яйца, бобы, орехи.  \n - Питательная ценность: строительный материал для клеток, '
            'участвуют в создании тканей и мышц, важны для иммунной системы. \n\n 🍓<b>Углеводы:</b> \n - Продукты: '
            'злаки, '
            'хлеб, картофель, фрукты, овощи.'
            '\n - Питательная ценность: основной источник энергии для организма, особенно важны для мозга и мышц.'
            '\n\n 🍓<b>Жиры:</b> \n - Продукты: рыба, орехи, масло, авокадо. \n - Питательная ценность: источник '
            'энергии, '
            'необходимы для усвоения некоторых витаминов, помогают поддерживать здоровье кожи и волос.'
            '\n\n 🍓<b>Витамины и минералы:</b> \n - Продукты: фрукты, овощи, зелень, ягоды. \n\n'
            '<em>Какие бывают витамины?</em>\n Витамин А (ретинол): важен для зрения, роста клеток, иммунитета и '
            'здоровья кожи.'
            '\n Витамин С (аскорбиновая кислота): помогает укрепить иммунную систему, участвует в синтезе коллагена, '
            'антиоксидант. \n Витамин K: важен для свертываемости крови и здоровья костей и др. \n\n<em>Какие бывают '
            'минералы?</em> \n Железо: необходимо для транспортировки кислорода в организме. \n Кальций: важен для '
            'здоровья костей и зубов. \n Калий: важен для нормального функционирования сердца, мышц и нервов'
            ' и др.'
            '\n\n - Питательная ценность: '
            'необходимы для правильного функционирования организма, участвуют в метаболических процессах, укрепляют '
            'иммунитет. \n\n 🍓<b>Пищевые волокна:</b> \n - Продукты: овощи, фрукты, злаки. \n - Питательная ценность: '
            'помогают улучшить пищеварение, контролировать уровень сахара в крови, насыщают и помогают в контроле '
            'аппетита. \n\n 📹Видеоролик: '
            'https://youtu.be/u0CdAEdmhhM?si=64tkKJMDhJUTEW4T')
    bot.send_message(message.chat.id, text, parse_mode='HTML')

    photo = open('images/пищевая_ценность.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)
    photo.close()
    bot.register_next_step_handler(message, study_6)
    marcup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn = types.KeyboardButton('Дальше')
    marcup.add(btn)
    bot.send_message(message.chat.id, 'Нажмите на кнопку "Дальше", чтобы продолжить.', reply_markup=marcup)


def study_6(message):
    text = ('<b>6. Значение воды для организма </b> \n\n Вода играет ключевую роль в функционировании организма. '
            'Вот несколько ключевых значений воды для организма: \n\n 🧊 <b>Гидратация</b> \n Вода служит основным '
            'компонентом клеток, тканей и органов. Она помогает поддерживать оптимальную температуру тела, участвует '
            'в транспорте питательных веществ и кислорода к клеткам, а также удаляет отходы через мочу, пот и другие '
            'процессы.'
            '\n\n 🧊 <b>Участие в химических реакциях</b> \n Многие биохимические реакции в организме происходят в '
            'водной среде. Вода служит растворителем для многих важных веществ, таких как минералы, витамины и '
            'микроэлементы.'
            '\n\n 🧊 <b>Поддержание здоровья пищеварительной системы</b> \n Вода необходима для разбавления желудочного '
            'сока и улучшения пищеварения. Также она помогает предотвратить запоры.'
            '\n\n 🧊 <b>Участие в терморегуляции</b> \n Путем потоотделения вода помогает охлаждать тело при повышенных '
            'температурах окружающей среды или физической активности.'
            '\n\n 🧊 <b>Поддержание здоровья кожи</b> \n Употребление достаточного количества воды помогает '
            'поддерживать увлажненность кожи, что способствует ее здоровью и эластичности.'
            '\n\n Почему пить воду важно каждый день? Ответ на этот вопрос находится в видео.\n'
            '📹 https://youtu.be/ymdrYISHFAs?si=6p1UmK3_NHFPcLCB')

    bot.send_message(message.chat.id, text, parse_mode='HTML')
    photo = open('images/вода.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)
    photo.close()
    photo = open('images/вода_2.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)
    photo.close()
    bot.register_next_step_handler(message, study_7)
    marcup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn = types.KeyboardButton('Дальше')
    marcup.add(btn)
    bot.send_message(message.chat.id, 'Нажмите на кнопку "Дальше", чтобы продолжить.', reply_markup=marcup)


def study_7(message):
    text = ('<b>7. Cоставление плана питания.</b>'

            '\n\n<b>Калорийность</b> – это количество тепловой энергии, которая вырабатывается организмом при усвоении '
            'съеденных продуктов. Иначе её так и называют – энергетическая ценность продуктов питания. Она зависит '
            'от химического состава, то есть количества основных компонентов — белков, жиров, углеводов и других '
            'веществ. Информацию об энергетической ценности указывают на этикетках продуктов питания.'
            '\n\nСуточная потребность человека в калориях состоит из двух переменных – индивидуальные энергозатраты и '
            'величина основного обмена веществ. '
            '\n<b>Величина основного обмена веществ (ВООВ) </b>— это минимальное количество энергии, необходимое для '
            'осуществления жизненно важных процессов организма (физиологических, биохимических, функционирование '
            'органов и систем). Норма калорий рассчитывается индивидуально и зависит от пола, веса, возраста, '
            'образа жизни и от физической активности в течение дня. '
            '\n\nДля более точного определения суточной потребности в калориях (СПК), произведем расчет по '
            'следующей формуле:\n\n<b>Формула Маффина — Джеора:</b>\n\nФормула для мужчин:\nВООВ = 10 х вес [кг] + '
            '6,25 х '
            'рост [см] - 5 х возраст [лет] + 5.\n\nФормула для женщин:\nВООВ = 10 х вес [кг] + 6,25 х рост [см] - '
            '5 х возраст [лет] - 161.'
            '\n\n<b>Суточная потребность в калориях (СПК).</b>'
            '\nСПК = ВООВ * КФА (баланс питания)'
            '\n\n1) Сидячий образ жизни без нагрузок – ВООВ умножить на 1,2 (Низкая физическая активность, работа за '
            'письменным столом).\n2) Занятия 1-3 раза в неделю – ВООВ умножить на 1,375. \n3) Занятия 3-5 дней в неделю '
            '– ВООВ умножить на 1,55.\n4) Интенсивные тренировки 6-7 раз в неделю – ВООВ умножить на 1,725.'
            '\n5) Спортсмены высокого уровня в период соревнований, тяжёлые ежедневные упражнения, спорт и '
            'физическая работа / двухразовые тренировки, участие в марафонах и соревнованиях – ВООВ умножить на 1,9.'
            '\n\n И снова видеоролик: 📹 https://youtu.be/-GzTWkiox-U')

    photo = open('images/составление_рациона.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)
    photo.close()
    bot.send_message(message.chat.id, text, parse_mode='HTML')
    bot.send_message(message.chat.id, 'Материал, посвященный разделу "Питание" окончен!🎇',
                     parse_mode='HTML')
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Тест по разделу "Питание"🔤', callback_data='test2'))
    btn2 = types.InlineKeyboardButton('Закончить обучение', callback_data='FINAL')
    markup.add(btn2)
    bot.send_message(message.chat.id, 'Что дальше?', reply_markup=markup)


def run_fun(message):
    choise = int(message.text)
    if choise == 2:
        bot.register_next_step_handler(message, study_2)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn = types.KeyboardButton('Перейти')
        markup.add(btn)
        bot.send_message(message.chat.id, 'Хорошо! Для этого нажмите "Перейти"',
                         reply_markup=markup)
    elif choise == 3:
        bot.register_next_step_handler(message, study_3)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn = types.KeyboardButton('Перейти')
        markup.add(btn)
        bot.send_message(message.chat.id, 'Хорошо! Для этого нажмите "Перейти"',
                         reply_markup=markup)
    elif choise == 4:
        bot.register_next_step_handler(message, study_4)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn = types.KeyboardButton('Перейти')
        markup.add(btn)
        bot.send_message(message.chat.id, 'Хорошо! Для этого нажмите "Перейти"',
                         reply_markup=markup)
    elif choise == 5:
        bot.register_next_step_handler(message, study_5)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn = types.KeyboardButton('Перейти')
        markup.add(btn)
        bot.send_message(message.chat.id, 'Хорошо! Для этого нажмите "Перейти"',
                         reply_markup=markup)
    elif choise == 6:
        bot.register_next_step_handler(message, study_6)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn = types.KeyboardButton('Перейти')
        markup.add(btn)
        bot.send_message(message.chat.id, 'Хорошо! Для этого нажмите "Перейти"',
                         reply_markup=markup)
    elif choise == 7:
        bot.register_next_step_handler(message, study_7)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn = types.KeyboardButton('Перейти')
        markup.add(btn)
        bot.send_message(message.chat.id, 'Хорошо! Для этого нажмите "Перейти"',
                         reply_markup=markup)


def process_weight_step(message):
    global weight
    try:
        weight = float(message.text)
        if weight > 0:
            bot.send_message(message.chat.id, 'Теперь введите ваш рост в сантиметрах.')
            bot.register_next_step_handler(message, process_height_step)
        else:
            bot.send_message(message.chat.id, 'Пожалуйста, введите положительное число для веса. 😫')
            bot.register_next_step_handler(message, process_weight_step)  # Повторный запрос веса
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите корректное число для веса. 😫')
        bot.register_next_step_handler(message, process_weight_step)  # Повторный запрос веса


def process_height_step(message):
    try:
        global height
        height = float(message.text)
        # Вычисление ИМТ
        if height > 0:
            height_in_meters = height / 100
            bmi = weight / (height_in_meters ** 2)
            # bot.send_message(message.chat.id, f'Ваш ИМТ: {bmi:.2f}')
            if 20 <= bmi <= 25:
                bot.send_message(message.chat.id, f'Ваш ИМТ: {bmi:.2f}. Идеальный вес, риски для здоровья минимальны.')
            elif 25 < bmi <= 30:
                bot.send_message(message.chat.id, f'Ваш ИМТ: {bmi:.2f}. Наличие лишнего веса; для активных мужчин до '
                                                  f'27 – это может быть нормой, но для большинства людей рекомендуется '
                                                  f'стремление к норме.')
            elif 30 < bmi <= 35:
                bot.send_message(message.chat.id, f'Ваш ИМТ: {bmi:.2f}. Первая стадия ожирения, значительное увеличение'
                                                  f' рисков для здоровья.')
            elif bmi > 35:
                bot.send_message(message.chat.id, f'Ваш ИМТ: {bmi:.2f}. Продвинутое ожирение, крайне важно обратиться '
                                                  f'к врачу и начать программу коррекции веса.')
            bot.send_message(message.chat.id, 'Давайте высчитаем идеальный вес для вашего роста. Пожалуйста, '
                                              'укажите ваш пол ("мужчина" или "женщина"):')
            bot.register_next_step_handler(message, process_gender_step)
        else:
            bot.send_message(message.chat.id, 'Пожалуйста, введите корректное число для роста. 😫')
            bot.register_next_step_handler(message, process_height_step)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите корректное число для роста. 😫')
        bot.register_next_step_handler(message, process_height_step)


# Функция для обработки пола пользователя и расчета идеального веса по формуле Купера

def process_gender_step(message):
    if message.text.lower() == 'мужчина':
        cooper_ideal_weight = (height - 100) - ((height - 150) / 4)
        bot.send_message(message.chat.id,
                         f'Идеальный вес по формуле Купера для вашего роста: {cooper_ideal_weight:.2f} кг')
    elif message.text.lower() == 'женщина':
        cooper_ideal_weight = (height - 100) - ((height - 150) / 2.5)
        bot.send_message(message.chat.id,
                         f'Идеальный вес по формуле Купера для вашего роста: {cooper_ideal_weight:.2f} кг')
    else:
        bot.send_message(message.chat.id, 'Пожалуйста, укажите ваш пол как "мужчина" или "женщина".')
        bot.register_next_step_handler(message, process_gender_step)
        return  # Добавляем return, чтобы избежать выполнения кода ниже при неверном вводе пола

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Узнать примерный рацион на день 📄', callback_data='day'))
    markup.add(types.InlineKeyboardButton('Изучать теорию 🧠', callback_data='2'))
    markup.add(types.InlineKeyboardButton('Высчитать индекс массы тела еще разочек ➕➖', callback_data='1'))

    bot.send_message(message.chat.id, 'Что бы вы хотели сделать дальше?', reply_markup=markup)


def process_ideal(message):
    global weightt
    try:
        weightt = float(message.text)
        if weightt > 0:
            bot.send_message(message.chat.id, 'Теперь введите ваш <b>рост</b> в сантиметрах.',
                             parse_mode='HTML')

            bot.register_next_step_handler(message, take_height)
        else:
            bot.send_message(message.chat.id, 'Пожалуйста, введите положительное число для веса. 😫')
            bot.register_next_step_handler(message, process_ideal)
            return
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите корректное число для веса. 😫')
        bot.register_next_step_handler(message, process_ideal)


def take_height(message):
    try:
        global heightt
        heightt = float(message.text)

        if heightt > 0:

            bot.send_message(message.chat.id, f'Супер! Укажите ваш пол - "женщина" 🙍‍♀️  ️или "мужчина" 🙎‍♂️.')
            bot.register_next_step_handler(message, take_gender)
        else:
            bot.send_message(message.chat.id, 'Пожалуйста, введите корректное число для роста. 😫')
            bot.register_next_step_handler(message, take_height)
            return
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите корректное число для роста. 😫')
        bot.register_next_step_handler(message, take_height)


def take_gender(message):
    try:
        global gender
        gender = str(message.text)
        if gender == 'женщина' or gender == 'мужчина' or gender == 'Женщина' or gender == 'Мужчина':
            bot.send_message(message.chat.id, f'Прекрасно! Теперь укажите уровень вашей активности'
                                              f' (укажите цифру от 1 до 5): \n '
                                              f'1 - Сидячий образ жизни без нагрузок; \n 2 - Занятия 1-3 раза в неделю;'
                                              f' \n'
                                              f' 3 - Занятия 3-5 дней в неделю; \n 4 - Интенсивные тренировки 6-7 раз '
                                              f'в неделю; \n 5 - Спортсмены высокого уровня в период соревнований, '
                                              f'тяжёлые '
                                              f'ежедневные упражнения, спорт и физическая работа / двухразовые '
                                              f'тренировки, участие в марафонах и соревнованиях.')
            bot.register_next_step_handler(message, take_level_fis)
        else:
            bot.send_message(message.chat.id, 'Что-то не так! 🤔 Возможно, вы неправильно ввели. '
                                              'Введите "мужчина" или "женщина".')
            bot.register_next_step_handler(message, take_gender)
            return
    except ValueError:
        bot.send_message(message.chat.id, 'Что-то не так! 🤔 Возможно, вы неправильно ввели. '
                                          'Введите "мужчина" или "женщина"')
        bot.register_next_step_handler(message, take_gender)


def take_level_fis(message):
    try:
        global level
        level = int(message.text)
        if 1 <= level <= 5:
            bot.send_message(message.chat.id, 'Красота! Теперь введите возраст.')
            bot.register_next_step_handler(message, take_age)
        else:
            bot.send_message(message.chat.id, 'Нееет. 🫨 Введите цифру от 1 до 5.')
            bot.register_next_step_handler(message, take_level_fis)
            return
    except ValueError:
        bot.send_message(message.chat.id, 'Нееет. 🫨 Введите цифру от 1 до 5.')
        bot.register_next_step_handler(message, take_level_fis)


def take_age(message):
    try:
        age = int(message.text)
        if age > 0:
            bot.send_message(message.chat.id, 'Прелесть. 🤗')
            # Рассчитаем суточную калорийность
            if gender == 'мужчина' or gender == 'Мужчина':
                boob = 10 * weightt + 6.25 * heightt - 5 * age + 5
            else:
                boob = 10 * weightt + 6.25 * heightt - 5 * age - 161

            if level == 1:
                kkal = boob * 1.2
            elif level == 2:
                kkal = boob * 1.375
            elif level == 3:
                kkal = boob * 1.55
            elif level == 4:
                kkal = boob * 1.75
            elif level == 5:
                kkal = boob * 1.9
            bot.send_message(message.chat.id, f'Ваша суточная потребность в калориях: {kkal} ккал')

            if 1500 < kkal < 1599:
                bot.send_message(message.chat.id, f'<b>Завтрак: </b> \n'
                                                  f'- Омлет из двух яиц с овощами (помидоры, шпинат, перцы);'
                                                  f'\n- Кусок хлеба со сливочным маслом; \n'
                                                  f'- Чай или кофе без сахара и молока; \n'
                                                  f'<b>Перекус: </b> \n'
                                                  f'- Греческий йогурт с добавлением орехов или семян;'
                                                  f'\n- Фрукт (яблоко, груша или апельсин); \n<b>Обед: </b> \n- Куриная '
                                                  f'грудка '
                                                  f'(паровая или запеченная) с овощным салатом (листья салата, огурцы, '
                                                  f'морковь) и '
                                                  f'заправкой из оливкового масла и лимонного сока;\n- Макароны '
                                                  f'отварные; \n<b>'
                                                  f'Полдник: </b> \n- Орехи грецкие; \n<b>Ужин</b>:\n- Гриль или '
                                                  f'запеченная рыба '
                                                  f'(лосось, треска, тунец) с овощным гарниром (брокколи, цветная '
                                                  f'капуста, спаржа). \n Учтите, что порции должны быть небольшими! 🍝'
                                                  f'\n \n  Обратите внимание, что конкретные потребности в питательных '
                                                  f'веществах'
                                                  f' могут различаться в зависимости от индивидуальных факторов. '
                                                  f'Пожалуйста, '
                                                  f'проконсультируйтесь с диетологом или врачом, прежде чем изменять '
                                                  f'свой рацион. 😉'
                                 , parse_mode='HTML')
            elif 1600 < kkal < 1699:
                bot.send_message(message.chat.id, f'<b>Завтрак: </b> \n'
                                                  f'- Омлет из двух яиц с овощами (помидоры, шпинат, перцы);'
                                                  f'\n- Кусок хлеба со сливочным маслом; \n'
                                                  f'- Чай или кофе без сахара и молока; \n'
                                                  f'<b>Перекус: </b> \n'
                                                  f'- Греческий йогурт с добавлением орехов или семян;'
                                                  f'\n- Фрукт (яблоко, груша или апельсин); \n<b>Обед: </b> \n- Куриная '
                                                  f'грудка '
                                                  f'(паровая или запеченная) с овощным салатом (листья салата, огурцы, '
                                                  f'морковь) и '
                                                  f'заправкой из оливкового масла и лимонного сока;\n- Макароны '
                                                  f'отварные; \n<b>'
                                                  f'Полдник: </b> \n- Орехи грецкие;\n- Хлебец с творожным сыром; '
                                                  f'\n<b>Ужин</b>:\n- Гриль или '
                                                  f'запеченная рыба '
                                                  f'(лосось, треска, тунец) с овощным гарниром (брокколи, цветная '
                                                  f'капуста, спаржа).\n\n  Учтите, что порции должны быть небольшими! 🍝'
                                                  f'\n \n  Обратите внимание, что конкретные потребности в питательных '
                                                  f'веществах'
                                                  f' могут различаться в зависимости от индивидуальных факторов. '
                                                  f'Пожалуйста, '
                                                  f'проконсультируйтесь с диетологом или врачом, прежде чем изменять '
                                                  f'свой рацион. 😉'
                                 , parse_mode='HTML')
            elif 1700 < kkal < 1799:
                bot.send_message(message.chat.id, f'<b>Завтрак: </b> \n'
                                                  f'- Омлет из двух яиц с овощами (помидоры, шпинат, перцы);'
                                                  f'\n- Кусок хлеба со сливочным маслом; \n'
                                                  f'- Чай или кофе без сахара и молока; \n'
                                                  f'<b>Перекус: </b> \n'
                                                  f'- Греческий йогурт с добавлением орехов или семян;'
                                                  f'\n- Фрукт (яблоко, груша или апельсин); \n<b>Обед: </b> \n- Куриная '
                                                  f'грудка '
                                                  f'(паровая или запеченная) с овощным салатом (листья салата, огурцы, '
                                                  f'морковь) и '
                                                  f'заправкой из оливкового масла и лимонного сока;\n- Макароны '
                                                  f'отварные; \n<b>'
                                                  f'Полдник: </b> \n- Орехи грецкие; '
                                                  f'\n<b>Ужин</b>:\n- Гриль или '
                                                  f'запеченная рыба '
                                                  f'(лосось, треска, тунец) с овощным гарниром (брокколи, цветная '
                                                  f'капуста, спаржа);\n- Рис отварной. '
                                                  f'\n\n  Учтите, что порции должны быть небольшими! 🍝'
                                                  f'\n \n  Обратите внимание, что конкретные потребности в питательных '
                                                  f'веществах'
                                                  f' могут различаться в зависимости от индивидуальных факторов. '
                                                  f'Пожалуйста, '
                                                  f'проконсультируйтесь с диетологом или врачом, прежде чем изменять '
                                                  f'свой рацион. 😉'
                                 , parse_mode='HTML')
            elif 1800 < kkal < 1899:
                bot.send_message(message.chat.id, f'<b>Завтрак: </b> \n'
                                                  f'- Омлет из двух яиц с овощами (помидоры, шпинат, перцы);'
                                                  f'\n- Кусок хлеба со сливочным маслом; \n'
                                                  f'- Чай или кофе без сахара и молока; \n'
                                                  f'<b>Перекус: </b> \n'
                                                  f'- Греческий йогурт с добавлением орехов или семян;'
                                                  f'\n- Фрукт (яблоко, груша или апельсин); \n<b>Обед: </b> \n- Грибной'
                                                  f' крем-суп; \n- Куриная '
                                                  f'грудка '
                                                  f'(паровая или запеченная) с овощным салатом (листья салата, огурцы, '
                                                  f'морковь) и '
                                                  f'заправкой из оливкового масла и лимонного сока;\n- Макароны '
                                                  f'отварные; \n<b>'
                                                  f'Полдник: </b> \n- Орехи грецкие; '
                                                  f'\n<b>Ужин</b>:\n- Гриль или '
                                                  f'запеченная рыба '
                                                  f'(лосось, треска, тунец) с овощным гарниром (брокколи, цветная '
                                                  f'капуста, спаржа).\n\n  Учтите, что порции должны быть небольшими! 🍝'
                                                  f'\n \n  Обратите внимание, что конкретные потребности в питательных '
                                                  f'веществах'
                                                  f' могут различаться в зависимости от индивидуальных факторов. '
                                                  f'Пожалуйста, '
                                                  f'проконсультируйтесь с диетологом или врачом, прежде чем изменять '
                                                  f'свой рацион. 😉', parse_mode='HTML')
            elif 1900 < kkal < 1999:
                bot.send_message(message.chat.id, f'<b>Завтрак: </b> \n'
                                                  f'- Омлет из трех яиц с овощами (помидоры, шпинат, перцы);'
                                                  f'\n- Кусок хлеба со сливочным маслом; \n'
                                                  f'- Чай или кофе без сахара и молока; \n'
                                                  f'<b>Перекус: </b> \n'
                                                  f'- Греческий йогурт с добавлением орехов или семян;'
                                                  f'\n- Фрукт (яблоко, груша или апельсин); \n<b>Обед: </b> \n- Грибной'
                                                  f' крем-суп; \n- Куриная '
                                                  f'грудка '
                                                  f'(паровая или запеченная) с овощным салатом (листья салата, огурцы, '
                                                  f'морковь) и '
                                                  f'заправкой из оливкового масла и лимонного сока;\n- Макароны '
                                                  f'отварные; \n<b>'
                                                  f'Полдник: </b> \n- Орехи грецкие; '
                                                  f'\n<b>Ужин</b>:\n- Гриль или '
                                                  f'запеченная рыба '
                                                  f'(лосось, треска, тунец) с овощным гарниром (брокколи, цветная '
                                                  f'капуста, спаржа).\n\n  Учтите, что порции должны быть небольшими! 🍝'
                                                  f'\n \n  Обратите внимание, что конкретные потребности в питательных '
                                                  f'веществах'
                                                  f' могут различаться в зависимости от индивидуальных факторов. '
                                                  f'Пожалуйста, '
                                                  f'проконсультируйтесь с диетологом или врачом, прежде чем изменять '
                                                  f'свой рацион. 😉', parse_mode='HTML')
            elif 2000 < kkal < 2199:
                bot.send_message(message.chat.id, f'<b>Завтрак: </b> \n'
                                                  f'- Омлет из трех яиц с овощами (помидоры, шпинат, перцы);'
                                                  f'\n- Кусок хлеба со сливочным маслом; \n'
                                                  f'- Чай или кофе с сахаром и молоком; \n'
                                                  f'<b>Перекус: </b> \n'
                                                  f'- Греческий йогурт с добавлением орехов или семян;'
                                                  f'\n- Фрукт (яблоко, груша или апельсин); \n<b>Обед: </b> \n- Грибной'
                                                  f' крем-суп; \n- Куриная '
                                                  f'грудка '
                                                  f'(паровая или запеченная) с овощным салатом (листья салата, огурцы, '
                                                  f'морковь) и '
                                                  f'заправкой из оливкового масла и лимонного сока;\n- Макароны '
                                                  f'отварные; \n<b>'
                                                  f'Полдник: </b> \n- Орехи грецкие; '
                                                  f'\n<b>Ужин</b>:\n- Гриль или '
                                                  f'запеченная рыба '
                                                  f'(лосось, треска, тунец) с овощным гарниром (брокколи, цветная '
                                                  f'капуста, спаржа).\n\n  Учтите, что порции должны быть небольшими! 🍝'
                                                  f'\n \n  Обратите внимание, что конкретные потребности в питательных '
                                                  f'веществах'
                                                  f' могут различаться в зависимости от индивидуальных факторов. '
                                                  f'Пожалуйста, '
                                                  f'проконсультируйтесь с диетологом или врачом, прежде чем изменять '
                                                  f'свой рацион. 😉', parse_mode='HTML')
            elif 2100 < kkal < 2299:
                bot.send_message(message.chat.id, f'<b>Завтрак: </b> \n'
                                                  f'- Омлет из трех яиц с овощами (помидоры, шпинат, перцы);'
                                                  f'\n- Кусок хлеба со сливочным маслом; \n'
                                                  f'- Чай или кофе с сахаром и молоком; \n'
                                                  f'<b>Перекус: </b> \n'
                                                  f'- Жирный йогурт с добавлением орехов или семян;'
                                                  f'\n- Фрукт (яблоко, груша или апельсин); \n<b>Обед: </b> \n- Грибной'
                                                  f' крем-суп; \n- Куриная '
                                                  f'грудка '
                                                  f'(паровая или запеченная) с овощным салатом (листья салата, огурцы, '
                                                  f'морковь) и '
                                                  f'заправкой из оливкового масла и лимонного сока;\n- Макароны '
                                                  f'отварные; \n<b>'
                                                  f'Полдник: </b> \n- Орехи грецкие; '
                                                  f'\n<b>Ужин</b>:\n- Гриль или '
                                                  f'запеченная рыба '
                                                  f'(лосось, треска, тунец) с овощным гарниром (брокколи, цветная '
                                                  f'капуста, спаржа).\n\n  Учтите, что порции должны быть небольшими! 🍝'
                                                  f'\n \n  Обратите внимание, что конкретные потребности в питательных '
                                                  f'веществах'
                                                  f' могут различаться в зависимости от индивидуальных факторов. '
                                                  f'Пожалуйста, '
                                                  f'проконсультируйтесь с диетологом или врачом, прежде чем изменять '
                                                  f'свой рацион. 😉', parse_mode='HTML')
        else:
            bot.send_message(message.chat.id, 'Кажется, вы еще не родились. 😃 Введите корректный возраст!')
            bot.register_next_step_handler(message, take_age)
            return
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Изучать теорию 🧠', callback_data='2'))
        markup.add(types.InlineKeyboardButton('Высчитать ИМТ ➕➖', callback_data='1'))
        markup.add(types.InlineKeyboardButton('Узнать примерный рацион на день 📄', callback_data='day'))
        bot.send_message(message.chat.id, 'Что дальше?', reply_markup=markup)
    except ValueError:
        bot.send_message(message.chat.id, 'Ошибочка! Введите корректный возраст!')
        bot.register_next_step_handler(message, take_age)


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b> Help </b> <em> information! </em> <u> eeee </u>', parse_mode='HTML')


@bot.message_handler(commands=['site'])
def main(message):
    webbrowser.open('https://youtu.be/JVI1FdLcUuk?si=24PZTL43Sd4pcdS1')


@bot.message_handler()
def info(message):
    if message.text.lower() in ['привет', 'здравствуйте', 'hello', 'здарова', 'здорово', 'хелоу', 'хеллоу',
                                'добрый день', 'добрый вечер', 'доброго времени суток',
                                'привет!', 'здравствуйте!', 'добрый день!', 'добрый вечер!',
                                'доброго времени суток!', 'gutan tag', 'приветик']:
        items = [f'Привет, {message.from_user.first_name}!', 'Здравствуйте!', f'Приветствую Вас, '
                                                                              f'{message.from_user.first_name}!',
                 'Приветик :)', 'Bonjour!']
        rand = random.choice(items)
        bot.send_message(message.chat.id, text=rand)
        cat = open('images/cat.jpg', 'rb')
        bot.send_photo(message.chat.id, cat)
        cat.close()
    elif message.text.lower() == 'салам':
        bot.send_message(message.chat.id, f'Ва-алейкум Ас-Салям')
    elif message.text.lower() in ['спс', 'спасибо', 'спасиб', 'спасибки', 'спс!', 'спасибо!', 'спасиб!', 'спасибки!']:
        bot.send_message(message.chat.id, f'Обращайтесь!')
    elif message.text.lower() == "как дела?":
        bot.send_message(message.chat.id, "Все супер :)")
    elif message.text.lower() in ['доброе утро', 'доброе утро!', 'утречко', 'утро', 'доброго утра']:
        bot.send_message(message.chat.id, f'Самого добрейшего утра, {message.from_user.first_name}!')
        video = open('images/good_morning.mp4', 'rb')
        bot.send_video(message.chat.id, video)
        video.close()
    elif message.text.lower() in ['guten morgen']:
        bot.send_message(message.chat.id, f'Guten Morgen, {message.from_user.first_name}!')
        video_morning = open('images/good_morning.mp4', 'rb')
        bot.send_video(message.chat.id, video_morning)
        video_morning.close()


@bot.message_handler(
    content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'audio', 'document', 'voice'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://youtu.be/dQw4w9WgXcQ?si=9fJKA3zR11MCYJT5')
    markup.row(btn1)
    bot.reply_to(message, 'Какое красивое фото!', reply_markup=markup)


bot.polling(none_stop=True)
