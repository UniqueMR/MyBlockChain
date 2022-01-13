import hashlib
import json
import time
from Transaction import TransactionEncoder

'''
定义区块类
'''
class Block:
    def __init__(self, timestamp, transactions, previous_hash = ''):
        '''
        区块链的初始化
        :param timestamp: 创建时间戳
        :param data: 区块数据，使用json格式存储
        :param previous_hash: 上一个区块的hash
        :param hash: 当前区块的hash（当前区块的hash值在获取当前区块所有内容后，利用sha256算法创建）
        :param nonce: 随机数，初始化为0，用来查找一个有效hash的次数。由于内容的很小变动都将导致hash值截然不同，因此nonce的引入将使得hash值变得很难预测
        '''
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        '''
        使用hash256算法计算区块哈希值
        hash256算法可以将任意长度的数据压缩成一固定长度的信息摘要
        微小的信息改变都会导致得到的hash值截然不同，可以用来校验数据是否改动
        通过hash值反推内容的难度远大于从内容得到hash值的难度
        '''
        # 将区块信息拼接然后生成sha256的hash值，使用cls=TransactionEncoder指定编码器
        raw_str = self.previous_hash + str(self.timestamp) + json.dumps(self.transactions, ensure_ascii=False, cls=TransactionEncoder) + str(self.nonce)
        sha256 = hashlib.sha256()
        sha256.update(raw_str.encode('utf-8'))
        hash = sha256.hexdigest()
        return hash
    
    def mine_block(self, difficulty):
        '''
        实现挖矿方法，通过大量尝试来寻找一个有效的hash值创建一个新的区块
        :param difficulty: 难度
        '''
        time_start = time.clock()
        # 要求在hash值前difficulty各位为0
        while self.hash[0 : difficulty] != ''.join(['0'] * difficulty):
            # 符合要求才可以退出，否则一直更新nonce值，并重新计算hash值
            self.nonce += 1
            self.hash = self.calculate_hash()
        print("挖到区块:%s, 耗时:%f秒" % (self.hash, time.clock() - time_start))

    