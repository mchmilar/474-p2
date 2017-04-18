# Pass customer of id of customer who is browsing
# Pass our knowledge base which is our network information
# Pass which network to search, eg: tn, kn, vn
get_network_purchases(customer_id, knowledge_base, network):
  customer = knowledge_base[customer_id]
  rcmnd_items = []
  
  # Iterate through all people in their network
  for tn_member in customer["network"][network]:
    purchases = tn_member["purchased-items"]
	
    # iterate through all purchases of this member
    for purchase in purchases:
      purchase_time = time.mktime(datetime.strptime(purchases["date"], 
	                              "%Y-%m-%d").timetuple())
      current_time = time.time()
      rating = purchase["product"]["rating"]
	  
      # If the purchase date and rating of the purchase
      # meet our criteria, add it to the list
      if current_time - purchase_time > six_months && rating > 2:
        rcmnd_items.append(purchase["product"]["product-id"])
  
  # Return our list of suggested items 
  # from our specified network
  return rcmnd_items
        