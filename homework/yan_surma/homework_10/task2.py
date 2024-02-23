def repeat_me(count):

    def multiplier(func):

        def wrapper(*args):
            for i in range(count):
                func(*args)
            print('finished')

        return wrapper

    return multiplier


@repeat_me(count=10)
def some(text):
    print(text)


some('Test text')
