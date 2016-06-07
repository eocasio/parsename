#-*- encoding: utf-8 -*-
class NameParser(object):
    
    def __init__(self, full_name):
        
        self.prefixes = ["de","del","de la", "de lo", "de las", "de los" ]
        
        self.first_name = ""
        self.middle_name = ""
        self.paternal_name = ""
        self.maternal_name = ""
        self.name_parts = ""
        self.full_name = full_name
        
        if not full_name.strip():
            raise Exception("String required")
        else:
            self.name_parts = full_name.split()
        
        self.parse_name()
        
    def parse_name(self):
        """ Parsing puertorrican names """
        
        name_parts = self.name_parts
        
        self.first_name = name_parts[0]
        
        remaining_parts = name_parts[1:]
        
        # Get paternal_name
        active_prefix = False
        temp_name = ""
        temp_name_list = []
        
        for part in remaining_parts:
            
            if active_prefix:
                temp_name = temp_name + " " + part
                if not (temp_name.lower() in self.prefixes):
                    active_prefix = False
                    temp_name_list.append(temp_name)
                    temp_name = ""                    
            elif part.lower() == "de":
                # Has prefix
                temp_name = part
                active_prefix = True
            else:
                temp_name_list.append(part)
        
        #~ print temp_name_list
        
        try:
            if len(temp_name_list) >= 3:                
                self.middle_name = temp_name_list[0]
                self.paternal_name = temp_name_list[1]
                self.maternal_name = temp_name_list[2]
            else:
                self.paternal_name = temp_name_list[0]
                self.maternal_name = temp_name_list[1]
                
        except IndexError:
            pass

    def __repr__(self):
        return "first_name: %s\nmiddle_name: %s\npaternal_name: %s\nmaternal_name: %s" % (self.first_name, self.middle_name, self.paternal_name, self.maternal_name)


if __name__ == "__main__":
    
    names = ["Edwood Ocasio",
    "Edwood Ocasio Vicente",
    "Manuel Joel Vicente Yera",
    "Maria L.M. Rivera Torres",
    "Nestor García de Jesus",
    "Jose Colón de la Torre",
    "Jose De los Angeles De Jesus",
    "Jose C. De los Angeles De Jesus",
    " ",
    ]
    
    
    for full_name in names:
        
        nm = NameParser(full_name)
        print "first:", nm.first_name
        print "middle:", nm.middle_name
        print "paternal:", nm.paternal_name
        print "maternal:",nm.maternal_name
        print
