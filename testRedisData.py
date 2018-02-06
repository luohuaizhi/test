# encoding:utf-8
import redis
import time


def main():
    """
    redis-cli -h 101.37.161.139 -a bycx321
    """
    redis_host = "101.37.161.139"
    redis_password = "bycx321"
    redis_cli = redis.StrictRedis(host=redis_host, password=redis_password)
    try:
        key = "TEST_KEY_1484"
        # string
        print redis_cli.delete(key)
        print redis_cli.set(key, "hello")
        print redis_cli.get(key)
        print redis_cli.append(key, "world")
        print redis_cli.get(key)
        print redis_cli.strlen(key)
        # timeout
        print redis_cli.delete(key)
        print redis_cli.setex(key, 10, "hello")
        print redis_cli.get(key)
        print redis_cli.ttl(key)
        # time.sleep(10)
        print redis_cli.get(key)
        # not set
        print redis_cli.delete(key)
        print redis_cli.setnx(key, "hello") # 设置key为hello
        print redis_cli.setnx(key, "world") # 设置key为world，key已经有值，设置失败
        print redis_cli.get(key) # 只能得到第一次设置的值
        print redis_cli.setrange(key, 20, "111111") # 从20位置开始替换，若索引值超过原值长度，则补0
        print redis_cli.getrange(key, 1, -1) # 获取1到-1（最后）的子串
        print redis_cli.mset({"key1":1, "key2":2, "key3":3})
        print redis_cli.mget("key1", "key2", "key3")
        print redis_cli.msetnx({"key3":7, "key4":8, "key5":9}) # 已经有值的key会设置失败，从而导致整次设置失败
        print redis_cli.mget("key1", "key2", "key3", "key4", "key5")

        # integer
        print redis_cli.delete(key)
        print redis_cli.set(key, 1)
        print redis_cli.incr(key)  # 累加1
        print redis_cli.incr(key, 2)  # 累加2
        print redis_cli.incrby(key, 5) # 累加5
        print redis_cli.decr(key) # 累减1
        print redis_cli.decr(key, 3) # 累减3
        print redis_cli.getset(key, 0) #获取旧值，并获取新值，一次原子操作
        
        # list
        print redis_cli.delete(key) # 删除key
        print redis_cli.lpush(key, 1,2,3,4,5) # 从左添加元素，若key不存在添加key
        print redis_cli.lpushx(key, 6) # 从左添加元素，返回添加后元素个数，若key不存在不做任何操作，返回0, 只能添加一个元素
        print redis_cli.lpop(key) # 弹出left头部元素
        print redis_cli.llen(key) # 获取链表长度
        print redis_cli.lrange(key, 0, -1) # 取从位置0开始到位置-1（最后）结束的元素。
        print redis_cli.lrem(key, 1, 1) # 从头部(left)向尾部(right)变量链表，删除2个值等于a的元素，返回值为实际删除的数量。
        print redis_cli.lrem(key, 1, 1) # 从头部(left)向尾部(right)变量链表，删除2个值等于a的元素，返回值为实际删除的数量。
        print redis_cli.lset(key, 1, 2) # 将左起索引值为1的元素值设置为新值2。
        print redis_cli.lindex(key, 1) # 查看左起索引值为1的元素值
        print redis_cli.ltrim(key, 0, 2) # 保留左起索引值0到2之间的3个元素，注意第0个和第2个元素均被保留。
        ele1 = redis_cli.lindex(key, 1) # 获取左起索引值为1的元素值
        print redis_cli.linsert(key, "after", ele1, 88) # 在1号元素后插入元素88
        print redis_cli.lrange(key, 0, -1)
        print redis_cli.linsert(key, "before", ele1, 99) # 在1号元素前插入元素99
        print redis_cli.lrange(key, 0, -1)
        # r
        print redis_cli.delete(key)
        print redis_cli.rpush(key, 1,2,3,4,5)
        print redis_cli.lrange(key, 0, -1)
        print redis_cli.rpushx(key, 6)
        print redis_cli.lrange(key, 0, -1)
        print redis_cli.rpop(key) # 从最右po出元素
        print redis_cli.lrange(key, 0, -1)
        newkey = key+"new"
        print redis_cli.lpush(key, 1,1)
        print redis_cli.rpoplpush(key, newkey) # 从key尾部po出元素到newkey头部
        print redis_cli.lrange(key, 0, -1)
        print redis_cli.lrange(newkey, 0, -1)

        # set
        print redis_cli.delete(key)
        print redis_cli.sadd(key, 1,2,3,4,5) # 添加、设置成员
        print redis_cli.smembers(key) # 获取成员
        print redis_cli.scard(key) # 获取成员数量
        print redis_cli.sismember(key, 4) # 判断是否包含该成员
        print redis_cli.srandmember(key) # 随机获取一个成员，成员依然在Set中存在
        print redis_cli.smembers(key) # 查看成员
        print redis_cli.spop(key) # 从尾部弹出一个元素，由于是Set所以得到并不是之前插入的第一个或最后一个成员。
        print redis_cli.smembers(key) # 查看成员
        print redis_cli.srem(key, 1) # 删除一个成员
        print redis_cli.smembers(key) # 查看成员
        key1 = key+"B"
        print redis_cli.sadd(key1, 9,8,7)
        print redis_cli.smove(key, key1, 2) # 将2从key移到key1
        print redis_cli.smove(key, key1, 2) # 将2从key移到key1, 由于此时key中没有2，移动失败
        print redis_cli.smembers(key) # 查看成员
        print redis_cli.smembers(key1) # 查看成员
        # 与、或、非
        key2 = key+"C"
        print redis_cli.delete(key)
        print redis_cli.sadd(key, 1,2,3) # 添加、设置成员
        print redis_cli.sadd(key1, 1,4,5) # 添加、设置成员
        print redis_cli.sadd(key2, 3,6,9) # 添加、设置成员
        print redis_cli.sinter(key, key1, key2) # 取交集
        interkey = key+"inter"
        print redis_cli.sinterstore(interkey, key, key1, key2) # 取交集并存储
        print redis_cli.delete(interkey)
        print redis_cli.sunion(key, key1, key2) # 取并集
        unionkey = key+"unionkey"
        print redis_cli.sinterstore(unionkey, key, key1, key2) # 取并集并存储
        print redis_cli.delete(unionkey)
        print redis_cli.sdiff(key, key1, key2) # 取非,key和key1相比，再用这个结果继续和key2进行差异比较
        notkey = key+"not"
        print redis_cli.sdiffstore(unionkey, key, key1, key2) # 取非，并存储
        print redis_cli.delete(notkey)
        # Sorted-Sets和Sets类型极为相似,各种操作命令也相似
        print redis_cli.delete(key)
        print redis_cli.zadd(key, 1, "one", 2, "two", three=3, four=4) # 添加、设置成员
        print redis_cli.zcard(key) # 获取成员数量
        print redis_cli.zcount(key, 1, 2) # 获取分数满足表达式1 <= score <= 2的成员的数量
        print redis_cli.zscan(key, match="*o*") # 查看匹配的成员
        print redis_cli.zrange(key, 0, -1) # 查看所有成员。
        print redis_cli.zrange(key, 0, -1, withscores=True) # WITHSCORES选项表示返回的结果中包含每个成员及其分数，否则只返回成员。
        print redis_cli.zrank(key, "one") # 查看成员one的索引位置
        # print redis_cli.zrem(key, "one", "two") # 删除成员one和two，返回实际删除成员的数量。
        print redis_cli.zscore(key, "one") # 获取成员one的分数。返回值是字符串形式。
        print redis_cli.zincrby(key, "one", 2) # 将成员one的分数增加2，并返回该成员更新后的分数。
        print redis_cli.zincrby(key, "one", -1) # 将成员one的分数增加-1，并返回该成员更新后的分数。
        print redis_cli.zrange(key, 0, -1, withscores=True)
        print redis_cli.zrangebyscore(key, 1, 3, start=1, num=2, withscores=True)  # 获取分数满足表达式1 <= score <= 3的成员。
        print redis_cli.zrangebyscore(key, 1, 3, 1, 2, True)  # 获取分数满足表达式1<= score<= 3的成员。从1开始取2个，同时返回分数
        # dict
        print redis_cli.delete(key)
    except Exception as e:
        print e.message
    finally:
        print redis_cli.delete(key)
    return None


if __name__ == "__main__":
    main()
