# mytrades
MyTrades is a small and tiny application to manage a personal depot/stock. This means, you can add, list and remove depot items (based on Yahoo Finance, https://de.finance.yahoo.com)  and add/list transactions to/of them.

After managing your personal depot/stock, you are able to create graphs about the development of the items.

## technology
The tool uses Python programming language and is built on top of Linux Bash.

Pre-Requisites:
- Linux OS (Fedora, Ubuntu...)
- Python 3.7 (most probably runs with every Python 3.X version, was build on top of 3.7), including pip3 packages:
  - yfinance 0.1.59
  - console-menu 0.6.0

## installation + launch
1. make sure pre-requisites are met
2. clone gitrepo locally into an empty directory (e.g. `mytrades`)
3. chmod +x to `trade` file in root directory and to all files in directory `code`
4. run `.\trade` in root directory

## usage
In the console menu select option #1 to go to sub-menu "Depot". Here you are able to add new items to your depot using selection #2. When adding an item, the program asks for a symbol code. This code must be existing in the Yahoo Finance database. The tool does an online lookup of the symbol (internet connection needed!). In the Depot msub-menu you have the two further options to list or remove items.
In the sub-menu "Transactions" you are able to add transactions (by selecting menu entry #2) to a depot item. Every transaction will ask for a depot item symbol (Yahoo Finance symbol), a "booking" time stamp, a unit value (positive = buy, negative = sell), a unit price and a possible fee. Transactions can be listed (grouped by depot item, but not removed. Removing a transaction can be achieved by adding a negation of the transaction.
