from Block import Block
import time

from Transaction import Transaction

'''
定义区块链类
'''
class BlockChain:
    def __init__(self):
        self.chain = [self._create_genesis_block()]
        # 设置初始难度，此处初始难度设置为5
        self.difficulty = 5
        # 待处理的交易
        self.pending_transactions = []
        # 设置一个挖矿奖励
        self.mining_reward = 100

    @staticmethod
    def _create_genesis_block():
        '''
        生成区块
        '''
        timestamp = time.asctime()
        block = Block(timestamp, [], '')
        return block

    def get_latest_block(self):
        '''
        获取链上最后一个也是最新一个区块
        '''
        return self.chain[-1]

    # def add_block(self, block):
    #     '''
    #     添加区块
    #     :param block: 要添加的区块 
    #     '''
    #     block.previous_hash = self.get_latest_block().hash
    #     # 开始挖矿
    #     block.mine_block(self.difficulty)
    #     # 挖矿结束后添加到链上
    #     self.chain.append(block)
    def add_transaction(self, transaction):
        '''
        添加交易
        :param transaction: 新交易
        '''
        # 根据业务对交易进行一系列验证
        '''...'''
        # 添加待处理的交易
        self.pending_transactions.append(transaction)

    def verify_blockchain(self):
        '''
        校验区块链数据是否完整 是否被篡改过
        '''

        for i in range(1, len(self.chain)):
            current_block = self.chain[i] # 当前遍历到的区块
            previous_block = self.chain[i - 1] # 当前区块的上一个区块
            if current_block.hash != current_block.calculate_hash():
                # 如果当前区块的hash值不等于根据当前内容计算得到的hash值，说明数据出现了变动
                return False

            if current_block.previous_hash != previous_block.calculate_hash():
                # 如果所指向区块的hash值不等于根据前一个区块内容计算得到的hash值，说明上个区块数据出现了变动，或者本区块所指向的上个区块hash值被改动
                return False
        return True

    def mine_pending_transaction(self, mining_reward_address):
        '''
        挖取等待处理的交易
        :param mining_reward_address: 挖矿奖励的地址
        '''
        block = Block(time.asctime(), self.pending_transactions, self.get_latest_block().hash)
        block.mine_block(self.difficulty)
        self.chain.append(block)
        # 挖矿成功后，重置待处理的业务，添加一笔事务，即此次挖矿的奖励
        self.pending_transactions = [
            Transaction(None, mining_reward_address, self.mining_reward)
        ]
        # self.add_transaction(Transaction(None, mining_reward_adress, self.mining_reward))

    def get_balance_of_address(self, address):
        '''获取钱包金额
        :param address: 钱包的地址
        '''
        balance = 0
        for block in self.chain:
            for trans in block.transactions:
                if trans.from_address == address:
                    # 自己发起的交易 支出
                    balance -= trans.amount
                if trans.to_address == address:
                    # 收入
                    balance += trans.amount
        return balance

    '''
    谁挖矿成功后，就会在待处理的交易中产生一笔新的交易，包含自己挖矿的奖励，所以奖励并非实时到账，在下一次挖矿成功后，此次挖矿的奖励才能到账
    '''
