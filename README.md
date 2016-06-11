# parsename
Python class to parse common long names used in Puerto Rico.

This class is a quick solution to parse most of the long composed names I have encountered in my data wrangling adventures. 

This class was designed to deal with name prefixes common in Puerto Rico like "de", "de la", "de los", "de las" and brake names into these components:

  1. first name
  2. initial
  3. paternal name (spanish: apellido paterno)
  4. maternal name (spanish: apellido materno)
 
  It is not a full name parser, like [python-nameparser](https://github.com/derek73/python-nameparser), which I highly recommend for handling English names with titles and other suffixes and prefixes.  

This work is licensed under the BSD License.
