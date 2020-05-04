from io import StringIO


def json_to_markdown(data):
    return json_to_markdown_stream(data).getvalue()


def json_to_markdown_stream(data, stream=None):
    if stream is None:
        stream = StringIO()

    stream.write('Slug:\n')
    stream.write('DOI:\n')  # should be in the export?
    stream.write('Title: %s\n' % data['title'])
    stream.write('Date: %s\n' % data['publishDate'][:10])
    stream.write('PubAuthors: %s\n' % '\n    '.join('%s, %s.' % (
        name[-1], '. '.join(first_names[0] for first_names in name[:-1]))
        for name in (author['name'].split() for author in data['authors'])
    ))
    stream.write('MathsURL:\n')
    stream.write('PMRURL: %s\n' % data['modelPmrWorkspaceUri'])
    return stream
