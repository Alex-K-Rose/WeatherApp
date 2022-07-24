# WeatherApp

How to use Micro Service

REQUEST
- Instantiate MilkshakeRpcClient object
- Use .call() method of class object passing in location string
- String must be city i.e. "Sandiego" or city and state seperated with comma and without spacing i.e. "Sandiego,CA"

RECIEVE
- .call() method returns one of three possible string values 
- Possible string values are
  - "It is Milkshake Weather"
  - "Not Milkshake Weather"
  - "Request Failed"
  
  ![UML Sequence Diagram](https://github.com/Alex-K-Rose/WeatherApp/blob/master/WeatherApp.png?raw=true)
