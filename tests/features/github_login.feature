Feature: GitHub Login
	
	As a valid github user,
	I want to be able to login to the github application,
	So that I can access the github website

@smoke
Scenario: Login to Github with a valid Github user
	Given the user is a valid Github user
	When the user logs in to Github with a valid user
	Then the user is logged into the github website


