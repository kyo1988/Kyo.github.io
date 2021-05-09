---
layout: post
title: SALES FORECASTING
excerpt: "This is a modified version of the report for Business Analyics in Bath Full Time MBA Class of 2020."
categories: Business Analyics
tags: [Business Analyics]
comments: true
---

* Table of Contents
{:toc}

This is a modified version of the report for Business Analyics in Bath Full Time MBA Class of 2020.

# SALES FORECASTING

## Introduction
In this section, it is assumed and discussed that the recommended pizza will be added to the university catering service provider.  The firm also can offer a variety of food lines mainly including sandwiches, wraps, crisps, salad and sushi meals.  The supply chain management and cash-flow decisions of the company depend on one-month-ahead sales forecasting for 6 main meals.  However, the current method to predict the demands can be primitive.  This is primary because the monthly predictions have been done by the average of the last four month’s sales for each product with seasonal adjustments counted on their instinct.  In addition, weekly demand estimation is simply done by the monthly one divided by four or five based on the number of days in the target month.  Therefore, in section B, it is discussed how to improve one-month-ahead sales forecast.  The data related to sales history for six of the main food lines is extracted which is divided by two part in terms of the amount of sales to analyze in Figure 12 and Figure 13 respectively.  It is seen apparently most of food lines have a seasonality with the exception of ‘Wraps’ which might be almost constant.  

![Figure 12](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598707217/%E5%9B%B312.png "Figure 12")
![Figure 13](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598707276/%E5%9B%B313.png "Figure 13")

Although there are several types of quantitative methods including time series and explanatory, the data will be analyzed by time series.  One of the main reasons to do so is there is no other given explanatory data related to sales of food lines such as the size of market and share of that.  This means each food line sales cannot be regressed to other factors.  Therefore, time series analysis is suitable for the data.   Time series analysis assume the observed data is the sum of three elements which are the trend (constant change), seasonality (cycle change) and noise (random change), which are shown in Figure 14 though Figure 19 <cite>(Downey, 2011)</cite>.  

![Figure 14](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598707433/%E5%9B%B314.png "Figure 14")
![Figure 15](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598707953/%E5%9B%B315.png "Figure 15")
![Figure 16](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598708030/%E5%9B%B316.png "Figure 16")
![Figure 17](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598708062/%E5%9B%B317.png "Figure 17")
![Figure 18](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598708095/%E5%9B%B318.png "Figure 18")
![Figure 19](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598708130/%E5%9B%B319.png "Figure 19")

There is a significant difference between stationary and non-stationary time series.  This is because time series analysis also assumes the series is stationary which means no trend, no seasonality and the nature including amplitude and frequency of non-time varying noise <cite>(Janert, 2010)</cite>.  Hence, the assessment of the property plays the key role of the analysis.  The autocorrelation value of stationary time series incline to decrease rapidly <cite>(Palachy, 2019)</cite>.  Autocorrelation means each data point is interacted with the succeeding one in the data <cite>(Downey, 2011)</cite>.  In addition, partial autocorrelation can reveal authentic correlation of a series and its lag with the exception of the one contributing from the intermediate lags <cite>(Prabhakaran, 2019)</cite>.  From Figure 20 to Figure 25 show autocorrelations of the sales of food lines seem to degrade relatively gradually which may mean these time series are non-stationary.

![Figure 20](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598708425/%E5%9B%B320.png "Figure 20")
![Figure 21](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598708459/%E5%9B%B321.png "Figure 21")
![Figure 22](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598708491/%E5%9B%B322.png "Figure 22")
![Figure 23](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598708523/%E5%9B%B323.png "Figure 23")
![Figure 24](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598708555/%E5%9B%B324.png "Figure 24")
![Figure 25](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598708602/%E5%9B%B325.png "Figure 25")

Other ways to asses stationary are statistical tests primary including ADF (Augmented Dickey Fuller) test and KPSS (Kwiatkowski-Phillips-Schmidt-Shin) test <cite>(SINGH, 2018)</cite>.  The null hypothesis of the former test is the time series obtains non-stationary which means if the P-Value is less than the significance level (0.05), the null hypothesis might be rejected <cite>(Prabhakaran, 2019)</cite>. On the other hand, the null hypothesis of the latter test is reversed of the former (ibid).  The result of ADF and KPSS test for the sales data of food lines are shown Figure 26 and Figure 27 respectively.  Figure 26 shows P-Values are higher than 5% with the exception of ‘Wraps’, which means the time series of other food lines are likely to fail to reject null hypothesis and therefore they tend to be non-stationary.  However, time series of ‘Wraps’ considerably inclined to reject null hypothesis and hence is likely to be stationary.  One of main reasons to support the stationary of ‘Wraps’ sales is the null hypothesis is more likely to be rejected as ADF statistic value is more negative <cite>(Brownlee, 2016)</cite>.  Figure 27 demonstrates sales of ‘Crisps’ might be non-stationary due to the significance of P-Values (0.024 < 0.05).  However, the remains tend to be stationary because their P-Values are not significant (rejected non-stationary hypothesis).  There seems to be the contradictions between ADF test results and KPSS ones, however, there are the several types of stationarities which are strict stationary (the mean, variance and covariance do not depend on time), trend stationary (the equivalent of the strict one after removed a trend) and difference stationary (the equivalent of the strict one after differencing) <cite>(SINGH, 2018)</cite>.  In addition, KPSS test can categorize strict stationary or trend stationary and ADF test is also known as a difference stationarity test (ibid).

![Figure 26](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598708708/%E5%9B%B326.png "Figure 26")
![Figure 27](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598708742/%E5%9B%B327.png "Figure 27")

As a result of introducing the type of stationary, the sales of food lines can be separated as strict stationary, trend one and non-stationary (See Figure 28).

![Figure 28](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598708826/%E5%9B%B328.png "Figure 28")

However, stationary is required to improve the accuracy of the prediction due to the fact that time series modeling supposed to be so as a fundamental assumption.  There is some method to transform the series (strict) stationary such as taking the logarithm, differencing and removing rolling average <cite>(Prabhakaran, 2019)</cite>.  In fact, the differencing the sales of ‘Crisps’ seems to obtain strict stationary with ADF statistic value -7.230 (P-Value 0.000) and KPSS statistic value 0.136 (P-Value 0.100), which mean both tests might reject nonstationary hypothesis.  Hence, after executed the differentiation for other non-strict stationary, they might have strict stationary except the sales of ‘Salad’, which are shown in Figure 29 and Figure 30.  

![Figure 29](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598708899/%E5%9B%B329.png "Figure 29")
![Figure 30](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598708932/%E5%9B%B330.png "Figure 30")

Instead of differencing, removing 9 month moving average for the sales of ‘Salad’, it is more likely to possess strict stationary with ADF statistic value -4.506 (P-Value 0.000) and KPSS statistic value 0.304 (P-Value 0.100).  As a result of some transformations, more forecastable time series are obtained.   

## Box–Jenkins Method
### ARIMA
There are several forecast models for the time series mainly including autoregressive integrated moving average (ARIMA) model.  ARIMA is a forecast model based on the past data, its lags and the lagged error, which is determined by three factors that are the minimum number of differencing required to transform the series stationary (‘d’), the number of lags of the data to be employed as forecasters (‘p’) and the number of lagged estimated errors (‘q’) (ibid).  As it has shown, all series can be transformed to strict stationary one and therefore these might be modeled by ARIMA.  The parameters (p, q, d) were calibrated by minimizing Akaike Information Criteria (AIC) which is one of the common criteria to find the best model ones and it means the lower is better seen in Figure 31 <cite>(Prabhakaran, 2019)</cite>.  

![Figure 31](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598709070/%E5%9B%B331.png "Figure 31")

Figure 32 though 37 visualizes the estimated data in comparison with the observed one and the average of the last 4 month’s sales for the one.  It seems to relatively capture the features of the series such as trend and cycle in comparison with the current forecasting method, however, still the comparably differences between them are remained.  

![Figure 32](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598709420/%E5%9B%B332.png "Figure 32")
![Figure 33](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598709479/%E5%9B%B333.png "Figure 33")
![Figure 34](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598709636/%E5%9B%B334.png "Figure 34")
![Figure 35](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598709733/%E5%9B%B335.png "Figure 35")
![Figure 36](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598709768/%E5%9B%B336.png "Figure 36")
![Figure 37](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598709803/%E5%9B%B337.png "Figure 37")

### SARIMAX
Seasonal Autoregressive Integrated Moving-Average with Exogenous Regressors (SARIMAX) can be the well-known natural extension of ARIMA, which may improve the predictability further to adapt seasonal differencing that deduct the value from preceding season (ibid).  The best parameters including seasonal modeling ones (added bar s after the name of ARIMA ones to distinguish them) are selected in the certain range  as they have the lowest AIC in Figure 38.  

![Figure 38](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598709875/%E5%9B%B338.png "Figure 38")

However, the outcomes of modeling (shown in Figure 39 through Figure 44) might not suitable for the sales date of food lines due to the fact that it seems to overestimate the seasonality.  This may mean the more complex and lower AIC model do not lead to the higher accuracy of the prediction.  Therefore, it is required to adapt time series into another framework for the further improvement.

![Figure 39](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598710020/%E5%9B%B339.png "Figure 39")
![Figure 40](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598710072/%E5%9B%B340.png "Figure 40")
![Figure 41](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598710105/%E5%9B%B341.png "Figure 41")
![Figure 42](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598710150/%E5%9B%B342.png "Figure 42")
![Figure 43](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598710182/%E5%9B%B343.png "Figure 43")
![Figure 44](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598710214/%E5%9B%B344.png "Figure 44")

## State Space Model
One of the best alternatives of Box–Jenkins approach such as ARIMA can be state space models <cite>(Meulman and Koopman, 2007)</cite>.  It formulates the unobserved dynamic process (state) of time series, which can divide a several components such as deterministic (or stochastic) level, slope and seasonal, therefore, they are individually formulated and estimated (ibid).  Although there are several state space models, the best fit models are determined by the lowest AIC which is shown in Figure 45.  Figure 46 through 51 demonstrate the comparison observed data, current forecast (4 months moving average) and the best fit liner state space model.  It can be seen state space model might be able to predict more accuracy than ARIMA models with exception of the eldest year (2018-2019).  

![Figure 45](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598710394/%E5%9B%B345.png "Figure 45")
![Figure 46](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598710429/%E5%9B%B346.png "Figure 46")
![Figure 47](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598710473/%E5%9B%B347.png "Figure 47")
![Figure 48](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598710511/%E5%9B%B348.png "Figure 48")
![Figure 49](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598710555/%E5%9B%B349.png "Figure 49")
![Figure 50](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598710588/%E5%9B%B350.png "Figure 50")
![Figure 51](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598710644/%E5%9B%B351.png "Figure 51")

## The Prophet Forecasting Model
Another type of mothed can be Prophet which is developed by Facebook for time series analysis <cite>(Taylor and Letham, 2017)</cite>.  This model estimates the trend of time series by extending the generalized additive model which is a class of regression models and do so the seasonality by Fourier series, the parameters of which are calibrated by AIC automatically (ibid).  The result seen in Figure 52 through 57 seem to predict more feasible than ARIMA and state space model with exception of the latest year (after the late of 2021).  

![Figure 52](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598710814/%E5%9B%B352.png "Figure 52")
![Figure 53](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598710857/%E5%9B%B353.png "Figure 53")
![Figure 54](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598710891/%E5%9B%B354.png "Figure 54")
![Figure 55](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598710947/%E5%9B%B355.png "Figure 55")
![Figure 56](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598710979/%E5%9B%B356.png "Figure 56")
![Figure 57](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598711016/%E5%9B%B357.png "Figure 57")

## LSTM RNN
One of the major alternatives to rise the predictability of time series can be Long Short-Term Memory network (LSTM).  It is a specialized layer of Recurrent Neural Network (RNN) that is more suitable for time series than other type of NN to manage an internal state encapsulating the data seen earlier <cite>(TensorFlow, 2020)</cite>.  The architecture of LSTM RNN used for sales predictions of food lines is seen in Figure 58, which has the input shape, which is 3-time step with 1 feature, 100 neurons in LSTM layer, dropout  50% and a Dense output layer with 1 neuron.  It is also used the Mean Absolute Error (MAE) loss function and RMSprop  as an optimization algorithm to fit for 1000 training epochs with a batch size of 1.  It is trained by 67% of the data and the remains are used for the predictions.  The forecast by LSTM RNN (seen in Figure 59 through Figure 64) show it tends to underestimate the amount of sales in the reason of forecast period (the latest 17 months).  

![Figure 58](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598711340/%E5%9B%B358.png "Figure 58")


![Figure 59](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598711386/%E5%9B%B359.png "Figure 59")
![Figure 60](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598711426/%E5%9B%B360.png "Figure 60")
![Figure 61](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598711478/%E5%9B%B361.png "Figure 61")
![Figure 62](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598711514/%E5%9B%B362.png "Figure 62")
![Figure 63](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598711556/%E5%9B%B363.png "Figure 63")
![Figure 64](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598711596/%E5%9B%B364.png "Figure 64")

## Comparison 
Mean Square Error (MSE) can be one of the most common method to compare the model accuracy.  Figure 65 demonstrates MSEs of the models, the parameters of which are chosen by the lowest AIC.  It can be seen the most accurate model might depend on the food lines, for example, ARIMA model should be selected if it is required to forecast the sales of ‘Salad’ because it lead to the lowest MSE, however, as for ‘Sushi’ and ‘Crisps’, LSTM model is preferable.  In addition, Prophet model is recommended if the objective of sales predictions is ‘Wraps’, ‘Sandwiches’ and ‘Crisps’.

![Figure 65](https://res.cloudinary.com/djiyxp5ax/image/upload/v1598711636/%E5%9B%B365.png "Figure 65")

## Reference
* Brownlee, J., 2016. How to Check if Time Series Data is Stationary with Python [Online]. Available from: https://machinelearningmastery.com/time-series-data-stationary-python/ [Accessed 30 March 2020].
* Brownlee, J., 2017. Long Short-Term Memory Networks with Python
* Downey, A.B., 2011. Think Stats
* Janert, P.K., 2010. Data Analysis with Open Source Tools
* Janssens, W., Wijnen, K., Pelsmacker, P.D., Kenhove, P.V., 2008. Marketing Research with SPSS (FT Prentice Hall)
* Lilien, G.L. and Rangaswamy, A., 2002. Marketing Engineering: Computer Assisted Marketing Analysis and Planning
* Meulman, J.J. and Koopman, S.J., 2007. An Introduction to State Space Time Series Analysis
* Palachy, S., 2019. Detecting stationarity in time series data [Online]. Available from: https://towardsdatascience.com/detecting-stationarity-in-time-series-data-d29e0a21e638 [Accessed 30 March 2020].
* Prabhakaran, S., 2019. ARIMA Model – Complete Guide to Time Series Forecasting in Python [Online]. Available from: https://www.machinelearningplus.com/time-series/arima-model-time-series-forecasting-python/ [Accessed 30 March 2020].
* Prabhakaran, S., 2019. Time Series Analysis in Python – A Comprehensive Guide with Examples [Online]. Available from: https://www.machinelearningplus.com/time-series/time-series-analysis-python/ [Accessed 30 March 2020].
* SINGH, A., 2018. A Gentle Introduction to Handling a Non-Stationary Time Series in Python [Online]. Available from: https://www.analyticsvidhya.com/blog/2018/09/non-stationary-time-series-python/ [Accessed 30 March 2020].
* Taylor, S.J. and Letham, B., 2017. Forecasting at scale. PeerJ Preprints 5:e3190v2 https://doi.org/10.7287/peerj.preprints.3190v2
* TensorFlow, 2020. Time series forecasting [Online]. Available from: https://www.tensorflow.org/tutorials/structured_data/time_series [Accessed 30 March 2020].
* Tieleman, T. and Hinton, G., 2012. Lecture 6.5-rmsprop: Divide the Gradient by a Running Average of Its Recent Magnitude. COURSERA: Neural Networks for Machine Learning, 4, 26-31.
* Wierenga, B., 2008. Handbook of Marketing Decision Models