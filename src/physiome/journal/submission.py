import json
from io import StringIO

kind_map = {
    "original": "Original Article",
    "retrospective": "Retrospective Article",
    "review": "Review",
    "letter": "Letter",
    "draft": "Draft",
    "special": "Special Issue",
}


def json_to_markdown(data):
    return json_to_markdown_stream(data).getvalue()


def json_to_markdown_stream(data, stream=None):
    if isinstance(data, (bytes, str)):
        data = json.loads(data)

    if stream is None:
        stream = StringIO()
    curator_name = (
        ' %s' % data['curator']['displayName']
        if 'curator' in data and data['curator']
        and 'displayName' in data['curator']
        else '')

    stream.write('Slug: %s\n' % data['figshareArticleDoi'])
    stream.write('DOI: %s\n' % data['figshareArticleDoi'])
    stream.write('SubmissionID: %s\n' % data['id'])
    stream.write('ManuscriptID: %s\n' % data['manuscriptId'])
    stream.write('Title: %s\n' % data['title'])
    stream.write('Date: %s\n' % data['publishDate'][:10])
    stream.write('SubmissionDate: %s\n' % data['submissionDate'][:10])
    stream.write('PublishDate: %s\n' % data['publishDate'][:10])
    stream.write('LastPublishDate: %s\n' % data['lastPublishDate'][:10])
    stream.write('Curator:%s\n' % curator_name)
    stream.write('Kind: %s\n' % kind_map.get(data['kind'], data['kind']))
    stream.write('PubAuthors: %s\n' % '\n    '.join(
        '%s, %s.' % (
            name[-1], '. '.join(first_names[0] for first_names in name[:-1]))
        for name in (author['name'].split() for author in data['authors'])
    ))
    stream.write('PubAuthorsORCID: %s\n' % '\n    '.join(
        author['orcid'] or '\u200b' for author in data['authors']
    ))
    # stream.write('MathsURL:\n')
    stream.write('PMRURL: %s\n' % data['modelPmrWorkspaceUri'])
    # stream.write('RunModelURL:\n')
    stream.write('PrimaryPaperName: %s. %s, ' % (
        data['primaryPapers'][0]['title'],
        data['primaryPapers'][0]['year'],
    ))
    if isinstance(data['primaryPapers'][0]['authors'], list):
        stream.write('%s\n' % (
            ', '.join(('%s. %s' % (
                '.'.join(fn[0] for fn in author['firstName'].split()),
                author['lastName'],
            ) for author in data['primaryPapers'][0]['authors']))
        ))
    else:
        stream.write('%s\n' % (data['primaryPapers'][0]['authors']))

    stream.write('PrimaryPaperURL:')
    if 'doi' in data['primaryPapers'][0]:
        stream.write(' https://doi.org/%s\n' % data['primaryPapers'][0]['doi'])
    else:
        stream.write('\n')

    # stream.write('FulltextURL: %s\n' % data['primaryPapers'][0]['link'])
    # stream.write('ArchiveURL: %s\n' % data['primaryPapers'][0]['link'])
    stream.write('FulltextURL:\n')
    stream.write('ArchiveURL:\n')
    stream.write('Abstract: %s\n' % data['abstract'])
    return stream
