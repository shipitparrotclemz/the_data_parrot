# The Simpson's Paradox

Ahoy parrot!

This is a repository of code examples for the Data Parrot Newsletter!

If you are an aspiring Data Analyst, Data Scientist or Machine Learning Engineer, this newsletter is just for you!

The medium article for this repository is here:
- https://medium.com/@shipitparrot/the-data-parrot-simpsons-paradox-3796b312a67

## Displaying the Seeds foraged by each parrot

```commandline
// Create a virtual environment, with python 3.9
virtualenv venv -p $(which python3.9)

// Activate the virtual environment
source venv/bin/activate

// Install the requirements into your virtual environment
pip install -r requirements.txt

// Run the bar plot script
python3 plot_seeds_by_parrot.py
```