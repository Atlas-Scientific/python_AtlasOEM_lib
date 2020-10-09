from AtlasOEM import AtlasOEM

class AtlasOEM_RTD(AtlasOEM):
    
    DEFAULT_ADDRESS = 0x68
    
    def __init__(self, address=None, name = "", bus=None):
        super(AtlasOEM_RTD, self).__init__((address or self.DEFAULT_ADDRESS), name, bus)
        
    def read_new_reading_available(self):
        return self.read_byte(0x07)

    def write_new_reading_available(self, val):
        self.write_byte(0x07, val)

    def read_calibration_data(self):
        return self.read_32(0x08)/1000.0

    def write_calibration_data(self, val):
        self.write_32(0x08, (int)(val*1000))

    def write_calibration_request(self, val):
        self.write_byte(0x0C, val)
        
    def read_calibration_confirm(self):
        return self.read_byte(0x0D)
        
    def read_RTD_reading(self):
        return self.read_32(0x0E)/1000.0
        