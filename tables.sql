	create table water(
	id SERIAL PRIMARY KEY,
	timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	level float,
	nodename varchar(20),
	container_instance varchar(20)
	);

	create table air(
	id SERIAL PRIMARY KEY,
	timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	pm25 float,
	pm10 float,
	temperature float,
	humidity float,
	co float,
	nh2 float,
	nh3 float,
	aqi float,
	aql float,
	aqimp boolean,
	datainterval boolean,
	nodename varchar(20),
	container_instance varchar(20)
	);

	create table wind(
	id SERIAL PRIMARY KEY,
	timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	solarradiation float,
	temperature float,
	relativehumidity float,
	winddirection float,
	windspeed float,
	gustspeed float,
	dewpoint float,
	batterydcvoltage float,
	rain float,
	pressure float,
	nodename varchar(20),
	container_instance varchar(20)
	);
