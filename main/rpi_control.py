import RPi.GPIO as GPIO
import time
import glob

FAN1_GPIO_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN1_GPIO_PIN, GPIO.OUT)

# These commands can be done at boot in /etc/modules
#os.system('modprobe w1-gpio')
#os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
TEMPERATURE_SENSOR_FILE = device_folder + '/w1_slave'


from math import sqrt
def mean_std_dev(durations):
    """ Calculate mean and standard deviation of data durations[]: """
    length, mean, std = len(durations), 0, 0
    for duration in durations:
        mean = mean + duration
    mean = mean / float(length)
    for duration in durations:
        std = std + (duration - mean) ** 2
    std = sqrt(std / float(length))
    mean = int(round(mean))
    std = int(round(std))
    return mean, std


def read_temp_raw():
    with open(TEMPERATURE_SENSOR_FILE) as tfile:
        text = tfile.readlines()
        return text

def read_current_temperature():
    """
    Read the temperature 10 times and returns an average of those measurements
    NOTE: Temperature is in Celsius
    """
    temperatures = []
    for i in xrange(0,10):
        lines = read_temp_raw():
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temperatures.append(float(temp_string) / 1000.0)
        time.sleep(0.1)
    mean, std = mean_std_dev(temperatures)
    return mean, std


def turn_on_cooling():
    GPIO.output(FAN1_GPIO_PIN, GPIO.HIGH)

def turn_off_cooling():
    GPIO.output(FAN1_GPIO_PIN, GPIO.LOW)


