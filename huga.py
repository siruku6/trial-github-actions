def complexity_is_under_10(val: int) -> bool:
    if val > 10:
        for i in range(10):
            if i > 2:
                res = _loop_20(i)
                if res:
                    return True
            else:
                return False
    elif val > 5:
        for i in range(10):
            if i > 2:
                res = _loop_20(i)
                if res:
                    return True
            else:
                return False
    return False


def _loop_20(i: int) -> bool:
    for j in range(20):
        if i + j > 10:
            return True
    return False


def complexity_is_under_20(val: int) -> bool:
    train_count: int = val
    square_train_count: int = train_count ** 2

    if val > 10:
        for i in range(10):
            if i > 2:
                for j in range(20):
                    if i + j > 10:
                        return True
            elif train_count > 14:
                return False
            else:
                train_count += 1
                for k in range(square_train_count):
                    if k > 10:
                        return True
    elif val > 5:
        # 関数に切り出すと、複雑度が下がる
        return _loop_ijk(square_train_count)
    else:
        for i in range(10):
            if i > 2:
                for j in range(20):
                    if i + j > 10:
                        return True
            elif train_count > 14:
                return False
            else:
                train_count += 1
                return True
    return False


def _loop_ijk(train_count: int, square_train_count: int) -> bool:
    """
    複雑度を下げるために切り出された関数
    """
    for i in range(10):
        if i > 2:
            for j in range(20):
                if i + j > 10:
                    return True
        elif train_count > 14:
            return False
        else:
            train_count += 1
            for k in range(square_train_count):
                if k > 10:
                    return True
