# Circadian-Lights
This is a repository detailing how to set up and use a Raspberry Pi connected to WS2812B LED lights.

My implementation turns the lights blue 15 minutes before my scheduled waking time, gradually increasing the brightness until I wake up.
To turn the lights red, the local sunset time is accessed every 24 hours using an OpenWeather API key, to maintain accuracy througout the year.

## Creating Virutal Environment
### Install venv (if not installed)
```
sudo apt install python3-venv -y
```
### Create a Virtual Environment
```
python3 -m venv ws2812b_env (you can rename)
```
### Activate the Virtual Environment
```
source ws2812b_env/bin/activate
```
### Install the required libraries
```
pip install -r requirements.txt
```
### Run your Script inside the Virtual Environment
```
python lights.py
```
