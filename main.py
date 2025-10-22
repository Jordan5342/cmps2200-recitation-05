import random, time
import tabulate

def ssort(L):
    ### selection sort
    if (len(L) == 1):
        return(L)
    else:
        m = L.index(min(L))
        print('selecting minimum %s' % L[m])
        L[0], L[m] = L[m], L[0]
        print('recursively sorting L=%s\n' % L[1:])
        return [L[0]] + ssort(L[1:])

def qsort(a, pivot_fn):
    if len(a) <= 1:
        return a
    else:
        pivot_idx = pivot_fn(a)
        pivot = a[pivot_idx]
        left = [x for i, x in enumerate(a) if x < pivot]
        middle = [x for i, x in enumerate(a) if x == pivot]
        right = [x for i, x in enumerate(a) if x > pivot]
        return qsort(left, pivot_fn) + middle + qsort(right, pivot_fn)

def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.
    """
    start = time.time()
    sort_fn(mylist.copy())
    return (time.time() - start) * 1000

def compare_sort(sizes=[100, 200, 500, 1000, 2000, 5000, 10000]):
    """
    Compare the running time of different sorting algorithms.
    """
    qsort_fixed_pivot = lambda a: qsort(a, lambda x: 0)
    qsort_random_pivot = lambda a: qsort(a, lambda x: random.randint(0, len(x) - 1))
    tim_sort = lambda a: sorted(a)
    
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        #random.shuffle(mylist)
        
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist) if size <= 500 else float('inf'),
            time_search(qsort_random_pivot, mylist),
            time_search(tim_sort, mylist),
        ])
    return result

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot', 'timsort'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())

random.seed()
test_print()