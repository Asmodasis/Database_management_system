# Database Management System


[![license](https://img.shields.io/github/license/asmodasis/Database_management_system.svg)](LICENSE)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

This is an example file with maximal choices selected.

This repository is for a database management system designed for the course Cs657 at the University of Nevada, Reno. Taught by Dr. Dongfang Zhao. Database management systems handle the table operations like: creating, deleting, updating and querying tables. As well as the management 


## Table of Contents

- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [API](#api)
- [Contributing](#contributing)
- [License](#license)


## Install

This module depends upon a knowledge of [Markdown]().

```sh
$ sudo apt-get install python3
$ sudo apt-get install python3-pip
$ sudo python3 -m pip install os
$ sudo python3 -m pip install shutil
```

### File Dependencies
 - The transaction states are tracked with a text file named transaction_state.txt. This file is required for the usage of transactions.

## Usage

```sh
$ python3 DBMS.py 
>> CREATE DATABASE db_1;
>> CREATE TABLE tbl_1 (a1 int, a2 varchar(20)); 
```
Will activate SQL input mode. For the sake of demonstrating transactions. This project will only support SQL input mode.
Please input each command in the file PA4_test.sql sequentially. 


## Meta

Shawn Ray - shawnray@nevada.unr.edu

[Github](https://github.com/Asmodasis)

## Contributing

1. Fork it (<https://github.com/Asmodasis/Database_Management_system/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## License

[MIT](../LICENSE)