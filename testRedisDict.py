# encoding:utf-8
import redis
import time


def main():
    """
    redis-cli -h 127.0.0.1 -a test321
    """
    redis_host = "127.0.0.1"
    redis_password = "test321"
    redis_cli = redis.StrictRedis(host=redis_host, password=redis_password)
    try:
        key = "TEST_KEY_1484"
        # string
        print redis_cli.delete(key)
        print redis_cli.hset(key, "test1", 1)  # 设置 key={test1:1}
        print redis_cli.hget(key, "test1")  # 获取key[test1]
        print redis_cli.hexists(key, "test1")  # 是否存在key[test1]
        print redis_cli.hset(key, "test2", 2)  # 设置 key={test2:2}
        print redis_cli.hlen(key)  # 查看key下的键值对数量
        print redis_cli.hdel(key, "test1", "test2")  # 批量删除key下的键，返回实际删除的键数量
        print redis_cli.hlen(key)  # 查看key下的键值对数量
        print redis_cli.hexists(key, "test1")  # 是否存在key[test1]
        print redis_cli.hsetnx(key, "test1", 1)   # 设置 key={test1:1}
        print redis_cli.hsetnx(key, "test1", 1.11)   # 如果key[test1]已存在设置失败
        print redis_cli.hget(key, "test1")  # 获取key[test1]
        print redis_cli.hincrby(key, "test1", 2)   # 设置 key[test1] 累加2
        print redis_cli.hget(key, "test1")  # 获取key[test1]
        print redis_cli.hset(key, "test2", 2)  # 设置 key={test2:2}
        print redis_cli.hgetall(key)  # 获取key，得到dict对象
        print redis_cli.hkeys(key)  # 获取key下的所有键，得到list对象
        print redis_cli.hvals(key)  # 获取key下的所有值，得到list对象
        print redis_cli.hmget(key, "test1", "test2")  # 批量获取key下的指定键，得到list对象
        print redis_cli.hmset(key, {"test3": 3, "test4": 4})  # 批量设置键值，无则添加，有则覆盖，
        print redis_cli.hgetall(key)
    except Exception as e:
        print e.message
    finally:
        print redis_cli.delete(key)
    return None


if __name__ == "__main__":
    main()
