import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "!!Please Drink Water Now!!",
            message = "It's been 1 hour since you last drank water, Please drink now...",
            app_icon= "C:/Users/Akash/git2/watericon.ico",
            timeout=10
        )
        time.sleep(60*60)