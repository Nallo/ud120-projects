#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

### People in the Enron dataset.
print "People:", len(enron_data)

### Features for each people in the Enron dataset.
print "Features for each people:", len(enron_data["SKILLING JEFFREY K"])

### POIs in the Enron dataset.
poi_count = 0
for k in enron_data.keys():
    if enron_data[k]["poi"] == 1:
        poi_count += 1
print "POIs:", poi_count

### Total Stock of James Prentice.
print "James Prentice total stock:", \
                    enron_data["PRENTICE JAMES"]["total_stock_value"]

### Email from Wesley Colwell to POI.
print "Email from Wesley Colwell to POI:", \
                    enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

### Value of stock options exercised by Jeffrey K Skilling.
print "Stock options exercised by Jeffrey K Skilling:", \
                    enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print "Skilling total payments - CEO:", \
                    enron_data["SKILLING JEFFREY K"]["total_payments"]
print "Fastow total payments - CFO:  ", \
                    enron_data["FASTOW ANDREW S"]["total_payments"]
print "Lay total payments - Chairman:", \
                    enron_data["LAY KENNETH L"]["total_payments"]

### Quantified salaries in the Enron dataset.
salaries_count = 0
for k in enron_data.keys():
    if enron_data[k]["salary"] != 'NaN':
        salaries_count += 1
print "Salaries:", salaries_count

### Emails in the Enron dataset.
emails_count = 0
for k in enron_data.keys():
    if enron_data[k]["email_address"] != 'NaN':
        emails_count += 1
print "Emails:", emails_count

### Missing total payments in the Enron dataset.
payments_count = 0
missing_payment_count = 0
for k in enron_data.keys():
    payments_count += 1
    if enron_data[k]["total_payments"] == 'NaN':
        missing_payment_count += 1
print "Missing payments:", missing_payment_count
print "Missing payments percetage:", 100.0 * missing_payment_count/payments_count

### Missing total payments for POIs in the Enron dataset.
payments_count = 0
missing_payment_count = 0
for k in enron_data.keys():
    payments_count += 1
    if enron_data[k]["total_payments"] == 'NaN' and enron_data[k]["poi"] == 1:
        missing_payment_count += 1
print "Missing POIs payments percetage:", 100.0 * missing_payment_count/payments_count

### Display the dictionary of the CFO.
print enron_data["LAY KENNETH L"]
