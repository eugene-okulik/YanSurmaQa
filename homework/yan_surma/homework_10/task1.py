def finish_me(func):
    def wrapper(*args):
        result = func(*args)
        print('finished')
        return result

    return wrapper


@finish_me
def cat(name):
    print(f'Cat {name} always eat, sleep, miay and repeat!')


cat('Bob')
