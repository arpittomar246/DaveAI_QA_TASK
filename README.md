# QA Assignment

## Part 1: API testing

Automated API tests for the public Reqres API using Python and pytest.

## Project structure
```
tests/api_tests.py   - 4 API test cases
requirements.txt     - libraries that are required
README.md            - this file
```

## Dependencies
- Python 
- requests, pytest 

## Setup (run the commands according to the numbering)
1. Create and activate a python virtual environment:
```
   1. python -m venv venv
   2. venv\Scripts\activate
```
2. Install the libraries
```
   3. pip install -r requirements.txt
```
3. to run this assignment we need a API key. Go to  https://app.reqres.in and create a free account and copy the free API key.

```
   4. set apiKeys=copied API key
```

## How to run the tests
```
5. pytest tests/api_tests.py -v
```

## Test cases

| Test | Endpoint | What it checks | Expected |
|---|---|---|---|
| test_validate_success_response_200 | GET /api/users?page=2 | Request succeeds and the response has the right page | 200 |
| test_user_has_correct_details | GET /api/users/12 | User 12's id, name and email are correct | 200 |
| test_incorrect_user_id | GET /api/users/999 | A user that does not exist | 404 |
| test_login_without_password | POST /api/login | Login with the password missing | 400, "Missing password" |

## Design choices
- **pytest** was used because test cases are simple functions with plain `assert`
  commands which are easy to read and understand.
- **Positive and negative test cases:** two test cases check that valid requests is success or not
  and return correct data; other two test cases check that the API handles ibad input or not
- **The API key is read from an environment variable** so it is never stored
  in the code.
- **Each test makes only one API call** to stay within Reqres free limit of
  100 calls per day.

## Results
All 4 tests passed. Full output is in `results.txt`.

## Observations
During the development the repeated test case runs returned 429 Too Many Requests,
which is Reqres rate limit. Tests should be run once after changes are
complete to stay within the daily limit.


```







```



# Part 2: Website UI Testing

UI test cases for https://www.iamdave.ai using Python, Selenium and ChromeDriver.

## How to run
```
python -m pytest tests/ui_tests.py -v
```
Google Chrome must be installed.

## Test cases

| Test | What it checks |
|---|---|
| test_homepage_title_and_logo | Homepage opens, title contains "DaveAI", logo is visible |
| test_main_heading_is_present | The main heading (h1) is shown on the homepage |
| test_book_demo_button_opens_demo_page | Clicking "Book Demo" opens the /book-demo/ page |
| test_demo_form_accepts_email_input | The demo form's email field accepts typed text |

## Design choices
- **unittest with setUp() and tearDown()**: every test opens a fresh browser
  and closes it afterwards so that test cases are independent of each other.
- **Explicit waits (WebDriverWait)** instead of fixed sleeps, so tests wait
  only as long as needed and dont fail while the page is still loading.
- **The form is not submitted**, to avoid sending a fake enquiry to a real
  business.





```







```



# Part 3 Load Testing with Locust

## How to run
```
set apiKeys=your-key-here
locust -f tests/load_tests.py --headless -u 5 -r 1 -t 2m --html Locust_report.html (-u = number of user run at a time, -r = how many user start each second, -t = how much time test will run, --html = will record the results of run)

```

## Test plan
- **Endpoint tested:** GET /api/users?page=2 
- **User behaviour:** each user sends a request then waits 40 seconds
- **Limits:** the task allows 100 calls per day and Reqres allows 20 calls
  per minute 


The 40-second wait keeps traffic under 20 calls per minute, and the
2-minute run time keeps the total under 100 calls.


## Observations
Because of the 20-calls-per-minute limit, this test checks how the API
responds when 5–10 users are active at the same time.