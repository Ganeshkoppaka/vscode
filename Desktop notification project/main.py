from email import message
from msilib.schema import Icon
from turtle import title
from plyer import notification
import time

if __name__=="__main__":
    
        notification.notify(
            title="PLEASE DRINK WATER",
            message="it is time to drink glass of water",
            app_icon="C:\desktop notification project\Iconsmind-Outline-Glass-Water.ico",
            timeout=10
        )
        # time.sleep(60*60)