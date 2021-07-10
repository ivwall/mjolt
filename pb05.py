# pip3 install python-bitcoinrpc

from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from pprint import pprint

import json
import decimal
import time

from decimal import Decimal
class DecimalEncoder (json.JSONEncoder):
    def default (self, obj):
       if isinstance (obj, Decimal):
       #if instance (obj, Decimal):
           return int (obj)
       return json.JSONEncoder.default (self, obj)

def transaction (tx):
	print("....  process tx ......")
	print(type(tx))	
	print("....  process tx ......")

# rpc_user and rpc_password are set in the bitcoin.conf file
rpc_user = "bitcoin"
rpc_pass = "abc1234" 
#rpc_host = "10.10.89.92" # if running locally then 127.0.0.1
rpc_host = "10.0.2.15" # if running locally then 127.0.0.1
rpc_client = AuthServiceProxy(f"http://{rpc_user}:{rpc_pass}@{rpc_host}:8332", timeout=240)

print("getblockcount")
result = rpc_client.getblockcount()
#result = "206457"
result = "92938"
pprint(result)
print(result)
print()

print("getblockchaininfo)")
result = rpc_client.getblockchaininfo()
pprint(result)
print(result)
print()

print("getblockhash(1)")
blkhash = rpc_client.getblockhash(1)
pprint(blkhash)
print(blkhash)
print()

print("getblock")
block = rpc_client.getblock(blkhash)
pprint(block)
print(block)
print()

print("getblock 2")
block = rpc_client.getblock(blkhash,2)
pprint(block)
#print(block)
print()

print(type(block))

print (json.dumps (block, cls = DecimalEncoder))
print()
print()
print("weight {}".format(block["weight"]))
print("nextblock {}".format(block["nextblockhash"]))
print("nTx {}".format(block["nTx"]))
nTx = block["nTx"]
print(type(nTx))
print("tx {}".format(block["tx"]))

nextBlockHash = block["nextblockhash"]

print(nextBlockHash)

nextHashBlock = True
while nextHashBlock:
	block = rpc_client.getblock( nextBlockHash, 2 )
	pprint (json.dumps (block, cls = DecimalEncoder))
	print()
	print("nTx {}".format(block["nTx"]))
	print("tx {}".format(block["tx"]))
	print()
	nextBlockHash = block["nextblockhash"]
	print()
	print()
	nTx = block["nTx"] 
	one = 1
	if nTx > one:
		transaction (block["tx"])
		time.sleep(10)
	else:
		time.sleep(0.5)






