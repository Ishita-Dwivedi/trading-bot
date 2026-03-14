# Simplified Binance Futures Trading Bot

This project is a Python CLI trading bot that places orders on Binance Futures Testnet.

## Features
- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL
- CLI input validation
- Logging of requests and responses
- Error handling

## Setup

1. Clone repository
2. Install dependencies

pip install -r requirements.txt

3. Add API keys in config.py

## Example Usage

Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 72000