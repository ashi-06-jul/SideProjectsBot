import re
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, Voice)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, )

from github import Github, GithubException                    

from teleBotDatabase import TeleDB
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("GITHUB_TOKEN", "")
g = Github(token)
db = TeleDB()
db.setup()



FILL, AUDIO, SUBMIT, NAME, COLLEGE, GITHUB_ID, GITHUB_REPO = range(7)



def start(update, context):
    id = update.message.chat_id
    update.message.reply_text('Listen audio carefully.')
    context.bot.send_voice(chat_id=id, voice=open('audio/Introductory.ogg', 'rb'))
    update.message.reply_text('Press /fillup to Continue')

    return FILL

def fill(update, context):
    text = update.message.text
    if text == '/fillup':
        update.message.reply_text('To Enroll, Verify you are human via audio note.\n\n'
        'Send Reacorded Audio')
    elif text == 'Change':
        update.message.reply_text('Send audio again.')
    else:
        update.message.reply_text('Press /fillup to send us about yourself')
        return FILL

    return AUDIO



def audio(update, context):
    file = context.bot.get_file(update.message.voice.file_id)
    file.download(f'ReceivedAudio/{update.message.from_user["username"]}.ogg')

    reply_keyboard = [['Submit'], ['Change']]
    update.message.reply_text('Want to change the audio or submit it?',
                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    

    return SUBMIT


def submit_audio(update, context):
    update.message.reply_text('What is your name?')

    
    return NAME

        


def name(update, context):
    context.user_data['Name'] = update.message.text
    regex = '[A-Za-z]{2,25}( [A-Za-z]{2,25})?'

    if(re.search(regex, context.user_data['Name'])):
        update.message.reply_text('Which college are you from?',
                reply_markup=ReplyKeyboardRemove())


    else:
        update.message.reply_text('Please enter a valid Name.',
                reply_markup=ReplyKeyboardRemove())
        return NAME
    
    return COLLEGE



def college(update, context):
    context.user_data['College'] = update.message.text
    update.message.reply_text('Please share your github User Name for us to keep a track of your work.')

    return GITHUB_ID



def github_id(update, context):
    update.message.text
    try:
        g.get_user(update.message.text)
        context.user_data['Github'] = update.message.text
        update.message.reply_text("You've passed level 0.\n"
                        "let's move towards Level 1.")
        update.message.reply_text('Write 100 lines of code in github repo.\n\n'
                    'Once completed, Share that repository name.')


    except GithubException as e:
        update.message.reply_text('Please! Enter a valid GitHub user name...')

        return GITHUB_ID

    return GITHUB_REPO


def github_repository(update, context):
    link = 'https://t.me/joinchat/OI-x6EorSA6kxlF6MQmasw'
    try:
        repo = g.get_repo(f"{context.user_data['Github']}/{update.message.text}")
        repo.get_contents("/")
        update.message.reply_text("Great, You've passed Leve 1.\n\n"
        f"Click to join Telgram group {link}\n\n"
        "Please further communicate with SideProjects admin. Happy Coding!")

    except GithubException as e:
        update.message.reply_text('Please! Enter a valid Repo Name...')
        return GITHUB_REPO





    db.add_item(**context.user_data)

    # Send message to the channel
    context.bot.send_message(chat_id=-1001467021890,text=
        f'''
New Candidate\n\n
Name : {context.user_data['Name']}\n
College : {context.user_data['College']}\n
Github Id : {context.user_data['Github']}\n
'''
    )

#     context.bot.send_voice(chat_id=-1001467021890, voice=open(f'ReceivedAudio/{update.message.from_user["username"]}.ogg', 'rb'))
    

    return ConversationHandler.END



def cancel(update, context):
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def main():

    updater = Updater(
        os.getenv("TELEGRAM_TOKEN",""), use_context=True)

    dp = updater.dispatcher
    

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            FILL: [MessageHandler(Filters.text, fill)],

            AUDIO: [MessageHandler(Filters.voice, audio)],

            SUBMIT: [MessageHandler(Filters.regex('Submit'), submit_audio),
                    MessageHandler(Filters.regex('Change'), fill)
                    ],

            NAME: [MessageHandler(Filters.text, name)],

            COLLEGE: [MessageHandler(Filters.text, college)],

           
    
            GITHUB_ID: [MessageHandler(Filters.text, github_id)],
            GITHUB_REPO: [MessageHandler(Filters.text, github_repository)],

            
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
