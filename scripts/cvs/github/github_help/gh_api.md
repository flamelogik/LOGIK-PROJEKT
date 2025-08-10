# gh api Command

Makes an authenticated HTTP request to the GitHub API and prints the response.

## Usage

```
gh api <endpoint> [flags]
```

## Flags

*   `--cache duration`: Cache the response, e.g. "3600s", "60m", "1h"
*   `-F`, `--field key=value`: Add a typed parameter in key=value format
*   `-H`, `--header key:value`: Add a HTTP request header in key:value format
*   `--hostname string`: The GitHub hostname for the request (default "github.com")
*   `-i`, `--include`: Include HTTP response status line and headers in the output
*   `--input file`: The file to use as body for the HTTP request (use "-" to read from standard input)
*   `-q`, `--jq string`: Query to select values from the response using jq syntax
*   `-X`, `--method string`: The HTTP method for the request (default "GET")
*   `--paginate`: Make additional HTTP requests to fetch all pages of results
*   `-p`, `--preview names`: GitHub API preview names to request (without the "-preview" suffix)
*   `-f`, `--raw-field key=value`: Add a string parameter in key=value format
*   `--silent`: Do not print the response body
*   `--slurp`: Use with "--paginate" to return an array of all pages of either JSON arrays or objects
*   `-t`, `--template string`: Format JSON output using a Go template; see "gh help formatting"
*   `--verbose`: Include full HTTP request and response in the output

## Inherited Flags

*   `--help`: Show help for command

## Examples

```bash
# List releases in the current repository
$ gh api repos/{owner}/{repo}/releases

# Post an issue comment
$ gh api repos/{owner}/{repo}/issues/123/comments -f body='Hi from CLI'

# Post nested parameter read from a file
$ gh api gists -F 'files[myfile.txt][content]=@myfile.txt'

# Add parameters to a GET request
$ gh api -X GET search/issues -f q='repo:cli/cli is:open remote'

# Set a custom HTTP header
$ gh api -H 'Accept: application/vnd.github.v3.raw+json' ...

# Opt into GitHub API previews
$ gh api --preview baptiste,nebula ...

# Print only specific fields from the response
$ gh api repos/{owner}/{repo}/issues --jq '.[].title'

# Use a template for the output
$ gh api repos/{owner}/{repo}/issues --template \
  '{{range .}}{{.title}} ({{.labels | pluck "name" | join ", " | color "yellow"}}){{"\n"}}{{end}}'

# Update allowed values of the "environment" custom property in a deeply nested array
$ gh api -X PATCH /orgs/{org}/properties/schema \
   -F 'properties[][property_name]=environment' \
   -F 'properties[][default_value]=production' \
   -F 'properties[][allowed_values][]=staging' \
   -F 'properties[][allowed_values][]=production'

# List releases with GraphQL
$ gh api graphql -F owner='{owner}' -F name='{repo}' -f query='\n  query($name: String!, $owner: String!) {\n    repository(owner: $owner, name: $name) {\n      releases(last: 3) {\n        nodes { tagName }\n      }\n    }\n  }\n'

# List all repositories for a user
$ gh api graphql --paginate -f query='\n  query($endCursor: String!) {\n    viewer {\n      repositories(first: 100, after: $endCursor) {\n        nodes { nameWithOwner }\n        pageInfo {\n          hasNextPage\n          endCursor\n        }\n      }\n    }\n  }\n'

# Get the percentage of forks for the current user
$ gh api graphql --paginate --slurp -f query='\n  query($endCursor: String!) {\n    viewer {\n      repositories(first: 100, after: $endCursor) {\n        nodes { isFork }\n        pageInfo {\n          hasNextPage\n          endCursor\n        }\n      }\n    }\n  }\n' | jq 'def count(e): reduce e as $_ (0;.+1);\n[.[].data.viewer.repositories.nodes[]] as $r | count(select($r[].isFork))/count($r[])'
```

## Environment Variables

*   `GH_TOKEN`, `GITHUB_TOKEN` (in order of precedence): an authentication token for `github.com` API requests.
*   `GH_ENTERPRISE_TOKEN`, `GITHUB_ENTERPRISE_TOKEN` (in order of precedence): an authentication token for API requests to GitHub Enterprise.
*   `GH_HOST`: make the request to a GitHub host other than `github.com`.

## Learn More

Use `gh <command> <subcommand> --help` for more information about a command.
Read the manual at https://cli.github.com/manual
Learn about exit codes using `gh help exit-codes`
Learn about accessibility experiences using `gh help accessibility`
