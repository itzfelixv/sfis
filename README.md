# SingularityFinance Script
## Overview

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

Setup complete. You can run the script now.
```

Alternatively, if you wish to use pre-defined values (for example, from a previous configuration or an example setup), you can initialize with the -a flag:
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
For any questions or support, feel free to reach out at [itzfelixv@gmail.com](mailto:itzfelixv@gmail.com).
