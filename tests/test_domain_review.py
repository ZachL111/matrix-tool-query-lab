import unittest

from src.matrix_tool_query_lab.domain_review import DomainReview, review_lane, review_score


class DomainReviewTests(unittest.TestCase):
    def test_review_lane(self) -> None:
        item = DomainReview(67, 36, 11, 62)
        self.assertEqual(review_score(item), 199)
        self.assertEqual(review_lane(item), "ship")


if __name__ == "__main__":
    unittest.main()
