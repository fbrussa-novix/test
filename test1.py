
import threading
import ctypes
import time


class thread_with_exception(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):

        # target function of the thread class
        try:
            for nn in range(100000000):
                a = 1231 * 12311 / (nn+1)
                # while True:
                ##print('running ' + self.name + ' ' + str(nn))
        finally:
            print('ended')

    def get_id(self):

        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id

    def raise_exception(self):
        thread_id = self.get_id()
        print(thread_id)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
                                                         ctypes.py_object(SystemExit))
        print(res)
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')


print("start")
t1 = thread_with_exception('Thread 1')
t1.start()
time.sleep(2)
print("try end")
t1.raise_exception()
t1.join()
