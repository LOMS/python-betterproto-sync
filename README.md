# Better Protobuf / gRPC Support for Python

This is 'synchronous' fork of https://github.com/danielgtaylor/python-betterproto 

It **cannot** be used alongside with original package. 

Basically, this is the same package, but without `async`/`await`. So, there will be no 'grpclib' dependency.
Currently, Fork is based on latest stable version of `betterproto` - `1.2.5`.
 
Additionally, I dropped support for python <3.9, because I don't have time for this.

This fork is not well-tested (yet), I hope I will delete this as soon, as betterproto v2
will be released and [issue #20](https://github.com/danielgtaylor/python-betterproto/issues/20)
satisfied. 

## Installation

### Regular mode:

pip: `pip install git+https://github.com/LOMS/python-betterproto-sync.git@master#egg=betterproto-sync`

poetry: `poetry add git+https://github.com/LOMS/python-betterproto-sync.git#master`

### Development mode:

pip: `pip install --editable git+https://github.com/LOMS/python-betterproto-sync.git@master#egg=betterproto-sync`

poetry: `poetry add --editable git+https://github.com/LOMS/python-betterproto-sync.git#master`

Pay attention to `master` branch here, I recommend to use certain commit hash instead of branch name.

## Documentation

Search documentation in original repo - https://github.com/danielgtaylor/python-betterproto 

Keep in mind - this is version 1.2.5

## License

Copyright © 2019 Daniel G. Taylor

http://dgt.mit-license.org/
