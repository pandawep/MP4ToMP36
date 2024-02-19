from pyrogram import Client, filters
from pydub import AudioSegment
from io import BytesIO
from config import API_ID, API_HASH, BOT_TOKEN

# Define your start message
START_MESSAGE = """
Hello! I'm your MP4 to MP3 converter bot. Just send me an MP4 file, and I'll convert it to MP3 for you!
"""

# Initialize the Pyrogram client
app = Client(
    "mp4_to_mp3_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Define the start command handler
@app.on_message(filters.command(["start"]))
def start_command(client, message):
    # Send the start message
    message.reply_text(START_MESSAGE)

# Define the audio conversion handler
@app.on_message(filters.document & filters.video)
def convert_to_mp3(client, message):
    # Download the video file
    video_file = client.download_media(message)

    # Convert MP4 to MP3
    sound = AudioSegment.from_file(video_file)
    audio_buffer = BytesIO()
    sound.export(audio_buffer, format='mp3')

    # Send the MP3 file to the user
    client.send_audio(
        chat_id=message.chat.id,
        audio=audio_buffer.getvalue(),
        reply_to_message_id=message.message_id
    )

# Run the bot
app.run()
