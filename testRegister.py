class myRegister(object):
    _Registered = {}

    @staticmethod # 静态方法 无需实力化类即可使用
    def register(name, func):
        myRegister._Registered[name] = func

    @staticmethod
    def get(name, **kargs):
        f = myRegister._Registered[name]
        return f(**kargs)


register_machine = myRegister()


def printF1(word):
    print('printF1{word}'.format(word=word))


def printF2(word):
    print('printF2{word}'.format(word=word))


def printF3(sname, sword):
    print('{word} {name}'.format(name=sname, word=sword))


if __name__ == "__main__":
    register_machine.register('f1', lambda word: printF1(word))
    register_machine.register('f2', lambda word: printF2(word))
    register_machine.register('f3', lambda sname, word: printF3(sname, word))

    _FUNC_NAME = 'f1'
    register_machine.get(_FUNC_NAME, word="hellof1")
    _FUNC_NAME = 'f2'
    register_machine.get(_FUNC_NAME, word="hellof2")
    _FUNC_NAME = 'f3'
    register_machine.get(_FUNC_NAME, sname='Tom', word='Hi')
