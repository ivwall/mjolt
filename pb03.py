# pip3 install python-bitcoinrpc

from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from pprint import pprint

# rpc_user and rpc_password are set in the bitcoin.conf file
rpc_user = "bitcoin"
rpc_pass = "abc1234" 
rpc_host = "10.10.89.92" # if running locally then 127.0.0.1
rpc_client = AuthServiceProxy(f"http://{rpc_user}:{rpc_pass}@{rpc_host}:8332", timeout=240)

print("getblockcount")
result = rpc_client.getblockcount()
pprint(result)
print(result)
print()

print("getblockchaininfo)")
result = rpc_client.getblockchaininfo()
pprint(result)
print(result)
print()

print("getblockhash(92938)")
blkhash = rpc_client.getblockhash(92938)
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
print(block)
print()
