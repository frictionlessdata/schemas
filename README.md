# JSON Schemas for Data Protocol Formats

JSON Schemas, and a registry, for the Data Package family of specifications. Read more about Data Packages at [Data Protocols](http://dataprotocols.org/).

The schemas are implemented using [JSON Schema](http://json-schema.org/), a specification which provides a simple declarative format for describing the structure of JSON documents.

The registry is implemented as simple CSV file, and there are libraries in [Javascript](https://github.com/okfn/datapackage-registry-js) and [Python](https://github.com/okfn/datapackage-registry-py) that work with the registry directly.

## The schemas

Here you'll find schemas for [Data Package](http://dataprotocols.org/data-packages/), various Data Package Profiles, [JSON Table Schemas](http://dataprotocols.org/json-table-schema/), [CSV Dialect Description Format](http://dataprotocols.org/csv-dialect/) and more.

## The registry

The registry enables consumers to get access to schemas and documentation for the family of Data Package specifications, and related specifications like JSON Table Schema and CSV Dialect Description Format. See [Data Protocols](http://dataprotocols.org/) for more information.

### Contributing

Yes we welcome and encourage additions to the registry! Any spec that is added must meet the following criteria:

* Be related to the Data Packages family of specifications.
* Have a publicly -accessible web page describing the specification.
* Have a JSON Schema file that describes the specification.

See the existing entries in the registry, and then take the following steps to add a new entry:

1. Make a new pull request called `registry/{NAME_OF_SPECIFICATION}`
2. The pull request features a JSON Schema file for the new specification, and adds the spec to `registry.csv`
3. Write a brief description of the spec as part of the pull request.
