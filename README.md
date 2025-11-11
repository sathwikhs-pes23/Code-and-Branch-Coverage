# Code-and-Branch-Coverage

This repository demonstrates the principles of code and branch coverage through a simple Python-based order processing system. It includes functions to calculate discounts and update order statuses, along with a comprehensive test suite using `pytest` designed to achieve high coverage.

## Core Logic

The primary logic is contained within `order_processor.py`.

### `calculate_discount(customer_type, total_amount)`

This function calculates a discount based on the customer's type and the total order amount. The discount rules are as follows:

-   **Regular Customers:**
    -   Receive a 5% discount for orders over $1000.
    -   No discount for orders of $1000 or less.
-   **Premium Customers:**
    -   Receive a 10% discount on all orders.
-   **VIP Customers:**
    -   Receive a 20% discount for orders over $5000.
    -   Receive a 10% discount for orders of $5000 or less.
-   An unknown customer type will raise a `ValueError`.

### `update_order_status(order)`

This function updates the status of an order based on its current state. The order is represented as a dictionary.

-   If the status is `"pending"`:
    -   It changes to `"processing"` if the order is paid.
    -   It changes to `"awaiting_payment"` if the order is not paid.
-   If the status is `"processing"`:
    -   It changes to `"shipped"` if all items are available.
    -   It changes to `"backorder"` if items are not available.
-   Orders with any other status remain unchanged.

## Testing for Coverage

The test suite in `test_processor_CS536.py` uses the `pytest` framework to verify the correctness of the order processing logic. The tests are specifically written to cover various execution paths and decision branches within the functions.

-   **`test_calculate_discount`**: Uses `pytest.mark.parametrize` to efficiently test all customer types, amount thresholds, and edge cases, including the handling of unknown customer types.
-   **`test_update_order_status`**: Includes individual tests for each possible state transition (`pending` -> `processing`, `pending` -> `awaiting_payment`, etc.) and a test to ensure that statuses like `"shipped"` are not modified.

## Running the Tests

To run the tests locally, you will need Python and `pytest`.

### 1. Clone the Repository

```bash
git clone https://github.com/sathwikhs-pes23/Code-and-Branch-Coverage.git
cd Code-and-Branch-Coverage
```

### 2. Install Dependencies

The only dependency is `pytest`.

```bash
pip install pytest
```

### 3. Execute the Test Suite

Run `pytest` from the root directory of the project.

```bash
pytest
```

The output will show the results of all executed tests. You can also run pytest with coverage flags to generate a coverage report.

```bash
pytest --cov=order_processor --cov-report=term-missing
