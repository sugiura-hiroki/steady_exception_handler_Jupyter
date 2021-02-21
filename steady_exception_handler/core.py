import sys

# iPython限定
class SteadyExceptionHandler():
    def __init__(self, *callbacks):
        self.__callbacks = callbacks
        self.ip = get_ipython()
        self.ip.events.register('pre_execute', self.preExecute_recordLastError)
        self.ip.events.register('post_execute', self.postExecute_checkError)
        try:
            self.last_traceback = sys.last_traceback
        except:
            self.last_traceback = None

    def preExecute_recordLastError(self):
        try:
            self.last_traceback = sys.last_traceback
        except:
            self.last_traceback = None

    def postExecute_checkError(self):
        try:
            sys.last_traceback
        except:
            return
        if self.last_traceback is not sys.last_traceback:
            for callback in self.__callbacks:
                callback()

    def registerEvents(self, *callbacks):
        self.__callbacks += callbacks

    def reset(self):
        self.__callbacks = []

