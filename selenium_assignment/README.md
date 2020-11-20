- [Selenium Assignment](#selenium-assignment)
  * [About](#about)
  * [Features](#features)
  * [How to run](#how-to-run)
    + [Selenium](#selenium)
    + [Config](#config)
    + [Running tests](#running-tests)
  * [Folder Structure](#folder-structure)
    + [drivers_package](#drivers-package)
    + [helper_methods](#helper-methods)
    + [logging_package](#logging-package)
    + [logs](#logs)
    + [test_bundles](#test-bundles)
    + [test_eobuwie](#test-eobuwie)
    + [test_steam](#test-steam)
  * [Scenarios](#scenarios)
    + [Steam](#steam)
      - [Login](#login)
      - [Test Steam Cart](#test-steam-cart)
      - [Test Steam Wishlist](#test-steam-wishlist)
    + [Eobuwie](#eobuwie)
      - [Login](#login-1)
      - [Test Eobuwie Cart](#test-eobuwie-cart)
      - [Test Eobuwie Cart](#test-eobuwie-cart-1)

## Selenium Assignment
### About
This directory contains python 3.7 + selenium project that tests two websites: [steam](https://store.steampowered.com/) and [eobuwie](https://www.eobuwie.com.pl/).
### Features
- Multiple scenarios for both websites
- Info Logging to timestamped files
- Easy switching between browsers
****
### How to run
I assume that you have python 3.3+ installed
#### Selenium
In order to run this project you need to have [selenium](https://selenium-python.readthedocs.io/installation.html) installed
```bash
pip install selenium 
```
You may want to consider using venv.

Alretnatively you may utilize the requirement.txt file present in the repo and do:
```bash
pip install -r requirements.txt
```
#### Config
In order to utilize tests present in the project you need to create **config.json** file in this directory:
```bash
2021_TAU/selenium_assignments/config.json
```
Config Template is available in the repository and looks like this:
```json
{
    "username": "",
    "password": "",
    "email": "",
    "driver": ""
}
```
**username**: steam username required to login
**password**: password for the test account used in testing
**email**: test e-mail used as a login for the e-obuwie website
**driver**: supply either: "chrome", "firefox" or "opera" - if you'd like to test a different browser, this is the place where you change it
#### Running tests
In order to run tests you need to **cd** into the directory that contains tests:
*/test_bundle
*/test_steam
*/test_eobuwie
```bash
cd path/to/project/2021_TAU/selenium_assignments/test_steam/
```
and then run it using python 3:
```bash
python3 name_of_test_file.py
```
****
### Folder Structure
#### drivers_package
This directory contais a simple script that choose a driver based on the **config["driver"]** value.
#### helper_methods
This directory contains simple scripts that help with waiting for certain elements of websites to be loaded.
#### logging_package
This directory contains logging functionality.
In order to log files you need to import this two methods into the test file:
```python
from logging_package.logger import create_logfile
from logging_package.logger import create_log
```
At the beggining of your test call the method to create a logfile in the logs directory:
```python
create_logfile()
```
The create_log method takes two arguments:
- log_level [integer] - values taken from the standard python logging package and can be: 20, 30, 40 or 50, by default the logging is set to INFO (20) 
- log_message ["string"] - message that you want to log
Example:
```python
create_log(20, "your log message")
```
#### logs
This directory contains logs after your tests ran - logs themselves are not stored in repo.
#### test_bundles
This directory contains bundles of tests - multiple tests running after eachother. Currently there is only one bundle: test_bundle_login.py that tests login process for both websites.
#### test_eobuwie
This directory contains [eobuwie](https://www.eobuwie.com.pl/).
#### test_steam
This directory contains tests for [steam](https://store.steampowered.com/).
****
### Scenarios
#### Steam
##### Login
1. Go to [steam](https://store.steampowered.com/)
2. Click on the login button
3. Submit credentials
##### Test Steam Cart
1. Go to [steam](https://store.steampowered.com/)
2. Click on the login button
3. Submit credentials
4. Input "Cyberpunk 2077" into the searchbar on the main website
5. Press search
6. Choose "Cyberpunk 2077" from the list
7. Add "Cyberpunk 2077" to the cart
8. Check if "Cyberpunk 2077" is in the cart
9. Remove "Cyberpunk 2077" from the cart
##### Test Steam Wishlist
1. Go to [steam](https://store.steampowered.com/)
2. Click on the login button
3. Submit credentials
4. Input "Cyberpunk 2077" into the searchbar on the main website
5. Press search
6. Choose "Cyberpunk 2077" from the list
7. Add "Cyberpunk 2077" to the wishlist
8. Go to the wishlist
9. Check if "Cyberpunk 2077" is on the wishlist
10. Remove "Cyberpunk 2077" from the wishlist
#### Eobuwie
##### Login
1. Go to [eobuwie](https://www.eobuwie.com.pl/)
2. Close GDPR pop up
3. Click on login button
4. Submit credentials
##### Test Eobuwie Cart
1. Go to [eobuwie](https://www.eobuwie.com.pl/)
2. Close GDPR pop up
3. Click on login button
4. Submit credentials
5. Search for black shoes in the searchbar on the profile page
6. Click on the first result
7. Add to the cart
8. Choose the size of the shoes
9. Go to the shopping cart
10. Check if shoes are in the shopping cart and remove them
##### Test Eobuwie Cart
1. Go to [eobuwie](https://www.eobuwie.com.pl/)
2. Close GDPR pop up
3. Click on login button
4. Submit credentials
5. Search for black shoes in the searchbar on the profile page
6. Add the first result to the faviourites list
7. Go to the favourites list
8. Delete from the favourites list
