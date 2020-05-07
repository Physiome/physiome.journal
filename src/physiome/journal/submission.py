import json
from io import StringIO


def json_to_markdown(data):
    return json_to_markdown_stream(data).getvalue()


def json_to_markdown_stream(data, stream=None):
    if isinstance(data, (bytes, str)):
        data = json.loads(data)

    if stream is None:
        stream = StringIO()

    stream.write('Slug: %s\n' % data['figshareArticleDoi'])
    stream.write('DOI: %s\n' % data['figshareArticleDoi'])
    stream.write('Title: %s\n' % data['title'])
    stream.write('Date: %s\n' % data['publishDate'][:10])
    stream.write('SubmissionDate: %s\n' % data['submissionDate'][:10])
    stream.write('PublishDate: %s\n' % data['publishDate'][:10])
    stream.write('LastPublishDate: %s\n' % data['lastPublishDate'][:10])
    stream.write('Kind: %s\n' % data['kind'])
    stream.write('PubAuthors: %s\n' % '\n    '.join(
        '%s, %s.' % (
            name[-1], '. '.join(first_names[0] for first_names in name[:-1]))
        for name in (author['name'].split() for author in data['authors'])
    ))
    stream.write('PubAuthorsORCID: %s\n' % '\n    '.join(
        author['orcid'] or 'null' for author in data['authors']
    ))
    stream.write('MathsURL:\n')
    stream.write('PMRURL: %s\n' % data['modelPmrWorkspaceUri'])
    stream.write('RunModelURL:\n')
    stream.write('PrimaryPaperName: %s. %s, %s\n' % (
        data['primaryPapers'][0]['title'],
        data['primaryPapers'][0]['year'],
        ', '.join(('%s. %s' % (
            '.'.join(fn[0] for fn in author['firstName'].split()),
            author['lastName'],
        ) for author in data['primaryPapers'][0]['authors']))
    ))
    stream.write('PrimaryPaperURL: https://doi.org/%s\n' % (
        data['primaryPapers'][0]['doi'],))
    stream.write('FulltextURL: %s\n' % data['primaryPapers'][0]['link'])
    stream.write('ArchiveURL: %s\n' % data['primaryPapers'][0]['link'])
    stream.write('Abstract: %s\n' % data['abstract'])
    return stream
