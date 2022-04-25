# SI507-Final-Project



## Code Running Instruction 
  - API keys: The necessary API keys are stored in the crendential.py and this file will be uploaded to Github for security reason, but it will be uploaded               through Canvas. Note: Google Maps API key is uploaded, and please do not use it and replace it with your own API key </br>
  
  - Before running the code, the credential file is needed to obtain the API keys and please click the button to run the code directly. </br>
  - Click the local link in the command line with port 8000 (I specify it for my computer) to start using the project.</br>
  - After clicking the starting button, the page will direct to the user input page, which will require user to input the location, category of the restaurant, and display preferences. </br>
  - Please note that the format of the phone number should be 123-456-7890 with - between numbers.
  - While the information (graphically or not) is displayed on the browser, please turn to the command line to wait for the prompt.</br>
  - The system will generate the recommendation based on the user's response (yes or no).</br>
  - After the recommendation, please back to the browser to see the menu of the restaurant (Some restaurants may not have built-in menu, I kindly provide Google search prompt to let you search the reataurant directly.</br>
  - With the selected dishes, the system will start delivering the food</br>

## Data Structure Description
The data structure I have implemented is a tree structure which is similar to the structure we used in project 2 and I store the questions in a tree structure like the followings:</br>
![alt text](https://github.com/YuanChengRua/SI507-Final-Project/blob/main/%E6%88%AA%E5%B1%8F2022-04-24%20%E4%B8%8B%E5%8D%886.00.09.png?raw=true)

The system will initially recommend the nearest restaurant to the user and if the user like the restaurant, the system will redirect to the restaurant’s page, otherwise, the system will ask the user which dimension of the restaurant needs to be changed and after the user’s selection, the order of the table will be changed automatically based on the dimension selected; and the recommendation will be changed correspondingly. </br>

![alt text](https://github.com/YuanChengRua/SI507-Final-Project/blob/main/%E6%88%AA%E5%B1%8F2022-04-24%20%E4%B8%8B%E5%8D%886.00.36.png?raw=true)




