customer_name = raw_input("please enter customer_name:")
job_number = raw_input("please enter job_number:")
fabricator_name = raw_input ("please enter fabricator_name:")
if job_number.isnumeric():
	print(job_number,"finish in 2 weeks")
else:
	print("invalid job_number")
