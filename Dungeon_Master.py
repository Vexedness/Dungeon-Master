import discord
import requests
import json
import random
# gamw thn panagia sou
client = discord.Client()

happy_words = ["happy","glad","fantastic","good","amazing","cheerful"]

starter_insults = ["Piss off!","Kill yourself!","You are a disgrace!"]

def get_quote():
    response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
    json_data = json.loads(response.text)
    quote = json_data['insult']
    return(quote)
#SAVE INSULTS FROM API TO DB
def update_insults(insulting_message):
    if "insults" in db.key():
        insults = db["insults"]
        insults.append(insulting_message)
        db["insults"] = insults
    else:
        db["insults"] = [insulting_message]
#DELETE INSULTS FROM DB
def delete_insults(index):
    insults = db["insults"]
    if len(insults) > index:
        del insults[index]
        db["insults"] = insults


@client.event
async def on_ready():
    print('We are horny and strapped as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
#SUP
    if message.content.startswith('$sup'):
        await message.channel.send('Hey bro, nice cock!')
#API COMMAND
    if message.content.startswith('$wisdom'):
        quote = get_quote()
        await message.channel.send(quote)
#DB KINDA SORTA W/E
    options = starter_insults
    if "insults" in db.key():
        options = options + db["insults"]
#SAVE NEW INSULT
    if msg.startswith("$new"):
        insulting_message = msg.split("$new ",1)[1]
        update_insults(insulting_message)
        await message.channel.send("New insult has been added... Cunt.")
#DELETE INSULT
    if msg.startswith("del"):
        insults = []
        if "insults" in db.key():
            index = int(msg.split("$del",1)[1])
            delete_insults(index)
            insults = db["insults"]
        await message.channel.send(insults)
#SEE INSULT LIST
    if msg.startswith("list"):
        insults = []
        if "insults" in db.key():
            insults = db["insults"]
        await message.channel.send(insults)
#KEY WORDS
    if any(word in msg for word in happy_words):
        await message.channel.send(random.choice(options))

client.run('ODI4NjAyNzgwOTUxMzgwMDI4.YGr-eQ.in_CP3R8-ZyUA7vNgbpgUScd-a8')