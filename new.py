from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import os
#States
FIRST, SECOND = range(2)
#Callback data
ONE, TWO, THREE, FOUR, FIVE = range(5)
def start(update, context):
    fname = update.message.from_user.first_name
    # Build inline keyboard
    keyboard1 = [InlineKeyboardButton("<100K samples",
                                      callback_data=str(ONE))]
    keyboard2 = [InlineKeyboardButton(">100K samples",
                                      callback_data=str(TWO))]
    
    # create reply keyboard markup
    reply_markup = InlineKeyboardMarkup([keyboard1, keyboard2])
    # send message with text and appended inline keyboard
    update.message.reply_text(
        "Welcome {}. Let's figure out the best possible classifier for you data.\n\nHow many samples do you have?".format(fname),
        reply_markup=reply_markup
    )
    # tell ConversationHandler that we are in state 'FIRST' now
    return FIRST

def end(update,context):
    """Returns 'ConversationHandler.END', which tells the CoversationHandler that the conversation is over"""
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        "Goodbye, and all the best\n\nIf you need my help again click on /start"
    )
    return ConversationHandler.END

def main():
    #setting to appropriate values
    TOKEN = "1099106816:AAEEfUuB0WKPZ7vieQKk7gbiqGymoGPuFO0"
    # set up updater
    updater = Updater(token=TOKEN, use_context=True)
    # set up dispatcher
    dispatcher = updater.dispatcher
    #print a message to terminal to log successful start
    print("Bot started")
    # Set up ConversationHandler with states FIRST and SECOND
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler(command='start',
                                     callback=start)],
        states={
            FIRST: [CallbackQueryHandler(linear_svc, pattern='^' + str(ONE) + '$'),
                   ],
            SECOND: [CallbackQueryHandler(end, pattern='^' + str(ONE) + '$'),]
                },
            fallbacks=[CommandHandler(command='start',
                                      callback=start)]
        )
    # add ConversationHandler to dispatcher
    dispatcher.add_handler(conv_handler)
    
    # start the bot
    updater.start_polling()
    # run the bot until Ctrl+C is pressed
    updater.idle()