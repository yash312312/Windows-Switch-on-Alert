from pushbullet import PushBullet
from dotenv import main
import os

main.load_dotenv()

'''
    Store the access token in a variable access_token in the .env file
    access_token=XXXXXXXX
    .
    ├── .env
    └── main.py
'''

pb = PushBullet(os.getenv('access_token'))

push = pb.push_note("Alert", "Laptop has been switched on")
