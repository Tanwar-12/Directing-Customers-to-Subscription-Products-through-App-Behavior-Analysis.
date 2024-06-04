# 𝙼𝙰𝙲𝙷𝙸𝙽𝙴 𝙻𝙴𝙰𝚁𝙽𝙸𝙽𝙶 𝙿𝚁𝙾𝙹𝙴𝙲𝚃

## 𝐓𝐈𝐓𝐋𝐄 : 𝐃𝐢𝐫𝐞𝐜𝐭𝐢𝐧𝐠-𝐂𝐮𝐬𝐭𝐨𝐦𝐞𝐫𝐬-𝐭𝐨-𝐒𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧-𝐏𝐫𝐨𝐝𝐮𝐜𝐭𝐬-𝐭𝐡𝐫𝐨𝐮𝐠𝐡-𝐀𝐩𝐩-𝐁𝐞𝐡𝐚𝐯𝐢𝐨𝐫-𝐀𝐧𝐚𝐥𝐲𝐬𝐢𝐬.

#### 𝐎𝐕𝐄𝐑𝐕𝐈𝐄𝐖:

* In today's market many companies have a mobile presence. Often, these companies provide free products/services in their mobile apps in an attempt to transition their customers to a paid membership. Some examples of paid products, which originate from free ones, are YouTube Red, Pandora Premium, Audible Subscription, YouTube Premium, and You Need a Budget. Since marketing efforts are never free, these companies need to know exactly who to target with offers and promotions.

* Market: The target audience is customers who use a company's free products. In this case study, this refers to users who installed (and used) the companies free mobile app.

* Product: The paid memberships often provide enhanced versions of the free products already given for free, alongside new features. For example, Youtube Red allows you to leave the app while still listening to a video.

![image](https://github.com/Tanwar-12/Directing-Customers-to-Subscription-Products-through-App-Behavior-Analysis./assets/110081008/b83f0c77-8887-451c-8059-fae676dc4839)

## 𝐆𝐎𝐀𝐋 𝐎𝐅 𝐓𝐇𝐄 𝐏𝐑𝐎𝐉𝐄𝐂𝐓:
**The objective of this model is to predict which users will not subscribe to the paid membership, so that greater marketing efforts can go into trying to convert them to paid users.**

### 𝐁𝐔𝐒𝐈𝐍𝐄𝐒𝐒 𝐂𝐀𝐒𝐄:
* In this Case Study we will be working for a fintech company that wants to provide its customers with a paid mobile app subscription that will allow them to track all of their finances in one place. To attract customers, the company releases a free version of their app with some of the main features unlocked.

* The company has tasked you to identify which users will mostly likely NOT enroll in paid products, so that additional offers can be given to them. Because of the costs of these offers, the company does not want to offer them to everybody, especially customers who were going to enroll anyways.

 ####  𝐀𝐁𝐎𝐔𝐓 𝐃𝐀𝐓𝐀:
* By working for the company. We have access to each customer's app behavior data. This data allows us to see the date & time of app installation, as well as the features the users engaged with within the app. App behavior is characterized as the list of app screens the user looked at, and whether the user played the financial mini-games available.

* The app usage data is only from the user's first day in the app. This limitation exists because users can enjoy a 24-hour free trial of the premium features, and the company wants to target them with new offers shortly after the trail is over.

* The Data for this project is from manufacturing fields based on trends found in real world case studies. The fields describe what companies usually track from their users.

### 𝐃𝐚𝐭𝐚 𝐃𝐞𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧:

* User : this is Unique id of each perticuter user of app

* first_open : this is the date/month/year, time the user frist time open the app
  
* dayofweek : this shows the day out of 7 days a week an user join the app where 0:Sunday & 6:Saturday

* hour : This is outoff 24 hour of day the user 1st open the app

* age : This is simply the age of the user

* screen_list : This describe the every single screen name the user visited in that 1st 24-hour (screen name seperated by comma)

* numscreens : The Number of screen the user visited in 1st 24 hour

* minigame : The app has minigame feature, this shows whether the player played any minigame of Not (1:Played, 0: Not Played)

* liked : There are like button for each feature in the app, shows whether the user cliked any like button of any feature in app or NOT (1: click like button, 0: Not clicked)

* used_premium_feature : This shows whether the user used any premium feature (that is for free in 1st 24 hour) or not in 1st 24 hour (1: used, 0: not used)

* enrolled : This is target that shows whether the user enrolled to premium after the free trial (1: enrolled, 0: not enrolled)

* enrolled_date : date & time of enrollment to premium product if they enrolled to premium

𝐈𝐌𝐏𝐎𝐑𝐓𝐈𝐍𝐆 𝐓𝐇𝐄 𝐋𝐈𝐁𝐑𝐀𝐑𝐈𝐄𝐒
* Numpy,Pandas,matplotlib.seaborn...

### 𝐋𝐎𝐀𝐃 𝐓𝐇𝐄 𝐃𝐀𝐓𝐀

  𝐁𝐀𝐒𝐈𝐂 𝐂𝐇𝐄𝐂𝐊𝐒
  
  ### 𝐄𝐗𝐏𝐋𝐎𝐑𝐀𝐓𝐎𝐑𝐘 𝐃𝐀𝐓𝐀 𝐀𝐍𝐀𝐋𝐘𝐒𝐈𝐒
  **Histogam of Numerical columns**
  ![image](https://github.com/Tanwar-12/Directing-Customers-to-Subscription-Products-through-App-Behavior-Analysis./assets/110081008/19498393-436a-4db6-b115-4d1b0f779b89)

**Correlation between independent features & response variable**

![image](https://github.com/Tanwar-12/Directing-Customers-to-Subscription-Products-through-App-Behavior-Analysis./assets/110081008/6cf91fe6-501b-4cd9-a548-d1168dc93683)

![image](https://github.com/Tanwar-12/Directing-Customers-to-Subscription-Products-through-App-Behavior-Analysis./assets/110081008/0da8632b-44d7-4a72-be6b-7bf88ac32be6)

![image](https://github.com/Tanwar-12/Directing-Customers-to-Subscription-Products-through-App-Behavior-Analysis./assets/110081008/4f6aaed5-68f2-42ce-a43d-0b62ea57123b)

![image](https://github.com/Tanwar-12/Directing-Customers-to-Subscription-Products-through-App-Behavior-Analysis./assets/110081008/a83d9654-d504-42e6-bc23-bad062b91ad8)

_**Here we conclude that most of users (more that 20000 out-off total 50000 users) do not used the 1st 24 hour premium free trial & infact they direcly jumped to the premium at the time of they 1st open the app**_

### 𝐅𝐄𝐀𝐓𝐔𝐑𝐄 𝐄𝐍𝐆𝐈𝐍𝐄𝐄𝐑𝐈𝐍𝐆:
* drop( the columns='first_open','enrolled_date','Date_Delta_in_Hour'
  

### 𝐃𝐀𝐓𝐀 𝐏𝐑𝐄𝐏𝐑𝐎𝐂𝐄𝐒𝐒𝐈𝐍𝐆 & 𝐅𝐄𝐀𝐓𝐔𝐑𝐄 𝐒𝐂𝐀𝐋𝐈𝐍𝐆
![image](https://github.com/Tanwar-12/Directing-Customers-to-Subscription-Products-through-App-Behavior-Analysis./assets/110081008/025db4e1-7d20-4b94-80d0-697b4485c1fa)

![image](https://github.com/Tanwar-12/Directing-Customers-to-Subscription-Products-through-App-Behavior-Analysis./assets/110081008/13521ae1-042a-4741-9c5d-5e81fb19a4e9)
## 𝐌𝐎𝐃𝐄𝐋 𝐁𝐔𝐈𝐋𝐃𝐈𝐍𝐆
𝐋𝐎𝐆𝐈𝐒𝐓𝐈𝐂 𝐑𝐄𝐆𝐑𝐄𝐒𝐒𝐈𝐎𝐍
#### 𝐌𝐎𝐃𝐄𝐋 𝐓𝐑𝐀𝐈𝐍𝐈𝐍𝐆
#####  𝐌𝐎𝐃𝐄𝐋 𝐄𝐕𝐀𝐋𝐔𝐀𝐓𝐈𝐎𝐍 & 𝐏𝐑𝐄𝐃𝐈𝐂𝐓𝐈𝐎𝐍

#### Classification Report:  
                   precision    recall  f1-score   support

           0       0.79      0.79      0.79      5257
           1       0.77      0.77      0.77      4743

    accuracy                           0.78     10000
    macro avg      0.78      0.78      0.78     10000
    weighted avg   0.78      0.78      0.78     10000

Model Accuracy : 0.7802
Precision Score : 0.7664921465968586
Recall Score :  0.7716635041113219
F1-Score :  0.7690691321706241

* Model Accuracy = sum of diagonal value of cm/sum of all values of cm(confusion matrix)

* We also look for Precision to insure that model accuracy is inceased not because of some overfitting issues
  
* Precision Score = True Positive / (True Positive + False Positive), meaning that out-of all predicted positives what percentage are Actual positives
  
* Recall Score = True Positives / (True Positives + False Negatives, meaning that out-of all Actual Positives What Percentage are predicted to be positives
  
* We will also calculate f1-score as it creates a balance between Precision & Recall coz it is weighted average of Precision & Recall thereby it considers both False Positives & False
  
*  Negative Intuitively f1-score is not easy to understand as accuracy but it is much better metric in case of class imbalanced data as in our case.
  
* F1-Score = Precision*Recall / (Precision+Recall)




![image](https://github.com/Tanwar-12/Directing-Customers-to-Subscription-Products-through-App-Behavior-Analysis./assets/110081008/dfb2a7a7-ae0e-4ed5-b021-bd03cb51b382)

![image](https://github.com/Tanwar-12/Directing-Customers-to-Subscription-Products-through-App-Behavior-Analysis./assets/110081008/ab43764e-1a62-44f3-a345-6ddfa851961b)

From both the plots we can conclude that both Actual & Predicted values follows same class distribution

**FEATURE IMPORTANCE**
![image](https://github.com/Tanwar-12/Directing-Customers-to-Subscription-Products-through-App-Behavior-Analysis./assets/110081008/de3a7c2e-fb41-473e-9fdf-7859108f4095)

![image](https://github.com/Tanwar-12/Directing-Customers-to-Subscription-Products-through-App-Behavior-Analysis./assets/110081008/4617d7bf-f011-4f53-b2a4-9090195d8f62)

### 𝐂𝐎𝐍𝐂𝐋𝐔𝐒𝐈𝐎𝐍𝐒 & 𝐅𝐈𝐍𝐀𝐋 𝐑𝐄𝐒𝐔𝐋𝐓𝐒
* Positively Affecting features to enrollment: Other_sceens, VerifyPhone, CMCount, VerifyMobile, VerifyDateOfBirth, Rewards, EditProfile, etc, without any doubt all above features are situated to moving towards the enrollment screens.
  
* Negatively Affecting features to enrollment: LoanCount, VerifyCountry, Alerts, age, numscreens, Login, ResendToken, etc, if we see all these features are irritating & no user want to do this.




