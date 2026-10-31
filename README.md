## Install dependencies

Make sure Python with `venv` support is installed, then run from the project directory:

```bash
bash run.sh
```

The script creates a `.venv` virtual environment if needed and installs dependencies from `requirements.txt`.

## Display data

Data is displayed only when `main.py` is called with the `show` argument:

```bash
.venv/bin/python main.py show
```

## Total purchases by category

Run `main.py` with the `sum` argument to display the total purchase amount for each category:

```bash
.venv/bin/python main.py sum
```

The total is calculated as the sum of `quantity * price` for each category, rounded to two decimal places and sorted by total amount in descending order.

## Total purchases by category for an age range

Run `main.py` with the `sum-by-age` argument to display the total purchase amount for each category for users aged 18 to 25, inclusive:

```bash
.venv/bin/python main.py sum-by-age
```

To select a different age range, change the last two arguments (`18` and `25`) in the `purchases_by_users_age_range` call in `main.py`. They specify the minimum and maximum age, and both boundaries are included. Age limits are currently configured in the code, not through command-line arguments.

The total is calculated as the sum of `quantity * price` for each category, rounded to two decimal places and sorted by total amount in descending order.
