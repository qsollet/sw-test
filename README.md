# SW-test

Small application to generate and manage shorturl

## Shorturl object

- id: 6 alphanum char (the short url)
- url: string, the long url
- created_at
- accessed: increment the number of time accessed
- updated_at (can also be describe as last accessed at)

## API endpoint

- shorturl creation: `/c/<url>`
- redirection: `/r/<shorturl>` or directly `/<shorturl>`
- deprecate url: `/d/`
