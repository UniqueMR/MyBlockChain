from time import time
from BlockChain import BlockChain
from Block import Block
import time

from Transaction import Transaction

# 构建测试所使用的区块链
block_chain = BlockChain()
# 添加两笔交易
block_chain.add_transaction(Transaction('address1', 'address2', 100))
block_chain.add_transaction(Transaction('address2', 'address1', 50))
# address3挖去等待处理的交易
block_chain.mine_pending_transaction('address3')
# 查看账户余额
print('address1 余额', block_chain.get_balance_of_address('address1'))
print('address2 余额', block_chain.get_balance_of_address('address2'))
print('address3 余额', block_chain.get_balance_of_address('address3'))
# address2 挖取等待处理的交易
block_chain.mine_pending_transaction('address2')
# 查看账户余额
print('address1 余额', block_chain.get_balance_of_address('address1'))
print('address2 余额', block_chain.get_balance_of_address('address2'))
print('address3 余额', block_chain.get_balance_of_address('address3'))