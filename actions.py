from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_core_sdk.events import AllSlotsReset
from rasa_core_sdk.events import Restarted
import zomatopy
import json
from email.message import EmailMessage
import smtplib
email_restaurant_list = []

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'

	def run(self, dispatcher, tracker, domain):
		config={"user_key":"34e58384c8a9a49fc09ea68cd5ad7196"}
		zomato = zomatopy.initialize_app(config)
		# Get cuisine and min/max budget range from slot
		cuisine = tracker.get_slot('cuisine')
		min_range = float(tracker.get_slot('min_range'))
		max_range = float(tracker.get_slot('max_range'))
		loc = tracker.get_slot('location')



		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		# cuisines_dict = {'American': 1, 'Chinese': 25, 'Italian': 55,
        #                  'Mexican': 73, 'North Indiann': 50, 'South Indian': 85}

		cuisines_dict = {'american': 1, 'chinese': 25, 'italian': 55,
                         'mexican': 73, 'north indian': 50, 'south indian': 85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 50)
		d = json.loads(results)
		response=""


		if d['results_found'] == 0:
			response= "Sorry, we didn't find any results for this query."
		else:
			restaurant_list = d['restaurants']
			#print(type(restaurant_list[0]['restaurant']['average_cost_for_two']), float(min_range))
			budget_restaurant = [restaurant for restaurant in restaurant_list if ((float(restaurant['restaurant']['average_cost_for_two']) > float(min_range)) & (float(restaurant['restaurant']['average_cost_for_two']) < int(max_range)))]
			# Sort the results according to the restaurant's rating
			budget_restaurant_sorted = sorted(budget_restaurant, key=lambda k: float(k['restaurant']['user_rating']['aggregate_rating']), reverse=True)

			# Build the response
			response = ""
			restaurant_list = False
			if len(budget_restaurant_sorted) == 0:
				dispatcher.utter_message("Oops! no restaurant found for this query. :("+ "\n")

			else:
				# Pick the top 5
				budget_restaurant_top5 = budget_restaurant_sorted[:5]
				global email_restaurant_list
				email_restaurant_list = budget_restaurant_sorted[:10]
				#print(email_restaurant_list)
				for restaurant in budget_restaurant_top5:
					response = response + restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location']['address'] + " has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n" + "\n"
				dispatcher.utter_message("Here are our picks!"+ "\n" + response)
			return [SlotSet('location', loc)]

class CheckLocation(Action):

	city_list = []


	def __init__(self):

		self.city_list = ["Ahmedabad","Bengaluru","Chennai","Delhi","Hyderabad","Kolkata","Mumbai","Pune",
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
		self.city_list = [x.lower() for x in self.city_list]

	def name(self):
		return "action_check_location"

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		city = str(loc).lower()
		if not (self.check_location(city)):
			dispatcher.utter_message("We do not operate in " + str(loc) + " yet. Please try some other city.")
			return [SlotSet('location', None), SlotSet("is_location", False)]
		else:
			return [SlotSet('location', loc), SlotSet("is_location", True)]

	def check_location(self, loc):
		return loc.lower() in self.city_list

class SendMail(Action):

	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):
		# Get user's email id
		to_email = tracker.get_slot('emailid')
		# Get location and cuisines to put in the email
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		#global email_restaurant_list
		restaurant_count = len(email_restaurant_list)
		# Construct the email 'subject' and the contents.
		email_subj = "Top " + str(restaurant_count) + " " + str(cuisine).capitalize() + " restaurants in " + str(loc).capitalize()
		email_msg = "Hi there! Here are the " + email_subj + "." + "\n" + "\n" +"\n"
		for restaurant in email_restaurant_list:
			email_msg = email_msg + restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated " + str(restaurant['restaurant']['user_rating']['aggregate_rating']) + "\n" +"\n"

		# Open SMTP connection to our email id.
		s = smtplib.SMTP("smtp.gmail.com", 587)
		s.starttls()
		s.login("manhojkummar@gmail.com", "Manojk123")

		# Create the msg object
		msg = EmailMessage()

		# Fill in the message properties
		msg['Subject'] = email_subj
		msg['From'] = "manhojkummar@gmail.com"

		# Fill in the message content
		msg.set_content(email_msg)
		msg['To'] = str(to_email)

		s.send_message(msg)
		s.quit()
		dispatcher.utter_message("**** EMAIL SENT! HAPPY DINING :) ****")
		return []

class ActionRestarted(Action): 	
	def name(self):
		return 'action_restart'
	def run(self, dispatcher, tracker, domain):
		return[Restarted()] 