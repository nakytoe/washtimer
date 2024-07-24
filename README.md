
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-24 20:00:00 EEST+0300 2024-07-24 21:00:00 EEST+0300              12.399
	          2 2024-07-24 19:00:00 EEST+0300 2024-07-24 21:00:00 EEST+0300              9.9875
	          3 2024-07-24 18:00:00 EEST+0300 2024-07-24 21:00:00 EEST+0300            8.643667
	          4 2024-07-24 17:00:00 EEST+0300 2024-07-24 21:00:00 EEST+0300               8.374

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-24 07:00:00 EEST+0300 2024-07-24 08:00:00 EEST+0300               2.733
	          2 2024-07-24 07:00:00 EEST+0300 2024-07-24 09:00:00 EEST+0300                2.79
	          3 2024-07-24 07:00:00 EEST+0300 2024-07-24 10:00:00 EEST+0300            2.856667
	          4 2024-07-24 07:00:00 EEST+0300 2024-07-24 11:00:00 EEST+0300             2.90475


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
