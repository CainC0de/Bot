import discord

# Crie uma instância do bot
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = discord.Client(intents=intents)

# Evento para executar quando o bot estiver online
@bot.event
async def on_ready():
    print(f'Bot está online como {bot.user.name}')

# Token do seu bot (substitua com o seu token)
TOKEN = 'SEU_TOKEN_AQUI'

# Inicie o bot com o token
bot.run('MTA2MjcwMjE5ODE1MDE1MjIwMg.Gtl0uA.z4-T8MQROAYJ3vJN4z6cmM8MRrYC3d3J0oPnaQ')
