import unittest
from datetime import datetime


class Payment(unittest.TestCase):

    def test_split_array(self):
        data2 = ['ERICK=MO00:01-09:00,TH12:00-14:00,SU20:00-22:00']
        data = []
        for item in range(len(data2)):
            data.append(data2[item].split('='))
        return data

    def test_convert_time(self):
        datetime.strptime('00:00', '%H:%M').time()
        datetime.strptime('09:00', '%H:%M').time()
        datetime.strptime('18:00', '%H:%M').time()
        datetime.strptime('00:01', '%H:%M').time()
        datetime.strptime('14:00', '%H:%M').time()
        datetime.strptime('15:00', '%H:%M').time()
        datetime.strptime('16:00', '%H:%M').time()

    def test_split_hours(self):
        self = [
            ['RENE', 'MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'],
            ['ASTRID', 'MO10:00-12:00,TH12:00-14:00,SU20:00-22:00'],
            ['ANGEL', 'MO10:00-12:00,TH12:00-14:00,SU20:00-22:00'],
            ['MIGUEL',
             'MO10:00-12:00,TH12:00-14:00,SU20:00-22:00,MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'],
            ['ERICK', 'MO00:01-09:00,TH12:00-14:00,SU20:00-22:00']
        ]
        count = 0
        for elem in self:
            self[count][1] = elem[1].split(',')
            count += 1
        return self


if __name__ == '__main__':
    unittest.main()
