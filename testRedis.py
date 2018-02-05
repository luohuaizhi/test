import redis


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
        # print redis_cli.set(key, "5555555555")
        # print redis_cli.get(key)
        # print redis_cli.strlen(key)
        # print redis_cli.delete(key)
        # print redis_cli.delete(key)
        # integer
        # print redis_cli.set(key, 1)
        # print redis_cli.get(key)
        # print redis_cli.strlen(key)
        # list
        print redis_cli.delete(key) # 删除key
        print redis_cli.lpush(key, 1,2,3,4,5) # 从左添加元素，若key不存在添加key
        print redis_cli.lpushx(key, 1,2,3,4,5) # 从左添加元素，返回添加后元素个数，若key不存在不做任何操作，返回0
        print redis_cli.lpop(key) # 弹出left头部元素
        print redis_cli.llen(key) # 获取链表长度
        print redis_cli.lrange(key, 0, -1) # 取从位置0开始到位置-1（最后）结束的元素。
        print redis_cli.lrem(key, 1, 1) # 从头部(left)向尾部(right)变量链表，删除2个值等于a的元素，返回值为实际删除的数量。
        print redis_cli.lrem(key, 1, 1) # 从头部(left)向尾部(right)变量链表，删除2个值等于a的元素，返回值为实际删除的数量。
        print redis_cli.lset(key, 1, 2) # 将左起索引值为1的元素值设置为新值2。
        print redis_cli.lindex(key, 1) # 查看左起索引值为1的元素值
        print redis_cli.ltrim(key, 1) # 保留左起索引值0到2之间的3个元素，注意第0个和第2个元素均被保留。
        print redis_cli.rpop(key)
        print redis_cli.delete(key)
        print redis_cli.lpush(key, 1,2,3,4,5)
        print redis_cli.spop(key) #
        print redis_cli.delete(key)
        print redis_cli.lpush(key, 1,2,3,4,5)
        print redis_cli.blpop(key)
        print redis_cli.delete(key)
        print redis_cli.lpush(key, 1,2,3,4,5)
        print redis_cli.brpop(key)
        print redis_cli.delete(key)
        # dict
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
        print redis_cli.move(key, key1, 2) # 将2从key移到key1
        print redis_cli.move(key, key1, 2) # 将2从key移到key1, 由于此时key中没有2，移动失败
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
        print redis_cli.sunion(key, key1, key2) # 取并集
        unionkey = key+"unionkey"
        print redis_cli.sinterstore(unionkey, key, key1, key2) # 取并集并存储
        print redis_cli.sdiff(key, key1, key2) # 取非,key和key1相比，再用这个结果继续和key2进行差异比较
        unionkey = key+"not"
        print redis_cli.sdiffstore(unionkey, key, key1, key2) # 取非，并存储

        # Sorted-Sets和Sets类型极为相似,各种操作命令也相似
        print redis_cli.delete(key)
        print redis_cli.zadd(key, 1,2,3) # 添加、设置成员
        print redis_cli.zcard(key) # 获取成员数量
        print redis_cli.zismember(key, 4) # 判断是否包含该成员
        print redis_cli.zrandmember(key) # 随机获取一个成员，成员依然在Set中存在
        print redis_cli.zmembers(key) # 查看成员
    except Exception as e:
        print e.message
    finally:
        print redis_cli.delete(key)
    return None


if __name__ == "__main__":
    main()