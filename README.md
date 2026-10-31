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

## Purchase shares by category for an age range

Run `main.py` with the `share-by-age` argument to display each category's share of total spending for users aged 18 to 25, inclusive:

```bash
.venv/bin/python main.py share-by-age
```

The output includes `category`, `total_amount`, and `share_percent`. Each share is calculated as the category total divided by total spending across all categories for the selected age range, multiplied by 100 and rounded to two decimal places. Results are sorted by total amount in descending order. If total spending is zero, shares are displayed as zero.

To select a different age range, change the last two arguments (`18` and `25`) in the `purchases_share_by_users_age_range` call in `main.py`. Both boundaries are included.

## Top 3 categories by purchase share for an age range

Run `main.py` with the `top-3-by-age` argument to display the three categories with the highest spending shares for users aged 18 to 25, inclusive:

```bash
.venv/bin/python main.py top-3-by-age
```

The output includes `category`, `total_amount`, and `share_percent`, sorted by share in descending order and limited to three categories. Each share is calculated from total spending across all categories for the selected age range, before selecting the top three.

To select a different age range, change the last two arguments (`18` and `25`) in the `purchases_share_by_users_age_range` call under `top-3-by-age` in `main.py`. Both boundaries are included.
