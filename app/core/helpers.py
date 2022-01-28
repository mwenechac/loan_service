from datetime import datetime

def get_annual_interest(amount, interest, start_date, end_date):
	end_date = datetime.strptime(end_date, "%Y-%m-%d")
	delta = end_date.date() - start_date
	annual_interest = amount * (interest/100) * (delta.days/365)
	return annual_interest
