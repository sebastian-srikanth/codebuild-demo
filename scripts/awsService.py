import logging
import pytz


ist = pytz.timezone("Asia/Kolkata")
logging.basicConfig(level=logging.DEBUG)

class aws_service:
	region = 'ap-south-1' # Mumbai Region

	def __init__(self):
		self.logger = logging.getLogger(type(self).__name__)
		self.logger.info(f'logged to {self.region} region')

	def user_login(self,user='anonymous-user'):
		self.logger.info(f'{user} has logged in !!!  ')

# call_service = aws_service()
# call_service.user_login()