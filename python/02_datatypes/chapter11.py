from collections import namedtuple

import arrow

brewing_time = arrow.utcnow()
brewing_time.to("Europe/Rome")
chaiProfile = namedtuple("chaiProfile",["flavor","aroma"])
print(chaiProfile)

