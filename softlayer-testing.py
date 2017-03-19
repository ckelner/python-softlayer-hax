# Script to hack against SoftLayer
# Init: 2017/03/19
# Author: Chris Kelner
#

import SoftLayer
import argparse
import json

class SoftlayerHax:
    def __init__(self, user, key):
        self.client = SoftLayer.Client(username=user, api_key=key)
        self.LB = SoftLayer.LoadBalancerManager(self.client)

    def getRoutingMethods(self):
        print self.LB.get_routing_methods()

# Entry
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='usage: python softlayer-testing.py -user <SL_USER_ID> -api_key <SL_API_KEY>')
    parser.add_argument('-user', help='Your SL user ID', required=True)
    parser.add_argument('-api_key', help='Your SL API Key', required=True)
    args = parser.parse_args()
    sl = SoftlayerHax(args.user, args.api_key)
    sl.getRoutingMethods()
