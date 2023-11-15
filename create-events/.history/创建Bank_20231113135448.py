import WA as wa
import time
from functools import wraps
def time_this_function(func):
    #作为装饰器使用，返回函数执行需要花费的时间
    @wraps(func)
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(func.__name__,end-start)
        return result
    return wrapper


@time_this_function
def ggg():
    get = wa.get_audio_getSelectedObjects()["objects"]
    for Objects in get:
                getD = wa.get_descendants(Objects["id"])['return']
                for i in getD:
                    print(i)


ggg()                   
wa.client.disconnect()

