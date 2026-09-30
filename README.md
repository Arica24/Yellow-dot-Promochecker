# Yellow Dot Promotion Checker

A small Python tool I originally built in Carnets on iOS to help with product checks during my part-time retail job.

## Why I built it

Some products were excluded from a promotion and needed a yellow dot sticker to show they remained full price. Checking product IDs across several printed pages was slow, especially while helping customers or replenishing stock.

I made a phone-based lookup: enter a product ID and check whether it appears in the saved exclusion list. Footwear was outside the scope because the small number of footwear exclusions was already familiar to the team.

## Features

- Look up product IDs using a Python set.
- Accept lowercase input and remove surrounding spaces.
- Validate basic input.
- Keep checking until the user types `exit`.
- Maintain product IDs in a separate text file.

## Run on a computer

Requires Python 3.9 or newer. No extra packages are required.

Keep `promo_checker.py` and `excluded_products.txt` in the same folder. Open a terminal in that folder and run:

```bash
python3 promo_checker.py
```

On Windows, use `python promo_checker.py` if needed.

Example:

```text
Enter product ID: kd8313
YELLOW DOT: excluded from this promotion according to the saved list.
```

If a product is absent, the tool asks you to check the current promotion sheet. An absent ID could be a typo, a footwear item or an item missing from an outdated list; absence alone does not confirm a discount.

## Carnets on iOS

Copy both files into the same Carnets working folder. In a notebook cell, run:

```python
%run promo_checker.py
```

The computer version was checked with Python; the revised version has not been tested in Carnets.

## Updating the list

Edit `excluded_products.txt`: use one product ID per line. Blank lines and lines beginning with `#` are ignored. Duplicate IDs are removed automatically when loaded.

The bundled list is historical and user-supplied. It is not an authoritative source of current pricing or promotion rules. Both IA7520 and UA7520 are retained from the original code and need checking against the source sheet.

## Improvements to the original

The original inline set had missing commas. Python silently joined adjacent strings, so some genuine product IDs could not be found. Separating the IDs into a text file removes that issue.

The original code also reported every unlisted ID as being on promotion. This version reports that it is absent from the exclusion list and asks for confirmation.

## Skills demonstrated

Python functions, sets, loops, conditional logic, string handling, file handling, input validation and solving a practical workplace problem.

## Attribution

Original concept and lookup code by Arica Bhuiyan. 


