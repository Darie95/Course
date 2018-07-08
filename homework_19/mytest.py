import unittest
import homework_19.tasks
from mock import patch
import datetime
import homework_19.homework_17_1
from PIL import Image


class TestMyCode(unittest.TestCase):
    def test_image(self):
        image = Image.open('large.jpeg')
        result_1 = homework_19.homework_17_1.resize(image, 100, 100)
        result_2 = homework_19.homework_17_1.resize(image, 100, None)
        result_3 = homework_19.homework_17_1.resize(image, None, 100)
        self.assertEqual((100, 100), result_1.size)
        self.assertEqual((100, 75), result_2.size)
        self.assertEqual((133, 100), result_3.size)
        self.assertRaises(ValueError, homework_19.homework_17_1.resize,image, None, None )

    def test_date(self):
        with patch('homework_19.tasks.datetime') as mock_date:
            mock_date.now.return_value = datetime.datetime(2018, 7, 5, 12, 30,
                                                           12)
            mock_date.side_effect = lambda *args, **kw: datetime(*args, **kw)
            assert homework_19.tasks.datetime.now() == datetime.datetime(2018,
                                                                         7, 5,
                                                                         12, 30,
                                                                         12)
            result = homework_19.tasks.task_2()
        self.assertEqual('2018-07-05,12:30', result)
