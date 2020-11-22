import numpy as np

def evaluation_label(T, P, L):
    AY = (T == L)
    AN = (T != L)
    PY = (P == L)
    PN = (P != L)

    TP = AY & PY
    FP = AN & PY
    FN = AY & PN
    TN = AN & PN

    ALL = (TP, FP, FN, TN)
    TP, FP, FN, TN = map(sum, ALL)

    epsilon = 1e-7
    accuracy = (TP + TN) / (TP + FP + TN + FN + epsilon)
    precision = TP / (TP + FP + epsilon)
    recall = TP / (TP + FN + epsilon)
    f1_score = (2 * recall * precision) / (recall + precision + epsilon)

    return accuracy, precision, recall, f1_score

def evaluation(T, P):
    final_results = {}
    labels = set(T) | set(P)

    for label in labels:
        results = evaluation_label(T, P, label)
        final_results[label] = results

    return final_results

def macro_f1(T, P):
    results = evaluation(T, P)
    results = np.array([results[k][3] for k in results])

    return results.mean(), results.std()

def display_evaluation(T, P, label_map=None, print_fn=print):
    results = evaluation(T, P)
    for k in sorted(results):
        label = k if label_map is None else label_map.get(k, k)
        ss = [f'{col}{r:.4f}' for col, r in zip('APRF', results[k])]
        print_fn(f'{label}: ' + ' '.join(ss))

    return results

def main():
    def to_ndarray(arr):
        return np.array(list(arr))

    def lab(s1, s2, name):
        print(f'\n[{name}]')
        s1, s2 = map(to_ndarray, (s1, s2))
        display_evaluation(s1, s2)
        f1, std = macro_f1(s1, s2)
        print(f'Macro F1/Std: {f1:.4f}/{std:.4f}')

    lab('ABCBA', 'ABCBA', 'Exact Match')
    lab('ABCBA', 'ABCBB', 'A Little')
    lab('ABCBA', 'AAAAA', 'All A')
    lab('ABCBA', 'BBBBB', 'All B')
    lab('ABCBA', 'CCCCC', 'All C')

if __name__ == '__main__':
    main()
