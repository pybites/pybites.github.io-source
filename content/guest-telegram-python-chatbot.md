Title: DisAtBot - How I Built a Chatbot With Telegram And Python
Date: 2017-12-10 23:30
Category: Tools
Tags: bots, code challenge, guest, DisAtBot, chatbots, opensource, Telegram, Mexico
Slug: guest-telegram-python-chatbot
Authors: Rodolfo Ferro
Summary: Rodolfo recently joined our [Code Challenges](https://pybit.es/pages/challenges.html) and built *Disaster Attention Bot (DisAtBot)*, a chatbot that helps people affected by natural disasters. In this article he shows how he built this bot with Telegram and (of course) Python. Show him some love because who knows, this could be a life saver (pun intended)! We are delighted to have him show this interesting project he submitted for [Code Challenge 43](https://pybit.es/codechallenge43.html) which earned him a book on chatbots. /Rod please share ...
cover: images/featured/pb-guest.png

Rodolfo recently joined our [Code Challenges](https://pybit.es/pages/challenges.html) and built *Disaster Attention Bot (DisAtBot)*, a chatbot that helps people affected by natural disasters. In this article he shows how he built this bot with Telegram and (of course) Python. Show him some love because who knows, this could be a life saver (pun intended)! We are delighted to have him show this interesting project he submitted for [Code Challenge 43](https://pybit.es/codechallenge43.html) which earned him a book on chatbots. /Rod please share ...

> *"¿Quién convocó a tanto muchacho, de dónde salió tanto voluntario, cómo fue que la sangre sobró en los hospitales, quién organizó las brigadas que dirigieron el tránsito de vehículos y de peatones por toda la zona afectada? No hubo ninguna convocatoria, no se hizo ningún llamado y todos acudieron"*
>
> **"El jueves negro que cambió a México"**
> – Emilio Viale, 1985.

## A bit of context...

Since September 19th, 2017 [Mexico has been hit by several earthquakes](https://en.wikipedia.org/wiki/2017_Central_Mexico_earthquake) ([The Guardian](https://www.theguardian.com/world/live/2017/sep/20/mexico-city-earthquake-dozens-dead-powerful-quake-live-updates), [CNN](http://edition.cnn.com/2017/09/19/americas/mexico-earthquake/index.html)). This made me wonder how we could better handle the reporting of damaged zones, people buried under the rubble of buildings, injured people in need of medical attention and other situations.

[Verificado 19s](http://www.verificado19s.org) was an immediate solution to follow up reports from social media and visualize the info on an online map. This required a lot of real-time (24/7) monitoring of posts on social media from people that were located in the effected areas. And that data was updated every ~10 minutes.

So I started thinking about a way to optimize this process for future situations, not only for earthquakes, but for disaster situations in general. This incentivized me to work on this bot for Pybites [Code Challenge 43 - Build a Chatbot Using Python](https://pybit.es/codechallenge43.html).

## So DisAtBot was born

DisAtBot automates the process of reporting incidents via messaging platforms, such as Telegram, Facebook Messenger, Twitter, etc. At this time it only supports Telegram, but I hope to expand it to other social media. If you'd like to contribute, see the Contribute section at the end.

You can find DisAtBot at:

- Telegram: [https://t.me/DisAtBot](https://t.me/DisAtBot)
- The official repo: [https://github.com/RodolfoFerro/DisAtBot](https://github.com/RodolfoFerro/DisAtBot)

The idea was to have a simple flow that allowed disaster reporting to be quick and easy. The general process of DisAtBot is as follows:

![disatbot flow]({filename}/images/disatbot-flow.png)

The idea is that any user can interact with the bot by selecting options from button menus in the conversation. This greatly speeds up incidents reporting.

The next step would be opening a ticket which will be stored in a database, for the corresponding government instance/public organization/NGO/etc. to validate and send assistance. When no more help is needed, or the situation is under control, the ticket is closed.

## Setup

First clone [the repo](https://github.com/RodolfoFerro/DisAtBot). I used Python 3.6 and the following packages:

- [pandas](http://pandas.pydata.org/)

- [geopandas](http://geopandas.org/)

- [geocoder](http://geocoder.readthedocs.io/)

- [googlemaps](https://developers.google.com/maps/documentation/)

- [geojsonio](http://geojson.io/)

- [Shapely](https://shapely.readthedocs.io/en/latest/)

- [python-telegram-bot](https://python-telegram-bot.org/)

To install all dependencies create [a virtual env](http://pybit.es/the-beauty-of-virtualenv.html) and run:

```bash
pip install -r requirements.txt
```

Then cd into the scripts folder and run the bot as follows:

```bash
python DisAtBot.py
```

## Design

The focus of the initial version was the creation of menu buttons for an easy interaction with the user. The second –*and main*– issue addressed was the conversation handler. A [finite state machine](https://en.wikipedia.org/wiki/Finite-state_machine) was needed to preserve the desired flow and the responses for each state.

I won’t go too deep into the explanation, but the code below will show how I tackled this.

First of all, Telegram’s library has several methods to create button menus for user responses during the conversation flow. The idea is to create a Keyboard Markup to handle responses through buttons. This can either be Inline (buttons will appear in the conversation window) or as a Reply Keyboard (buttons will be displayed under the textbox to write messages).

An example can be seen in the menu function:
```python
def menu(bot, update):
    """
    Main menu function.
    This will display the options from the main menu.
    """
    # Create buttons to select language:
    keyboard = [[send_report[LANG], view_map[LANG]],
                [view_faq[LANG], view_about[LANG]]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)

    user = update.message.from_user
    logger.info("Menu command requested by {}.".format(user.first_name))
    update.message.reply_text(main_menu[LANG], reply_markup=reply_markup)

    return SET_STAT
```

As you can see, the `keyboard` variable is a list that contains the four buttons to be displayed. The layout can be set by nesting lists inside. In this case the **Report** and **Map** buttons are in the first row, while **FAQ** and **About** buttons are in the second row. This looks like:

![disatbot menu]({filename}/images/disatbot-menu.jpg)

Continuing with the code, a `ReplyMarkup` is needed to handle the button responses. It specifies the layout of the menu: if only one menu is displayed, if it needs to be resized, etc. 

A logger is used for the bot, and the `update.message.reply(...)` function is used to update the displayed text according to the response from the user. The `SET_STAT` variable returned in this function is a (predefined) integer to return the state at that time, and to follow the flow.

We now understand the menu creation and handling. The reason of using buttons is that we want a quick interaction because the bot is used in an emergency situation.

The conversation handler - Telegram's `ConversationHandler` - takes care of setting the state or step of the flow we're currently at, the finite state machine I mentioned earlier. Note that each state also needs to handle its respective information (button responses, etc.)

This code shows the conversation handler:

```python
def main():
    """
    Main function.
    This function handles the conversation flow by setting
    states on each step of the flow. Each state has its own
    handler for the interaction with the user.
    """
    global LANG
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(telegram_token)

    # Get the dispatcher to register handlers:
    dp = updater.dispatcher

    # Add conversation handler with predefined states:
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            SET_LANG: [RegexHandler('^(ES|EN)$', set_lang)],

            MENU: [CommandHandler('menu', menu)],

            SET_STAT: [RegexHandler(
                        '^({}|{}|{}|{})$'.format(
                            send_report['ES'], view_map['ES'],
                            view_faq['ES'], view_about['ES']),
                        set_state),
                       RegexHandler(
                        '^({}|{}|{}|{})$'.format(
                            send_report['EN'], view_map['EN'],
                            view_faq['EN'], view_about['EN']),
                        set_state)],

            LOCATION: [MessageHandler(Filters.location, location),
                       CommandHandler('menu', menu)]
        },

        fallbacks=[CommandHandler('cancel', cancel),
                   CommandHandler('help', help)]
    )

    dp.add_handler(conv_handler)

    # Log all errors:
    dp.add_error_handler(error)

    # Start DisAtBot:
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process
    # receives SIGINT, SIGTERM or SIGABRT:
    updater.idle()
```

It might seem a bit confusing at first, but it boils down to:
- The conversation handler has the states of the flow.
- It also has entry points (such as the `start` function), and fallbacks (such as the `cancel` and `help` functions).
- It also contains some error handlers.
- A global `LANG` variable is used, since the implementation - I forgot to mention - support interacting in English or Spanish! To support this I created dictionaries for each interaction in both languages.

If you want to check the full code of this bot, check out [the scripts directory](https://github.com/RodolfoFerro/DisAtBot/tree/master/scripts) where you'll find the main script and the language dictionaries.

Some other features implemented are geolocation handling and `About` / `FAQ` sections. But the best way to know about this project is by watching it in action (for a live demo go to 8.30):

<iframe src="https://drive.google.com/file/d/1dOvF17AYKiic85HmzMjnK5Qza2Tg0PNw/preview" width="800" height="480"></iframe>

## Future work

For future development I am thinking about adding a map. The system already creates a GeoJSON file from the locations acquired. 

As mentioned I am considering expanding this to other platforms like Facebook Messenger and Twitter. Another good thing to add would be a website explaining the main use cases of the bot, maybe a wiki –*kinda*– site? 

If you have any other ideas or suggestions feel free to [contact me](https://twitter.com/FerroRodolfo) or:

## Contribute

If you're interested in contributing to this project, feel free to take a look at the repo's [CONTRIBUTING](https://github.com/RodolfoFerro/DisAtBot/blob/master/CONTRIBUTING.md) file. I'd be very pleased if this project would grow out to something used in real life to alleviate the dramatic consequences of natural disaster, which always seem to hit when least expected.

---
Keep Calm and Code in Python!

[Rodolfo](pages/guests.html#rodolfoferro)
