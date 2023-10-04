## Accounts
### Signup
`
curl --location 'http://localhost:8000/api/accounts/signup' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Bob smith",
    "email": "bob@gmail.com",
    "password": "password",
    "password2": "password"
}'
`
### SignIn 
`
curl --location 'http://localhost:8000/api/token/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "bob@gmail.com",
    "password": "password"
}'
`

&nbsp;
## Realtors
### Realtors List View 
`
curl --location 'http://localhost:8000/api/realtors/'
`

### Realtors Topseller
`
curl --location 'http://localhost:8000/api/realtors/topseller'
`

### Realtors Retrieve View 
`
curl --location 'http://localhost:8000/api/realtors/2' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkzODQ5MzI1LCJpYXQiOjE2OTM4NDkwMjUsImp0aSI6Ijk0ODJhNzk4M2QzMzQ3OGViNjI2NjU5OGZlZGQzYzA3IiwidXNlcl9pZCI6MX0.BnwkR4xUOv4iWT3uAc6NBwkq2lx9zEcAwCjguy6C8mQ'
`

&nbsp;
## Listings 
### Listings list
`
curl --location 'http://localhost:8000/api/listings/'
`

### Retrieve Listings
`
curl --location 'http://localhost:8000/api/listings/4531-rockford-mountain-lane' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkzODkyMzA3LCJpYXQiOjE2OTM4OTIwMDcsImp0aSI6IjZkZTA4MmU0YmUzYjQxY2NhYzdlYWM0MTdhOTg2NWM2IiwidXNlcl9pZCI6MX0.bc-7itwOA-kF-hvmR3XsgFJsz48fJeycv6bo9xqF9ZE'
`

### Listings Search 
`
curl --location 'http://localhost:8000/api/listings/search' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk0MDU4NjEwLCJpYXQiOjE2OTQwNTgzMTAsImp0aSI6IjYzZGQwNDljZDkxZDQwYWRiMjU5NjI4ODg1M2Y4NjgyIiwidXNlcl9pZCI6MX0.KlYYMAcx_oYv6VvCuzAB3eTpZzDJ4icAHOahZTo18jM' \
--data '{
    "sale_type": "For Sale",
    "price": "$400,000+",
    "bedrooms": "1+",
    "home_type": "House",
    "bathrooms": "1+",
    "sqft": "1000+",
    "days_listed": "Any",
    "has_photos": "3+",
    "open_house": "false",
    "keywords": ""
}'
`

&nbsp;
## Contact
### New Request
`
curl --location 'http://localhost:8000/api/contacts/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Thomas Anderson",
    "email": "thomas@gmail.com",
    "subject": "Looking to buy a home",
    "message": "Hello world"
}'
`
