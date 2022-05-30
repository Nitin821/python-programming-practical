What are the possible outcome(s) from the following code?  
import random
PICK=random.randint (1,3)
CITY= ["DELHI", "MUMBAI", "CHENNAI", "KOLKATA"]
for I in CITY:
    for J in range (0, PICK):
        print (I, end = "")
    print ()
(i)	(ii)	(iii)	(iv)
DELHIDELHI	DELHI	DELHI	DELHI
MUMBAIMUMBAI	DELHIMUMBAI	MUMBAI	MUMBAIMUMBAI
CHENNAICHENNAI	DELHIMUMBAICHENNAI	CHENNAI	KOLKATAKOLKATAKOLKATA
KOLKATAKOLKATA		KOLKATA	
Ans. Option (i) and (iii) are possible
© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
