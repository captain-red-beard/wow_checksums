# WoW Hashes
Verification of files for a popular MMORPG.

Currently only supports 3.3.5a.

## How to use
Run the following command in your terminal
```
python get_checksums.py ../path_to_where_your_client_files_are
```
then run
```
python compare_result.py enUS
```
replacing enUS with your specific localization.

## Todo
- Put am empathesis that hashes of hashes cannot be trusted, so take those results as a grain of salt
- Switch to recursive directory hashing so every directory can have a hash returned back up to it's parent directory