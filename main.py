#!/usr/bin/env python3

import logging

TCID_LENGTH = 11

def validator(tc_id: str) -> bool:

    if len(tc_id) != TCID_LENGTH:
        logging.warning("TC id length is not 11. Length: %d" % len(tc_id))
        return False

    if tc_id[0] == '0':
        logging.warning("First digit cannot be 0.")
        return False

    id_arr = [int(d) for d in list(tc_id)]

    d9 = 7 * (sum(id_arr[:-2][0::2])) - sum(id_arr[:-2][1::2])
    d9 = d9 % 10

    if d9 != id_arr[9]:
        logging.warning("Not pass digit 10 validation.")
        return False

    d10 = sum(id_arr[:-1]) % 10

    if d10 != id_arr[10]:
        logging.warning("Not pass digit 11 validation.")
        return False

    return True


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    logging.info("TC id validator")

    tc_id = "10000000146"

    result = validator(tc_id)

    if result:
        logging.info("%s is valid." % tc_id)
    else:
        logging.info("%s is not valid." % tc_id)

