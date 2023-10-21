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


&nbsp;
## Services
### CA Services Retrieve
`
curl --location 'http://localhost:8000/api/services/3' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk3MDIxNzIxLCJpYXQiOjE2OTcwMjE0MjEsImp0aSI6Ijc4MTE5M2FhYjllNjRlNTdiN2FjOWUwOTEwMmRmYmM5IiwidXNlcl9pZCI6MX0.TfW0BI9OCCSW0uv-c8T7mVosmBEfTmxNJwMlmPNdQwY'
`

### Service List View
`
curl --location 'http://localhost:8000/api/services/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk3MDIxNzIxLCJpYXQiOjE2OTcwMjE0MjEsImp0aSI6Ijc4MTE5M2FhYjllNjRlNTdiN2FjOWUwOTEwMmRmYmM5IiwidXNlcl9pZCI6MX0.TfW0BI9OCCSW0uv-c8T7mVosmBEfTmxNJwMlmPNdQwY'
`

### Create Services
`
curl --location 'http://localhost:8000/api/services/create' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk3ODkyODEwLCJpYXQiOjE2OTc4OTI1MTAsImp0aSI6ImI1MGY1ODBiODRlYTRmOTRhYWM3MjBhYWFhMjcyODJjIiwidXNlcl9pZCI6MX0.Eg2W7JvJ60mu8qufxBhPb7qyYn58A3e56jkM5yf21ZM' \
--form 'ca_id="4"' \
--form 'short_title="ITR Filing"' \
--form 'subtitle="File your ITR returns"' \
--form 'intro_photo=@"/path/to/file"' \
--form 'price="1000"' \
--form 'intro_video=@"/path/to/file"' \
--form 'title="ITR Filing Title"' \
--form 'service_required_for="For Salaried / Self own business"' \
--form 'description_main="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry'\''s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."' \
--form 'description_1="Description 1"' \
--form 'description_2="Description 2"' \
--form 'description_3="Description 3"' \
--form 'description_4="Description 4"' \
--form 'description_5="Description 5"' \
--form 'description_6="Description 6"' \
--form 'description_7="Description 7"' \
--form 'description_8="Description 8"' \
--form 'service_include_1="Service Included 1"' \
--form 'service_include_2="Service Included 2"' \
--form 'service_include_3="Service Included 3"' \
--form 'service_include_4="Service Included 4"' \
--form 'service_include_5="Service Included 5"' \
--form 'service_include_6="Service Included 6"' \
--form 'service_include_7="Service Included 7"' \
--form 'service_include_8="Service Included 8"' \
--form 'document_required_1="Documents required 1"' \
--form 'document_required_2="Documents required 2"' \
--form 'document_required_3="Documents required 3"' \
--form 'document_required_4="Documents required 4"' \
--form 'document_required_5="Documents required 5"' \
--form 'document_required_6="Documents required 6"' \
--form 'document_required_7="Documents required 7"' \
--form 'document_required_8="Documents required 8"' \
--form 'document_required_9="Documents required 9"' \
--form 'total_duration="03:00:00"' \
--form 'steps_1="Steps 1"' \
--form 'steps_2="Steps 2"' \
--form 'steps_3="Steps 3"' \
--form 'steps_4="Steps 4"' \
--form 'steps_5="Steps 5"' \
--form 'steps_6="Steps 6"' \
--form 'steps_7="Steps 7"' \
--form 'steps_8="Steps 8"' \
--form 'steps_9="Steps 9"' \
--form 'saved_as="Draft"' \
--form 'star_rating="4.1"'
`