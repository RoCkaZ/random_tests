Running 3 cycles, each with 300 write() operations:  
  .. cycle #001: 3.953 secs vs. 10.735 secs  
  .. cycle #002: 3.953 secs vs. 10.734 secs  
  .. cycle #003: 3.953 secs vs. 10.719 secs  
Total duration WITHOUT setting timeout: 3.953 seconds  
Total duration WITH setting timeout: 10.729 seconds (2.7x slower)  

Running 5 cycles, each with 100 write() operations:  
  .. cycle #001: 0.422 secs vs. 3.141 secs  
  .. cycle #002: 0.437 secs vs. 3.125 secs  
  .. cycle #003: 0.438 secs vs. 3.140 secs  
  .. cycle #004: 0.438 secs vs. 3.125 secs  
  .. cycle #005: 0.437 secs vs. 3.141 secs  
Total duration WITHOUT setting timeout: 0.434 seconds  
Total duration WITH setting timeout: 3.134 seconds (7.2x slower)  

Running 10 cycles, each with 20 write() operations:  
  .. cycle #001: 0.000 secs vs. 0.625 secs  
  .. cycle #002: 0.016 secs vs. 0.609 secs  
  .. cycle #003: 0.016 secs vs. 0.640 secs  
  .. cycle #004: 0.000 secs vs. 0.625 secs  
  .. cycle #005: 0.016 secs vs. 0.625 secs  
  .. cycle #006: 0.000 secs vs. 0.641 secs  
  .. cycle #007: 0.000 secs vs. 0.625 secs  
  .. cycle #008: 0.015 secs vs. 0.625 secs  
  .. cycle #009: 0.000 secs vs. 0.625 secs  
  .. cycle #010: 0.016 secs vs. 0.625 secs  
Total duration WITHOUT setting timeout: 0.008 seconds  
Total duration WITH setting timeout: 0.626 seconds (79.3x slower)
