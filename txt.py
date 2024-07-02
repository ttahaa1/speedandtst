from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.channels import LeaveChannelRequest
import asyncio
from colorama import init, Fore

init(autoreset=True)

api_id, api_hash, session_string = '22379637', '7a5777d4bd0480856f9e7b129acc7a9f', '1BJWap1sBu39jH0wUORvU_DrarebQ6YzNbS7DrxU328-JOXFmZ0Erg5XFwc4cLrCtb9NzIZponHAsdAwtypvurTgzM170vK7imQ_V4cNLs3OqokHpnZPJyRMjengWuXpkKAtzt-JdUWqexgyn_UAWlYcoeuNCMuesrxQGeT15XAtpHUhbT0Ioh2a66wZOYxR-z3rR2ea2jsYyyN1SVjZ5IS3t83baBh4Ry3gCTEYD2l0iBXGeZmyz4fDQiMZlXtsD6itYIYi0eTWUukLaG6Hwz5p2AohtiExo7CM5TDtkHBvwhIToKNF_QLs-XBVIHQCTkmUMrTm7hbf2rF1Obstj3hoDE__WaoM='
client = TelegramClient(StringSession(session_string), api_id, api_hash)

async def main():
    await client.start()
    choice = input(Fore.CYAN + "هل تريد مغادرة القنوات أو المجموعات؟\n" + Fore.YELLOW + "(c للمغادرة من القنوات، g للمغادرة من المجموعات)\n" + Fore.GREEN + "اختر (c/g): ").strip().lower()
    
    if choice in ['c', 'g']:
        confirm = input(Fore.CYAN + "هل أنت متأكد من مغادرة جميع " + ("القنوات" if choice == 'c' else "المجموعات") + "؟\n" + Fore.GREEN + "(y/n): ").strip().lower()
        if confirm == 'y':
            print(Fore.RED + "جاري مغادرة جميع " + ("القنوات..." if choice == 'c' else "المجموعات..."))
            async for dialog in client.iter_dialogs():
                if (choice == 'c' and dialog.is_channel and not dialog.is_group) or (choice == 'g' and dialog.is_group):
                    print(Fore.RED + f"مغادرة {'القناة' if choice == 'c' else 'المجموعة'}: {dialog.name}")
                    await client(LeaveChannelRequest(dialog.id))
            print(Fore.GREEN + f"تم مغادرة جميع {'القنوات' if choice == 'c' else 'المجموعات'}.")
    await client.disconnect()

asyncio.run(main())
