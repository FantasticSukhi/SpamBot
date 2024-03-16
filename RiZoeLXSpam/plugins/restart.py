from .. import Riz, Riz2, Riz3, Riz4, Riz5, Riz6, Riz7, Riz8, Riz9, Riz10, SUDO_USERS
from telethon import events
import os
import random
import sys


@Riz.on(events.NewMessage(pattern=".restart"))
@Riz2.on(events.NewMessage(pattern=".restart"))
@Riz3.on(events.NewMessage(pattern=".restart"))
@Riz4.on(events.NewMessage(pattern=".restart"))
@Riz5.on(events.NewMessage(pattern=".restart"))
@Riz6.on(events.NewMessage(pattern=".restart"))
@Riz7.on(events.NewMessage(pattern=".restart"))
@Riz8.on(events.NewMessage(pattern=".restart"))
@Riz9.on(events.NewMessage(pattern=".restart"))
@Riz10.on(events.NewMessage(pattern=".restart"))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "​🇷​​🇪​​🇸​​🇹​​🇦​​🇷​​🇹​​🇮​​🇳​​🇬​ ​🇾​​🇴​​🇺​​🇷​ ​🇲​​🇦​​🇲​​🇧​​🇦​ ​🇸​​🇵​​🇦​​🇲​​🇲​​🇪​​🇷​​🇸​.... ​🇵​​🇱​​🇪​​🇦​​🇸​​🇪​ ​🇼​​🇦​​🇮​​🇹​ ​🇺​​🇳​​🇹​​🇮​​🇱​ ​🇮​​🇹​ ​🇸​​🇹​​🇦​​🇷​​🇹​​🇸​ ​🇦​​🇬​​🇦​​🇮​​🇳. ਓ ਬਾਈ ਵਹਲੀ ਕਾਹਲੀ ਆ ਤੇਨੁ ॥ ਥੰਡ ਰੱਖ ਲਾ ਏਹ ਬੋਟ ਈ ਏਹਨੇ ਥੋਡਾ ਟਾਈਮ ਲਗਾਉਨਾ ਹੀ ਹੁੰਦਾ। ਤੂ ਈ ਕਰ ਆਪਦੀ ਬੇਬੇ ਤੋੰ ਚਾਹ ਬਨਵਾ ਕੇ ਲੈ ਆ। ਇਕੁ ਤੂ ਆਪੇ ਲਾਇ ਤੇ ਇਕੁ ਮੇਰਾ ਮਾਲਕ ਲਾਈ, ਮੇਰਾ ਮਾਲਕ @ɪᴛᴢ_ᴍᴇ_ʙʟᴀᴄᴋᴍᴀᴍʙᴀ ਲੇ ਚੱਕ ਮ ਤਾੰ ਆਈਡੀ ਵੀ ਦੇ ਦਿਤੀ ਆ।"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await Riz.disconnect()
        except Exception:
            pass
        try:
            await Riz2.disconnect()
        except Exception:
            pass
        try:
            await Riz3.disconnect()
        except Exception:
            pass
        try:
            await Riz4.disconnect()
        except Exception:
            pass
        try:
            await Riz5.disconnect()
        except Exception:
            pass
        try:
            await Riz6.disconnect()
        except Exception:
            pass
        try:
            await Riz7.disconnect()
        except Exception:
            pass
        try:
            await Riz8.disconnect()
        except Exception:
            pass
        try:
            await Riz9.disconnect()
        except Exception:
            pass
        try:
            await Riz10.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
