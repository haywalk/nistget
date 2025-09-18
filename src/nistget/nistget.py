#!/usr/bin/python3

# This file is part of nistget.
#
# nistget is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software 
# Foundation, either version 3 of the License, or (at your option) any later 
# version.
#
# nistget is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# nistget. If not, see http://www.gnu.org/licenses/.

from requests import get
from time import time
import sys

NIST_URL = 'https://beacon.nist.gov/beacon/2.0/pulse/time/previous/{}'
USAGE = f'Usage: {sys.argv[0]} [timestamp in milliseconds]'

def get_pulse(timestamp=None):
	'''
	Get a pulse from a specific timestamp.

	timestamp: UNIX timestamp
	'''

	# use the current timestamp if none is specified
	if timestamp == None:
		timestamp = int(time() * 1000)

	url = NIST_URL.format(timestamp)
	resp = get(url)
	return resp.json()['pulse'] # get 'pulse' section from JSON

if __name__ == '__main__':
	'''
	Program entry point.
	'''

	timestamp = None

	# help
	if len(sys.argv) > 1 and sys.argv[1] == 'help':
		print(USAGE)
		sys.exit(0)

	# get timestamp from CLI
	elif len(sys.argv) > 1:
		timestamp = sys.argv[1]

	# attempt to get pulse
	try:
		pulse = get_pulse(timestamp)
		print(pulse['timeStamp'])
		print(pulse['outputValue'])
	
	# failed to get pulse
	except:
		print(USAGE, file=sys.stderr)
		sys.exit(1)
