# data-directory
This directory contains data files (.dat), which are generically read and written using the mytrades-functions "read_matrix" and "write_matrix".

There are currently two data files, which are storing data about your personal depot and related item transactions. Data files don't have fixed field length, fields are separated by pipe character (|).

## depot.dat
This file stores information about your depot items. Before you're able to add transactions to a depot item it must be added here first. All depot items are identified by the Yahoo Finance Symbol which can be looked up here: https://de.finance.yahoo.com/. The file structure is as follows:

- Symbol (string)
- ISIN (string)
- Short Name (string)

## transactions.dat
This file stores information about your item transactions. So every buy or sell of item units must be tracked here. Every buy is identified by a positive unit value, every sell by a negative unit value. The file structure is as follows:

- Symbol (string)
- Timestamp (datetime)
- Units (float)
- UnitPrice (float)
- Fees (float)
