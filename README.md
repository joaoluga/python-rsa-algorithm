# python-rsa-algorithm
## < Disclaimer ! >
> 1. This code was developed during my graduation (computer engineering @FIAP)
> 2. It was a challenge during our 'cyber security' classes.

## < What it is ? >
* This project is related to a challenge involving the RSA algorithm which we had to create our own code to process prime numbers with more than 30 digits (and, of course, your code should be performatic).
* Also, the code should generate prime numbers based on a given number of digits

## < Improvements ! >
* In this section I'll try to explain some improvements that I wasn't able to achieve back then.
    * **Large prime numbers**: The far as I could get, with an acceptable process time, was 900 digits. But what I realize in my tests it that the random generate of prime used to take longer with high prime numbers. Even using Miller Rabin Primality test, this is a task that I couldn't get in the highest performance. (probably I should have worked a little bit more in this class, since I just borrowed a script done here: https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python )
    * **Encode and Decode**: These two guys was, also, methods that used to take longer to process as the prime numbers get larger. I tried harder to used the best lopping methods that I could research, but as I achieve the solution that is in the code right now, I didn't found any other method to give more speed to them. (mea culpa: actually I found solutions like numba, cython, but I didn't tried them. But, in my research, I checked that they can give more speed to the loops )  

## HOPE YOU LIKE IT!
...and, if you want, give me your feedback ;)