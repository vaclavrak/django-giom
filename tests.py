

test_data = """<status>
  <windspeed>0</windspeed>
  <winddir>3</winddir>
  <windgust>0</windgust>
  <pressure>1021.4</pressure>
  <systemp>18.0</systemp>
  <temperature>4.0</temperature>
  <baraltitude>231.0</baraltitude>
  <windchill>4.0</windchill>
  <relhumidity>77.5</relhumidity>
  <abshumidity>4.6</abshumidity>
  <dewpoint>0.4</dewpoint>
  <devname>GIOM 3000AE    </devname>
</status>"""


import unittest
from mock import MagicMock

from giom_data.GiomDataReader import GiomDataReader

class TestGiomParser(unittest.TestCase):

    def test_parsexml(self):
        gdr = GiomDataReader("http://aaa")
        gdr.read_data_xml = MagicMock(return_value = test_data)

        gdr.read()
        self.assertEqual(0.0, gdr['windspeed'])
        self.assertEqual(3.0, gdr['winddir'])
        self.assertEqual(0.0, gdr['windgust'])
        self.assertEqual(1021.4, gdr['pressure'])
        self.assertEqual(18.0, gdr['systemp'])
        self.assertEqual(4.0, gdr['temperature'])
        self.assertEqual(231.0, gdr['baraltitude'])
        self.assertEqual(4.0, gdr['windchill'])
        self.assertEqual(77.5, gdr['relhumidity'])
        self.assertEqual(4.6, gdr['abshumidity'])
        self.assertEqual(0.4, gdr['dewpoint'])


if __name__ == '__main__':
    unittest.main()