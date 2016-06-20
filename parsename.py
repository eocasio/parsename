#-*- encoding: utf-8 -*-
"""
Copyright (c) 2016, Edwood Ocasio
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import re

class NameParser(object):
    
    def __init__(self, full_name):
        
        self.prefixes = ["de la", "de lo", "de las", "de los"]
        self.prefixes_start = [ "de", "del",  "mc"]
        
        self.initial_regex = re.compile(r'^(\w\.|[A-Z])?$', re.U)
        
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
    
    def is_initial(self, part):
        
        return bool(self.initial_regex.match(part))
        
    def parse_name(self):
        """ Parsing puerto rican names """
        
        name_parts = self.name_parts
        
        self.first_name = name_parts[0]
        
        remaining_parts = name_parts[1:]
        
        # Get paternal_name
        active_prefix = False
        temp_name = ""
        temp_name_list = []
        has_initial = False
        
        for part in remaining_parts:
            
            if self.is_initial(part):
                #~ temp_name_list.append(part)
                has_initial = True
                
            if active_prefix:
                temp_name = temp_name + " " + part
                if not (temp_name.lower() in self.prefixes):
                    active_prefix = False
                    temp_name_list.append(temp_name)
                    temp_name = ""                    
            elif part.lower() in self.prefixes_start:
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
                if has_initial:
                    self.middle_name = temp_name_list[0]
                    self.paternal_name = temp_name_list[1]
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
    "Mario C. De los Angeles De la Torres",
    "MARIA DEL C COSTA",
    "CYNTHIA M. CHARLESTONE",
    "MARIA DE L. DIAZ",
    "JOHN JAMES GONZALEZ ORTIZ",
    "SONIALY A MC CLINTOSH",
    "MARIA DE TORRES CRUZ",
    "Nestor del Valle",
    " ",
    ]
    
    
    for full_name in names:
        
        nm = NameParser(full_name)
        print nm
        print 

