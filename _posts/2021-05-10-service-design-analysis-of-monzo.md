---
layout: post
title: Service Design Analysis of Monzo 
excerpt: "This is a modified version of the report for Service Design in Bath Full Time MBA Class of 2020."
categories: Business Start-Up Design
tags: [ Business Start-Up Design]
comments: true
---

* Table of Contents
{:toc}

This is a modified version of the report for Enterprise in Action in Bath Full Time MBA Class of 2020.

# Service Design Analysis of Monzo

## Introduction

‘Every Company Will Be a Fintech Company’ argued Strange (2019).  Some of the major examples are Shopify (web monthly subscription service for merchant) and Mindbody (fitness studio management assistant service), both of which earn a half of their profit by financial services (ibid).  However, no single firm might be able to cover all of financial services infrastructure and therefore, they concentrate on each layer of that such as fraud, payment and data, which are offered as a service by them (ibid).  One of the companies focused on the payment layer in financial services infrastructure is Monzo which is a digital bank that forcuses to simplify the process its users maintain their payment by enabling them to monitor spending, divide bills, transfer money and more on their mobile <cite>(CBInshight, 2020)</cite>.  One of major difference with other bank Apps is viewing real-time balances due to the fact that most of banks spend 48 hours to count their transaction on its user’s statements due to the cloud computing <cite>(AWS, 2020)</cite>.  This is primary because the cloud such as Amazon Web Service (AWS) can provide the banks with all IT infrastructures to run their business, which is quite cheaper (maximally 75% of whole IT budget is used) than when they purchase individually and thus they can spend the money to improve their services fully and rapidly expand the ones <cite>(Strange, 2019)</cite>.  This essay will discuss the service of the fintech company and recommendation for the improvement of the payment service including tax calculation of the firm in terms of service design method such as Ethnography, Script and Staging.

## Ethnography (Fieldwork)
Ethnographic studies are required to clarify the salient attributes of the observed service experience <cite>(Fragnière, Nanchen and Sitten, 2012)</cite>.  The author participated the pretransition (verification process in the register one) and post transaction (user feedback process), both of which are called immersion episodes and used to identify the salient attributes of the payment service.  

### Immersion Episode 1: Pretransaction (Verification)
In the registoring process, after typed in the installed Monzo App on the mobile phone via its landing page and Apple store (or Google play), the user has to be verified.  The firm selected two stage verification, which are required to the identification such as a biometric card (the author selected, other forms including passport or photo-card driving license are also acceptable) and short self introduction video with the statement ("This is [Username]. I have a Monzo account").  This process is only on the mobile app and therefore, the author felt some concern and fear about the data security in the process because no employees directly stay with him (which is the major difference between Monzo and retail bank including HSBC). 

### Immersion Episode 2: Posttransaction (User feedback)
Monzo opens the Monzo Community Forum to collect user feedback.  After a new feature launched, the bank announce it to the customers on the online forum which is linked to its one of the landing pages named ‘Making Monzo’.  The users can comment their feedback directly for the feature they used after created their own account and the employees repley to their one intarctively.  All discussion has been saved and can be arranged in order of the timeline then every customers can read all of them.  For instance, they do not export the notification as an evidence for the payment such as PDF, which is remarkable difference from retail banks because the screenshot of payment confirmation is unlikely to be acceptable for some institutions.  This unenabled notification export problem has been alerted by a customer in the Monzo on the web community forum and the employees have responded and then they are struggling to solve the issue.  Therefore, while there is still some difficulty and inconvenience of the Monzo services, the customers can communicate with the staff of Monzo on the web community.

### Salient Attribution
Mental (or emotional) salient attributions has appeared through the immersion episodes and semi-directed interviews (see appendix) in this industory.  They can be security (from episode 1), commitment and consistency (from episode 2).  On the other hand, functional attributions might be emerged via competitor’s analysis, two major examples of which are Revolut and Starling <cite>(Lauren, 2020)</cite>.  The former provides free ATM withdrawals as far as £200 per month with 2% fee, which is marginally less expensive than Monzo (ibid).  The latter has slightly less understandable overdraft charges than Monzo, which is set to 15% annual charge rate in comparison to limiting maximum of the charge fee to £15.50 per month and a £20 buffer.  This may mean almost zero cash withdrawal cost and overdraft charge fee are functional minimum requirement as for the mobile banking consumers.  This is because enabling the users to withdraw and overdraft itself seem not to lead to the competitive advantage and therefore, only implement of these services with cheaper price than the competitors tend to have a perceived value for the users.  

## Script (Blueprint)
The service blueprint highlights how different the customer journey, frontstage (touch points), back-stage and these interactions because it is quite structured and support to coordinate the roles of different functions <cite>(REASON, LØVLIE and FLU, 2016)</cite>.  However, Monzo operates above 1600 microservices on AWS <cite>(AWS, 2020)</cite>.  Therefore, the scope of blueprint is required to focus on their core business which is online payment on the mobile.  

### Blueprint of the Existing Service
Figure 1 demonstrates the customer journey and its interactions of their whole payment transaction.  As the figure shows, a customer installed the app with registration to receive the debit card which enable them to purchase what they want via the card after they charge the money through their online account on Monzo.  After payment, they can obtain the notification of the payment on the web or app (mobile) and then unlike most banks, they can confirm their balance counted on this transaction immediately.  

![Figure 1](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598793894/%E5%9B%B31c.png "Figure 1")
Figure 1: The service blueprint of Monzo mobile payment service. * Dotted line: Line of interaction, Line: Line of visibility and Double line: Line of internal interaction

Monzo provides mainly free mobile account for the customers, however, recently has released the premium account called ‘Business Pro’ which costs £5 per month for small businesses and freelancers, the main feature of which is ‘Tax Pots’ that can calculate the tax based on their salary instead of an accountant <cite>(EPSTEIN, 2020)</cite>.  The tax calculation is used by third-party accounting software <cite>(O'Hear, 2020)</cite>.  Therefore, the blueprint of the payment service including tax calculation is seen in Figure 2.

![Figure 2](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598793940/%E5%9B%B32c.png "Figure 2")
Figure 2: The service blueprint of Monzo mobile payment service with ‘TaxPods’ for premium users.

## Staging (Recommendation)
The issue of introducing the premium account with new features mainly ‘Taxpods’ is if the customers have the willing-to-pay (WTP).  One of the methods to detect their WTP is theatre-based approaches which is based on the script (and role play) to envision the problem recommendation suggested by the service <cite>(Fragnière, Nanchen and Sitten, 2012)</cite>.  

### Blueprint of the Improved Service
As a result of playing a role as a premium user, the most significant mental silent attributions can be consistency among of them.  This is primary because Monzo is aiming to be ‘a bank that lives on your smartphone’ <cite>(AWS, 2020)</cite>.  This is likely to imply all payment transactions should be able to be delivered on the mobile for the consistency of their mission and therefore, the tax payment calculated by ‘TaxPods’ also should be able to be granted on the mobile.  In addition, the tax payment tends to be done regularly and annually and therefore, it should be done automatically.  Furthermore, the tax amount calculation is based on the customer’s annual income <cite>(EPSTEIN, 2020)</cite>.  Therefore, it might be required to restrict withdrawing a part of their deposit automatically in order to prepare the automatic tax payment because now the customer can deposit the money for any purpose in another pod in the same account by hand but they cannot do so automatically therefore it is important for mitigating customer’s pain and then it should be able to be confirmed and be noticed to the users as it is happened for the same reason of automatic reservation.  Figure 3 shows the blueprint of the recommended mobile payment service of Monzo including the tax payment for the premium users.  It is seen the customer is not required to a certain additional action for these improvements, however, they might feel they are going to prepare the tax payment by the reserve for the tax notification, which is likely to rise their WTP.  

![Figure 3](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598793972/%E5%9B%B33c.png "Figure 3")
Figure 3: The service blueprint of Monzo recommended mobile payment service.

## Future remark (Additional recommendations)
Tax calculation service (‘Taxpods’) was built as a result of customer surveys and feedbacks <cite>(O'Hear, 2020)</cite>.  In addition, the recommended service improvement in this essay are likely to increase WTP, however, how much they are going to pay for these services seem not to be verified sufficiently by the firm.  Theatre-based experimental study might also provide the solution for the pricing issue.  Therefore, the experiment should be designed for WTP and Price What You Want (PWYW).  The individuals selected randomly from the certain target segment such as millenniums are required to choose the feasible given options, the examples of which are GBP 0  , GBP 2, GBP 4, GBP 5 , GBP 7 <cite>(Catenazzo and Fragnière, 2010)</cite>.  Although it depends on the result of the experiment, at least, the one might be able to conclude if the customers have WTP and then if they have, how much PWYW is.

## Conclusion
This essay has discussed about the payment service of Monzo, especially pre transaction and post one of tax calculation which is offered for the premium users.  Moreover, the recommendation for the improvement of the total payment service including tax calculation in terms of service design method such as Ethnography, Script and Staging.  As a result of these analysis, the current tax calculation service seems to be not consistent with their mission and although they can reduce the cost the users hire an accountant or purchase an accounting service to integrate third party software with their service, there is still inconvenience and inconsistency.  This is mainly because the customers have an obligation to pay the tax after the calculation, and they must reserve the certain amount of money for the tax payment.  In addition, the service may not validate if the users have a willing to pay and how much they can pay for it.  Theatre-based statistic experiments can answer both issues.

## Appendix (The Result of Semi-directed Interview)
![Figure Appendix](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598794008/appendix_c.png "Figure Appendix")

## Reference
* Lauren, 2020. Monzo Review: Should you make the switch? [Online]. Available from: https://moneytothemasses.com/banking/monzo-review-should-you-make-the-switch/amp [Accessed 17 April 2020].
* CBInshight, 2020. Monzo [Online]. Available from: https://www.cbinsights.com/company/mondo [Accessed 17 April 2020].
* AWS, 2020. Monzo Case Study [Online]. Available from: https://aws.amazon.com/jp/solutions/case-studies/monzo/ [Accessed 17 April 2020].
* Strange, A., 2019. Every Company Will Be a Fintech Company [Online]. Available from: https://a16z.com/2020/01/21/every-company-will-be-a-fintech-company/ [Accessed 17 April 2020].
* Fragnière, E., Nanchen, B. and Sitten, M., 2012. Performing Service Design Experiments Using Ethnomethodology and Theatre-Based Reenactment: A Swiss Ski Resort Case Study
* REASON, B., LØVLIE, L. and FLU, M.B., 2016. SERVICE DESIGN FOR BUSINESS A Practical Guide to Optimizing the Customer Experience
* EPSTEIN, S., 2020. Monzo’s next big move is taking on broken business banking [Online]. Available from: https://www.wired.co.uk/article/monzo-business-account [Accessed 17 April 2020].
* O'Hear, S., 2020. Monzo launches free and paid-for business bank accounts [Online]. Available from: https://techcrunch.com/2020/03/17/monzo-business-bank-accounts/amp/ [Accessed 17 April 2020].
* Catenazzo, G. and Fragnière, E., 2010. Pricing Traditional Travel Agency Services: A Theatre-Based Experimental Study