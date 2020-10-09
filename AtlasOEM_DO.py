from AtlasOEM import AtlasOEM

class AtlasOEM_DO(AtlasOEM):
    
    DEFAULT_ADDRESS = 0x67
    
    def __init__(self, address=None, name = "", bus=None):
        super(AtlasOEM_DO, self).__init__((address or self.DEFAULT_ADDRESS), name, bus)
        
    def read_new_reading_available(self):
        return self.read_byte(0x07)

    def write_new_reading_available(self, val):
        self.write_byte(0x07, val)

    def write_calibration_request(self, val):
        self.write_byte(0x08, val)
        
    def read_calibration_confirm(self):
        return self.read_byte(0x09)
        
    def read_salinity_compensation(self):
        return self.read_32(0x0A)/100.0

    def write_salinity_compensation(self, val):
        self.write_32(0x0A, (int)(val*100))
        
    def read_pressure_compensation(self):
        return self.read_32(0x0E)/100.0

    def write_pressure_compensation(self, val):
        self.write_32(0x0E, (int)(val*100))

    def read_temperature_compensation(self):
        return self.read_32(0x12)/100.0

    def write_temperature_compensation(self, val):
        self.write_32(0x12, (int)(val*100))
        
    def read_salinity_confirmation(self):
        return self.read_32(0x16)/100.0   
        
    def read_pressure_confirmation(self):
        return self.read_32(0x1A)/100.0      
        
    def read_temperature_confirmation(self):
        return self.read_32(0x1E)/100.0    
        
    def read_DO_reading(self):
        return self.read_32(0x022)/100.0
        
    def read_percent_saturation_reading(self):
        return self.read_32(0x026)/100.0
        