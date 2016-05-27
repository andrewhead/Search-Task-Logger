# Search Task Logger

This is a web API for logging search tasks from a browser equipped with the [search task add-on](https://github.com/andrewhead/Search-Task-Addon).
It's written for academic research, to find out where participants spend their time during information seeking tasks.

## Data security

The deploy scripts install an SSL certificate to encrypt HTTPS communication which might contain the contents and time of pages users visit.
I recommend using [Let's Encrypt](https://letsencrypt.org/) to generate the SSL certificates.
The certificate that we point Nginx to should be the generated `fullchain.pem` file.
In the future, it would be great to automate the process of renewal with the `webroot` subcommand.

Currently, there is no encryption of communication with Postgres from the server code.
This is because I make an assumption that all access to the database will occur over `localhost`, and the only folks who will have access to `localhost` are those trusted with seeing the data unencrypted.
If this assumption changes in the future, then queries to Postgres should also be encrypted.
