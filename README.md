# PyWeatherCast

PyWeatherCast is a Python-based command-line tool that empowers users to effortlessly retrieve detailed weather information for any city. Whether you are a weather enthusiast or need specific details such as temperature, humidity, and more, PyWeatherCast has you covered.

## Features

- **City-Specific Weather:** Obtain real-time weather data for any city by simply providing its name.

- **Customizable Requests:** Tailor your weather requests by specifying the details you're interested in.

- **Flexible Output:** Receive weather information in a format that suits your needs.

## Usage

### Basic Usage

```bash
python main.py CityName
```

Replace `CityName` with the name of the city you're interested in.

### Customizing Requests

```bash
python main.py CityName --details temperature humidity
```

This command fetches specific details, such as temperature and humidity, for the specified city.

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AndJann/PyWeatherCast.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd PyWeatherCast
   ```

3. **Run the script:**

   ```bash
   python main.py  CityName
   ```
or

   ```bash
   python main.py  CityName --parameter temperature wind_speed etc...
   ```

## Dependencies

- Python 3.x
