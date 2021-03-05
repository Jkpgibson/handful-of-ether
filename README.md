# handful-of-ether

TODOs

- Write web3.py app to sync with an ethereum node
- Use it to analyze data in similar fashion to this paper (https://cseweb.ucsd.edu/~smeiklejohn/files/imc13.pdf)
- Organize the data so we can make conclusions from it
- ? ? ?
- Profit

## Parser
- 

## 


## Go-Ethereum Setup 

In WSL:
```shell
sudo add-apt-repository -y ppa:ethereum/ethereum

sudo apt-get update
sudo apt-get install ethereum
```

After installing, use the following command to sync with the network with full mode.
```shell
geth --datadir /mnt/{your storage address} --syncmode full --cache 1024 --nousb --ipcpath "~/geth-ipc"
```

Use `geth attach ~/geth-ipc` to open the js console.
