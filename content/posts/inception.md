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

# October, 2024: Positive and Unlabeled Learning

Positive and unlabeled learning (PUL) is a semi-supervised method of binary classification available when positive samples are reliable and negative samples are missing or unreliable. 

The PUL problem is a common occurrence in the healthcare domain for rare conditions. For example, many diseases are influenced by genetics, it is common that a small number of genes will be known to correlated positively with a disease, but there isn't information about the significance of the rest of the genes on a given disease.

Another healthcare use case is in finding drugs which can treat a given disease. A small set of molecules may be known to have efficacy against the condition, but the rest of the chemicals in a database are of unknown efficacy. Discovering new therapies might be possible with PUL.

The goal of the PU learning is to create a function `f` such that f(x) = p(y = 1|x) with the best accuracy possible. Elkan and Noto (2) prove that this can be done with a non-traditional classifier `g` which predicts g(x) = p(s = 1|x) where s represents whether the sample is labeled 1 or unlabeled 2. 

## Implementation with ScikitLearn

Starting with a random n-class classification problem we make an additional set of PU labels pu_y ∈ {-1,1}:

```
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

```
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

```
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

```
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