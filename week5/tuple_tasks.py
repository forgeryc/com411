def likelihood_min_max():
    likelihoods = (50, 38, 27, 99, 4)
    out = (min(likelihoods), max(likelihoods))
    return out


def run_task1():
    like = likelihood()
    print(f"Minimum likelihood of failing: {like}%")


def run_task2():
        minmax = likelihood_min_max()
        print(f"Minimum likelihood of failing: {minmax[0]}%")
        print(f"Maximum likelihood of failing: {minmax[1]}%")
