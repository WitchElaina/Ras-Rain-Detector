import rain
import thermistor
import PCF8591 as ADC
import RPi.GPIO as GPIO

ADC_addr = {
    'rain': 0,
    'aDHT': 1,
    'thm': 2
}

PCF_addr = 0x48

def init():
    ADC.setup(PCF_addr)

if __name__ == '__main__':
    init()
    # rain.rain_mainloop(ADC_addr['rain'])
    thermistor.thm_loop(ADC_addr['thm'])