from AtlasOEM_PH import AtlasOEM_PH
from AtlasOEM_RTD import AtlasOEM_RTD

import time

def main(): 
    PH = AtlasOEM_PH() # create an OEM PH object
    RTD = AtlasOEM_RTD() # create an OEM RTD object
    
    PH.write_active_hibernate(1) # tell the circuits to start taking readings
    RTD.write_active_hibernate(1)
    
    RTD_reading = 0;
    
    while True:
        if RTD.read_new_reading_available():              # if we have a new reading
            RTD_reading = RTD.read_RTD_reading()            # get it from the circuit
            #print("OEM RTD reading: " + str(RTD_reading))  # print the reading
            RTD.write_new_reading_available(0)  # then clear the new reading register 
                                                # so the circuit can set the register
                                                # high again when it acquires a new reading
            if RTD_reading > -1000:             # if theres a temperature probe connected
                PH.write_temperature_compensation(RTD_reading)  # compensate the pH circuit's temperature
                
        else:
            #print("waiting")
            time.sleep(.3)                      #if theres no reading, wait some time to not poll excessively
            
        if PH.read_new_reading_available():              # if we have a new reading
            pH_reading = PH.read_PH_reading()            # get it from the circuit
            pH_temp = PH.read_temperature_confirmation() # get what temperature the reading occured at
            print("OEM pH reading: " + str(pH_reading) + " @ " + str(pH_temp))  # print the reading
            PH.write_new_reading_available(0)   # then clear the new reading register 
                                                # so the circuit can set the register
                                                # high again when it acquires a new reading
        else:
            #print("waiting")
            time.sleep(.3)                      #if theres no reading, wait some time to not poll excessively
        
if __name__ == '__main__':
    main()
