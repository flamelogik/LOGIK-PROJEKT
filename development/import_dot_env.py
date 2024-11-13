import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access API keys
lucidlink_api_key = os.getenv('LUCIDLINK_API_KEY')
masvio_api_key = os.getenv('MASV_IO_API_KEY')
frameio_api_key = os.getenv('FRAME_IO_API_KEY')
s3_api_key = os.getenv('S3_DEEP_ARCHIVE_API_KEY')

# Now you can use these variables in your script to make API calls
