from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
from email.message import EmailMessage
import smtplib
email_restaurant_list = []

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		config={"user_key":"34e58384c8a9a49fc09ea68cd5ad7196"}
		zomato = zomatopy.initialize_app(config)
		# Get cuisine and min/max budget range from slot
		cuisine = tracker.get_slot('cuisine')
		min_range = tracker.get_slot('min_range')
		max_range = tracker.get_slot('max_range')
		loc = tracker.get_slot('location')



		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict = {'american': 1, 'chinese': 25, 'italian': 55,
                         'mexican': 73, 'north indian': 50, 'south indian': 85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 50)
		d = json.loads(results)
		response=""


		if d['results_found'] == 0:
			response= "Sorry, we didn't find any results for this query."
		else:
			restaurant_list = d['restaurants']
			budget_restaurant = [restaurant for restaurant in restaurant_list if ((restaurant['restaurant']['average_cost_for_two'] > min_range) & (restaurant['restaurant']['average_cost_for_two'] < max_range))]
			# Sort the results according to the restaurant's rating
			budget_restaurant_sorted = sorted(budget_restaurant, key=lambda k: k['restaurant']['user_rating']['aggregate_rating'], reverse=True)

			# Build the response
			response = ""
			restaurant_exist = False
			if len(d_budget_rating_sorted) == 0:
				dispatcher.utter_message("Oops! no restaurant found for this query. :("+ "\n")

			else:
				# Pick the top 5
				budget_restaurant_top5 = budget_restaurant_sorted[:5]
				global email_restaurant_list
				email_restaurant_list = budget_restaurant_sorted[:10]
				if(email_restaurant_list and len(email_restaurant_list) > 0):
					restaurant_exist = True
				for restaurant in budget_restaurant_top5:
					response = response + restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location']['address'] + " has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n" + "\n"
				dispatcher.utter_message("Here are our picks!"+ "\n" + response)
			return [SlotSet('location', loc)]


	# 		response = self.get_restaurant_on_budget(min_range, max_range, d['restaurants'])
    #
	# 	dispatcher.utter_message("-----"+response)
	# 	return [SlotSet('location',loc)]
    #
    # def get_restaurant_on_budget(self, min_range, max_range, restaurant_list):

class CheckLocation(Action):

	city_list = ["Ahmedabad","Bangalore","Chennai","Delhi","Hyderabad","Kolkata","Mumbai","Pune",
"Agra","Ajmer","Aligarh","Allahabad","Amravati","Amritsar","Asansol","Aurangabad",
"Bareilly","Belgaum","Bhavnagar","Bhiwandi","Bhopal","Bhubaneswar",
"Bikaner","Bokaro Steel City","Chandigarh","Coimbatore","Cuttack","Dehradun",
"Dhanbad","Durg-Bhilai Nagar","Durgapur","Erode","Faridabad","Firozabad","Ghaziabad",
"Gorakhpur","Gulbarga","Guntur","Gurgaon","Guwahati",
"Gwalior","Hubli", "Dharwad","Indore","Jabalpur","Jaipur","Jalandhar","Jammu","Jamnagar","Jamshedpur","Jhansi","Jodhpur",
"Kannur","Kanpur","Kakinada","Kochi","Kottayam","Kolhapur","Kollam","Kota","Kozhikode","Kurnool","Lucknow","Ludhiana",
"Madurai","Malappuram","Mathura","Goa","Mangalore","Meerut",
"Moradabad","Mysore","Nagpur","Nanded","Nashik","Nellore","Noida","Palakkad","Patna","Pondicherry","Raipur","Rajkot",
"Rajahmundry","Ranchi","Rourkela","Salem","Sangli","Siliguri",
"Solapur","Srinagar","Sultanpur","Surat","Thiruvananthapuram","Thrissur","Tiruchirappalli","Tirunelveli","Tiruppur",
"Ujjain","Vijayapura","Vadodara","Varanasi",
"Vasai-Virar City","Vijayawada","Visakhapatnam","Warangal"]

	def name(self):
		return "check_location"

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		city = str(loc)
		if not (self.check_location(city)):
			dispatcher.utter_message("We do not operate in " + loc + " yet. Please try some other city.")
			return [SlotSet('location', None), SlotSet("is_location", False)]
		else:
			return [SlotSet('location', loc), SlotSet("is_location", True)]

	def check_location(self, loc):
		return loc.lower() in city_list

class SendMail(Action):

	def name(self):
		return 'send_mail'

	def run(self, dispatcher, tracker, domain):
		# Get user's email id
		to_email = tracker.get_slot('emailid')
		# Get location and cuisines to put in the email
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		global email_restaurant_list
		restaurant_count = len(email_restaurant_list)
		# Construct the email 'subject' and the contents.
		email_subj = "Top " + str(restaurant_count) + " " + cuisine.capitalize() + " restaurants in " + str(loc).capitalize()
		email_msg = "Hi there! Here are the " + d_email_subj + "." + "\n" + "\n" +"\n"
		for restaurant in email_restaurant_list:
			email_msg = email_msg + restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n" +"\n"

		# Open SMTP connection to our email id.
		s = smtplib.SMTP("smtp.gmail.com", 587)
		s.starttls()
		s.login("smupgrad@gmail.com", "pgdmlaiupgrad")

		# Create the msg object
		msg = EmailMessage()

		# Fill in the message properties
		msg['Subject'] = d_email_subj
		msg['From'] = "smupgrad@gmail.co"

		# Fill in the message content
		msg.set_content(d_email_msg)
		msg['To'] = to_email

		s.send_message(msg)
		s.quit()
		dispatcher.utter_message("**** EMAIL SENT! HAPPY DINING :) ****")
		return []

class isBudgetRange(Action):

	def name(self):
		return "verify_budget"

	def run(self, dispatcher, tracker, domain):
		min_range = None
		max_range = None
		error_msg = "Sorry!! price range not supported, please re-enter."
		try:
			budgetmin = int(tracker.get_slot('min_range'))
			budgetmax = int(tracker.get_slot('max_range'))
		except ValueError:
			dispatcher.utter_message(error_msg)
			return [SlotSet('min_range', None), SlotSet('max_range', None), SlotSet('budget_ok', False)]
		min_dict = [0, 300, 700]
		max_dict = [300, 700]
		if budgetmin in min_dict and (budgetmax in max_dict or budgetmax > 700):
			return [SlotSet('min_range', budgetmin), SlotSet('max_range', budgetmax), SlotSet('budget_ok', True)]
		else:
			dispatcher.utter_message(error_msg)
			return [SlotSet('min_range', 0), SlotSet('max_range', 10000), SlotSet('budget_ok', False)]
