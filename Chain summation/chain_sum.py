def chain_sum(num: int):
    def inner(sub_num=None):
        if sub_num is None:
            return num
        else:
            return chain_sum(num + sub_num)

    return inner


print(chain_sum(5)())
print(chain_sum(5)(2)())
print(chain_sum(5)(100)(-10)())