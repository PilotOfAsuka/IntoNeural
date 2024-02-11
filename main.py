import misc as m
import asyncio
import handlers


async def on_startup():
    print("Bot is running")


async def main():
    m.dp.startup.register(on_startup)
    await m.bot.delete_webhook(drop_pending_updates=True)
    await m.dp.start_polling(m.bot, allowed_updates=m.dp.resolve_used_update_types())

if __name__ == "__main__":

    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(main())
    finally:
        loop.close()


