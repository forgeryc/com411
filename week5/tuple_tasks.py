def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods)
def run_task1():
    like = likelihood()
    print(f"Minimum likelihood of failing: {like}%")