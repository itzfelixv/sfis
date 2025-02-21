# SingularityFinance Script
## Overview
SingularityFinance Script (SFIS) is designed for interacting with testnets in order to participate in airdrop events. This script automates essential tasks like token wrapping, unwrapping, staking, unstaking, and bridging, allowing you to efficiently manage your testnet assets and increase your chances of qualifying for airdrops. By running the script, you can perform routine actions required by various projects on supported testnets, and potentially earn rewards in the form of airdrops.
## Installation
### 1. Clone the Repository
```bash
git clone https://github.com/ddatnee/sfis.git
cd sfis
```

### 2. Install Python Dependencies
Make sure you have pip installed, then install the required Python libraries from the requirements.txt file:
```bash
pip install -r requirements.txt
```

### 3. Configure the Script
To initialize the configuration, run the following command:
```bash
python3 sfis.py -i
```

```bash
Welcome to the configuration setup!
This setup will guide you through the process of entering amounts for wrapping, unwrapping, staking, unstaking and bridging tokens.

Enter your wrap amount > 
Enter your unwrap amount > 
Enter your stake amount > 
Enter your unstake amount > 
Enter your bridge amount > 
Selecting default primary token: wsfi
Select the secondary token (aimm/usdc) >
Enter swap amount for wsfi -> aimm >
Enter liquidity amount for wsfi -> aimm >
Enter slippage for wsfi -> aimm (Eg. 2% = 0.02) > 
Enter percentage of liquidity to remove for wsfi -> aimm (Eg. 20% = 0.2) > 
Enter the travel destination address (Leaves empty to use default) >
Enter travel amount > 

Setup complete. You can run the script now.
```

Alternatively, if you wish to use pre-defined values, you can initialize with the -a flag:
```bash
python3 sfis.py -i -a
```

```bash
Setup complete. You can run the script now.
```

### 4.Run the Script
Once the configuration is set up, you can run the script with your private key or a private key file:
- **Using your private key directly:**
```bash
python3 sfis.py -pk <your-private-key>
```

- **Using a private key file:**
```bash
python3 sfis.py -f <path-to-private-key-file>
```
## Important Notes
- **Daily Tasks**: The script will perform daily operations, such as (un)staking, (un)wrapping, swapping and bridging tokens.
- **Bridging Task**: ~~The bridging task requires waiting for Layer 1 (L1) confirmation. After running the script for the first time, please allow for a 1-hour wait before re-running the script with the `-P` and `-F` flags to prove and finalize the bridging process.~~ Disabled.
```bash
python3 sfis.py ... -P
```
```bash
python3 sfis.py ... -F
```

## Contributing
We welcome contributions to enhance the functionality of this script! If you have ideas for new features or improvements, feel free to fork the repository and submit a pull request.
To Contribute:
1. Fork the repository.
2. Create a new branch for your changes.
3. Write tests to verify your changes.
4. Submit a pull request with a description of your changes.

## License
This project is licensed under the CC BY-NC 4.0 License. See the [LICENSE](LICENSE) file for more details.

## Contact
For any questions or support, feel free to reach out at [itz.felixv@gmail.com](mailto:itz.felixv@gmail.com).
