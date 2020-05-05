import unittest
import json
from textwrap import dedent

import pkg_resources
from physiome.journal import submission


class SubmissionTestCase(unittest.TestCase):

    def test_json_to_markdown(self):
        data = json.loads(pkg_resources.resource_string(
            'physiome.journal.tests', 'submission.json'))
        value = submission.json_to_markdown(data)
        self.assertEqual(dedent('''
        Slug:
        DOI:
        Title: Example article title
        Date: 2020-04-20
        PubAuthors: Smith, J.
            Dobson, J. S.
            Doe, P.
        MathsURL:
        PMRURL: https://models.example.org/workspace/240
        RunModelURL:
        PrimaryPaperName: Example primary paper. 2020, B. Smith, J.S. Dobson
        PrimaryPaperURL: https://doi.org/10.0999/ex.2020.00
        FulltextURL: https://www.example.org/articles/10.0999/ex.2020.00/pdf
        ArchiveURL: https://www.example.org/articles/10.0999/ex.2020.00/pdf
        Abstract: We describe an example paper here
        ''').lstrip(), value)
