import argparse
import logging

from bot.client import BinanceClient
from bot.orders import create_order
from bot.validators import validate_side, validate_order_type, validate_price
from bot.logging_config import setup_logging


def main():

    setup_logging()
    logging.info("CLI started")

    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    validate_side(args.side)
    validate_order_type(args.type)
    validate_price(args.type, args.price)

    client = BinanceClient()
    client.set_leverage(args.symbol, 20)
    response = create_order(
        client,
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    # Print full API response
    print("\nFull Response:", response)

    if "orderId" in response:
        print("Order ID:", response["orderId"])
        print("Status:", response["status"])
        print("Executed Qty:", response["executedQty"])
    else:
        print("Order failed or API returned error")


if __name__ == "__main__":
    main()