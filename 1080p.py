#from spdatabase import *
from pyrogram import Client, filters
import requests,os,csv
from time import time
import time
from datetime import datetime
from pytz import timezone

#create_table()
now=datetime.now()
crtda = now.strftime('%d/%m/%y')
crtda2 = now.strftime('%d-%m-%y')

indexlink = "https://index.mrspidy616.workers.dev"


api_id = 11405252
api_hash = "b1a1fc3dc52ccc91781f33522255a880"
bot_token = "6326333011:AAHHvjzDx7zc8nKXzobh_dNRoS5yH7KTPmw"




app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)


async def progress(current, total):
    print(f"{current * 100 / total:.1f}%")



async def main():
   async with app:
     link = "https://www.pornhub.com/playlist/263313231"
     status = await app.send_message(-1002034630043,f"Update Started!\nDate:{crtda}\nIndex Link: {indexlink}/Backup/{crtda2}/")
     os.system(f"""yt-dlp   --downloader aria2c   -o '%(title)s.%(ext)s' -f 'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]' --write-thumbnail --embed-metadata """ + link)
     for  filename in os.listdir():
      if filename.endswith(".mp4"):
            await app.send_video(-1002034630043, video=filename,caption=filename.replace(".mp4",""),thumb=filename.replace(".mp4",".jpg"),progress=progress)     
            #os.system(f'''rclone --config './rclone.conf' move """{filename.replace('.mp4','.jpg')}"""  'PH_Pics:/Pictures/'  ''')              
            os.system(f'''rclone --config './rclone.conf' move  """{filename}"""  'Drive:/Backup/Full/{crtda2}'  ''')
            os.system(f"""rclone --config './rclone.conf' move "Drive:/Backup/Full/{crtda2}" "TD:Backup/Full/{crtda2}" -vP --delete-empty-src-dirs --drive-server-side-across-configs=true """)
            try:
              os.remove(filename)
            except:
               print("File Moved I guess!!!")        
     await app.send_message(-1002034630043, "Update Completed Successfully...", reply_to_message_id=status.id)      


app.run(main())
