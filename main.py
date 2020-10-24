



import requests
import argparse
import time
import traceback



parser = argparse.ArgumentParser()

# add arguments
parser.add_argument("-ip", "--ip_address", help="Set IP")
args = parser.parse_args()
print(args)

PORT_MIN = 0
PORT_MAX = 65353


# add protocol
if not args.ip_address.startswith("http"):
	args.ip_address = "http://{}".format(args.ip_address)

# find good port
for port in range(PORT_MIN, PORT_MAX):

	try:

		response = requests.post(args.ip_address)	# send request

		# dump response file
		with open("response_files/{}_response_{}.html".format(str(port), str(response.status_code)), 'w+', encoding='utf8') as f:
			f.write(response.text)

		# print port if response code is 200
		if response.status_code == 200:
			print("Port:", port, "\tResponse:", response.status_code)

		time.sleep(0.5)

	except Exception as e:
		error = str(traceback.format_exc())

		print("Port:", port, "\tError:", str(e))

		with open("response_files/{}_response_{}.txt".format(str(port), "ERR"), 'w+', encoding='utf8') as f:
			f.write(error)

		time.sleep(0.5)