import discord
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = discord.Client()
today = datetime.now()

@bot.event
async def on_ready():
    python_pt = bot.get_channel(884454021576949780)
    java_pt = bot.get_channel(884454120092753951)
    web_fun_pt = bot.get_channel(884459590429843476)
    projAlgos_pt = bot.get_channel(884459879232860233)
    cohort_java_Matt = bot.get_channel(884446303491338324)
    cohort_java_Reena = bot.get_channel(884446303491338324)

    if today.isoweekday() == 0:
        print("Presence posted for Sunday")
        await python_pt.send("@stack-python-PT 📘 Hello :python: ninjas! I'll be here until 4PM PST. If you have any questions or need extra :eyes: please feel free to reach out.")
        await java_pt.send("@stack-java-PT ☕ Hello :java: ninjas! I'll be here until 4PM PST. If you have any questions or need extra :eyes: please feel free to reach out.")
        await web_fun_pt.send("@stack-web-fund-PT 🧱 Hello ninjas! I'll be here until 4PM PST. If you have any questions or need extra :eyes: please feel free to reach out.")
        await projAlgos_pt.send("@stack-project-algos-PT 📓 Hello ninjas! I'll be here until 4PM PST. If you have any questions or need extra :eyes: please feel free to reach out.")
    if today.isoweekday() == 1:
        print("Presence posted for Monday")
        await python_pt.send("@stack-python-PT 📘 Hello :python: ninjas! I'll be here until 5PM PST. If you have any questions or need extra :eyes: please feel free to reach out.")
        await java_pt.send("@stack-java-PT ☕ Hello :java: ninjas! I'll be here until 5PM PST. If you have any questions or need extra :eyes: please feel free to reach out.")
        await web_fun_pt.send("@stack-web-fund-PT 🧱 Hello ninjas! I'll be here until 5PM PST. If you have any questions or need extra :eyes: please feel free to reach out.")
        await projAlgos_pt.send("@stack-project-algos-PT 📓 Hello ninjas! I'll be here until 5PM PST. If you have any questions or need extra :eyes: please feel free to reach out.")
    if today.isoweekday() == 2 or today.isoweekday() == 3:
        print("Presence posted for Tuesday/Wednesday")
        await python_pt.send("@stack-python-PT 📘 Hello :python: ninjas! I'll be here until 8PM PST. If you have any questions or need extra :eyes: please feel free to reach out.")
        await java_pt.send("@stack-java-PT ☕ Hello :java: ninjas! I'll be here until 8PM PST. If you have any questions or need extra :eyes: please feel free to reach out.")
        await web_fun_pt.send("@stack-web-fund-PT 🧱 Hello ninjas! I'll be here until 8PM PST. If you have any questions or need extra :eyes: please feel free to reach out.")
        await projAlgos_pt.send("@stack-project-algos-PT 📓 Hello ninjas! I'll be here until 8PM PST. If you have any questions or need extra :eyes: please feel free to reach out.")
        if today.isoweekday() == 2:
            print("Office hours posted for Reena's cohort")
            await cohort_java_Reena.send("@cohort-ReenaD 🏫 Office hour starting at 4 PST. Bring homework for peer code review, questions, errors and anything you've got going on you may need help with or need eyes for :java:")
        elif today.isoweekday() == 3:
            print("Office hours posted for Matt's cohort")
            await cohort_java_Matt.send("@cohort-MattS-2 🏫 Office hour starting at 4 PST. Bring homework for peer code review, questions, errors and anything you've got going on you may need help with or need eyes for :java:")

    server_count = 0
    for server in bot.guilds:
        print(f"- {server.id} (name: {server.name})")
        server_count += 1
    print("taBot is in " + str(server_count) + " servers.")

@bot.event
async def close():
    python_pt = bot.get_channel(884454021576949780)
    await python_pt.send("@stack-python-PT 📘 If any of us (TA's) helped you today, please give us some feedback on how we did! This form gives you the ability to voice how we are doing. The feedback doesn't go directly to us, so feel free to speak your mind and help us improve. https://operations462398.typeform.com/to/rX5h1pbL#ta_name=cameron_s")
    java_pt = bot.get_channel(884454120092753951)
    await java_pt.send("@stack-java-PT ☕ If any of us (TA's) helped you today, please give us some feedback on how we did! This form gives you the ability to voice how we are doing. The feedback doesn't go directly to us, so feel free to speak your mind and help us improve. https://operations462398.typeform.com/to/rX5h1pbL#ta_name=cameron_s")
    web_fun_pt = bot.get_channel(884459590429843476)
    await web_fun_pt.send("@stack-web-fund-PT 🧱 If any of us (TA's) helped you today, please give us some feedback on how we did! This form gives you the ability to voice how we are doing. The feedback doesn't go directly to us, so feel free to speak your mind and help us improve. https://operations462398.typeform.com/to/rX5h1pbL#ta_name=cameron_s")
    projAlgos_pt = bot.get_channel(884459879232860233)
    await projAlgos_pt.send("@stack-project-algos-PT 📓 If any of us (TA's) helped you today, please give us some feedback on how we did! This form gives you the ability to voice how we are doing. The feedback doesn't go directly to us, so feel free to speak your mind and help us improve. https://operations462398.typeform.com/to/rX5h1pbL#ta_name=cameron_s")

bot.run(DISCORD_TOKEN)