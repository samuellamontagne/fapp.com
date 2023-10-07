# Input = - Range of dates +- a certain amount of days
#         - Departing destination
#         - Landing destination
# Output = A list of flights with custom 'layovers' to achieve cheapest price possible

# Logic: 
#       Make a query for the range of departing dates and find the cheapest flight to London, Paris or Lisbon (hardcoded for now since they are the cheapest destinations to get in europe)
#       Find a connecting flight to the landing destination that is keeping you in the airport less than say 8 hours.
#       *Maybe* Look for a city that is close but much cheaper (ex, copenhaguen is MUCH cheaper than Malmo, but they are so close.

