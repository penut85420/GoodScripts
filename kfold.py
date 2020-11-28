def kfold_split(ds, i):
    train_idx = list(range(len(ds)))
    train_idx.remove(i)
    test = ds[i]

    train = list()
    for idx in train_idx:
        train.extend(ds[idx])

    return train, test
