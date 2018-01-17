#############################################################
# Pratyush Raunak					    #
# Python Automation
# pip  install facebook-sdk
# sudo apt-get install python-virtualenv - To setup virtualenv
# virtualenv facebookenv
# source facebookenv/bin/activate
#
#							    #									
#############################################################


import facebook #import facebook-sdk
import urllib3 #not necessary if using facebook-sdk
import requests #neede to request graph-API




token = 'EAACEdEose0cBAGZC8NN05mBuLohfABLPBeNPiYBLKRHpShkY03KYHAgmUNxjZA106ZCqRcPPS2MoYXh0SdGIbfnkvhro5ByTeSDQIcEkkBLZAMDcZBTH6PFGIIe3W67OlfqkBo5rPZA6lLBKEHfNxNTZBE4MZC3dB7Rs0qmWkNbZAgE9GsGoFKd0r30lOFGhlPZB6btqF67iKXwgZDZD'  #Facebook API-token https://developers.facebook.com/tools/explorer 

graph = facebook.GraphAPI(token)
#profile = graph.get_object("me")
#friends = graph.get_connections("me", "friends")
#args = {fields  = 'birthday,name,id,education'}
fb = graph.request("me/friends?fields=id,name,birthday,education")
#print friends
#friend_list1 = [friend['name'] for friend in friends['data']]
for row in fb:
	print row
#print friend_list1
#print friend_list2
#print friend_list3


