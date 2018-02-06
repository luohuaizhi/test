# encoding:utf-8
import redis
import time


def main():
    """
    redis-cli -h 127.0.0.1 -a test321
    """
    redis_host = "127.0.0.1"
    redis_password = "test321"
    redis_cli = redis.StrictRedis(host=redis_host, port=6379, db=0, password=redis_password)
    try:
        print redis_cli.flushdb() # 清空数据库
        print redis_cli.randomkey() # 随机获得一个key，如果数据库为空，返回nil
        print redis_cli.set("key1", "hello")
        print redis_cli.set("key2", "world")
        print redis_cli.randomkey()
        print redis_cli.keys("key*") # 获得当前数据库所有的“key*”
        print redis_cli.exists("key3") # 查看key是否存在
        print redis_cli.set("key3", 1)
        print redis_cli.type("key2") # 查看key对应的值类型
        print redis_cli.type("key3")
        print redis_cli.move("key3", 1) # 移动对应key(key3)到对应数据库(1)
        print redis_cli.select(1) #  切换到数据库(1)
        print redis_cli.exists("key3") # 查看key是否存在
        print redis_cli.get("key3")
        print redis_cli.delete("key3")
        print redis_cli.select(0) #  切换到数据库(0)
        print redis_cli.exists("key3") # 查看key是否存在
        print redis_cli.get("key2")
        print redis_cli.rename("key2", "key3") # 将key2重命名key3
        print redis_cli.get("key2")
        print redis_cli.get("key3")
        print redis_cli.rename("key1", "key3") # 尝试将key2重命名key3，若key3存在则失败
        print redis_cli.get("key1")
        print redis_cli.get("key3")
        print redis_cli.expire("key1", 100) # 设置key1键时效100秒
        print redis_cli.ttl("key1") # 查看key1时效
        print redis_cli.expire("key1", 10) # 重置key1键时效10秒
        print redis_cli.ttl("key1") # 查看key1时效
        print redis_cli.persist("key1") # 取消key1超时，设置为永久
        print redis_cli.ttl("key1") # 查看key1时效，持久键返回-1

        
    except Exception as e:
        print e.message
    finally:
        print redis_cli.flushdb()
    return None


if __name__ == "__main__":
    main()
