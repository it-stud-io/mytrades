# code-directory
This directory holds mytrades bsh-like python program files. There is a file for every use case in the application - all of these files must be executable (chmode +x) on OS level. In addition there is one python file (mytrades.py) which stores all general functionality and business logic.

## depot use cases
These are the depot related use case program files:
- List Depot Items: listdepotitems
- Add Depot Item: adddepotitem
- Remove Depot Item: removedepotitem - only works if there are no transactions related to the item, or if the transaction total unit sum equals 0 and last transaction is older than 3 years


## trasaction use cases
- List Transaction: listtransactions
- Add Transaction: addtransaction - there is no option to delete/remove transactions -> if you need to revert a transaction you will just have to add the negative counterpart
