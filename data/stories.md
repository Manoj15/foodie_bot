## interactive_story_4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"is_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"min_range": "700", "max_range": "10000"}
    - slot{"max_range": "10000"}
    - slot{"min_range": "700"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_mail
    - utter_ask_email_address
* send_mail{"emailid": "manhojkummar@gmail.com"}
    - slot{"emailid": "manhojkummar@gmail.com"}
    - action_send_email

## interactive_story_5
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* inform{"location": "Bengaluru"}
    - slot{"location": "Bengaluru"}
    - action_check_location
    - slot{"location": "Bengaluru"}
    - slot{"is_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"min_range": "300", "max_range": "700"}
    - slot{"max_range": "700"}
    - slot{"min_range": "300"}
    - action_restaurant
    - slot{"location": "Bengaluru"}
    - utter_ask_for_email_to_send
* send_mail
    - utter_ask_email_address
* send_mail{"emailid": "thecurvefitter@gmail.com"}
    - slot{"emailid": "thecurvefitter@gmail.com"}
    - action_send_email

## interactive_story_6
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_check_location
    - slot{"location": "chennai"}
    - slot{"is_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"min_range": "0", "max_range": "300"}
    - slot{"max_range": "300"}
    - slot{"min_range": "0"}
    - action_restaurant
    - slot{"location": "chennai"}
    - utter_goodbye

## interactive_story_7
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* inform{"location": "Bengaluru"}
    - slot{"location": "Bengaluru"}
    - action_check_location
    - slot{"location": "Bengaluru"}
    - slot{"is_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* restaurant_search{"min_range": "700", "max_range": "10000"}
    - slot{"max_range": "10000"}
    - slot{"min_range": "700"}
    - action_restaurant
    - slot{"location": "Bengaluru"}
    - utter_ask_for_email_to_send
* send_mail
    - utter_ask_email_address
* send_mail{"emailid": "thecurvefitter@gmail.com"}
    - slot{"emailid": "thecurvefitter@gmail.com"}
    - action_send_email
    - utter_email_sent

## interactive_story_8
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* inform{"location": "mangalore"}
    - slot{"location": "mangalore"}
    - action_check_location
    - slot{"location": "mangalore"}
    - slot{"is_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"min_range": "300", "max_range": "700"}
    - slot{"max_range": "700"}
    - slot{"min_range": "300"}
    - action_restaurant
    - slot{"location": "mangalore"}
    - utter_ask_for_email_to_send
* send_mail
    - utter_ask_email_address
* send_mail{"emailid": "manhojkummar@gmail.com"}
    - slot{"emailid": "manhojkummar@gmail.com"}
    - action_send_email
    - utter_email_sent

## interactive_story_9
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Kochi"}
    - slot{"location": "Kochi"}
    - action_check_location
    - slot{"location": "Kochi"}
    - slot{"is_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"min_range": "300", "max_range": "700"}
    - slot{"max_range": "700"}
    - slot{"min_range": "300"}
    - action_restaurant
    - slot{"location": "Kochi"}
    - utter_ask_for_email_to_send
* send_mail
    - utter_ask_email_address
* send_mail{"emailid": "thecurvefitter@gmail.com"}
    - slot{"emailid": "thecurvefitter@gmail.com"}
    - action_send_email
    - utter_email_sent

## interactive_story_10
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Kochi"}
    - slot{"location": "Kochi"}
    - action_check_location
    - slot{"location": "Kochi"}
    - slot{"is_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"min_range": "300", "max_range": "700"}
    - slot{"max_range": "700"}
    - slot{"min_range": "300"}
    - action_restaurant
    - slot{"location": "Kochi"}
    - utter_ask_for_email_to_send
* dont_send_mail
    - utter_no_email_sent

## interactive_story_11
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"is_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"min_range": "300", "max_range": "700"}
    - slot{"max_range": "700"}
    - slot{"min_range": "300"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_mail
    - utter_ask_for_email_to_send
* send_mail{"emailid": "manhojkummar@gmail.com"}
    - slot{"emailid": "manhojkummar@gmail.com"}
    - action_send_email
    - utter_email_sent

## interactive_story_12
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* inform{"location": "Bengaluru"}
    - slot{"location": "Bengaluru"}
    - action_check_location
    - slot{"location": "Bengaluru"}
    - slot{"is_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"min_range": "700", "max_range": "10000"}
    - slot{"max_range": "10000"}
    - slot{"min_range": "700"}
    - action_restaurant
    - slot{"location": "Bengaluru"}
    - utter_ask_for_email_to_send
* send_mail
    - utter_ask_email_address
* send_mail{"emailid": "manhojkummar@gmail.com"}
    - slot{"emailid": "manhojkummar@gmail.com"}
    - action_send_email
    - utter_email_sent
