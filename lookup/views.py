from django.shortcuts import render

# Create your views here.
def Home(request):

	import json
	import requests

	if request.method == 'POST':
		zipcode = request.POST['zipcode']
		api_req = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zipcode+"&distance=5&API_KEY=8F592778-219C-48B0-A760-43CB943E8CDF")

		try:
			api = json.loads(api_req.content)
		except Exception as e:
			api = 'error'

		if api[0]['Category']['Name'] == 'Good' :
			category_description = "(0 - 50)	Good : People are no longer exposed to any health risk."
			category_color ='good' 
		elif api[0]['Category']['Name'] == 'Moderate' :
		  	category_description = "(51 - 100)	Moderate : Acceptable air quality for a healthy adults but still pose threat to sensitive individual."
		  	category_color = 'moderate'
		elif api[0]['Category']['Name'] == 'Unhealthy for Sensitive Groups':
		  	category_description = "(101 - 150) Unhealthy for Sensitive Groups : Poor air quality can affect health issues such as difficulty in breathing."
		  	category_color = 'UnhealthyforSensitiveGroups'
		elif api[0]['Category']['Name'] == 'Unhealthy' :
		    category_description = "(151 - 200) Unhealthy : Toxic air can provoke health difficulties expecially to the young kids and elderly people."
		    category_color = 'Unhealthy'
		elif api[0]['Category']['Name'] == 'Very Unhealthy':
		  	category_description = "(201 - 300) Very Unhealthy : Breathing polluted AQI may lead to chronic health issues."
		  	category_color = 'veryunhealthy'
		elif api[0]['Category']['Name'] == 'Hazardous':
		  	category_description = "(301 - 500) Hazardous : AQI exceeding 400 is highly unacceptable to human- can lead to premature death."
		  	category_color = 'Hazardous'



		return render(request,'home.html',{

			"api":api,
			"category_description":category_description,
			"category_color":category_color

			})


		
	else:	
		api_req = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89128&distance=5&API_KEY=8F592778-219C-48B0-A760-43CB943E8CDF")

		try:
			api = json.loads(api_req.content)
		except Exception as e:
			api = 'error'

		if api[0]['Category']['Name'] == 'Good' :
			category_description = "(0 - 50)	Good : People are no longer exposed to any health risk."
			category_color ='good' 
		elif api[0]['Category']['Name'] == 'Moderate' :
		  	category_description = "(51 - 100)	Moderate : Acceptable air quality for a healthy adults but still pose threat to sensitive individual."
		  	category_color = 'moderate'
		elif api[0]['Category']['Name'] == 'Unhealthy for Sensitive Groups':
		  	category_description = "(101 - 150) Unhealthy for Sensitive Groups : Poor air quality can affect health issues such as difficulty in breathing."
		  	category_color = 'UnhealthyforSensitiveGroups'
		elif api[0]['Category']['Name'] == 'Unhealthy' :
		    category_description = "(151 - 200) Unhealthy : Toxic air can provoke health difficulties expecially to the young kids and elderly people."
		    category_color = 'Unhealthy'
		elif api[0]['Category']['Name'] == 'Very Unhealthy':
		  	category_description = "(201 - 300) Very Unhealthy : Breathing polluted AQI may lead to chronic health issues."
		  	category_color = 'veryunhealthy'
		elif api[0]['Category']['Name'] == 'Hazardous':
		  	category_description = "(301 - 500) Hazardous : AQI exceeding 400 is highly unacceptable to human- can lead to premature death."
		  	category_color = 'Hazardous'



		return render(request,'home.html',{

			"api":api,
			"category_description":category_description,
			"category_color":category_color

			})

def About(request):
	return render(request,'about.html',{})