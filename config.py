token = "1623926295:AAF_m8xVKYql8fxEwxstEEviXYw31EVhD8Y"  # bot token
bot_name = "@reputation13Bot"  # bot username
chat_id = -1001307021868  # id of chat where bot should work

# DB settings
database = "dc9smktko14646"
host = "ec2-34-198-31-223.compute-1.amazonaws.com"
user = "sjpvclnxuoymzv"
password = "3ecaf654d88ca1b7500a82debcdf6f6d945937daa8b9b2bb6a6663a82d4e9a26"

admins = [183654961, 0, 0]  # users ids that can use /ban and /unban commands

help_text = """
Hey, I'm A reputation Bot.
\nThere will be no further explanation, There will just be reputation.\nTo *add karma*, reply with the phrase "Thank you" to the message of the person who helped you.\nTo *reduce karma*, reply with the phrase "Minus" to the message of who you want to reduce karma.\nGroup - @SwiftiesWorld \nCreated By @TayLIfe

\n/top20 - displays top 20 users with positive karma
\n/untop20 - displays top 20 users with negative karma
\n/help - help on bot commands
"""

# text for new users
welcome_text = """
"""

# text for new users without username
welcome_user = """
"""

# text for chat where bot don't work
chat_error = "Sorry, but I don't work in this chat.\nJoin - @SwiftiesWorld\nCreated By @TayLife"

# karma text for user without username
username_error = "Unfortunately, the user you thanked doesn't have a username, so I can't change his karma :("

# text for message without reply
reply_to_like = "@%s, you must reply to a message that helped you!"
reply_to_unlike = "@%s, you must reply to a message you didn't like!"

# text with thanks to bot
like_to_bot = "@%s, always happy to help!"

# text with reduce karma to bot
unlike_to_bot = "@%s, I don't have a karma!"

# text with karma to urself
masturbate = "@%s, hey, you can't add karma to yourself!"
unmasturbate = "@%s, why don't you love yourself? :("

# text to karma add
like_message = """
Added karma to @%s
\n-------------------
@%s has %d karma
"""

# text to reduce karma
unlike_message = """
Reduces karma to @%s
\n-------------------
@%s has %d karma
"""

# text for a ban for a little karma
ban = "@%s has -100 karma. He is banned."

# text for ban if user doesn't exist in DB
cant_ban = "There is no such user in my database, you can ban it only manually."

# text for unban if user doesn't exist in DB
cant_unban = "There is no such user in my database, you can unban it only manually."

# text for ban
banned = "Banned"

# text for unban
unbanned = "Unbanned"
