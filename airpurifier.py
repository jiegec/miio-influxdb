# usage: python3 airpurifier.py IP TOKEN
# dependency: python-miio

import miio
import sys
import time

airpurifier = miio.airpurifier.AirPurifier(sys.argv[1], sys.argv[2])

status = airpurifier.status()
data = status.data
def print_data(key):
    print('miio,device=airpurifier,ip={} {}={} {}'.format(sys.argv[1], key, data[key], time.time_ns()))

print_data('aqi')
print_data('f1_hour')
print_data('f1_hour_used')
print_data('filter1_life')
print_data('humidity')
print_data('purify_volume')
print_data('sleep_time')
print_data('temp_dec')
print_data('use_time')
