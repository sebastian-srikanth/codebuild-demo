# from awsService import aws_service
import sys
from scripts.awsService import aws_service
import sys

class main:
	args = sys.argv[1].split(',')
	call_service = aws_service()
	call_service.user_login(args[0])


if __name__ == '__main__':
	main()
