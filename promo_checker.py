"""Check product IDs against a locally maintained promotion exclusion list."""
from pathlib import Path


def load_products(path):
    """Load one excluded product ID per line; ignore blanks and comments."""
    with Path(path).open(encoding='utf-8') as source:
        return {line.strip().upper() for line in source
                if line.strip() and not line.lstrip().startswith('#')}


def check_product(product_id, excluded_products):
    product_id = product_id.strip().upper()
    if not product_id or not product_id.isascii() or not product_id.isalnum():
        return 'Please enter a product ID using letters and numbers.'
    if product_id in excluded_products:
        return 'YELLOW DOT: excluded from this promotion according to the saved list.'
    return 'NOT ON EXCLUSION LIST: check the current promotion sheet before confirming a discount.'


def main():
    data_file = Path(__file__).resolve().parent / 'excluded_products.txt'
    try:
        excluded_products = load_products(data_file)
    except OSError as error:
        print(f'Could not load the product list: {error}')
        return
    print('YELLOW DOT PROMO CHECKER')
    print('Saved-list lookup only. Footwear is outside the scope of this list.')
    print("Type 'exit' to finish.\n")
    while True:
        try:
            product_id = input('Enter product ID: ')
        except (EOFError, KeyboardInterrupt):
            print('\nFinished.')
            break
        if product_id.strip().upper() == 'EXIT':
            print('Finished.')
            break
        print(check_product(product_id, excluded_products), '\n')


if __name__ == '__main__':
    main()
