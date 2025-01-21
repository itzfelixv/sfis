# SingularityFinance Script
# Github: https://github.com/ddatnee/sfis

from web3 import Web3
import requests, json, argparse, time, logging
from typing import Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

class SFI:
	def __init__(self, private_key: str) -> None:
		"""
		Initializes the SFI class with Web3 instances and contract details.
		"""
		self.SFI_RPC_URL = "https://rpc-testnet.singularityfinance.ai"
		self.SEPOLIA_RPC_URL = "https://ethereum-sepolia-rpc.publicnode.com"
		self.GELATO_API = "https://api.gelato.digital/raas/public/bridge/transactions"

		self.sfi_web3 = Web3(Web3.HTTPProvider(self.SFI_RPC_URL))
		self.sep_web3 = Web3(Web3.HTTPProvider(self.SEPOLIA_RPC_URL))

		if not (self.sfi_web3.is_connected() and self.sep_web3.is_connected()):
			raise ConnectionError("Couldn't connect to Web3 RPC. Try again later.")
		
		self.pk = private_key
		self.address = self.sep_web3.eth.account.from_key(self.pk).address

		self.contracts = {
			'sep': {},
			'sfi': {
				'wsfi': {
					'ca': '0x6dC404EFd04B880B0Ab5a26eF461b63A12E3888D',
					'abi': [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"allowance","type":"uint256"},{"internalType":"uint256","name":"needed","type":"uint256"}],"name":"ERC20InsufficientAllowance","type":"error"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"uint256","name":"balance","type":"uint256"},{"internalType":"uint256","name":"needed","type":"uint256"}],"name":"ERC20InsufficientBalance","type":"error"},{"inputs":[{"internalType":"address","name":"approver","type":"address"}],"name":"ERC20InvalidApprover","type":"error"},{"inputs":[{"internalType":"address","name":"receiver","type":"address"}],"name":"ERC20InvalidReceiver","type":"error"},{"inputs":[{"internalType":"address","name":"sender","type":"address"}],"name":"ERC20InvalidSender","type":"error"},{"inputs":[{"internalType":"address","name":"spender","type":"address"}],"name":"ERC20InvalidSpender","type":"error"},{"inputs":[],"name":"WithdrawFailed","type":"error"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"owner","type":"address"},{"indexed":True,"internalType":"address","name":"spender","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"dst","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"src","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Withdrawal","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"deposit","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]
				},
				'stake': {
					'ca': '0x22Dbdc9e8dd7C5E409B014BBcb53a3ef39736515',
					'abi': [{"inputs":[{"internalType":"address","name":"target","type":"address"}],"name":"AddressEmptyCode","type":"error"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"AddressInsufficientBalance","type":"error"},{"inputs":[],"name":"AlreadyInitialized","type":"error"},{"inputs":[],"name":"AlreadyInitializedOwner","type":"error"},{"inputs":[],"name":"CallerIsNotOwner","type":"error"},{"inputs":[],"name":"DepositTokenRecoveryNotAllowed","type":"error"},{"inputs":[],"name":"DepositsDisabled","type":"error"},{"inputs":[{"internalType":"uint256","name":"fee","type":"uint256"},{"internalType":"uint256","name":"maxFee","type":"uint256"}],"name":"ExceedsMaxEarlyUnlockFeePerDay","type":"error"},{"inputs":[{"internalType":"uint256","name":"period","type":"uint256"},{"internalType":"uint256","name":"maxPeriod","type":"uint256"}],"name":"ExceedsMaxLockingPeriod","type":"error"},{"inputs":[],"name":"FailedInnerCall","type":"error"},{"inputs":[],"name":"MissingAmount","type":"error"},{"inputs":[],"name":"MissingDepositToken","type":"error"},{"inputs":[],"name":"MissingOwner","type":"error"},{"inputs":[],"name":"MissingRewardsAPI","type":"error"},{"inputs":[],"name":"MissingToken","type":"error"},{"inputs":[],"name":"MissingZapperContract","type":"error"},{"inputs":[],"name":"ReentrancyGuardReentrantCall","type":"error"},{"inputs":[{"internalType":"uint256","name":"requestedUnlockDate","type":"uint256"},{"internalType":"uint256","name":"currentUnlockDate","type":"uint256"}],"name":"RequestedUnlockDateBeforeCurrent","type":"error"},{"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"SafeERC20FailedOperation","type":"error"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"zapper","type":"address"}],"name":"SenderIsNotZapper","type":"error"},{"inputs":[{"internalType":"uint256","name":"requestedWithdrawal","type":"uint256"},{"internalType":"uint256","name":"currentBalance","type":"uint256"}],"name":"WithdrawalRequestExceedsDeposited","type":"error"},{"inputs":[],"name":"ZeroMaxEarlyUnlockFeePerDay","type":"error"},{"inputs":[],"name":"ZeroMaxLockingPeriodInDays","type":"error"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"user","type":"address"},{"indexed":False,"internalType":"uint256","name":"claimed","type":"uint256"}],"name":"Claimed","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"newInstance","type":"address"}],"name":"Cloned","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"admin","type":"address"},{"indexed":False,"internalType":"uint256","name":"fees","type":"uint256"}],"name":"CollectedFees","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"user","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"lockingPeriod","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":True,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"user","type":"address"},{"indexed":False,"internalType":"uint256","name":"fee","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"secondsUntilUnlock","type":"uint256"}],"name":"PaidEarlyUnlockFee","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"admin","type":"address"},{"indexed":False,"internalType":"bool","name":"depositsEnabled","type":"bool"}],"name":"SetDepositsEnabled","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"admin","type":"address"},{"indexed":False,"internalType":"uint256","name":"earlyUnlockFeePerDay","type":"uint256"}],"name":"SetEarlyUnlockFeePerDay","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"admin","type":"address"},{"indexed":False,"internalType":"address","name":"zapperContract","type":"address"}],"name":"SetZapperContract","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"user","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Withdraw","type":"event"},{"inputs":[],"name":"MAX_EARLY_UNLOCK_FEE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MAX_EARLY_UNLOCK_FEE_PER_DAY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MAX_LOCKING_PERIOD","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MAX_PERCENTAGE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"claim","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"clone","outputs":[{"internalType":"address","name":"newInstance","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"collectFees","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint256","name":"_lockingPeriod","type":"uint256"}],"name":"deposit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_recipient","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint256","name":"_lockingPeriod","type":"uint256"}],"name":"depositFor","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"depositToken","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"depositsEnabled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"earlyUnlockFeePerDay","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"earlyUnlockFees","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getClone","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_depositToken","type":"address"},{"internalType":"address","name":"_rewardsAPI","type":"address"},{"internalType":"uint256","name":"maxLockingPeriodInDays","type":"uint256"},{"internalType":"uint256","name":"maxEarlyUnlockFeePerDay","type":"uint256"}],"name":"initialize","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pending","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"pendingFor","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"to","type":"address"}],"name":"recoverUnsupportedTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"rewardToken","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"rewardsAPI","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bool","name":"_depositsEnabled","type":"bool"}],"name":"setDepositsEnabled","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_earlyUnlockFeePerDay","type":"uint256"}],"name":"setEarlyUnlockFeePerDay","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"initialOwner","type":"address"}],"name":"setOwnerAfterClone","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_zapperContract","type":"address"}],"name":"setZapperContract","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"totalScore","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"userInfo","outputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"lockDate","type":"uint256"},{"internalType":"uint256","name":"unlockDate","type":"uint256"},{"internalType":"uint256","name":"score","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdrawAndClaim","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"zapperContract","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}]
				},
				'msgpasser': {
					'ca': '0x4200000000000000000000000000000000000016',
					'abi': [{"anonymous":False,"inputs":[{"indexed":True,"internalType":"uint256","name":"nonce","type":"uint256"},{"indexed":True,"internalType":"address","name":"sender","type":"address"},{"indexed":True,"internalType":"address","name":"target","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"gasLimit","type":"uint256"},{"indexed":False,"internalType":"bytes","name":"data","type":"bytes"},{"indexed":False,"internalType":"bytes32","name":"withdrawalHash","type":"bytes32"}],"name":"MessagePassed","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"WithdrawerBalanceBurnt","type":"event"},{"inputs":[],"name":"MESSAGE_VERSION","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_target","type":"address"},{"internalType":"uint256","name":"_gasLimit","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"initiateWithdrawal","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"messageNonce","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"sentMessages","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]
				}
			}
		}

	def _getContract(self, _type: str, key: str = "sfi"):
		"""
		Retrieves a contract instance.
		"""
		try:
			contract_info = self.contracts[key][_type]
			method_name = getattr(self, f"{key}_web3", None)
			if not method_name:
				logger.error(f"Method {method_name} not found or not callable.")
				raise
			else:
				return method_name.eth.contract(address=contract_info['ca'], abi=contract_info['abi'])

		except:
			logger.error(f"Contract not defined.")
			raise

	def _executeTransaction(self, transaction: dict, key: str = "sfi") -> dict:
		try:
			method_name = getattr(self, f"{key}_web3", None)
			if not method_name:
				logger.error(f"Method {method_name} not found or not callable.")
				raise
			else:
				signed_tx = method_name.eth.account.sign_transaction(transaction, private_key=self.pk)
				tx_hash = method_name.eth.send_raw_transaction(signed_tx.raw_transaction)
				tx_receipt = method_name.eth.wait_for_transaction_receipt(tx_hash)

				if tx_receipt.status == 1:
					logger.info(f"Transaction successful: {tx_hash.hex()}")
					return {'status': 'success', 'tx': tx_hash.hex()}
				else:
					logger.error("Transaction failed.")
					return {'status': 'failed'}

		except Exception as e:
			logger.error(f"Transaction error: {str(e)}")
			return {'status': 'failed', 'error': str(e)}

	def _userInfo(self) -> list:
		stakeContract = self._getContract("stake")
		return stakeContract.functions.userInfo(self.address).call()

	def _lockPeriod(self) -> int:
		inf = self._userInfo()
		return int(inf[2] - inf[1])

	def approveStake(self, _amount: int = 999_999_999 * (10**18)) -> dict:
		"""
		Approves staking a specific amount of tokens. (Default: 999.999.999)
		"""
		try:
			contract = self._getContract('wsfi')
			nonce = self.sfi_web3.eth.get_transaction_count(self.address)

			tx = contract.functions.approve(self.contracts['sfi']['stake']['ca'], _amount).build_transaction({
				'chainId': self.sfi_web3.eth.chain_id,
				'from': self.address,
				'nonce': nonce
			})

			return self._executeTransaction(tx)

		except Exception as e:
			logger.error(f"Error during approve: {str(e)}")
			return {'status': 'failed', 'error': str(e)}

	def stake(self, _amount: int) -> dict:
		"""
		Stakes a specified amount of tokens.
		"""
		
		try:
			logger.info(f"Approving staking amount: {_amount}")
			approval_result = self.approveStake(_amount)
			if approval_result['status'] != 'success':
				logger.error("Approval failed. Aborting staking process.")
				return {'status': 'failed', 'error': 'Approval failed'}
			time.sleep(5)


			contract = self._getContract('stake')
			nonce = self.sfi_web3.eth.get_transaction_count(self.address)
			
			_lockPeriod = self._lockPeriod()

			if _lockPeriod <= 0:
				logger.warning("Invalid lock period detected, setting to default (100 days).")
				_lockPeriod = 8640000 # 100 Days

			logger.info(f"Staking amount: {_amount}, Lock period: {_lockPeriod}, Nonce: {nonce}")

			tx = contract.functions.deposit(_amount, _lockPeriod).build_transaction({
					"chainId": self.sfi_web3.eth.chain_id, 
					"from": self.address, 
					"nonce": nonce
				})

			return self._executeTransaction(tx)

		except Exception as e:
			logger.error(f"Error during stake: {str(e)}")
			return {'status': 'failed', 'error': str(e)}
		
	def unstake(self, _amount: int) -> dict:
		"""
		Unstakes (withdraws and claims) a specified amount.
		"""
		try:
			contract = self._getContract('stake')
			nonce = self.sfi_web3.eth.get_transaction_count(self.address)

			tx = contract.functions.withdrawAndClaim(_amount).build_transaction({
					"chainId": self.sfi_web3.eth.chain_id, 
					"from": self.address, 
					"nonce": nonce
				})

			return self._executeTransaction(tx)

		except Exception as e:
			logger.error(f"Error during unstake: {str(e)}")
			return {'status': 'failed', 'error': str(e)}

	def wrap(self, _amount: int) -> dict:
		"""
		Wraps SFI tokens into wSFI.
		"""
		try:
			contract = self._getContract("wsfi")
			nonce = self.sfi_web3.eth.get_transaction_count(self.address)

			tx = contract.functions.deposit().build_transaction({
				"chainId": self.sfi_web3.eth.chain_id,
				"from": self.address,
				"nonce": nonce,
				"value": _amount
			})

			return self._executeTransaction(tx)

		except Exception as e:
			logger.error(f"Error during wrap: {str(e)}")
			return {'status': 'failed', 'error': str(e)}

	def unwrap(self, _amount: int) -> dict:
		"""
		Unwraps wSFI tokens into SFI.
		"""
		try:
			contract = self._getContract("wsfi")
			nonce = self.sfi_web3.eth.get_transaction_count(self.address)

			tx = contract.functions.withdraw(_amount).build_transaction({
				"chainId": self.sfi_web3.eth.chain_id,
				"from": self.address,
				"nonce": nonce
			})

			return self._executeTransaction(tx)

		except Exception as e:
			logger.error(f"Error during unwrap: {str(e)}")
			return {'status': 'failed', 'error': str(e)}

	def claim(self) -> dict:
		"""
		Claim SFI from stake.
		"""
		try:
			contract = self._getContract("stake")
			nonce = self.sfi_web3.eth.get_transaction_count(self.address)

			tx = contract.functions.claim().build_transaction({
				"chainId": self.sfi_web3.eth.chain_id,
				"from": self.address,
				"nonce": nonce
			})

			return self._executeTransaction(tx)

		except Exception as e:
			logger.error(f"Error during claim: {str(e)}")
			return {'status': 'failed', 'error': str(e)}

	def initWithdrawalOnchain(self, amount: int) -> dict:
		"""
		Initiates an on-chain withdrawal.
		"""
		try:
			contract = self._getContract('msgpasser')
			nonce = self.sfi_web3.eth.get_transaction_count(self.address)

			tx = contract.functions.initiateWithdrawal(
				self.address,
				amount,
				"0x"
			).build_transaction({
				"chainId": self.sfi_web3.eth.chain_id,
				"from": self.address,
				"nonce": nonce,
				"value": amount
			})

			return self._executeTransaction(tx)

		except Exception as e:
			logger.error(f"Error during initWithdrawalOnchain: {str(e)}")
			return {'status': 'failed', 'error': str(e)}

	def initWithdrawal(self, amount: int) -> dict:
		"""
		Initiates a withdrawal and calls the Gelato API to finish bridging SFI.
		"""
		try:
			onchain_result = self.initWithdrawalOnchain(amount)

			if onchain_result['status'] == 'failed':
				return {
					"status": "failed",
					"msg": "On-chain transaction failed."
				}

			tx_hash = onchain_result['tx']
			raw_tx = f"0x{self.sfi_web3.eth.get_raw_transaction(tx_hash).hex()}"
			ts = int(time.time())

			raw_json = {
				"direction": 1,
				"from": self.address,
				"to": self.address,
				"l1Token": "0x9a3f60032941C91cdeF5dBB58f2cE80e47e3ddCA",
				"l2Token": "0x9a3f60032941C91cdeF5dBB58f2cE80e47e3ddCA",
				"amount": str(amount),
				"data": "0x",
				"logIndex": 0,
				"blockNumber": 0,
				"transactionHash": tx_hash,
				"timestamp": ts,
				"messageStatus": 2,
				"button": True,
				"slug": "singularity-finance-testnet",
				"isWithdraw": True,
				"rawTx": raw_tx
			}

			logger.info("Calling Gelato API to finish...")

			response = requests.post(self.GELATO_API, json=raw_json)
			resp_json = response.json()

			logger.info(resp_json)

			if response.status_code == 200:
				
				return {
					"status": "success",
					"msg": resp_json
				}
			else:
				return {
					"status": "failed",
					"msg": f"Gelato API error: {response.text}"
				}

		except Exception as e:
			logger.error(f"Error during initWithdrawal: {str(e)}")
			return {
				"status": "failed",
				"msg": str(e)
			}

def executeOperation(operation, amount: int, times: int) -> None:
    """
    Executes a given operation a specified number of successful times.

    Args:
        operation (callable): The operation to execute.
        amount (int): The amount to process.
        times (int): The number of successful executions required.
    """
    successful_runs = 0

    while successful_runs < times:
        logger.info(f"Attempt {successful_runs + 1}/{times}: Executing operation.")
        try:
            result = operation(amount) if amount is not None else operation()
            if result['status'] == 'success':
                successful_runs += 1
                logger.info(f"Attempt {successful_runs}/{times}: Operation successful.")
            else:
                logger.warning(f"Attempt {successful_runs + 1}/{times}: Operation failed, trying again...")
        except Exception as e:
            logger.error(f"Attempt {successful_runs + 1}/{times}: Error occurred during operation: {str(e)}")
        
        time.sleep(5) 


def run(pk: str, config: Dict[str, int]) -> None:
	"""
	Executes the main workflow based on the given configuration.

	Args:
		pk (str): Private key for the wallet.
		config (Dict[str, int]): Configuration with amounts for operations.
	"""
	if not config:
		logger.error("Invalid configuration provided.")
		return

	sfi = SFI(private_key=pk)
	logger.info(f"--- Address: {sfi.address} ---")

	operations = [
		(sfi.wrap, config.get("wrapAmount"), 2),
		(sfi.unwrap, config.get("unwrapAmount"), 2),
		(sfi.stake, config.get("stakeAmount"), 2),
		(sfi.unstake, config.get("unstakeAmount"), 1),
		(sfi.claim, None, 2),
		(sfi.initWithdrawal, config.get("bridgeAmount"), 5)
	]

	for operation, amount, max_attempts in operations:
		logger.info(f"Starting operation: {operation.__name__}")
		if amount is not None:
			executeOperation(operation, amount, max_attempts)
		else:
			executeOperation(operation, None, max_attempts)

	logger.info("--- Workflow completed ---")


def setup(auto: bool) -> None:
	try:
		if not auto:
			try:
				print("Welcome to the configuration setup!")
				print("This setup will guide you through the process of entering amounts for wrapping, unwrapping, staking, unstaking and bridging tokens.")

				wrapAmount = float(input("Enter your wrap amount > "))
				unwrapAmount = float(input("Enter your unwrap amount > "))
				stakeAmount = float(input("Enter your stake amount > "))
				unstakeAmount = float(input("Enter your unstake amount > "))
				bridgeAmount = float(input("Enter your bridge amount > "))
			except ValueError:
				print("Error: Please enter valid numeric values for the amounts.")
				return
		else:
			wrapAmount = 3
			unwrapAmount = 1
			stakeAmount = 1
			unstakeAmount = 1
			bridgeAmount = 0.2

		try:
			config = {
				"wrapAmount": int(wrapAmount * 10**18),
				"unwrapAmount": int(unwrapAmount * 10**18),
				"stakeAmount": int(stakeAmount * 10**18),
				"unstakeAmount": int(unstakeAmount * 10**18),
				"bridgeAmount": int(bridgeAmount * 10**18)
			}
		except Exception as e:
			print(f"Error converting amounts to Wei: {e}")
			return

		try:
			with open("config.json", "w") as f:
				json.dump(config, f, indent=4)
		except IOError as e:
			print(f"Error writing to config.json: {e}")
			return

		print("Setup complete. You can run the script now.")

	except Exception as e:
		print(f"An unexpected error occurred: {e}")


def main():
	parser = argparse.ArgumentParser(description='SingularityFinance Script v1', add_help=True)
	parser.add_argument("-i", "--init", action="store_true", help="setup the script")
	parser.add_argument("-a", "--auto", action="store_true", help="setup the script, using the pre-defined values")
	parser.add_argument("-pk", type=str, help="run with a specified private key")
	parser.add_argument("-f", "--file", type=str, help="read private keys from a file and run with each")

	args = parser.parse_args()

	config = None

	if args.init:
		setup(auto=args.auto)
	elif args.pk:
		try:
			with open("config.json", "r") as f:
				config = json.load(f)
		except FileNotFoundError:
			print("Config file 'config.json' not found.")
			return
		except json.JSONDecodeError:
			print("Error decoding JSON in 'config.json'.")
			return
		run(args.pk, config)
	elif args.file:
		try:
			with open("config.json", "r") as f:
				config = json.load(f)
		except FileNotFoundError:
			print("Config file 'config.json' not found.")
			return
		except json.JSONDecodeError:
			print("Error decoding JSON in 'config.json'.")
			return
		# Read private keys from file
		with open(args.file, "r") as f:
			private_keys = f.readlines()

		for pk in private_keys:
			run(pk.strip(), config)
	else:
		print("Invalid arguments. Use -h or --help for usage information.")

if __name__ == "__main__":
	main()