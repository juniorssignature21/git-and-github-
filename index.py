import pdfkit

# From local HTML file
pdfkit.from_file('index.html', 'output.pdf')

# # Or from HTML string
# html = '<h1>Hello, PDF!</h1><p>This is a test.</p>'
# pdfkit.from_string(html, 'output.pdf')

# Or from a URL
# pdfkit.from_url('https://example.com', 'webpage.pdf')
