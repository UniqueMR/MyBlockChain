from time import time
from BlockChain import BlockChain
from Block import Block
import time

from Transaction import Transaction
    
blockChain = BlockChain()
# 添加两笔交易
blockChain.add_transaction(Transaction('address1', 'address2', 100))
blockChain.add_transaction(Transaction('address2', 'address1', 50))
# address3 挖取待处理的交易
blockChain.mine_pending_transaction('address3')
# 查看账户余额
print('address1 余额 ', blockChain.get_balance_of_address('address1'))
print('address2 余额 ', blockChain.get_balance_of_address('address2'))
print('address3 余额 ', blockChain.get_balance_of_address('address3'))
# address2 挖取待处理的交易
blockChain.mine_pending_transaction('address2')
print('address1 余额 ', blockChain.get_balance_of_address('address1'))
print('address2 余额 ', blockChain.get_balance_of_address('address2'))
print('address3 余额 ', blockChain.get_balance_of_address('address3'))