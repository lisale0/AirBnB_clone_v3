<img src="https://github.com/johncoleman83/AirBnB_clone/blob/master/dev/HBTN-hbnb-Final.png" width="160" height=auto />

# AirBnB Clone Phase #1

: python BaseModel Class, unittests, python CLI, & web static

## Description

Project attempts to clone the the AirBnB application and website, including the
database, storage, RESTful API, Web Framework, and Front End.

## Environment

* __OS:__ Ubuntu 14.04 LTS
* __language:__ Python 3.4.3
* __style:__ PEP 8 (v. 1.7.0)

<img src="https://github.com/johncoleman83/AirBnB_clone/blob/master/dev/hbnb_step5.png" />

## Testing


#### `unittest`

This project uses python library, `unittest` to run tests on all python files.
All unittests are in the `./tests` directory with the command:

* `python3 -m unittest discover -v ./tests/`

The bash script `init_test.sh` executes all these tests:

  * checks `pep8` style

  * runs all unittests

  * runs all w3c_validator tests

  * cleans up all `__pycache__` directories and the storage file, `file.json`

**Usage:**

```
$ ./dev/init_test.sh
```

#### CLI Interactive Tests

This project uses python library, `cmd` to run tests in an interactive command
line interface.  To begin tests with the CLI, run this script:

```
$ ./console.py
```

* For a detailed description of all tests, run these commands inside the
custom CLI:

```
$ ./console.py
(hbnb) help help
List available commands with "help" or detailed help with "help cmd".
(hbnb) help

Documented commands (type help <topic>):
========================================
Amenity    City  Place   State  airbnb  create   help  show
BaseModel  EOF   Review  User   all     destroy  quit  update

(hbnb) help User
class method with .function() syntax
        Usage: User.<command>(<id>)
(hbnb) help create
create: create [ARG]
        ARG = Class Name
        SYNOPSIS: Creates a new instance of the Class from given input ARG
```

* Tests in the CLI may also be executed with this syntax:

  * **destroy:** `<class name>.destroy(<id>)`

  * **update:** `<class name>.update(<id>, <attribute name>, <attribute value>)`

  * **update with dictionary:** `<class name>.update(<id>, <dictionary representation>)`


#### Continuous Integration

Uses [Travis-CI](https://travis-ci.org/) to run all tests on all commits to the
github repo

#### API Tests
In order to run the api, you need to open up the endpoint (route)
```
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5000 python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
...
```
In another terminal, you can test the API calls:
##### State
|   **Description**                  |  **HTTP Method** |   **format**   | 
|------------------------------------|------------------|----------------|
| Retrieve list of all state objects |     GET          | /api/v1/states |
| Retrieve  a state object   |     GET          | /api/v1/states/<state_id> |
| Delete a state object   |     DELETE          | /api/v1/states/<state_id> |
| Create a new state object   |     POST          | /api/v1/states |
| Alter a  state object   |     PUT          | /api/v1/states/<state_id> |

##### City
|   **Description**                  |  **HTTP Method** |   **format**   | 
|------------------------------------|------------------|----------------|
| Retrieve list of all city objects |     GET          | /api/v1/states/<state_id>/cities |
| Retrieve  a city object   |     GET          | /api/v1/cities/<city_id> |
| Delete a city object   |     DELETE          | /api/v1/cities/<city_id> |
| Create a new city object   |     POST          | /api/v1/states/<state_id>/cities |
| Alter a  city object   |     PUT          | /api/v1/cities/<city_id> |


##### Amenity
|   **Description**                  |  **HTTP Method** |   **format**   | 
|------------------------------------|------------------|----------------|
| Retrieve list of all amenity objects |     GET          | /api/v1/amenities |
| Retrieve  an amenity object   |     GET          | /api/v1/amenities/<amenity_id> |
| Delete an amenity object   |     DELETE          | /api/v1/amenities/<amenity_id> |
| Create a new amenity object   |     POST          | /api/v1/amenities |
| Alter an amenity object   |     PUT          | /api/v1/amenities/<amenity_id> |

##### User
|   **Description**                  |  **HTTP Method** |   **format**   | 
|------------------------------------|------------------|----------------|
| Retrieve list of all user objects |     GET          | /api/v1/users |
| Retrieve  a user object   |     GET          | /api/v1/users/<user_id> |
| Delete a user object   |     DELETE          | /api/v1/users/<user_id> |
| Create a new user object   |     POST          | /api/v1/users |
| Alter a user object   |     PUT          | /api/v1/users/<user_id> |

##### Place
|   **Description**                  |  **HTTP Method** |   **format**   | 
|------------------------------------|------------------|----------------|
| Retrieve list of all place objects |     GET          | /api/v1/cities/<city_id>/places |
| Retrieve a place object   |     GET          | /api/v1/places/<place_id> |
| Delete a place object   |     DELETE          | /api/v1/places/<place_id> |
| Create a new place object   |     POST          | /api/v1/cities/<city_id>/places |
| Alter a place object   |     PUT          | /api/v1/places/<place_id> |

## Authors
* Stuart Kuredjian [@dbconfession78](https://github.com/dbconfession78)
* Lisa Leung [@lisale0](https://github.com/lisale0)
* MJ Johnson, [@mj31508](https://github.com/mj31508)
* David John Coleman II, [davidjohncoleman.com](http://www.davidjohncoleman.com/)
* Kimberly Wong, [kjowong](http://github.com/kjowong) | [@kjowong](http://twitter.com/kjowong) | [kjowong@gmail.com](kjowong@gmail.com)
* Carrie Ybay, [hicarrie](http://github.com/hicarrie) | [@hicarrie_](http://twitter.com/hicarrie_)

## License

Public Domain, no copyright protection
