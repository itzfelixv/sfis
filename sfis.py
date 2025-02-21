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
		self.CRYMBO_API = "https://oracle-partners.crymbo.io/"

		self.sfi_web3 = Web3(Web3.HTTPProvider(self.SFI_RPC_URL))
		self.sep_web3 = Web3(Web3.HTTPProvider(self.SEPOLIA_RPC_URL))

		if not (self.sfi_web3.is_connected() and self.sep_web3.is_connected()):
			raise ConnectionError("Couldn't connect to Web3 RPC. Try again later.")
		
		self.pk = private_key
		self.address = self.sep_web3.eth.account.from_key(self.pk).address

		self.contracts = {
			'sep': {
				'portal': {
					'ca': '0x776CF4e50c7285810e4E25A79de56aA4E7116876',
					'abi': [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"BadTarget","type":"error"},{"inputs":[],"name":"CallPaused","type":"error"},{"inputs":[],"name":"ContentLengthMismatch","type":"error"},{"inputs":[],"name":"EmptyItem","type":"error"},{"inputs":[],"name":"GasEstimation","type":"error"},{"inputs":[],"name":"InvalidDataRemainder","type":"error"},{"inputs":[],"name":"InvalidHeader","type":"error"},{"inputs":[],"name":"LargeCalldata","type":"error"},{"inputs":[],"name":"NoValue","type":"error"},{"inputs":[],"name":"NonReentrant","type":"error"},{"inputs":[],"name":"OnlyCustomGasToken","type":"error"},{"inputs":[],"name":"OutOfGas","type":"error"},{"inputs":[],"name":"SmallGasLimit","type":"error"},{"inputs":[],"name":"TransferFailed","type":"error"},{"inputs":[],"name":"Unauthorized","type":"error"},{"inputs":[],"name":"UnexpectedList","type":"error"},{"inputs":[],"name":"UnexpectedString","type":"error"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":True,"internalType":"uint256","name":"version","type":"uint256"},{"indexed":False,"internalType":"bytes","name":"opaqueData","type":"bytes"}],"name":"TransactionDeposited","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"bytes32","name":"withdrawalHash","type":"bytes32"},{"indexed":False,"internalType":"bool","name":"success","type":"bool"}],"name":"WithdrawalFinalized","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"bytes32","name":"withdrawalHash","type":"bytes32"},{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"}],"name":"WithdrawalProven","type":"event"},{"inputs":[],"name":"balance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_mint","type":"uint256"},{"internalType":"uint256","name":"_value","type":"uint256"},{"internalType":"uint64","name":"_gasLimit","type":"uint64"},{"internalType":"bool","name":"_isCreation","type":"bool"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"depositERC20Transaction","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"},{"internalType":"uint64","name":"_gasLimit","type":"uint64"},{"internalType":"bool","name":"_isCreation","type":"bool"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"depositTransaction","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"donateETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"target","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"gasLimit","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"internalType":"struct Types.WithdrawalTransaction","name":"_tx","type":"tuple"}],"name":"finalizeWithdrawalTransaction","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"finalizedWithdrawals","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"guardian","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract L2OutputOracle","name":"_l2Oracle","type":"address"},{"internalType":"contract SystemConfig","name":"_systemConfig","type":"address"},{"internalType":"contract SuperchainConfig","name":"_superchainConfig","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_l2OutputIndex","type":"uint256"}],"name":"isOutputFinalized","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"l2Oracle","outputs":[{"internalType":"contract L2OutputOracle","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"l2Sender","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint64","name":"_byteCount","type":"uint64"}],"name":"minimumGasLimit","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"params","outputs":[{"internalType":"uint128","name":"prevBaseFee","type":"uint128"},{"internalType":"uint64","name":"prevBoughtGas","type":"uint64"},{"internalType":"uint64","name":"prevBlockNum","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"paused_","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"target","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"gasLimit","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"internalType":"struct Types.WithdrawalTransaction","name":"_tx","type":"tuple"},{"internalType":"uint256","name":"_l2OutputIndex","type":"uint256"},{"components":[{"internalType":"bytes32","name":"version","type":"bytes32"},{"internalType":"bytes32","name":"stateRoot","type":"bytes32"},{"internalType":"bytes32","name":"messagePasserStorageRoot","type":"bytes32"},{"internalType":"bytes32","name":"latestBlockhash","type":"bytes32"}],"internalType":"struct Types.OutputRootProof","name":"_outputRootProof","type":"tuple"},{"internalType":"bytes[]","name":"_withdrawalProof","type":"bytes[]"}],"name":"proveWithdrawalTransaction","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"provenWithdrawals","outputs":[{"internalType":"bytes32","name":"outputRoot","type":"bytes32"},{"internalType":"uint128","name":"timestamp","type":"uint128"},{"internalType":"uint128","name":"l2OutputIndex","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"uint8","name":"_decimals","type":"uint8"},{"internalType":"bytes32","name":"_name","type":"bytes32"},{"internalType":"bytes32","name":"_symbol","type":"bytes32"}],"name":"setGasPayingToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"superchainConfig","outputs":[{"internalType":"contract SuperchainConfig","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"systemConfig","outputs":[{"internalType":"contract SystemConfig","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"pure","type":"function"},{"stateMutability":"payable","type":"receive"}]
				},
				'oracle': {
					'ca': '0x1c56f18D964CB77743c1f6E57AcA0D9e783aDcfc',
					'abi': [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"bytes32","name":"outputRoot","type":"bytes32"},{"indexed":True,"internalType":"uint256","name":"l2OutputIndex","type":"uint256"},{"indexed":True,"internalType":"uint256","name":"l2BlockNumber","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"l1Timestamp","type":"uint256"}],"name":"OutputProposed","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"uint256","name":"prevNextOutputIndex","type":"uint256"},{"indexed":True,"internalType":"uint256","name":"newNextOutputIndex","type":"uint256"}],"name":"OutputsDeleted","type":"event"},{"inputs":[],"name":"CHALLENGER","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"FINALIZATION_PERIOD_SECONDS","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"L2_BLOCK_TIME","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PROPOSER","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"SUBMISSION_INTERVAL","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"challenger","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_l2BlockNumber","type":"uint256"}],"name":"computeL2Timestamp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_l2OutputIndex","type":"uint256"}],"name":"deleteL2Outputs","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"finalizationPeriodSeconds","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_l2OutputIndex","type":"uint256"}],"name":"getL2Output","outputs":[{"components":[{"internalType":"bytes32","name":"outputRoot","type":"bytes32"},{"internalType":"uint128","name":"timestamp","type":"uint128"},{"internalType":"uint128","name":"l2BlockNumber","type":"uint128"}],"internalType":"struct Types.OutputProposal","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_l2BlockNumber","type":"uint256"}],"name":"getL2OutputAfter","outputs":[{"components":[{"internalType":"bytes32","name":"outputRoot","type":"bytes32"},{"internalType":"uint128","name":"timestamp","type":"uint128"},{"internalType":"uint128","name":"l2BlockNumber","type":"uint128"}],"internalType":"struct Types.OutputProposal","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_l2BlockNumber","type":"uint256"}],"name":"getL2OutputIndexAfter","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_submissionInterval","type":"uint256"},{"internalType":"uint256","name":"_l2BlockTime","type":"uint256"},{"internalType":"uint256","name":"_startingBlockNumber","type":"uint256"},{"internalType":"uint256","name":"_startingTimestamp","type":"uint256"},{"internalType":"address","name":"_proposer","type":"address"},{"internalType":"address","name":"_challenger","type":"address"},{"internalType":"uint256","name":"_finalizationPeriodSeconds","type":"uint256"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"l2BlockTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestBlockNumber","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestOutputIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"nextBlockNumber","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"nextOutputIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"_outputRoot","type":"bytes32"},{"internalType":"uint256","name":"_l2BlockNumber","type":"uint256"},{"internalType":"bytes32","name":"_l1BlockHash","type":"bytes32"},{"internalType":"uint256","name":"_l1BlockNumber","type":"uint256"}],"name":"proposeL2Output","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"proposer","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"startingBlockNumber","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"startingTimestamp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"submissionInterval","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"}]
				}
			},
			'sfi': {
				# Tokens
				'wsfi': {
					'ca': '0x6dC404EFd04B880B0Ab5a26eF461b63A12E3888D',
					'abi': [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"allowance","type":"uint256"},{"internalType":"uint256","name":"needed","type":"uint256"}],"name":"ERC20InsufficientAllowance","type":"error"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"uint256","name":"balance","type":"uint256"},{"internalType":"uint256","name":"needed","type":"uint256"}],"name":"ERC20InsufficientBalance","type":"error"},{"inputs":[{"internalType":"address","name":"approver","type":"address"}],"name":"ERC20InvalidApprover","type":"error"},{"inputs":[{"internalType":"address","name":"receiver","type":"address"}],"name":"ERC20InvalidReceiver","type":"error"},{"inputs":[{"internalType":"address","name":"sender","type":"address"}],"name":"ERC20InvalidSender","type":"error"},{"inputs":[{"internalType":"address","name":"spender","type":"address"}],"name":"ERC20InvalidSpender","type":"error"},{"inputs":[],"name":"WithdrawFailed","type":"error"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"owner","type":"address"},{"indexed":True,"internalType":"address","name":"spender","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"dst","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"src","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Withdrawal","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"deposit","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]
				},
				'aimm': {
					'ca': '0xAa4aFA7C07405992e3f6799dCC260D389687077a',
					'abi': [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"allowance","type":"uint256"},{"internalType":"uint256","name":"needed","type":"uint256"}],"name":"ERC20InsufficientAllowance","type":"error"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"uint256","name":"balance","type":"uint256"},{"internalType":"uint256","name":"needed","type":"uint256"}],"name":"ERC20InsufficientBalance","type":"error"},{"inputs":[{"internalType":"address","name":"approver","type":"address"}],"name":"ERC20InvalidApprover","type":"error"},{"inputs":[{"internalType":"address","name":"receiver","type":"address"}],"name":"ERC20InvalidReceiver","type":"error"},{"inputs":[{"internalType":"address","name":"sender","type":"address"}],"name":"ERC20InvalidSender","type":"error"},{"inputs":[{"internalType":"address","name":"spender","type":"address"}],"name":"ERC20InvalidSpender","type":"error"},{"inputs":[],"name":"WithdrawFailed","type":"error"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"owner","type":"address"},{"indexed":True,"internalType":"address","name":"spender","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"dst","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"src","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Withdrawal","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"deposit","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}] 
				},
				'usdc': {
					'ca': '0xD2ED81BE83B33218737Ca188EB9AC28b79C6A0F3',
					'abi': [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"allowance","type":"uint256"},{"internalType":"uint256","name":"needed","type":"uint256"}],"name":"ERC20InsufficientAllowance","type":"error"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"uint256","name":"balance","type":"uint256"},{"internalType":"uint256","name":"needed","type":"uint256"}],"name":"ERC20InsufficientBalance","type":"error"},{"inputs":[{"internalType":"address","name":"approver","type":"address"}],"name":"ERC20InvalidApprover","type":"error"},{"inputs":[{"internalType":"address","name":"receiver","type":"address"}],"name":"ERC20InvalidReceiver","type":"error"},{"inputs":[{"internalType":"address","name":"sender","type":"address"}],"name":"ERC20InvalidSender","type":"error"},{"inputs":[{"internalType":"address","name":"spender","type":"address"}],"name":"ERC20InvalidSpender","type":"error"},{"inputs":[],"name":"WithdrawFailed","type":"error"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"owner","type":"address"},{"indexed":True,"internalType":"address","name":"spender","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"dst","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"src","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Withdrawal","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"deposit","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}] 
				},
				# Contracts
				'stake': {
					'ca': '0x22Dbdc9e8dd7C5E409B014BBcb53a3ef39736515',
					'abi': [{"inputs":[{"internalType":"address","name":"target","type":"address"}],"name":"AddressEmptyCode","type":"error"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"AddressInsufficientBalance","type":"error"},{"inputs":[],"name":"AlreadyInitialized","type":"error"},{"inputs":[],"name":"AlreadyInitializedOwner","type":"error"},{"inputs":[],"name":"CallerIsNotOwner","type":"error"},{"inputs":[],"name":"DepositTokenRecoveryNotAllowed","type":"error"},{"inputs":[],"name":"DepositsDisabled","type":"error"},{"inputs":[{"internalType":"uint256","name":"fee","type":"uint256"},{"internalType":"uint256","name":"maxFee","type":"uint256"}],"name":"ExceedsMaxEarlyUnlockFeePerDay","type":"error"},{"inputs":[{"internalType":"uint256","name":"period","type":"uint256"},{"internalType":"uint256","name":"maxPeriod","type":"uint256"}],"name":"ExceedsMaxLockingPeriod","type":"error"},{"inputs":[],"name":"FailedInnerCall","type":"error"},{"inputs":[],"name":"MissingAmount","type":"error"},{"inputs":[],"name":"MissingDepositToken","type":"error"},{"inputs":[],"name":"MissingOwner","type":"error"},{"inputs":[],"name":"MissingRewardsAPI","type":"error"},{"inputs":[],"name":"MissingToken","type":"error"},{"inputs":[],"name":"MissingZapperContract","type":"error"},{"inputs":[],"name":"ReentrancyGuardReentrantCall","type":"error"},{"inputs":[{"internalType":"uint256","name":"requestedUnlockDate","type":"uint256"},{"internalType":"uint256","name":"currentUnlockDate","type":"uint256"}],"name":"RequestedUnlockDateBeforeCurrent","type":"error"},{"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"SafeERC20FailedOperation","type":"error"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"zapper","type":"address"}],"name":"SenderIsNotZapper","type":"error"},{"inputs":[{"internalType":"uint256","name":"requestedWithdrawal","type":"uint256"},{"internalType":"uint256","name":"currentBalance","type":"uint256"}],"name":"WithdrawalRequestExceedsDeposited","type":"error"},{"inputs":[],"name":"ZeroMaxEarlyUnlockFeePerDay","type":"error"},{"inputs":[],"name":"ZeroMaxLockingPeriodInDays","type":"error"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"user","type":"address"},{"indexed":False,"internalType":"uint256","name":"claimed","type":"uint256"}],"name":"Claimed","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"newInstance","type":"address"}],"name":"Cloned","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"admin","type":"address"},{"indexed":False,"internalType":"uint256","name":"fees","type":"uint256"}],"name":"CollectedFees","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"user","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"lockingPeriod","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":True,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"user","type":"address"},{"indexed":False,"internalType":"uint256","name":"fee","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"secondsUntilUnlock","type":"uint256"}],"name":"PaidEarlyUnlockFee","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"admin","type":"address"},{"indexed":False,"internalType":"bool","name":"depositsEnabled","type":"bool"}],"name":"SetDepositsEnabled","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"admin","type":"address"},{"indexed":False,"internalType":"uint256","name":"earlyUnlockFeePerDay","type":"uint256"}],"name":"SetEarlyUnlockFeePerDay","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"admin","type":"address"},{"indexed":False,"internalType":"address","name":"zapperContract","type":"address"}],"name":"SetZapperContract","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"user","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Withdraw","type":"event"},{"inputs":[],"name":"MAX_EARLY_UNLOCK_FEE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MAX_EARLY_UNLOCK_FEE_PER_DAY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MAX_LOCKING_PERIOD","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MAX_PERCENTAGE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"claim","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"clone","outputs":[{"internalType":"address","name":"newInstance","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"collectFees","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint256","name":"_lockingPeriod","type":"uint256"}],"name":"deposit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_recipient","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint256","name":"_lockingPeriod","type":"uint256"}],"name":"depositFor","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"depositToken","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"depositsEnabled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"earlyUnlockFeePerDay","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"earlyUnlockFees","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getClone","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_depositToken","type":"address"},{"internalType":"address","name":"_rewardsAPI","type":"address"},{"internalType":"uint256","name":"maxLockingPeriodInDays","type":"uint256"},{"internalType":"uint256","name":"maxEarlyUnlockFeePerDay","type":"uint256"}],"name":"initialize","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pending","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"pendingFor","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"to","type":"address"}],"name":"recoverUnsupportedTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"rewardToken","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"rewardsAPI","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bool","name":"_depositsEnabled","type":"bool"}],"name":"setDepositsEnabled","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_earlyUnlockFeePerDay","type":"uint256"}],"name":"setEarlyUnlockFeePerDay","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"initialOwner","type":"address"}],"name":"setOwnerAfterClone","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_zapperContract","type":"address"}],"name":"setZapperContract","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"totalScore","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"userInfo","outputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"lockDate","type":"uint256"},{"internalType":"uint256","name":"unlockDate","type":"uint256"},{"internalType":"uint256","name":"score","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdrawAndClaim","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"zapperContract","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}]
				},
				'msgpasser': {
					'ca': '0x4200000000000000000000000000000000000016',
					'abi': [{"anonymous":False,"inputs":[{"indexed":True,"internalType":"uint256","name":"nonce","type":"uint256"},{"indexed":True,"internalType":"address","name":"sender","type":"address"},{"indexed":True,"internalType":"address","name":"target","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"gasLimit","type":"uint256"},{"indexed":False,"internalType":"bytes","name":"data","type":"bytes"},{"indexed":False,"internalType":"bytes32","name":"withdrawalHash","type":"bytes32"}],"name":"MessagePassed","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"WithdrawerBalanceBurnt","type":"event"},{"inputs":[],"name":"MESSAGE_VERSION","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_target","type":"address"},{"internalType":"uint256","name":"_gasLimit","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"initiateWithdrawal","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"messageNonce","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"sentMessages","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]
				},
				'citeaRouter': {
					'ca': '0xFEccff0ecf1cAa1669A71C5E00b51B48E4CBc6A1',
					'abi': [{"inputs":[{"internalType":"address","name":"_factory","type":"address"},{"internalType":"address","name":"_WETH","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"WETH","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"amountADesired","type":"uint256"},{"internalType":"uint256","name":"amountBDesired","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountTokenDesired","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountIn","outputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountOut","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsIn","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsOut","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"reserveA","type":"uint256"},{"internalType":"uint256","name":"reserveB","type":"uint256"}],"name":"quote","outputs":[{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETHSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermit","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermitSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityWithPermit","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapETHForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETHSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]
				},
				'citeaFactory': {
					'ca': '0xd8388EECE67C003eF952D32c4E3943113C5f5608',
					'abi': [{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"token0","type":"address"},{"indexed":True,"internalType":"address","name":"token1","type":"address"},{"indexed":False,"internalType":"address","name":"pair","type":"address"},{"indexed":False,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"constant":True,"inputs":[],"name":"INIT_CODE_PAIR_HASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"}]
				}
			}
		}
	
	def _getContractAddress(self, key: str, network: str = "sfi") -> str:
		"""
		Retrieves a contract address.
		"""
		try:
			return self.contracts[network][key]['ca']
		except:
			logger.error(f"Contract not defined.")
			raise
	
	def _getContract(self, key: str, network: str = "sfi"):
		"""
		Retrieves a contract instance.
		"""
		try:
			contract_info = self.contracts[network][key]
			method_name = getattr(self, f"{network}_web3", None)
			if not method_name:
				logger.error(f"Method {method_name} not found or not callable.")
				raise
			else:
				return method_name.eth.contract(address=contract_info['ca'], abi=contract_info['abi'])

		except:
			logger.error(f"Contract not defined.")
			raise


	def _executeTransaction(self, transaction: dict, network: str = "sfi") -> dict:
		try:
			method_name = getattr(self, f"{network}_web3", None)
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

	def _getL2OutputIndexAfter(self, _l2BlockNumber: int) -> int:
		contract = self._getContract('oracle', 'sep')
		return contract.functions.getL2OutputIndexAfter(_l2BlockNumber).call()

	def _getL2Output(self, _l2OutputIndex: int) -> int:
		contract = self._getContract('oracle', 'sep')
		return contract.functions.getL2Output(_l2OutputIndex).call()

	def _isWithdrawalProven(self, _withdrawalHash: str | bytes) -> bool:
		contract = self._getContract('portal', 'sep')
		return contract.functions.provenWithdrawals(_withdrawalHash).call() != [b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 0, 0]
	
	def _isWithdrawalFinalized(self, _withdrawalHash: str | bytes) -> bool:
		contract = self._getContract('portal', 'sep')
		try:
			finalized = contract.functions.finalizedWithdrawals(_withdrawalHash).call()
			return finalized
		except:
			return False 
		
	def _getPairAddress(self, pair: list) -> str:
		contract = self._getContract('citeaFactory')
		return contract.functions.getPair(pair[0], pair[1]).call()

	def _getPairBalance(self, pair: list) -> int:
		address = self._getPairAddress(pair)
		contract = self.sfi_web3.eth.contract(address=address, abi=[{"constant":True,"inputs":[{"name":"account","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"}])
		return contract.functions.balanceOf(self.address).call()

	def _getPairSupply(self, pair: list) -> int:
		address = self._getPairAddress(pair)
		contract = self.sfi_web3.eth.contract(address=address, abi=[{"constant":True,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"}])
		return contract.functions.totalSupply().call()

	def _getPairReserves(self, pair: list) -> list:
		address = self._getPairAddress(pair)
		contract = self.sfi_web3.eth.contract(address=address, abi=[{"constant":True,"inputs":[],"name":"getReserves","outputs":[{"name":"_reserve0","type":"uint112"},{"name":"_reserve1","type":"uint112"},{"name":"_blockTimestampLast","type":"uint32"}],"payable":False,"stateMutability":"view","type":"function"}])
		return contract.functions.getReserves().call()

	def _getEventData(self, tx_hash: str) -> dict:
		receipt = self.sfi_web3.eth.get_transaction_receipt(tx_hash)
		event_abi = next((item for item in self.contracts["sfi"]["msgpasser"]['abi'] if item.get("type") == "event" and item.get("name") == "MessagePassed"), None)
		event_signature = self.sfi_web3.keccak(text="MessagePassed(uint256,address,address,uint256,uint256,bytes,bytes32)").hex()

		if event_abi:
			for log in receipt['logs']:
				if log["topics"][0].hex() == event_signature:
					indexed_inputs = [i for i in event_abi["inputs"] if i["indexed"]]
					decoded_topics = {}
					for i, topic in enumerate(log["topics"][1:], start=0):
						param = indexed_inputs[i]
						decoded_topics[param["name"]] = self.sfi_web3.codec.decode([param["type"]], bytes.fromhex(topic.hex()))[0]

					non_indexed_inputs = [i for i in event_abi["inputs"] if not i["indexed"]]
					non_indexed_types = [i["type"] for i in non_indexed_inputs]
					non_indexed_values = self.sfi_web3.codec.decode(
						non_indexed_types, bytes.fromhex(log["data"].hex())
					)
					decoded_data = {param["name"]: value for param, value in zip(non_indexed_inputs, non_indexed_values)}
	
					decoded_event = {**decoded_topics, **decoded_data}
					return decoded_event
		else:
			return {}
		
	def _getAmountsIn(self, _amountOut: int, path: list) -> list:
		contract = self._getContract('citeaRouter')
		return contract.functions.getAmountsIn(_amountOut, path).call()
	
	def _getAmountsOut(self, _amountIn: int, path: list) -> list:
		contract = self._getContract('citeaRouter')
		return contract.functions.getAmountsOut(_amountIn, path).call()

	def _convertKeyPair(self, pair: list) -> list:
		try:
			return [self._getContractAddress(token) for token in pair]
		except KeyError as e:
			print(f"Error: Token '{e.args[0]}' not found in self.tokens.")
			return []
		
	def approve(self, _token: str, _amount: int, _spender: str, network: str = "sfi", *args) -> dict:
		"""
		Approves spending a specific amount of tokens.
		If _token is a contract address, use web3.eth.contract with a provided ABI or a default ERC-20 ABI.
		"""
		try:
			web3 = getattr(self, f"{network}_web3", None)
			if not web3:
				logger.error(f"Web3 instance for network {network} not found.")
				return {'status': 'failed', 'error': 'Web3 instance not available'}
			
			# Check if _token is a known key or a contract address
			if _token in self.contracts[network]:
				contract = self._getContract(_token, network)
			else:
				# Use provided ABI if available, otherwise default ERC-20 ABI
				abi = args[0] if args else [
					{
						"constant": False,
						"inputs": [
							{"name": "spender", "type": "address"},
							{"name": "value", "type": "uint256"}
						],
						"name": "approve",
						"outputs": [{"name": "", "type": "bool"}],
						"payable": False,
						"stateMutability": "nonpayable",
						"type": "function"
					}
				]
				contract = web3.eth.contract(address=web3.to_checksum_address(_token), abi=abi)
			
			nonce = web3.eth.get_transaction_count(self.address)
			tx = contract.functions.approve(
				self.contracts[network][_spender]['ca'], _amount
			).build_transaction({
				'chainId': web3.eth.chain_id,
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
			approval_result = self.approve('wsfi', _amount, 'stake')
			if approval_result['status'] != 'success':
				logger.error("Approval failed.")
				return {'status': 'failed', 'error': 'Approval failed'}
			time.sleep(5)

			contract = self._getContract('stake')
			nonce = self.sfi_web3.eth.get_transaction_count(self.address)
			
			_lockPeriod = self._lockPeriod()

			if _lockPeriod <= 0:
				logger.warning("Invalid lock period detected, setting to default (100 days).")
				_lockPeriod = 8640000 # 100 Days

			logger.info(f"Staking amount: {_amount}, Lock period: {_lockPeriod}")

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
		
	def swap(self, _amount: int, pairKey: list, slippage: int = 0.02) -> dict:
		try:
			contract = self._getContract('citeaRouter')

			logger.info(f"Approving swapping amount: {_amount}")
			approval_result = self.approve(pairKey[0], _amount, 'citeaRouter')
			if approval_result['status'] != 'success':
				logger.error("Approval failed. Aborting swapping process.")
				return {'status': 'failed', 'error': 'Approval failed'}
			time.sleep(5)

			pair = self._convertKeyPair(pairKey)
			_amountsOut = self._getAmountsOut(_amount, pair)
			_amountOutMin = int(_amountsOut[1]*(1 - slippage))
			
			logger.info(f"Setting slippage to {slippage*100}%")
			logger.info(f"Swapping {_amount} {pairKey[0]} for {_amountOutMin} {pairKey[1]} ...")
			
			nonce = self.sfi_web3.eth.get_transaction_count(self.address)

			tx = contract.functions.swapExactTokensForTokensSupportingFeeOnTransferTokens(_amount, _amountOutMin, pair, self.address, 2**256-1).build_transaction({
				'chainId': self.sfi_web3.eth.chain_id,
				'from': self.address,
				'nonce': nonce
			})

			return self._executeTransaction(tx)
		except Exception as e:
			logger.error(f"Error during swap: {str(e)}")
			return {'status': 'failed', 'error': str(e)}
		
	def addLiquidity(self, _amount: int, pairKey: list, slippage: int = 0.02) -> dict:
		try:
			contract = self._getContract('citeaRouter')

			pair = self._convertKeyPair(pairKey)
			_amountsOut = self._getAmountsOut(_amount, pair)

			_amountA = _amount
			_amountB = _amountsOut[1]

			_amountAMin = int(_amountA * (1 - slippage))
			_amountBMin = int(_amountB * (1 - slippage))

			logger.info(f"Approving adding liquidity amount: {_amountA}")
			approval_result = self.approve(pairKey[0], _amountA, 'citeaRouter')
			if approval_result['status'] != 'success':
				logger.error("Approval failed.")
				return {'status': 'failed', 'error': 'Approval failed'}
			time.sleep(5)

			logger.info(f"Approving adding liquidity amount: {_amountB}")
			approval_result = self.approve(pairKey[1], _amountB, 'citeaRouter')
			if approval_result['status'] != 'success':
				logger.error("Approval failed.")
				return {'status': 'failed', 'error': 'Approval failed'}
			time.sleep(5)

			logger.info(f"Setting slippage to {slippage*100}%")
			logger.info(f"Adding {_amount} {pairKey[0]} and {_amountsOut[1]} {pairKey[1]} to liquidity pool ...")
			
			nonce = self.sfi_web3.eth.get_transaction_count(self.address)

			tx = contract.functions.addLiquidity(
				pair[0],
				pair[1],
				_amountA,
				_amountB,
				_amountAMin,
				_amountBMin,
				self.address,
				2**256-1
			).build_transaction({
				'chainId': self.sfi_web3.eth.chain_id,
				'from': self.address,
				'nonce': nonce
			})

			return self._executeTransaction(tx)
		except Exception as e:
			logger.error(f"Error during swap: {str(e)}")
			return {'status': 'failed', 'error': str(e)}

	def removeLiquidity(self, _percentage: float, pairKey: list, slippage: int = 0.02) -> dict:
		try:
			contract = self._getContract('citeaRouter')

			pair = self._convertKeyPair(pairKey)
			liquidity = int(self._getPairBalance(pair) * _percentage)

			logger.info(f"Approving removing liquidity amount: {liquidity}")
			approval_result = self.approve(self._getPairAddress(pair), liquidity, 'citeaRouter', 'sfi', [{"constant":False,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"}])
			if approval_result['status'] != 'success':
				logger.error("Approval failed.")
				return {'status': 'failed', 'error': 'Approval failed'}
			time.sleep(5)

			supply = self._getPairSupply(pair)
			reserves = self._getPairReserves(pair)

			_amountAMin = int(reserves[0] * (liquidity / supply) * (1 - slippage))
			_amountBMin = int(reserves[1] * (liquidity / supply) * (1 - slippage))

			logger.info(f"Setting slippage to {slippage*100}%")
			logger.info(f"Removing {liquidity} liquidity from pool ...")

			nonce = self.sfi_web3.eth.get_transaction_count(self.address)

			tx = contract.functions.removeLiquidity(
				pair[0],
				pair[1],
				liquidity,
				_amountAMin,
				_amountBMin,
				self.address,
				2**256-1
			).build_transaction({
				'chainId': self.sfi_web3.eth.chain_id,
				'from': self.address,
				'nonce': nonce
			})

			return self._executeTransaction(tx)

		except Exception as e:
			logger.error(f"Error during removeLiquidity: {str(e)}")
			return {'status': 'failed', 'error': str(e)}

	def crymboTravelRules(self, amount: int, to: str = "0x03a519F1bD19CE974566bA91190b62D5C00E3A81") -> dict:
		"""
		Handles Crymbo Travel Rules compliance by fetching user data and sending SFI.
		"""
		try:
			# Initialize a new session to get fake data
			session = requests.Session()

			req = session.get(self.CRYMBO_API + "/api/auth/csrf")
			csrf = req.json().get('csrfToken')
			if not csrf:
				raise ValueError("Failed to retrieve CSRF token")

			session.post(self.CRYMBO_API + "/api/auth/callback/credentials", data={
				"walletAddress": "0xdda7fAcac3a29DC201ec5BdD349FdF9f87317556",
				"redirect": "false",
				"csrfToken": csrf,
				"callbackUrl": self.CRYMBO_API,
				"json": "true"
			})

			# Get the fake data
			req = session.get(self.CRYMBO_API + "/api/auth/session")
			res = req.json()
			if "user" not in res:
				raise ValueError("Failed to retrieve user data from session.")

			data = res["user"]

			# Build travel role data
			trd = {
				"firstname": data.get("firstname", ""),
				"lastname": data.get("lastname", ""),
				"email": data.get("email", ""),
				"phone": data.get("phone", ""),
				"address": data.get("contactAddress", ""),
			}

			# Send SFI
			nonce = self.sfi_web3.eth.get_transaction_count(self.address)

			tx = {
				"nonce": nonce,
				"to": to,
				"value": amount,
				"chainId": self.sfi_web3.eth.chain_id,
				"gas": 21000,
				"gasPrice": self.sfi_web3.eth.gas_price,
			}

			txExec = self._executeTransaction(tx)
			if txExec["status"] == "failed":
				raise ValueError("Failed to send SFI.")

			txHash = txExec.get("tx")

			# Build payload
			transactions_payload = {
				"address_from": self.address,
				"address_to": to,
				"amount": str(amount / (10**18)),
				"travel_role_data": json.dumps(trd),
				"travel_role_status": "Sent",
				"txHash": "0x" + txHash,
			}

			trx_payload = {
				"action": "addTransaction",
				"network": "SFI",
				"txHash": "0x" + txHash,
			}

			# Send travel rule data
			while True:
				req = requests.post(self.CRYMBO_API + "/api/transactions", json=transactions_payload)
				res_data = req.json()
				if "error" not in res_data:
					break

			while True:
				req = requests.post(self.CRYMBO_API + "/api/trx", json=trx_payload)
				res_data = req.json()
				if res_data.get("success"):
					break

			return {"status": "success", "msg": "Travel rule data sent."}

		except Exception as e:
			logger.error(f"Error during crymboTravelRules: {str(e)}")
			return {"status": "failed", "error": str(e)}

		

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
			ts = int(time.time() * 1000.0)

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
				"transactionHash": f"0x{tx_hash}",
				"timestamp": ts,
				"messageStatus": 2,
				"button": True,
				"slug": "singularity-finance-testnet",
				"isWithdraw": True,
				"rawTx": raw_tx
			}

			logger.info("Calling Gelato API...")

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
	
	def proveWithdrawal(self, tx_hash: str) -> dict:
		"""
		Proves a withdrawal by using the specified transaction hash.
		"""
		try:
			contract = self._getContract('portal', 'sep')
			nonce = self.sep_web3.eth.get_transaction_count(self.address)
			tx_receipt = self.sfi_web3.eth.get_transaction_receipt(tx_hash)
			tx_block_number = tx_receipt['blockNumber']	

			event_data = self._getEventData(tx_hash)
			if not event_data:
				logger.error("Failed to fetch event data for the transaction.")
				return {'status': 'failed', 'error': 'Event data not found'}
			
			try:
				output_index = self._getL2OutputIndexAfter(tx_block_number)
			except Exception as e: # aka. Output not finalized
				logger.error(f"Failed to get output index. Try again later.")
				return {'status': 'failed', 'error': 'Failed to retrieve output index. Try again later.'}

			l2_output = self._getL2Output(output_index)
			
			withdrawal_hash = event_data.get('withdrawalHash')
			if self._isWithdrawalProven(withdrawal_hash):
				logger.info("Withdrawal is already proven.")
				return {'status': 'success'}

			tx_nonce = event_data.get('nonce')
			value = event_data.get('value')

			if not (withdrawal_hash and tx_nonce and value):
				logger.error("Incomplete event data.")
				return {'status': 'failed', 'error': 'Incomplete event data'}

			hashed = self.sep_web3.solidity_keccak(['bytes32', 'uint256'], [withdrawal_hash, 0])

			block_number = l2_output[2]
			block = self.sfi_web3.eth.get_block(block_number)

			proof_data = self.sfi_web3.eth.get_proof(
				"0x4200000000000000000000000000000000000016",
				[hashed],
				block_number
			)
			if not proof_data or 'storageProof' not in proof_data or not proof_data['storageProof']:
				logger.error("Proof data retrieval failed.")
				return {'status': 'failed', 'error': 'Proof data retrieval failed'}

			proof = proof_data['storageProof'][0]['proof']
			storage_hash = proof_data['storageHash']
			
			tx = contract.functions.proveWithdrawalTransaction(
				(tx_nonce, self.address, self.address, value, event_data['gasLimit'], "0x"),
				output_index,
				(b'\x00' * 32, block['stateRoot'], storage_hash, block['hash']),
				proof
			).build_transaction({
				"chainId": self.sep_web3.eth.chain_id,
				"from": self.address,
				"nonce": nonce
			})

			return self._executeTransaction(tx, "sep")

		except Exception as e:
			logger.error(f"Error during proveWithdrawal: {e}")
			return {'status': 'failed', 'error': str(e)}

	def finalizeWithdrawal(self, tx_hash: str) -> dict:
		"""
		Finalize the withdrawal with the specified transaction hash.
		"""
		try:
			contract = self._getContract('portal', 'sep')
			nonce = self.sep_web3.eth.get_transaction_count(self.address)

			event_data = self._getEventData(tx_hash)
			if not event_data:
				logger.error("Failed to fetch event data for the transaction.")
				return {'status': 'failed', 'error': 'Event data not found'}

			withdrawal_hash = event_data.get('withdrawalHash')
			if self._isWithdrawalFinalized(withdrawal_hash):
				logger.info("Withdrawal already finalized.")
				return {'status': 'success'}

			tx_nonce = event_data.get('nonce')
			value = event_data.get('value')

			if not (withdrawal_hash and tx_nonce and value):
				logger.error("Incomplete event data.")
				return {'status': 'failed', 'error': 'Incomplete event data'}

			tx = contract.functions.finalizeWithdrawalTransaction(
				(tx_nonce, self.address, self.address, value, event_data['gasLimit'], "0x"),
			).build_transaction({
				"chainId": self.sep_web3.eth.chain_id,
				"from": self.address,
				"nonce": nonce
			})

			return self._executeTransaction(tx, "sep")
		except Exception as e:
			logger.error(f"Error during finalizeWithdrawal: {str(e)}")
			return {'status': 'failed', 'error': str(e)}

		
	def getWithdrawalList(self) -> dict:
		"""
		Retrieves a list of withdrawals needs to be proven.
		"""
		try:
			response = requests.get(f"{self.GELATO_API}?isWithdraw=true&slug=singularity-finance-testnet&fromAddress={self.address}")
			resp_json = response.json()

			# Get the latest 5 withdrawals
			withdrawals = resp_json['data'][-5:]
			logger.info(f"Got {len(withdrawals)} withdrawal(s).")
			return withdrawals
		
		except Exception as e:
			logger.error(f"Error during getWithdrawalList: {str(e)}")
			return []

	def proveWithdrawals(self) -> list:
		"""
		Handles the prove withdrawal process.
		"""
		try:
			withdrawals = self.getWithdrawalList()
			if not withdrawals:
				logger.info("No withdrawals found.")
				return {'status': 'success', 'msg': 'No withdrawals found.'}

			for w in withdrawals:
				logger.info(f"{'-'*100}")
				tx_hash = w['transactionHash']
				logger.info(f"Processing withdrawal: {tx_hash}")
				
				# Prove the withdrawal
				prove_res = self.proveWithdrawal(tx_hash)
				if prove_res.get('status') != 'success':
					continue 

				logger.info("Successfully processed withdrawal.")
			
			return {'status': 'success', 'msg': 'Processed all withdrawals.'}

		except Exception as e:
			logger.error(f"Error during proveWithdraws: {str(e)}")
			return {'status': 'failed', 'error': str(e)}

	def finalizeWithdrawals(self) -> list:
		"""
		Handles the finalize withdrawal process.
		"""
		try:
			withdrawals = self.getWithdrawalList()
			if not withdrawals:
				logger.info("No withdrawals found.")
				return {'status': 'success', 'msg': 'No withdrawals found.'}

			for w in withdrawals:
				logger.info(f"{'-'*100}")
				tx_hash = w['transactionHash']
				logger.info(f"Processing withdrawal: {tx_hash}")
				
				# Finalize the withdrawal
				final_res = self.finalizeWithdrawal(tx_hash)
				if final_res.get('status') != 'success':
					continue 

				logger.info("Successfully processed withdrawal.")
			
			return {'status': 'success', 'msg': 'Processed all withdrawals.'}

		except Exception as e:
			logger.error(f"Error during proveWithdraws: {str(e)}")
			return {'status': 'failed', 'error': str(e)}


def executeOperation(operation, amount: int, times: int, *args) -> None:
	"""
	Executes a given operation a specified number of successful times.

	Args:
		operation (callable): The operation to execute.
		amount (int): The amount to process.
		times (int): The number of successful executions required.
		*args: Additional arguments required for the operation.
	"""
	successful_runs = 0

	while successful_runs < times:
		logger.info(f"Attempt {successful_runs + 1}/{times}: Executing operation.")
		try:
			result = operation(amount, *args) if amount is not None else operation(*args)
			if result['status'] == 'success':
				successful_runs += 1
				logger.info(f"Attempt {successful_runs}/{times}: Operation successful.")
			else:
				logger.warning(f"Attempt {successful_runs + 1}/{times}: Operation failed, trying again...")
		except Exception as e:
			logger.error(f"Attempt {successful_runs + 1}/{times}: Error occurred during operation: {str(e)}")
		
		time.sleep(5) 
	
	
def run(pk: str, config: Dict[str, int], opr_type: int = 0) -> None:
	"""
	Executes the main workflow based on the given configuration
	"""
	if not config:
		logger.error("Invalid configuration provided.")
		return

	sfi = SFI(private_key=pk)
	logger.info(f"--- Address: {sfi.address} ---")

	if opr_type == 1:
		operations = [
			(sfi.proveWithdrawals, None, 1),
		]
	elif opr_type == 2:
		operations = [
			(sfi.finalizeWithdrawals, None, 1),
		]
	else:
		operations = [
			(sfi.wrap, config.get("wrapAmount"), 2),
			(sfi.unwrap, config.get("unwrapAmount"), 2),
			(sfi.stake, config.get("stakeAmount"), 2),
			(sfi.unstake, config.get("unstakeAmount"), 1),
			(sfi.claim, None, 2),
			(sfi.swap, config.get("citeaConfig")['swapAmount'], 3, config.get("citeaConfig")["pair"], config.get("citeaConfig")["slippage"]),
			(sfi.addLiquidity, config.get("citeaConfig")['addLiquidityAmount'], 1, config.get("citeaConfig")["pair"], config.get("citeaConfig")["slippage"]),
			(sfi.removeLiquidity, config.get("citeaConfig")['removeLiquidityPerc'], 1, config.get("citeaConfig")["pair"], config.get("citeaConfig")["slippage"]),
			(sfi.crymboTravelRules, config.get("travelConfig")['amount'], 3,  config.get("travelConfig")['to'])
			# (sfi.initWithdrawal, config.get("bridgeAmount"), 5) | Disabled
		]

	for operation, amount, max_attempts, *extra_args in operations:  
		logger.info(f"Starting operation: {operation.__name__}")
		if amount is not None:
			executeOperation(operation, amount, max_attempts, *extra_args)
		else:
			executeOperation(operation, None, max_attempts, *extra_args)

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

				# primary_tokens = ["wsfi", "sfi"]
				secondary_tokens = ["usdc", "aimm"]

				first_token = "wsfi"
				second_token = None
				
				# == Currently disabled. == 
				#
				# while first_token not in primary_tokens:
				# 	first_token = input("Select the first token (wsfi/sfi) > ").strip().lower()
				# 	if first_token not in primary_tokens:
				# 		print("Invalid choice! Please select 'wsfi' or 'sfi'.")
				#
				
				print("Selecting default primary token: wsfi")

				while second_token not in secondary_tokens:
					second_token = input(f"Select the secondary token ({'/'.join(secondary_tokens)}) > ").strip().lower()
					if second_token not in secondary_tokens:
						print(f"Invalid choice! Please select 'usdc' or 'aimm'.")

				swapAmount = float(input(f"Enter swap amount for {first_token} -> {second_token} > "))
				addLiquidityAmount = float(input(f"Enter liquidity amount for {first_token} -> {second_token} > "))
				swapSlippage = float(input(f"Enter slippage for {first_token} -> {second_token} (Eg. 2% = 0.02) > "))
				removeLiquidityPerc = float(input(f"Enter percentage of liquidity to remove for {first_token} -> {second_token} (Eg. 20% = 0.2) > "))

				travelTo = input("Enter the travel destination address (Leaves empty to use default) > ")
				if not travelTo:
					travelTo = "0x03a519F1bD19CE974566bA91190b62D5C00E3A81"
				travelAmount = float(input("Enter travel amount > "))

			except ValueError:
				print("Error: Please enter valid numeric values for the amounts.")
				return
		else:
			wrapAmount = 0.02
			unwrapAmount = 0.01
			stakeAmount = 0.01
			unstakeAmount = 0.01
			bridgeAmount = 0.02

			first_token = "wsfi"  
			second_token = "aimm" 
			swapAmount = 0.015
			addLiquidityAmount = 0.01
			removeLiquidityPerc = 0.2
			swapSlippage = 0.02

			travelAmount = 0.0001
			travelTo = "0x03a519F1bD19CE974566bA91190b62D5C00E3A81"

		try:
			config = {
				"wrapAmount": int(wrapAmount * 10**18),
				"unwrapAmount": int(unwrapAmount * 10**18),
				"stakeAmount": int(stakeAmount * 10**18),
				"unstakeAmount": int(unstakeAmount * 10**18),
				"bridgeAmount": int(bridgeAmount * 10**18),
				"citeaConfig": {
					"pair": [first_token, second_token],
					"swapAmount": int(swapAmount * 10**18),
					"addLiquidityAmount": int(addLiquidityAmount * 10**18),
					"removeLiquidityPerc": removeLiquidityPerc,
					"slippage": swapSlippage
				},
				"travelConfig": {
					"amount": int(travelAmount * 10**18),
					"to": travelTo
				}
			}
		except Exception as e:
			print(f"Error: {e}")
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
	parser.add_argument("-P", "--prove", action="store_true", help="prove 5 most recently withdrawals")
	parser.add_argument("-F", "--finalize", action="store_true", help="finalize 5 most recently withdrawals")

	args = parser.parse_args()

	config = None
	opr_type = 0

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
		
		if args.prove: opr_type = 1
		elif args.finalize: opr_type = 2

		run(args.pk, config, opr_type)
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
		
		if args.prove: opr_type = 1
		elif args.finalize: opr_type = 2

		# Read private keys from file
		with open(args.file, "r") as f:
			private_keys = f.readlines()

		for pk in private_keys:
			run(pk.strip(), config, opr_type)
	else:
		print("Invalid arguments. Use -h or --help for usage information.")

if __name__ == "__main__":
	main()
