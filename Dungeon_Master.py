import discord
import requests
import json
import random
import pymongo

dbclient = pymongo.MongoClient("mongodb+srv://Giorgos:cumzone@insultdb.xr2uz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = dbclient["insultdb"]

client = discord.Client()

happy_words = ["happy","glad","fantastic","good","amazing","cheerful"]

starter_insults = ["Piss off!","Kill yourself!","You are a disgrace!"]

def get_quote():
    response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
    json_data = json.loads(response.text)
    quote = json_data['insult']
    return(quote)


@client.event
async def on_ready():
    print('We are horny and strapped as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    
    if message.content.startswith('$sup'):
        await message.channel.send('Hey bro, nice cock!')

    if message.content.startswith('$wisdom'):
        quote = get_quote()
        await message.channel.send(quote)
        db["gamostavridia"].update_one(
                    { "insult" : quote },
                    { "$set": { "insult": quote}},
                    upsert = True  
                 )

client.run('ODI4NjAyNzgwOTUxMzgwMDI4.YGr-eQ.5aHzBNXTKy2ai9sprSg_mqTfEAo')