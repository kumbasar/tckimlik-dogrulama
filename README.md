# TC Id validator

## Usage

```bash
usage: main.py [-h] tc_id

positional arguments:
  tc_id       Set TC id

options:
  -h, --help  show this help message and exit

Process finished with exit code 0
```

Example:

```bash
kumbasar@x280:~/repo/tckimlik-verify$ ./main.py 10000000146
INFO:root:TC id validator
INFO:root:10000000146 is valid.
```


## Algorithm

1. Id must contain 11 digit
2. The first digit cannot be zero
3. 10th and 11th digit are use as a validator.
4. Verify tenth digit as follows:
```
Digit 10 == (7 * (Digit 1 + Digit 3 +  Digit 5 +  Digit 7 +  Digit 9) - (Digit 2 + Digit 4 +  Digit 6 +  Digit 8))  mod 10
```
5. Verify eleventh digit as follows:
```
Digit 11 == sum(Digit 1, Digit 2, ... , Digit 9, Digit 10) % 10
```

References: 
- [frmtr](https://www.frmtr.com/garip-olaylar/4181793-tc-kimlik-nolar-neden-hep-cift-rakam-ile-biter.html)
