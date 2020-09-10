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
        Slug: 10.0998/FK2.stagefigshare.0000001
        DOI: 10.0998/FK2.stagefigshare.0000001
        SubmissionID: 00000000-0000-0000-0000-000000000001
        ManuscriptID: S000001
        Title: Example article title
        Date: 2020-04-20
        SubmissionDate: 2020-04-19
        PublishDate: 2020-04-20
        LastPublishDate: 2020-04-30
        Curator: Mr. Curator
        Kind: Original Article
        PubAuthors: Smith, J.
            Dobson, J. S.
            Doe, P.
        PubAuthorsORCID: 0000-0000-0000-0001
            0000-0000-0000-0003
            0000-0000-0000-0002
        PMRURL: https://models.example.org/workspace/240
        PrimaryPaperName: Example primary paper. 2020, B. Smith, J.S. Dobson
        PrimaryPaperURL: https://doi.org/10.0999/ex.2020.00
        FulltextURL:
        ArchiveURL:
        Abstract: We describe an example paper here
        ''').lstrip(), value)

    def test_json_to_markdown_as_text(self):
        data = pkg_resources.resource_string(
            'physiome.journal.tests', 'submission.json')
        value = submission.json_to_markdown(data)
        self.assertEqual(dedent('''
        Slug: 10.0998/FK2.stagefigshare.0000001
        DOI: 10.0998/FK2.stagefigshare.0000001
        SubmissionID: 00000000-0000-0000-0000-000000000001
        ManuscriptID: S000001
        Title: Example article title
        Date: 2020-04-20
        SubmissionDate: 2020-04-19
        PublishDate: 2020-04-20
        LastPublishDate: 2020-04-30
        Curator: Mr. Curator
        Kind: Original Article
        PubAuthors: Smith, J.
            Dobson, J. S.
            Doe, P.
        PubAuthorsORCID: 0000-0000-0000-0001
            0000-0000-0000-0003
            0000-0000-0000-0002
        PMRURL: https://models.example.org/workspace/240
        PrimaryPaperName: Example primary paper. 2020, B. Smith, J.S. Dobson
        PrimaryPaperURL: https://doi.org/10.0999/ex.2020.00
        FulltextURL:
        ArchiveURL:
        Abstract: We describe an example paper here
        ''').lstrip(), value)

    def test_json_to_markdown_manual_primary_papers(self):
        # resulting authors will be a simple string
        data = json.loads(pkg_resources.resource_string(
            'physiome.journal.tests', 'submission_manual_primary_papers.json'))
        value = submission.json_to_markdown(data)
        self.assertEqual(dedent('''
        Slug: 10.0998/FK2.stagefigshare.0000001
        DOI: 10.0998/FK2.stagefigshare.0000001
        SubmissionID: 00000000-0000-0000-0000-000000000002
        ManuscriptID: S000002
        Title: Example article title
        Date: 2020-04-20
        SubmissionDate: 2020-04-19
        PublishDate: 2020-04-20
        LastPublishDate: 2020-04-30
        Curator: Mr. Curator
        Kind: Original Article
        PubAuthors: Smith, J.
            Dobson, J. S.
            Doe, P.
        PubAuthorsORCID: 0000-0000-0000-0001
            0000-0000-0000-0003
            0000-0000-0000-0002
        PMRURL: https://models.example.org/workspace/240
        PrimaryPaperName: Example primary paper. 2020, Smith, J., Doe, P.
        PrimaryPaperURL: https://doi.org/10.0999/ex.2020.00
        FulltextURL:
        ArchiveURL:
        Abstract: We describe an example paper here
        ''').lstrip(), value)

    def test_json_to_markdown_with_null_orcid(self):
        data = pkg_resources.resource_string(
            'physiome.journal.tests', 'submission_with_null_orcid.json')
        value = submission.json_to_markdown(data)
        # curator is also missing in this export.
        self.assertEqual(dedent('''
        Slug: 10.0998/FK2.stagefigshare.0000001
        DOI: 10.0998/FK2.stagefigshare.0000001
        SubmissionID: 00000000-0000-0000-0000-000000000003
        ManuscriptID: S000003
        Title: Example article title
        Date: 2020-04-20
        SubmissionDate: 2020-04-19
        PublishDate: 2020-04-20
        LastPublishDate: 2020-04-30
        Curator:
        Kind: Original Article
        PubAuthors: Smith, J.
            Dobson, J. S.
            Doe, P.
        PubAuthorsORCID: 0000-0000-0000-0001
            \u200b
            0000-0000-0000-0002
        PMRURL: https://models.example.org/workspace/240
        PrimaryPaperName: Example primary paper. 2020, B. Smith, J.S. Dobson
        PrimaryPaperURL: https://doi.org/10.0999/ex.2020.00
        FulltextURL:
        ArchiveURL:
        Abstract: We describe an example paper here
        ''').lstrip(), value)
