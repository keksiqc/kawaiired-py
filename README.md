# kawaiired-py
A Python wrapper for the kawaii.red API.

## Table of Contents
- [kawaiired-py](#kawaiired-py)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Getting started](#getting-started)
  - [Usage](#usage)
    - [Synchronous](#synchronous)
    - [Asynchronous](#asynchronous)
    - [Stats](#stats)
  - [Contributing](#contributing)
  - [License](#license)

## Installation
Install from pypi
```bash
pip install kawaiired-py
```
Install from source
```bash
pip install git+https://github.com/keksiqc/kawaiired-py
```

## Getting started
To use this wrapper, you'll need an API token from kawaii.red. Visit [their website](https://kawaii.red) to obtain a token.


## Usage
### Synchronous
```python
from kawaiired import KawaiiClient

client = KawaiiClient(token="your_token_here")

client.endpoints("gif")
# ['hug', 'kiss', 'pat', 'slap', 'tickle', 'waifu', 'wink', 'yiff']

client.get("gif", "kiss")
# https://api.kawaii.red/gif/kiss/kiss1.gif

client.random("gif")
# https://api.kawaii.red/gif/pat/pat1.gif

client.gif("kiss")
# https://api.kawaii.red/gif/kiss/kiss1.gif

stats = client.stats()
# <Stats>
```

### Asynchronous
```python
from kawaiired import KawaiiAioClient

client = KawaiiAioClient(token="your_token_here")

await client.endpoints("gif")
# ['hug', 'kiss', 'pat', 'slap', 'tickle', 'waifu', 'wink', 'yiff']

await client.get("gif", "kiss")
# https://api.kawaii.red/gif/kiss/kiss1.gif

await client.random("gif")
# https://api.kawaii.red/gif/pat/pat1.gif

await client.gif("kiss")
# https://api.kawaii.red/gif/kiss/kiss1.gif

stats = await client.stats()
# <Stats>
```

### Stats
The `stats()` method returns a Stats object with the following attributes:
```python
stats.endpoints         # List of available endpoints
stats.all               # Total number of requests
stats.failed            # Number of failed requests
stats.history           # List of recent requests
stats.most_endpoint     # Most used endpoint
stats.most_endpoints    # List of most used endpoints
stats.most_type         # Most used type (e.g., 'gif')
stats.most_types        # List of most used types
```

## Contributing
Contributions to this project are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch for your changes
3. Make your changes and commit them with a clear description
4. Open a pull request with a detailed explanation of your changes

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
