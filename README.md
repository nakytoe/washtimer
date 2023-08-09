
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-10 10:00:00 EEST+0300 2023-08-10 11:00:00 EEST+0300                2.89
	          2 2023-08-10 10:00:00 EEST+0300 2023-08-10 12:00:00 EEST+0300              2.8785
	          3 2023-08-10 10:00:00 EEST+0300 2023-08-10 13:00:00 EEST+0300            2.866333
	          4 2023-08-10 09:00:00 EEST+0300 2023-08-10 13:00:00 EEST+0300             2.81125

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-09 16:00:00 EEST+0300 2023-08-09 17:00:00 EEST+0300               0.644
	          2 2023-08-09 16:00:00 EEST+0300 2023-08-09 18:00:00 EEST+0300              0.6755
	          3 2023-08-10 03:00:00 EEST+0300 2023-08-10 06:00:00 EEST+0300            0.713667
	          4 2023-08-10 02:00:00 EEST+0300 2023-08-10 06:00:00 EEST+0300             0.72375


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
