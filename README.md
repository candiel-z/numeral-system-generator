# Numeral System Generator
A simple class that encodes any numeral system from the decimal system using the alphabet and decodes back

# Installing:
<li>place file into project directory</li>
<li>import as Python module</li>

# Class settings:
<li>max_output_length -- maximum output code string length not including '-'</li>
<li>alphabet_len -- slice length from ALPHABET</li>
<li>autoincrement_step -- step for returned generator</li>
<li>autoincrement -- possible to use get_generator()</li>
<li>disable_negative_numbers -- set amplitude >= 0; num < 0 will raise 'Input number out of range' exception</li>
<li>disable_out_of_range_exception -- num > amplitude will be counted from the begginning (e.g. 130/(-127 -- 128) -> -126)</li>
<li>remove_unnecessary_chars -- remove unused characters from the code string (e.g. -000F0 -> -F0)</li>

# Using
<li>This is a potential generator of URLs or identifiers in as large numeral system as is needed to reduce the length of the result. 
For example, you can put from -1,180,591,620,717,411,303,424 to 1,180,591,620,717,411,303,424 variants in just 10 characters string with an alphabet length 128. 
Which is x2.2 times less characters.</li>
<li>Also you can use this app as any-to-any numeral system converter.</li>
