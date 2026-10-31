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
