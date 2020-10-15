import re
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, Voice)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, )
import sqlite3
from github import Github, GithubException                    

from teleBotDatabase import TeleDB
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("GITHUB_TOKEN", "")
g = Github(token)
db = TeleDB()
db.setup()



STATUS,FILL,SETUP,NAME, COLLEGE,PAID_PROJECTS,OPERATING_SYSTEM,RAM_CONFIG,TYPING,AMAZING_THING_WITH_COMPUTER,CODE,EXPERIENCE_LEVEL,LINUX,MULTIPLE_SELECT,PROGRAMMING_LANGUAGE,PROGRAMMING_EXPERIENCE,MULTI_SELECT_FRAMEWORK,FRAMEWORK,STORAGE,INTERESTS,CMD,PLATEFORM_CODING,PROGRAMMING_SHOWCASE, LEADERSHIP, GITHUB_ID, GITHUB_REPO,POINTS = range(27)

PAID_PROJECTS_JOBS=[['yes - money situation is bad'], ['yes - want to earn but can not right away'],['no - open to interesting unpaid opportunities also']]
OS=[['windows'], ['linux'], ['mac']]
RAM=[['1GB or less'],['2GB - 4GB'],['more than 4GB'],['don’t know']]
TYPING_SPEED=[['typing takes 50% of my mind'],['know basic typing'],['can type well'],['god speed']]
LINES_OF_CODE=[['have never written code'],['can read and understand code'],['can write code but only small programs'],['have written 100+ lines of code till now'],['have written 500+ lines of code'],['have written 1000+ lines of code'], ['worked on many projects'],['earned money writing code']]
PROGRAMMING_LANGUAGE_OPTIONS = [['Done'],['Java'],['JavaScript'],['Python'],['CSS'],['C/C++'],['HTML/CSS'],['C#'],['PHP'],['Ruby'],['Golang'],['SQL'],['R'],['Ruby']]
HOW_MUCH_CODE_DONE=[['don’t know much but here to learn from zero'],['tried learning before but don’t know much'],['know at least 1 language but very basic'], ['confident with 1 language but not projects'], ['have made a project'], ['made project can share link/code if asked'],['worked on multiple projects']]
#SOURCE_OPTIONS = [['Friends'],['Whatsapp Group'],['LinkedIn'],['Facebook']]
STORIND_INFO=[['Can read from files'],['Can write to files'],['Have written database query'], ['Have connected with database'], ['Have created tables in database'],['Have setup database on system'],['Have experience of more than 1 database'],['Advanced database user']]
CMD_EXP=[['don’t know command line'],['know few commands on windows'],['learnt commands but not practised'], ['know few commands on mac/linux'],['know 10+ commands on any platform'],['advanced command line user']]
LINUX_EXP=[['Don’t know linux'],
['Heard of it - know a friend who uses'],
['Have used earlier but not now'],
['Have logged in to a server via putty/ssh'],
['Have dual boot system'],['linux is primary operating system'],
['Can install windows/linux'],
['Advanced linux user']]
WORK=[
['Can send details on voice note but no code'],
['Can send code files by mail'],
['Can send college project by mail'],
['Have github profile with code'],
['Link of upwork/freelancer like platforms'],
['Have project(s) hosted on internet'],
['Have give details of client facing experience']]
SETUP_ = [['Laptop'], ['Computer'], ['Smartphone'], ['Borrowed device'], ['Need help with Internet recharges']]
PLATEFORM=[['Github'],['Stackoverflow'],['freelancer'],['Upwork'],['Hackerrank'],['Topcoder']]
TECHNOLOGIES=[['Frontend'], ['Backend'], ['Android'], ['Ios'], ['Scripting languages'], ['data science'], ['Networking'],['System administration'],['ai/ml (since it is a trend)']]
FRAMEWORK_OPTIONS = [['Done'],['Ruby on Rails'],['Flask'],['React'],['Django'],['Angular'],['ASP.NET'],['METEOR'],['Laravel'],['Express'],['Spring'],['PLAY'],['CodeIgniter']]
PROGRAMMING_BEGINNER = [['Have written a simple hello world in a programming language'], ['Have written only 100 lines of code in any language'], ['Comfortable with loops and functions']]
PROGRAMMING_INTERMEDIATE = [['Have written more than 500 lines of code'], ['Comfortable with file handling and libraries'], ['Have collaborated with a team of programmers']]
PROGRAMMING_ADVANCE = [['Have written more than 1000 lines of code'], ['Have made a project']]


EXPERIENCE_OPTIONS = [['Beginner'],['Intermediate'],['Advance']]
LINUX_BEGINNER = [['Have used linux once but never again'],['Had tried to install linux once but faced issues']]
LINUX_INTERMEDIATE = [['Using Linux as the primary operating system'], ['Have used command line tools but not very comfortable']]
LINUX_ADVANCE = [['Have logged into a remote server'], ['Comfortable with few command line tools']]
PROGRAMMING_BEGINNER = [['Have written a simple hello world in a programming language'], ['Have written only 100 lines of code in any language'], ['Comfortable with loops and functions']]
PROGRAMMING_INTERMEDIATE = [['Have written more than 500 lines of code'], ['Comfortable with file handling and libraries'], ['Have collaborated with a team of programmers']]
PROGRAMMING_ADVANCE = [['Have written more than 1000 lines of code'], ['Have made a project']]
DATABASE_USED=[['Sqlite'],['Mysql'],['Mongodb'],['Oracle'],['Postgresql'],['Elasticsearch']]
TEAM_WORK=[['dependable - if i say i will do something to a team, i get around to doing it but maybe not on time'],
['disciplined - i follow a routine and don’t miss meetings'],
['leadership - i keep people connected while keeping group’s goals in mind'],
['thinking - i like to think about best next steps to a problem'],
['doing - i find available solutions and try to solve the problem'],
['people - i am good at being friends with various groups of people'],
['communication - i can understand the group’s current state and clearly communicate with both group and clients'],
['documentation - i am good at taking notes at meetings, maintaining status of projects']]
STORAGE_BEGINNER = [["Can read from a file using code"], ['Can write to a file using code']]
STORAGE_INTERMEDIATE = [['Used arrays, json or xml like nested data structures'], ['Used a database but only know basics']]
STORAGE_ADVANCE = [['Installed and comfortable with databases'], ['Used more than one databases - (mysql, sqlite, mongodb, elasticsearch)']]
INTERESTS_OPTONS = [["Backend"], ['Frontend'], ['App Development'], ['Communication'], ['Marketting']]
LEADERSHIP_OPTIONS = [['1'], ['2'], ['3'], ['4'], ['5']]
YES_NO_OPTIONS = [['Yes'], ['No']]

def start(update, context):
    id = update.message.chat_id
    update.message.reply_text('Welcome to the Side Projects, Listen audio carefully.')
    context.bot.send_voice(chat_id=id, voice=open('audio/Introductory.ogg', 'rb'))
    update.message.reply_text('''Press /1 to know workflow of Side Projects\nPress /2 to join Side Projects\nPress /3 to know about Paid Projects/Internships/Jobs\nPress /4 for Side projects evaluation process\n''')

    return STATUS

def status(update, context):
    text = update.message.text
    if text == '/1':
        update.message.reply_text('''We engage students through a 7 Day training program where we provide them assignments, job, and career advice, polish their CV and improve online presence while also giving them tips on client engagement. Press /0 to return to main menu.''')
        return STATUS
    elif text == '/2':
        update.message.reply_text('''In the process of identifying interested and enthusiastic candidates, we want you to take an assessment so press /fillup to take the assessment. This test has total 14 questions, there are no time limits.
If you get stuck up anywhere, you can complete the questions even after taking multiple breaks.''')
        return FILL
    elif text == '/3':
        update.message.reply_text('''We are currently doing projects on:-\n Telegram Bot\n Whatsapp Bot\n Zoho-Setup\n Khaata\n Talk Project\n ERP\n Heidi\n EZ Helper\n E-Commerce Website\nPress /0 to return to main menu.''')
        return STATUS
    elif text=='/4':
        update.message.reply_text('''In the process of identifying Interested and enthusiastic candidates, we want you to take an assessment so Press /fillup to take the assesment, This test has total 14 questions, there are no time limits.\n If you stuck up anywhere, you can complete the questions even after taking multiple breaks.''')
        return FILL
    else:
        update.message.reply_text('''Press /1 to know workflow of Side Projects\nPress /2 to join Side Projects\nPress /3 to know about Paid Projects/Internships/Jobs\nPress /4 for Side projects evaluation process\n''')
        return STATUS


def fill(update, context):
    text = update.message.text
    if text == '/fillup':
        update.message.reply_text('Do you have access to a laptop/computer - do you need help with internet recharges?',reply_markup=ReplyKeyboardMarkup(SETUP_, one_time_keyboard=True))
    elif text=='/0':
        return STATUS
    else:
        update.message.reply_text('Press /fillup to take the assesment')
        return FILL

    return SETUP

def setup(update, context):
    context.user_data['setup'] = update.message.text
    text = update.message.text

    if [text] in SETUP_:
        update.message.reply_text('What is your name?',
                reply_markup=ReplyKeyboardRemove())
    
    else:
        update.message.reply_text('Please enter the details from options available.',
                reply_markup=ReplyKeyboardMarkup(SETUP, one_time_keyboard=True))
        return SETUP
    
    return NAME

def name(update, context):
    context.user_data['name'] = update.message.text
    regex = '[A-Za-z]{2,25}( [A-Za-z]{2,25})?'

    
    if(re.search(regex, context.user_data['name'])):
        update.message.reply_text('Which college are you from?',
                reply_markup=ReplyKeyboardRemove())
    
    else:
        update.message.reply_text('Please enter a valid Name.',
                reply_markup=ReplyKeyboardRemove())
        return NAME
    
    return COLLEGE


def college(update, context):
    context.user_data['college'] = update.message.text
    update.message.reply_text('Do you necessarily want paid projects?',
                    reply_markup=ReplyKeyboardMarkup(PAID_PROJECTS_JOBS, one_time_keyboard=True))

    return PAID_PROJECTS


def paid_projects(update, context):
    context.user_data['paid_projects'] = update.message.text
    text = update.message.text

    if [text] in PAID_PROJECTS_JOBS:
        update.message.reply_text('What operating system do you use?',
                    reply_markup=ReplyKeyboardMarkup(OS, one_time_keyboard=True))

    else:
        update.message.reply_text('Please! select from the given options',
                    reply_markup=ReplyKeyboardMarkup(PAID_PROJECTS_JOBS, one_time_keyboard=True))
        return PAID_PROJECTS

    return OPERATING_SYSTEM

def operating_system(update, context):
    context.user_data['os'] = update.message.text
    text = update.message.text

    if [text] in OS:
        update.message.reply_text('How much RAM does your machine have?',
                    reply_markup=ReplyKeyboardMarkup(RAM, one_time_keyboard=True))

    else:
        update.message.reply_text('Please! select from the given options',
                    reply_markup=ReplyKeyboardMarkup(OS, one_time_keyboard=True))
        return OPERATING_SYSTEM

    return RAM_CONFIG

def ram_config(update, context):
    context.user_data['ram'] = update.message.text
    text = update.message.text

    if [text] in RAM:
        update.message.reply_text('How good are you at typing?',
                    reply_markup=ReplyKeyboardMarkup(TYPING_SPEED, one_time_keyboard=True))

    else:
        update.message.reply_text('Please! select from the given options',
                    reply_markup=ReplyKeyboardMarkup(RAM, one_time_keyboard=True))
        return RAM_CONFIG

    return TYPING

def typing(update, context):
    context.user_data['typing'] = update.message.text
    text = update.message.text

    if [text] in TYPING_SPEED:
        update.message.reply_text('What is the most amazing thing you have done with your computer?')

    else:
        update.message.reply_text('Please! select from the given options',
                    reply_markup=ReplyKeyboardMarkup(TYPING_SPEED, one_time_keyboard=True))
        return TYPING

    return AMAZING_THING_WITH_COMPUTER

def amazing_thing_with_computer(update, context):
    context.user_data['computer_work'] = update.message.text
    user = update.message.from_user
    regex = '[A-Za-z]{2,25}( [A-Za-z]{2,25})?'

    if(re.search(regex, context.user_data['computer_work'])):
        update.message.reply_text('How much programming do you know?',reply_markup=ReplyKeyboardMarkup(LINES_OF_CODE, one_time_keyboard=True))
        return CODE

    else:
        update.message.reply_text(
            'Please enter a valid Data')
    return AMAZING_THING_WITH_COMPUTER

def code(update, context):
    context.user_data['code'] = update.message.text
    text = update.message.text

    if [text] in LINES_OF_CODE:
        update.message.reply_text('Select your proficiency level in your stream?',
                    reply_markup=ReplyKeyboardMarkup(EXPERIENCE_OPTIONS, one_time_keyboard=True))

    else:
        update.message.reply_text('Please! select from the given options',
                    reply_markup=ReplyKeyboardMarkup(LINES_OF_CODE, one_time_keyboard=True))
        return CODE

    return EXPERIENCE_LEVEL

def experience_level(update, context):
    text = update.message.text

    if [text] in EXPERIENCE_OPTIONS:
        context.user_data['Experience_level'] = update.message.text
        
        if context.user_data['Experience_level'] == 'Beginner':
            context.user_data['Points'] = 0
            update.message.reply_text('Ok! Choose one option according to your experience in linux',
                        reply_markup=ReplyKeyboardMarkup(LINUX_BEGINNER, one_time_keyboard=True))

        elif context.user_data['Experience_level'] == 'Intermediate':
            context.user_data['Points'] = 5
            update.message.reply_text('Ok! Choose one option according to your experience in linux',
                        reply_markup=ReplyKeyboardMarkup(LINUX_INTERMEDIATE, one_time_keyboard=True))

        elif context.user_data['Experience_level'] == 'Advance':
            context.user_data['Points'] = 10
            update.message.reply_text('Ok! Choose one option according to your experience in linux',
                        reply_markup=ReplyKeyboardMarkup(LINUX_ADVANCE, one_time_keyboard=True))


    else:
        update.message.reply_text('Please! select from the given options',
                    reply_markup=ReplyKeyboardMarkup(EXPERIENCE_OPTIONS, one_time_keyboard=True))
        return EXPERIENCE_LEVEL
    
    return LINUX


    


# LINUX

def linux(update, context):
    text = update.message.text
    if [text] in LINUX_BEGINNER or [text] in LINUX_INTERMEDIATE or [text] in LINUX_ADVANCE:

        update.message.reply_text('Which programming languages do you know?',
                    reply_markup=ReplyKeyboardMarkup(PROGRAMMING_LANGUAGE_OPTIONS))
        context.user_data['Linux'] = text

    else:
        if context.user_data['Experience_level'] == 'Beginner':
            reply_keyboard = LINUX_BEGINNER
        elif context.user_data['Experience_level'] == 'Intermediate':
            reply_keyboard = LINUX_INTERMEDIATE
        else:
            reply_keyboard = LINUX_ADVANCE
        
        update.message.reply_text('Please! select from the given options',
                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
        return LINUX

    return PROGRAMMING_LANGUAGE



# PROGRAMMNG LANGUAGE                

def multiple_select(update, context):
    if "Programming_language" in context.user_data:
        context.user_data['Programming_language'] += "," + update.message.text
    else:
        context.user_data['Programming_language'] = update.message.text


    return PROGRAMMING_LANGUAGE
    


def programming_language(update, context):
    if context.user_data['Experience_level'] == 'Beginner':
        update.message.reply_text('Choose one option according to your experience in programming language',
                    reply_markup=ReplyKeyboardMarkup(PROGRAMMING_BEGINNER, one_time_keyboard=True))

    elif context.user_data['Experience_level'] == 'Intermediate':
        update.message.reply_text('Tell us your experience in programming language',
                    reply_markup=ReplyKeyboardMarkup(PROGRAMMING_INTERMEDIATE, one_time_keyboard=True))    

    elif context.user_data['Experience_level'] == 'Advance':
        update.message.reply_text('Tell us your experience about programming language',
                    reply_markup=ReplyKeyboardMarkup(PROGRAMMING_ADVANCE, one_time_keyboard=True))

    
    if 'Programming_language' in context.user_data:
        context.user_data["Programming_language"] = list(set(context.user_data["Programming_language"].split(",")))
    else:
        context.user_data['Programming_language'] = ['None']
    
    return PROGRAMMING_EXPERIENCE



def programming_experience(update, context):
    ReplyKeyboardRemove()
    text = update.message.text
    
    if [text] in PROGRAMMING_BEGINNER or [text] in PROGRAMMING_INTERMEDIATE or [text] in PROGRAMMING_ADVANCE:

        context.user_data['Programming_experience'] = update.message.text
        # About Framework
        update.message.reply_text("Select Framework on which you've worked",
                    reply_markup=ReplyKeyboardMarkup(FRAMEWORK_OPTIONS))
        
    
    else:
        if context.user_data['Experience_level'] == 'Beginner':
            reply_keyboard = PROGRAMMING_BEGINNER
        elif context.user_data['Experience_level'] == 'Intermediate':
            reply_keyboard = PROGRAMMING_INTERMEDIATE
        else:
            reply_keyboard = PROGRAMMING_ADVANCE

        update.message.reply_text('Please! select from the given options',
                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
        return PROGRAMMING_EXPERIENCE
    
    context.user_data['Programming_language'] = ', '.join(context.user_data['Programming_language'])

    
    return FRAMEWORK




def multi_select_framework(update, context):
    if "Framework" in context.user_data:
        context.user_data['Framework'] += "," + update.message.text
    else:
        context.user_data['Framework'] = update.message.text
        
    return FRAMEWORK


def framework(update, context):
    if context.user_data['Experience_level'] == 'Beginner':
        update.message.reply_text('Select your proficiency in file handling?',
                    reply_markup=ReplyKeyboardMarkup(STORAGE_BEGINNER, one_time_keyboard=True))

    elif context.user_data['Experience_level'] == 'Intermediate':
        update.message.reply_text('Select your proficiency in Data Structure?',
                    reply_markup=ReplyKeyboardMarkup(STORAGE_INTERMEDIATE, one_time_keyboard=True))

    elif context.user_data['Experience_level'] == 'Advance':
        update.message.reply_text('Select your proficiency in Database?',
                    reply_markup=ReplyKeyboardMarkup(STORAGE_ADVANCE, one_time_keyboard=True))



    if 'Framework' in context.user_data:
        context.user_data['Framework'] = list(set(context.user_data['Framework'].split(",")))
    else:
        context.user_data['Framework'] = ['None']

    return STORAGE


# Storage

def storage(update, context):
    ReplyKeyboardRemove()

    text = update.message.text
    if [text] in STORAGE_BEGINNER or [text] in STORAGE_INTERMEDIATE or [text] in STORAGE_ADVANCE:
        context.user_data['Storage'] = update.message.text
        update.message.reply_text('What is your field of interest in the given?',
                    reply_markup=ReplyKeyboardMarkup(INTERESTS_OPTONS, one_time_keyboard=True))

    else:
        if context.user_data['Experience_level'] == 'Beginner':
            reply_keyboard = STORAGE_BEGINNER
        elif context.user_data['Experience_level'] == 'Intermediate':
            reply_keyboard = STORAGE_INTERMEDIATE
        else:
            reply_keyboard = STORAGE_ADVANCE

        update.message.reply_text('Please! select from the given options',
                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
        return STORAGE
    
    context.user_data['Framework'] = ', '.join(context.user_data['Framework'])
    

    return INTERESTS


def interests(update, context):
    ReplyKeyboardRemove()
    context.user_data['Interest'] = update.message.text
    text = update.message.text
    
    if [text] in INTERESTS_OPTONS:
        update.message.reply_text('What is your experience with the command line?',
                        reply_markup=ReplyKeyboardMarkup(CMD_EXP, one_time_keyboard=True))
    
    else:
        update.message.reply_text('Please! select from the given options',
                    reply_markup=ReplyKeyboardMarkup(INTERESTS_OPTONS, one_time_keyboard=True))
        return INTERESTS
    
    return CMD



def cmd(update, context):
    ReplyKeyboardRemove()
    context.user_data['cmd'] = update.message.text
    text = update.message.text

    if [text] in CMD_EXP:
            update.message.reply_text('Which platforms are you active on?',reply_markup=ReplyKeyboardMarkup(PLATEFORM, one_time_keyboard=True))

    
    else:
        update.message.reply_text('Please! select from the given options',
                    reply_markup=ReplyKeyboardMarkup(CMD_EXP, one_time_keyboard=True))
        return CMD

    return PLATEFORM_CODING

def plateform_coding(update, context):
    ReplyKeyboardRemove()
    context.user_data['plateform'] = update.message.text
    text = update.message.text

    if [text] in PLATEFORM:
            update.message.reply_text('What can you show to the clients to prove you are good at programming?',reply_markup=ReplyKeyboardMarkup(WORK, one_time_keyboard=True))

    
    else:
        update.message.reply_text('Please! select from the given options',
                    reply_markup=ReplyKeyboardMarkup(PLATEFORM, one_time_keyboard=True))
        return PLATEFORM_CODING

    return PROGRAMMING_SHOWCASE

def programming_showcase(update, context):
    ReplyKeyboardRemove()
    context.user_data['showcase'] = update.message.text
    text = update.message.text

    if [text] in WORK:
            update.message.reply_text('When working with a team, which of the following roles do you like?',reply_markup=ReplyKeyboardMarkup(TEAM_WORK, one_time_keyboard=True))

    
    else:
        update.message.reply_text('Please! select from the given options',
                    reply_markup=ReplyKeyboardMarkup(TEAM_WORK, one_time_keyboard=True))
        return PROGRAMMING_SHOWCASE

    return LEADERSHIP

def leadership(update, context):
    ReplyKeyboardRemove()
    context.user_data['team_roles'] = update.message.text
    text = update.message.text

    if [text] in TEAM_WORK:
            update.message.reply_text('Please share your github User Name for us to keep a track of your work.')

    
    else:
        update.message.reply_text('Please! select from the given options',
                    reply_markup=ReplyKeyboardMarkup(TEAM_WORK, one_time_keyboard=True))
        return LEADERSHIP

    return GITHUB_ID



def github_id(update, context):
    context.user_data['github'] = update.message.text

    update.message.reply_text(
        f'''
Displayed below are your details,\n\n
Name : {context.user_data['name']}\n
College : {context.user_data['college']}\n
Github Id : {context.user_data['github']}\n\n
Please let us know if your previous details were correct. 
Press "Yes" to confirm or "No" to fill details again''',
            reply_markup=ReplyKeyboardMarkup(YES_NO_OPTIONS, one_time_keyboard=True))
    
    return POINTS


def points(update, context):
    text = update.message.text

    if text == "Yes":
        link = 'https://t.me/joinchat/OI-x6FTHLBCkfWAe7wavug'
        update.message.reply_text("Great, We will get back to you soon.\n\n"f"Click to join Telgram group {link}\n\n"
        "Please further communicate with SideProjects admin. Happy Coding!")
        db.add_item(**context.user_data)

    else:
        update.message.reply_text("Press \4 for main menu.")
        return STATUS
        


    #basics
    if context.user_data['os'] in ['windows','mac']:
        context.user_data['basics'] += 1
    else:
        context.user_data['b1'] += 2
    if context.user_data['ram'] in ['1GB or less','2GB - 4GB']:
        context.user_data['basics'] += 1
    else:
        context.user_data['basics'] += 2
    if context.user_data['ram'] in ['typing takes 50% of my mind','know basic typing']:
        context.user_data['basics'] += 1
    else:
        context.user_data['basics'] += 2

    #programming
    if context.user_data['code'] in ['have never written code','can read and understand code','can write code but only small programs''have written 100+ lines of code till now','have written 500+ lines of code','have written 1000+ lines of code', 'worked on many projects','earned money writing code']:
        context.user_data['programming'] += 1
    elif context.user_data['code'] in ['have written 100+ lines of code till now','have written 500+ lines of code']:
        context.user_data['programming'] += 2
    else:
        context.user_data['programming'] += 3

    if len(context.user_data['Programming_language'].split(',')) < 3:
        context.user_data['programming'] += len(context.user_data['Programming_language'].split(','))
    else:
        context.user_data['programming'] += 3
   

    # linux
    if context.user_data['Linux'] in ['Have used linux once but never again', 'Using Linux as the primary operating system', 'Have logged into a remote server'] :
        context.user_data['programming'] += 1
    else:
        context.user_data['programming'] += 2

    
    # programming_language
    if len(context.user_data['Programming_language'].split(',')) < 3:
        context.user_data['programming'] += len(context.user_data['Programming_language'].split(','))
    else:
        context.user_data['programming'] += 3


    # framework
    if len(context.user_data['Framework'].split(',')) < 3:
        context.user_data['Points'] += len(context.user_data['Framework'].split(','))
    else:
        context.user_data['Points'] += 3

    # storage
    if context.user_data['Storage'] in ["Can read from a file using code", 'Used arrays, json or xml like nested data structures', 'Installed and comfortable with databases'] :
        context.user_data['Points'] += 1
    else:
        context.user_data['Points'] += 2

#    db.add_item(context.user_data["setup"],
 #       context.user_data["name"],
  #      context.user_data["college"],
   #     context.user_data["paid_projects"],
    #    context.user_data["os"],
     #   context.user_data["ram"],
      #  context.user_data["typing"], 
		#context.user_data["computer_work"], 
#		context.user_data["code"], 
#		context.user_data["Experience_level"],
   #     context.user_data["Programming_language"], 
	#	context.user_data["Programming_experience"], 
     #  context.user_data["Framework"],
      #  context.user_data["Storage"],
       # context.user_data["Interest"],
       # context.user_data["cmd"],
       # context.user_data["plateform"],
       # context.user_data["showcase"],
       # context.user_data["team_roles"],
       # context.user_data["github"])
        

    context.bot.send_message(chat_id=-1001467021890,text=
        f'''
New Candidate\n\n
Name : {context.user_data['Name']}\n
College : {context.user_data['College']}\n
Source : {context.user_data['Source']}\n
Experience_level : {context.user_data['Experience_level']}\n
Linux Experience : {context.user_data['Linux']}\n
Programming Language : {context.user_data["Programming_language"]}\n
programming Experience : {context.user_data["Programming_experience"]}\n
Framework : {context.user_data["Framework"]}\n
Storage : {context.user_data["Storage"]}\n
Interest : {context.user_data['Interest']}\n
Leadership: {context.user_data['Leadership']}\n
Github Id : {context.user_data['Github']}\n
'''
    )

    context.bot.send_voice(chat_id=-1001467021890, voice=open(f'ReceivedAudio/{update.message.from_user["username"]}.ogg', 'rb'))

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
            STATUS: [MessageHandler(Filters.text, status)],

            FILL: [MessageHandler(Filters.text, fill)],

#            AUDIO: [MessageHandler(Filters.voice, audio)],

           # SUBMIT: [MessageHandler(Filters.regex('Submit'), submit_audio),
            #        MessageHandler(Filters.regex('Change'), fill)
             #       ],
            SETUP: [MessageHandler(Filters.text, setup)],

            NAME: [MessageHandler(Filters.text, name)],

            COLLEGE: [MessageHandler(Filters.text, college)],
            PAID_PROJECTS: [MessageHandler(Filters.text, paid_projects)],
            OPERATING_SYSTEM: [MessageHandler(Filters.text, operating_system)],
            RAM_CONFIG: [MessageHandler(Filters.text, ram_config)],
            TYPING: [MessageHandler(Filters.text, typing)],
            AMAZING_THING_WITH_COMPUTER: [MessageHandler(Filters.text, amazing_thing_with_computer)],
            CODE: [MessageHandler(Filters.text, code)],


          #  SIDEPROJECT: [MessageHandler(Filters.text, side_project)],

            EXPERIENCE_LEVEL: [MessageHandler(Filters.text, experience_level)],

            LINUX: [MessageHandler(Filters.text, linux)],

            PROGRAMMING_LANGUAGE: [MessageHandler(Filters.regex('^(Java|JavaScript|Python|CSS|C\+\+|C|C#|HTML|HTML5|PHP|Objective C|SQL|R|Ruby)$'), multiple_select),
                        MessageHandler(Filters.regex('Done$'), programming_language)
                        ],
            
            
            PROGRAMMING_EXPERIENCE: [MessageHandler(Filters.text, programming_experience)],
            

            FRAMEWORK: [MessageHandler(Filters.regex('^(Ruby on Rails|Flask|React|Django|Angular|ASP.NET|METEOR|Laravel|Express|Spring|PLAY|CodeIgniter)$'), multi_select_framework),
                            MessageHandler(Filters.regex('Done$'), framework)
                            ],

            STORAGE: [MessageHandler(Filters.text, storage)],

            INTERESTS: [MessageHandler(Filters.text, interests)],
            CMD: [MessageHandler(Filters.text, cmd)],
            PLATEFORM_CODING:[MessageHandler(Filters.text, plateform_coding)],
            PROGRAMMING_SHOWCASE: [MessageHandler(Filters.text, programming_showcase)],


            LEADERSHIP: [MessageHandler(Filters.text, leadership)],
    

            
    
            GITHUB_ID: [MessageHandler(Filters.text, github_id)],
          
            POINTS: [MessageHandler(Filters.text, points)],

            
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
