#Bot Initialization

token = "qbcde"
clan_id = 1292897968894246972

bot = commands.Bot(command_prefix="!", intents=disc.Intents.all())

@bot.command()
async def _isfree(ctx):
    day = int(datetime.datetime.today().weekday())
    if day == 1:
        pass #Do Monday
    elif day == 2:
        pass #Do Tuesday
    elif day == 3:
        pass #Do Wednesday
    elif day == 4:
        pass #Do Thursday
    elif day == 5:
        pass #Do Friday
    elif day == 6:
        pass #Do Tuesday
    else:
        print ("They're free bitch")
async def _update_schedule(ctx, ):
    try:
        pass
    except:
        print("Invalid Command")
async def _show_schedule(ctx, user):
    pass
async def _day_schedule():
    day = int(datetime.datetime.today().weekday())