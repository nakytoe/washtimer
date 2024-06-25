
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-25 09:00:00 EEST+0300 2024-06-25 10:00:00 EEST+0300               4.621
	          2 2024-06-25 09:00:00 EEST+0300 2024-06-25 11:00:00 EEST+0300                4.59
	          3 2024-06-25 08:00:00 EEST+0300 2024-06-25 11:00:00 EEST+0300            4.566667
	          4 2024-06-25 07:00:00 EEST+0300 2024-06-25 11:00:00 EEST+0300             4.49025

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-25 14:00:00 EEST+0300 2024-06-25 15:00:00 EEST+0300               2.738
	          2 2024-06-25 14:00:00 EEST+0300 2024-06-25 16:00:00 EEST+0300              2.7805
	          3 2024-06-25 14:00:00 EEST+0300 2024-06-25 17:00:00 EEST+0300            2.926333
	          4 2024-06-25 13:00:00 EEST+0300 2024-06-25 17:00:00 EEST+0300             3.00375


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
