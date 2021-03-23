#Takes a long log file of PGP encrypted messages and attempts to decrypt each with a known key
#Assumes you have used the gpg command to add the known key to your keyring

import subprocess

start = "-----BEGIN PGP SIGNED MESSAGE-----\n"
end = "-----END PGP SIGNATURE-----\n"

with open("FlagInHaystack.txt") as f:
    for l in f:
        if(l == start):
            temp = open("temp", 'w')
        if(l == end):
            temp.close()
            result = subprocess.run(["gpg", "-d", "temp"])
            if(result.returncode == 0):
                exit()
        else:
            temp.write(l)
