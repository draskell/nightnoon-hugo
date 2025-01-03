---
title: "Recently I Learned"
date: 2022-12-26T10:39:35-08:00
draft: false
tags:
- software dev
categories: 
- software dev
---

Welcome, I am using this blog to explore my interests. Anything that excites me enough to keep me up into the wee hours tinkering is fare play for the blog. Hence the title NightNoon, as in "Should I go to bed? No! It's barely night noon."

The site is built using Hugo which will serve as the first topic to explore for the blog. In this change log style post I am taking a page from [Simon Willison](https://simonwillison.net) who has suggested blogging in bite size chunks and starting with TIL posts. In my case more like this-month-I-learned TMIL.

# November, 2024: Sorting Algorithms

Recently in preparation for a technical interview at Microsoft I was asked to come to the interview prepared to write at least one sorting algorithm. This turned out to be a fun rabbit hole. I'd always taken for granted the built in sorting algorithms in languages like Python, but what algorithm is being used? (spoiler its Timsort) and how can I implement it?

Looking into the Python built-in `sorted` function I found it used  the "timsort" algorithm which was completely new to me. Looking it up I found it to be a composite algorithm based off two simpler methods "insertion sort" and "merge sort".

## Insertion Sort

Insertion sort is a simple algorithm which is known to be efficient, O(n), on small data, especially real world data which might be close to sorted already and may contain many duplicate records. On large, more random data it is generally not very efficient O(n2). In either case it has a memory complexity of O(1).

Reading about insertion sort also introduced me to the idea of "stable" sorting, whether or not the sorting algorithm keeps the original sort order of items with equal value in the list.


### Stable Sorting Example

Imagine rather than sorting simply integers the goal is to sort objects representing people on one of the attributes like age, for example:

``` Python
l = [
    {
        "birth_year": 1963,
        "name": "Michael Jordan",
    },
    {
        "birth_year": 1980,
        "name": "Tim Peters",
    },
    {
        "birth_year": 1963,
        "name": "Les Claypool",
    }
]
```

If we sort by birth year the two people born in 1963 may or may not stay in the original order, ie Michael Jordan before Les Claypool. If they stay in the original order the sorting algorithm is said to be stable.

### Insertion Sort Implementation

Insertion sort works by looking at an element in the list (starting with the second element) and checking each element before it to see if it's bigger. If so that element is moved one element down the list and the next element is considered.

![Insertion Sort](/posts/inception/insertion-sort.gif)

``` Python
def insertion_sort(array: List):
    """
    Sorts the input array using the insertion sort algorithm.

    Args:
        array (List): a list which can be sorted. The iterable array
            in this case must be a list because it is expected to be mutable
            for simplicity sake.21`

    Returns (List):
        The sorted list.
    """
    # Start from the second element in the list as the current
    # index (i).
    for i in range(1, len(arr))
        key = arr[i]
        # Start the search index (j) as the element before.
        j = i - 1

        # While the search index (j) is positive, still in the list
        # and the jth element is still larger than the current element
        # then move the jth element one position toward the end and
        # decrement the search index.
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Once the while condition is no longer valid, either because
        # the value at the jth position is now less than the current 
        # position key or the search index has reached the beginning of
        # the list (j = -1), then set the value after the search index to
        # the current key.
        arr[j + 1] = key

    # After iterating through the whole array the arr will be sorted
    # and can be retured.
    return arr

```

## Merge Sort

Merge sort is an algorithm which can be used on it's own to sort an array. It relies on a fundamental "merge" operation which takes two sorted lists and interleaves them in a way that preserves the sort order of the resulting list.

The merge operation:
``` Python
def merge(arr1, arr2):
    """
    Takes two sorted lists and returns a combined sorted list.
    """
    # Initialize a result list.
    res = []

    # Start the pointers for the first and second list to 0.
    i,j = 0,0
    # While the pointer index for the first list (i) is less than the length
    # of the first list and the pointer index for the second list (j) are
    # less than the lengths of the respective lists.
    while i < len(arr1) and j < len(arr2):
        # If the pointed value in the first array is less than the pointed 
        # value in the second array append the first array value to the result
        # and increment the corresponding pointer. Otherwise do the opposite.
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    # After the end of one list has been reached the other list may have
    # values which need to be added. We can just add the remainder of both
    # lists beyond the pointer one of which won't contain any values.
    res.extend(arr1[i:])
    res.extend(arr2[j:])
    return res
```

Given this merge functionality it's possible to implement another sorting strategy called "merge sort". Here's a recursive example of the merge sort algorithm:

``` Python
def merge_sort(arr):
    """
    A recursive algorithm for sorting an array using merge sort.

    """
    # Base case, an array of length one is sorted by default.
    if len(arr) <= 1:
        return arr
    
    # Find the middle index of the array.
    middle = len(arr) // 2
    # Split the array into a left and right array around the middle index.
    left = arr[:middle]
    right = arr[middle:]
    # Recursively call merge_sort on each side.
    left = merge_sort(left)
    right = merge_sort(right)
    # Use the merge function to combine the two sorted halves of the input
    # array.
    return merge(left, right)
```

Timsort doesn't use the full merge sort implementation, rather it uses the "insertion sort" algorithm to efficiently sort small sub arrays and the `merge` function to then combine the sorted sub arrays. 

Here's an example impementation of timesort in Python:

``` Python
def timsort(arr, sub_size=32):
    """
    """
    # Initialize a first in first out (FIFO) queue of sorted sub-arrays to merge.
    subs = deque()
    # Iterate through the sub lists, sort them with insertion sort, and append
    # them to the queue
    for i in range(0, len(arr), subsize):
        subs.append(insertion_sort(arr[i:i+subsize]))

    # While there are more than one list in the queue use merge to combine
    # the first two lists in the queue and append the result to the end.
    while len(subs) > 1:
        left = subs.popleft()
        right = subs.popleft()
        subs.append(merge(left,right))
    return subs[0]
```

There are a lot of efficiencies that can be used and quick profiling of this implementation vs the built in C-implementation of `sorted` reveals it's a lot slower, but I think these examples convey the overall idea of the sorting strategies:

``` Python
In [0]: arr = [random.randint(0,10000) for _ in range(10_000)]

In [1]: %timeit sorted(arr)
1.19 ms ± 7.36 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

In [11]: %timeit timsort(arr)
379 ms ± 24.9 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

## BONUS: Quicksort

I think my favorite sorting strategy that I found while studying for the interview was Quicksort. Here's an especially elegant recursive implementation in O(nlogn):

``` Python
def quicksort(arr):
    
    if len(arr) <= 1:
        return arr

    pivot_index = len(arr) // 2
    pivot_value = arr[pivot_index]

    middle = [x for x in arr if x == pivot_value]
    less = [x for x in arr if x < pivot_value]
    more = [x for x in arr if x > pivot_value]

    return quicksort(less) + middle + quicksort(more)
```

Profiling for comparison:
```
In [0]: %timeit quicksort(arr)
19.6 ms ± 70.9 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```
__NOTE__: this is random integer data not "real world" data and most of the benefits of defaulting to timsort are realized when considering real world data and sorting strings.

# October, 2024: Positive and Unlabeled Learning

Positive and unlabeled learning (PUL) is a semi-supervised method of binary classification available when positive samples are reliable and negative samples are missing or unreliable. 

The PUL problem is a common occurrence in the healthcare domain for rare conditions. For example, many diseases are influenced by genetics, it is common that a small number of genes will be known to correlated positively with a disease, but there isn't information about the significance of the rest of the genes on a given disease.

Another healthcare use case is in finding drugs which can treat a given disease. A small set of molecules may be known to have efficacy against the condition, but the rest of the chemicals in a database are of unknown efficacy. Discovering new therapies might be possible with PUL.

The goal of the PU learning is to create a function `f` such that f(x) = p(y = 1|x) with the best accuracy possible. Elkan and Noto (2) prove that this can be done with a non-traditional classifier `g` which predicts g(x) = p(s = 1|x) where s represents whether the sample is labeled 1 or unlabeled 2. 

## Implementation with ScikitLearn

Starting with a random n-class classification problem we make an additional set of PU labels pu_y ∈ {-1,1}:

``` Python
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score

def make_pu_classification():
    """
    Makes a set of features and targets for testing a Positive Unknown (PU) learning
    algorithm.

    Returns Tuple(np.Array, np.Array, np.Array):
        Returns a tuple of arrays in the order (features, traditional labels, positive unknown labels).
    """
    x, y = make_classification(
        n_samples=3000,
        n_features=20,
        n_informative=2,
        n_redundant=2,
        n_repeated=0,
        n_classes=2,
        n_clusters_per_class=2,
        weights=None,
        flip_y=0.01,
        class_sep=1.0,
        hypercube=True,
        shift=0.0,
        scale=1.0,
        shuffle=True,
        random_state=None,
    )
    # Create the PU target data set by converting all of the negative
    # targets to unknowns.
    pu_y = y.copy()
    pu_y[np.where(pu_y == 0)[0]] = -1.0
    return x, y, pu_y

x, y, pu_y = make_pu_classification()
```

In this case we're keeping the full labels as an accuracy test. We can see the traditional classification with an SVM model as a baseline for the PU algorithm:

``` Python
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=None)

# Initialize and train the SVC model. 
model = SVC()
model.fit(x_train, y_train)

# Make predictions on the test data
y_pred = model.predict(x_test)

# Evaluate the model
print(f'Accuracy: {accuracy_score(y_test, y_pred):.2f}')

Out:
    Accuracy: 0.93
```

__NOTE__: The accuracy will vary depending on the random data created for the problem.

Next we'll set up for the PU algorithm described in the unweighted PU learning algorithm (2). We choose an SVM model for `g`, the non-traditional classifier g(x) = p(s = 1|x) of the conditional probability that a sample will be labeled. We choose a validation set size for the untraditional model `g` and a threshold on the probability to consider conclusive in the binary binning of the model.

``` Python
# Define an estimator for non-traditional classifier g(x) = p(s = 1|x), the conditional probability
# that a sample is labeled (s = 1) given the features x. 
g = SVC(probability=True)
# Settings for the size of the validation set of Elkan/Noto PU learning algorithm. . Hold out ratio is the percentage of the
# positive values to withhold from the estimator model.
validation_ratio = 0.2
# The probability threshold for predicting that a sample is classified as true.
threshold = 0.5

# Separate a set of features as a hold out.
all_indices = np.arange(x.shape[0])
validation_size = int(np.ceil(x.shape[0] * validation_ratio))

# Choose indices in the size of validation_size to be used as the 
random_state = check_random_state(None)
random_state.shuffle(all_indices)
validation_indices = all_indices[:validation_size]
```

Finally we train the model and check the accuracy:

``` Python
x_validation = x[validation_indices]
y_validation = pu_y[validation_indices]
x_pos_validation = x_validation[np.where(y_validation == 1)]

# Training set
g.fit(x[~validation_indices], pu_y[~validation_indices])

# c is calculated based on holdout set predictions
hold_out_predictions = g.predict_proba(x_pos_validation)
hold_out_predictions = hold_out_predictions[:, 1]

# The constant probability that a positive sample is labeled.
c = np.mean(hold_out_predictions)

f = g.predict_proba(x) / c

y_pu = np.array([1.0 if p > threshold else 0.0 for p in f[:, 1]])

# Evaluate the model
print_accuracy_report(y, y_pu)

Out:
    Accuracy: 0.92
```

Neat! There are a lot of improvements which can be made on this approach, but we've demonstrated the basic working of the proof. See the references for further reading.

References:
1. [POSITIVE AND UNLABELED LEARNING ALGORITHMS AND APPLICATIONS:
A SURVEY](https://sensip.engineering.asu.edu/wp-content/uploads/2020/03/Jaskie_IISA_2019_Applications-and-Approaches-to-the-Positive-and-Unlabeled-Learning-problem-A-Survey-Final-Version.pdf)
1. [Learning Classifiers from Only Positive and Unlabeled Data](https://cseweb.ucsd.edu/~elkan/posonly.pdf)

# September, 2024: UV

This month I learned (or rather started using) UV, the Python package manager written in Rust. For years I've been using `pyenv` and `pipenv` to manage Python versions and environments/packages respectively. I liked the ergonomics and appreciated the features.

For PyEnv I liked:
1. Easy to install multiple versions of Python. 
2. A file checked into the project repository can tell other contributors what Python version to use and tell pyenv which python version to use based on the working directory.
3. It's written in bash, it's pretty fast and doesn't require installing other dependencies.

For pipenv I liked:
1. Deterministic builds from the lockfile.
2. Easy virtual env creation and destruction.
3. The `run` and `shell` commands make `source .venv/activate` and `deactivate` unnecessary.
4. Handling of environment variables.

Pain points:
1. When creating a new virtual env in a project `pipenv` isn't always aware of the Python version being set in the .python-version file so it's necessary to do something like `pipenv install --python $(cat .python-version)`. Not a big deal, but it's a pitfall (or maybe pipfall 😂) when someone is using the project.
1. There's no assurance when you make an environment that the Python version in the .python-version file is installed. 

## Enter UV

UV is the first tool I've looked at which will solve my use case with a single tool and it's simple enough to compel me to change. I had previously investigated Rye, but there were ergonomics for creating lock files for example that I didn't want to have to deal with, so I put a pin in it as "that's something I should probably use, but I'm not goint to switch now". With UV I've made the change.

The biggest change for me was away from Pipfile/Pipfile.lock and .python-version files to a pyproject.toml. This is a big change, but it's toward the community and I see it as a benefit although there is some friction. The pipenv and pyenv files are bespoke and have a learning curve for new engineers on a project.

I still get my non-negotiables:
1. Deterministic builds with a hash based lock file.
1. Easy to install multiple Python versions without downloading.
1. A project definition file in the repo calls out the Python version.

And a lot of what I liked:
1. Easy to create and destroy virtual envs. 
1. `Run` command.

Improvements:
1. One tool which will make sure that the Python version specified by the project is installed and the correct version is used in the virtual environment.
1. None of the fiddly .xrc file setup required to initialize pyenv.
1. Faster.

Tradeoffs:
1. No .env file handling so environment variables need to be handled another way.
1. Requires Rust.
1. No `shell` command, but `run` covers all the use cases, it was a nice to have. 

## Brief Usage Notes

My workflow is something like this:

1. I need a new project: `uv init project_name && cd project_name`
1. I need to add a dependency: `uv add ipython` or I can add several at once in the pyproject.toml `dependecies` list.
1. Run a script or start a REPL in the environment: `uv run ipython`

I did initially make a few aliases:
```
alias vact='source .venv/bin/activate'
alias vd=deactivate
```
I used these before the `run` command was released, but I find I don't use them anymore.

## Fix for the .env loading functionality

In some cases I've used python-dotenv in projects to load the .env content I need in my Python projects.

Another tool I've used is [direnv](https://github.com/direnv/direnv). This will load any .env file into the environment from the current working directory and unload it on change directory. 

# January, 2023: Hugo TIL

This will be my first TIL post about how I made this site with Hugo.

## Getting started

[Hugo](https://gohugo.io) is a simple static site generator written in GoLang with a wide range of open source themes available. This site is using the [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme.

Getting started is as easy as: 
1. Installing hugo `brew install hugo` 
1. Making a new project `hugo new site <SITE-NAME> -f yml`
1. Initializing the newly created project directory as a git repository
```
cd <SITE-NAME>
git init
```
1. Check out a [theme](https://themes.gohugo.io) as a submodule, for this site we're using PaperMod: 
```
git submodule add --depth=1 https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod
git submodule update --init --recursive # needed when you re-clone your repo (submodules may not get cloned automatically)
```
1. See your new site with `hugo server` then go to http://localhost:1313.

## Next steps

Deploy on Github pages. 
1. Create a repository with your github username: `<USERNAME>.github.io`. See more information about [github pages](https://pages.github.com).
1. Check out the github pages repository as a submodule into the public directory in your Hugo project. `git submodule add git@github.com:<USERNAME>/<USERNAME>.github.io.git public`.
1. After generating some content create the site `hugo` then add the output to the public directory `cd public && git add .`.
1. Push the changes: `git push`
1. [TODO] Next steps: deploy with github actions [Hugo deployment docs](https://gohugo.io/hosting-and-deployment/hosting-on-github/)

### Make a favicon

I made the simple favicon for this site using a [favicon generator](https://favicon.io/favicon-generator/). Unzip the download into the `<SITE-NAME>/static` directory.

### Customize the theme

Follow the directions in the theme to customize your site to your liking. In this case for PaperMod I chose to use profile mode and added an image for the landing page.

## Release

TO release changes to the site:
1. Make changes in the content/ directory for the Hugo parent project.
1. Check the changes with `hugo server`