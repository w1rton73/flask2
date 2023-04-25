from telegram.ext import *

BOT_TOKEN = '6012799864:AAE5j46mJ7zejMDxCJANH4lLvnKJ68p-GRw'
sp = ['35', '37', '39']
sl = {'35': 'phoebe.fairhead@hotmail.com:Penny002!','37': 'noahserickson@gmail.com:Ne212121!','39': 'email@email.ru:12345678'}

async def echo(update, context):
    # У объекта класса Updater есть поле message,
    # являющееся объектом сообщения.
    # У message есть поле text, содержащее текст полученного сообщения,
    # а также метод reply_text(str),
    # отсылающий ответ пользователю, от которого получено сообщение.
    if str(update.message.text) in sp:
        print(update.message.text)
        await update.message.reply_text(sl[str(update.message.text)])


async def start(update, context):
    """Отправляет сообщение когда получена команда /start"""
    user = update.effective_user
    await update.message.reply_html(
        rf"оправтье id аккаунта, после чего оплатите, и вам придут данные",)


def main():
    # Создаём объект Application.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    # Создаём обработчик сообщений типа filters.TEXT
    # из описанной выше асинхронной функции echo()
    # После регистрации обработчика в приложении
    # эта асинхронная функция будет вызываться при получении сообщения
    # с типом "текст", т. е. текстовых сообщений.
    text_handler = MessageHandler(filters.TEXT, echo)

    # Регистрируем обработчик в приложении.
    application.add_handler(text_handler)

    # Запускаем приложение.
    application.run_polling()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()