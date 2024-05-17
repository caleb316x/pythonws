
import time
import pusher
import random

pusher_client = pusher.Pusher(
  app_id='1803808',
  key='150195cef7da32949a7b',
  secret='e806343d86e5394eac73',
  cluster='ap1',
  ssl=True
)
eggs=[
        "peewee",
        "pullet",
        "small",
        "medium",
        "large",
        "extra_large",
        "jumbo",
        "crack"
    ]

while True:
    pusher_client.trigger('eggker', 'MessageSent', {'message': eggs[random.randrange(0,7)]})
    time.sleep(5)
