from django.contrib import admin
from microbot.models import TelegramMessage, TelegramChat, TelegramUpdate, TelegramUser, TelegramBot, Handler, EnvironmentVar, Request, Response, Hook, \
    UrlParam, HeaderParam, TelegramRecipient, State, TelegramChatState, Bot, KikMessage, KikUser, KikChat, KikChatState, KikBot, KikRecipient, \
    MessengerBot, MessengerMessage, MessengerRecipient, MessengerChatState

admin.site.register(TelegramMessage)
admin.site.register(TelegramChat)
admin.site.register(TelegramUser)
admin.site.register(TelegramUpdate)
admin.site.register(KikMessage)
admin.site.register(KikChat)
admin.site.register(KikUser)
admin.site.register(MessengerMessage)
admin.site.register(Bot)
admin.site.register(TelegramBot)
admin.site.register(KikBot)
admin.site.register(MessengerBot)
admin.site.register(Handler)
admin.site.register(Request)
admin.site.register(EnvironmentVar)
admin.site.register(Response)
admin.site.register(Hook)
admin.site.register(UrlParam)
admin.site.register(HeaderParam)
admin.site.register(TelegramRecipient)
admin.site.register(KikRecipient)
admin.site.register(MessengerRecipient)
admin.site.register(State)
admin.site.register(TelegramChatState)
admin.site.register(KikChatState)
admin.site.register(MessengerChatState)