import discord

intents = discord.Intents.default()
intents.members = True  # Abilita gli eventi dei membri

# token bot
TOKEN = ''

#
UTENTE_DI_ECCEZIONE_ID = ''

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Bot connesso come {client.user}')


@client.event
async def on_member_join(member):
    print(f"Nuovo membro {member.name} ({member.id}) è entrato nel server.")

    # Controlla se il nome dell'utente è "Mr Rip" o "rip" e se non è l'utente di eccezione
    if (
            member.name.lower() == 'mr rip' or member.name.lower() == 'rip' or member.name.lower() == 'mrrip') and str(
            member.id) != UTENTE_DI_ECCEZIONE_ID:
        try:
            await member.kick(reason="Nome non permesso.")
            print(f"Utente {member.name} ({member.id}) espulso.")
        except discord.Forbidden:
            print("Il bot non ha i permessi per espellere utenti.")
        except discord.HTTPException:
            print("Errore HTTP durante l'espulsione dell'utente.")


client.run(TOKEN)
