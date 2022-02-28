## Getting Started
#### To set up the project:
1. Run `pipenv install` in the root of the project where the Pipfile is located.
2. `cd` into the top level `glucosetracker` directory where the Makefile is located and run `make up` to start the server locally.

#### To upload csvs:
1. csv files for upload are located in the `api/data`.
2. `cd` into the top level `glucosetracker` directory where the Makefile is located and run `make upload`.


## Description
- Glucose levels can be found by either `reading_id` or `user_id`.
- `reading_id`: a unique id associated with a users glucose reading.
  - The endpoint is `api/v1/levels/reading/2400/` where `2400` is the `reading_id`.
- `user_id`: an id unique to an patient, associated with one or more readings.
  - The endpoint is `api/v1/levels/user/aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa/` where `aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa` is an example `user_id`.

## Assumptions
- Glucose readings will record with the following fields: `user id`, `reading id`, `device name`, `device serial`, `timestamp`, `recording type` and `glucose level`.
- Readings can be made with at least one of the above fields present in addition to `reading id`.
- `reading id` is automatically generated when a glucose reading is uploaded to the api.
- Glucose readings with missing int fields (e.g. `recording type` and `glucose level`) will use `-1` as a null value.