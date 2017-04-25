import sys

from twisted.internet import reactor, ssl
from twisted.internet.defer import inlineCallbacks
from twisted.python.modules import getModule
from twisted.web.server import Site
from twisted.python import log
from twisted.web.resource import Resource

from pytgram import polling, TelegramBot, MessageHandler
from pytgram.content import Message, InlineQuery, CallbackQuery, User
from pytgram import InlineQueryResultArticle, InputTextMessageContent, \
    InputLocationMessageContent, InlineQueryResultLocation, \
    InlineQueryResultPhoto, InlineQueryResultGif, InlineQueryResultMpeg4Gif, \
    InlineQueryResultVideo, InlineQueryResultAudio, InlineQueryResultDocument, \
    InlineQueryResultVenue, InlineQueryResultContact, InlineQueryResultGame
from pytgram import ReplyKeyboardMarkup, ReplyKeyboardRemove, \
    KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from pytgram import web_hook, set_webhook, get_webhook_info, \
    delete_webhook
bot = TelegramBot('281132289:AAHMXyQEeNcl-5BWVRzXcg1nNk-zDgjdvM4')


# print(get_webhook_info('281132289:AAHMXyQEeNcl-5BWVRzXcg1nNk-zDgjdvM4'))
# print(delete_webhook('281132289:AAHMXyQEeNcl-5BWVRzXcg1nNk-zDgjdvM4'))
# print(
#     set_webhook(
#         '281132289:AAHMXyQEeNcl-5BWVRzXcg1nNk-zDgjdvM4',
#         'https://telebot.artcom-net.ru/281132289:AAHMXyQEeNcl-5BWVRzXcg1nNk-zDgjdvM4',
#     )
# )


@MessageHandler(content=['text'])
@inlineCallbacks
def handler(message):
    print(message.chat.__dict__)
    d = yield bot.send_message(chat_id=message.chat.id, text='text received')

@MessageHandler(content=['inline_query'])
@inlineCallbacks
def handler_inline(message):
    print(message.__dict__)
    res = InlineQueryResultAudio(
        url='https://dl.last.fm/static/1490498411/131211148/302f3b77ced4e59932'
            '42f1afa97504029781d48f72b32783b08c46600e9c412a/Death+Grips+-+Get+'
            'Got.mp3',
        title='Vasya Title',

    )
    yield bot.answer_inline_query(inline_query_id=message.id, results=[res],
                                  cache_timer=2)


@MessageHandler(content=['photo'])
@inlineCallbacks
def handler_inline(message):
    res = yield bot.send_message(chat_id=message.chat.id, text='photo received')



def main():
    log.startLogging(sys.stdout)
    # site = Site(Resource())
    # polling(bot, interval=3)
    # reactor.listenTCP(80, site)
    reactor.listenTCP(80, web_hook(bot.token))
    # ssl_context = ssl.DefaultOpenSSLContextFactory(
    #     '/root/telebot/ssl/telebot.key',
    #     '/root/telebot/ssl/telebot.crt'
    # )
    # reactor.listenSSL(443, web_hook(bot.token), ssl_context)
    reactor.run()


if __name__ == '__main__':
    main()
