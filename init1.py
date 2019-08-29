import os
os.system("nodeos -e -p eosio --plugin eosio::producer_plugin --plugin eosio::chain_api_plugin --plugin eosio::http_plugin --access-control-allow-origin='*' --contracts-console --http-validate-host=false --verbose-http-errors >> nodeos.log 2>&1 &")

wallet = "docker_eos_default"
fileNamePwd = "pwd_" + wallet

#read password
file = open(fileNamePwd, "r")
password = str(file.read())
print(password)

#unlock wallet
cmdWalletUnlock = "cleos wallet unlock -n " + wallet + " --password " + password
print("CMD: ", cmdWalletUnlock)
os.system(cmdWalletUnlock)

#create key
accountName = "bob"
fileNameKey = "key_" + accountName

# import private key
file = open(fileNameKey, "r")
content = str(file.read())
strArr = content.split()
privateKey = strArr[2]

# print("Start nodeos")
# os.system("nodeos -e -p eosio --plugin eosio::producer_plugin --plugin eosio::chain_api_plugin --plugin eosio::http_plugin --access-control-allow-origin='*' --contracts-console --http-validate-host=false --verbose-http-errors >> nodeos.log 2>&1 &")
os.system("curl http://localhost:8888/v1/chain/get_info")

#create account
publicKey = strArr[5]
nameArr = ["bob", "alice", "ken", "jane", "han", "amy", "jimmy", "betty", "tom", "emily", "ed", "mia"]
for n in nameArr:
    cmdCreateAccount = "cleos create account eosio " + n + " " + publicKey
    print("CMD: ", cmdCreateAccount)
    os.system(cmdCreateAccount)


# Test: get Account
cmdGetAccount = "cleos get account " + nameArr[0]
print("CMD: ", cmdGetAccount)
os.system(cmdGetAccount)

# deploy hello.cpp contract
os.system("")