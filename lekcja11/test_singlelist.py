import unittest
from singlelist import SingleList


class TestSingleList(unittest.TestCase):
    def setUp(self):
        self.list = SingleList()

    def test_is_empty(self):
        self.assertTrue(self.list.is_empty())
        self.list.insert_head(1)
        self.assertFalse(self.list.is_empty())

    def test_count(self):
        self.list.insert_head(1)
        self.list.insert_head(2)
        self.list.insert_head(3)
        self.assertEqual(self.list.count(), 3)

    def test_insert_head(self):
        self.list.insert_head(123)
        self.assertEqual(self.list.head.data, 123)
        self.assertEqual(self.list.tail.data, 123)
        self.assertEqual(self.list.count(), 1)
        self.list.insert_head(456)
        self.assertEqual(self.list.head.data, 456)
        self.assertEqual(self.list.tail.data, 123)
        self.assertEqual(self.list.count(), 2)

    def test_insert_tail(self):
        self.list.insert_tail(123)
        self.assertEqual(self.list.head.data, 123)
        self.assertEqual(self.list.tail.data, 123)
        self.assertEqual(self.list.count(), 1)
        self.list.insert_tail(456)
        self.assertEqual(self.list.head.data, 123)
        self.assertEqual(self.list.tail.data, 456)
        self.assertEqual(self.list.count(), 2)

    def test_remove_head(self):
        self.list.insert_tail(1)
        self.list.insert_tail(2)
        self.list.insert_tail(3)
        self.list.remove_head()
        self.assertEqual(self.list.head.data, 2)

    def test_remove_tail(self):
        self.list.insert_tail(1)
        self.list.insert_tail(2)
        self.list.insert_tail(3)
        self.list.remove_tail()
        self.assertEqual(self.list.tail.data, 2)

    def test_join(self):
        self.list.insert_tail(1)
        self.list.insert_tail(2)

        list2 = SingleList()
        list2.insert_tail(3)
        list2.insert_tail(4)

        self.list.join(list2)
        self.assertEqual(self.list.head.data, 1)
        self.assertEqual(self.list.tail.data, 4)
        self.assertEqual(self.list.count(), 4)

    def test_clear(self):
        self.list.insert_tail(1)
        self.list.insert_tail(2)
        self.list.insert_tail(3)
        self.list.clear()
        self.assertTrue(self.list.is_empty())
        self.assertEqual(self.list.count(), 0)

    def test_search(self):
        self.list.insert_tail(1)
        self.list.insert_tail(2)
        self.list.insert_tail(3)
        node = self.list.search(2)
        self.assertEqual(node.data, 2)
        node = self.list.search(4)
        self.assertIsNone(node)

    def test_find_min(self):
        self.list.insert_tail(1)
        self.list.insert_tail(2)
        self.list.insert_tail(3)
        self.assertEqual(self.list.find_min().data, 1)

    def test_find_max(self):
        self.list.insert_tail(1)
        self.list.insert_tail(2)
        self.list.insert_tail(3)
        self.assertEqual(self.list.find_max().data, 3)

    def test_reverse(self):
        self.list.insert_tail(1)
        self.list.insert_tail(2)
        self.list.reverse()
        self.assertEqual(self.list.head.data, 2)
        self.assertEqual(self.list.tail.data, 1)


if __name__ == '__main__':
    unittest.main()
