# This thing makes my account get blocked until I change the password
# Its supposed to DM someone the lyrics of Still Alive.

from instagram_private_api import Client, ClientCompatPatch

username = ""
password = ""

api = Client(username, password)
results = api.feed.timeline()

# Set a recipient
recipient_username = ''

# Replace MESSAGE_TEXT with the text of the message you want to send
message_text = """This was a triumph
I'm making a note here
"Huge success"
It's hard to overstate my satisfaction
Aperture Science
We do what we must because we can
For the good of all of us
Except the ones who are dead
But there's no sense crying over every mistake
You just keep on trying till you run out of cake
And the science gets done and you make a neat gun
For the people who are still alive
I'm not even angry
I'm being so sincere right now
Even though you broke my heart
And killed me
And tore me to pieces
And threw every piece into a fire
As they burned it hurt because
I was so happy for you
Now, these points of data make a beautiful line
And we're out of beta, we're releasing on time
So I'm GLaD I got burned, think of all the things we learned
For the people who are still alive
Go ahead and leave me
I think I'd prefer to stay inside
Maybe you'll find someone else
To help you
Maybe Black Mesa?
That was a joke, ha-ha, fat chance
Anyway, this cake is great
It's so delicious and moist
Look at me, still talking when there's science to do
When I look out there, it makes me GLaD I'm not you
I've experiments to run, there is research to be done
On the people who are still alive
And believe me, I am still alive
I'm doing science and I'm still alive
I feel fantastic and I'm still alive
While you're dying, I'll be still alive
And when you're dead, I will be still alive
Still alive
Still alive
"""

# Login to your Instagram account
api = Client(username, password)

# Get the user ID of the recipient
recipient = api.username_info(recipient_username)['user']
recipient_id = recipient['pk']

# Send the message
api.send_direct_item(
    message={'text': message_text},
    recipients=[{'user_id': recipient_id}]
)
