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
- list shorturls (for debug): `/l/`

## How to run

Start the project with `docker-compose up`, then you can visit http://127.0.0.1:8000
To create a short url you can use this for example http://127.0.0.1:8000/c/https://www.nextinpact.com/
To consume the short url just click on the link that is then displayed on the page.
