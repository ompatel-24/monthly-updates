# A Monthly Update

[![Twitter Follow](https://img.shields.io/twitter/follow/monthupdate?style=social)](https://twitter.com/monthupdate)

This is a Python Twitter bot that automatically tweets a daily update with a progress bar showing how much of the current month has elapsed. The bot calculates the progress based on the current date and time zone, and uses the Twitter API to post a new tweet every day.

## Live Twitter Feed

Tweets by [@monthupdate](https://twitter.com/monthupdate)

<a class="twitter-timeline" data-lang="en" data-theme="dark" href="https://twitter.com/MonthUpdate?ref_src=twsrc%5Etfw">Tweets by MonthUpdate</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)
- [Contributing](#contributing)
- [License](#license)

## Requirements

To use this bot, you'll need:

- Python 3.x
- A Twitter developer account and API keys
- [Requriements File](requirements.txt)

## Installation

To install the bot, simply clone or download the repository to your local machine:

```
git clone https://github.com/ompatel-24E/monthly-updates.git
```

Then, open the `.env` file and replace the placeholders with your own Twitter API keys:

```python
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"
```

## Usage

To use the bot, simply run the `main.py` file:

```
python main.py
```

This will calculate the progress of the current month and post a new tweet to your Twitter account.

By default, the bot will run in the time zone of your local machine. If you want to run the bot in a specific time zone, you can modify the `est_tz` variable in the `main.py` file:

```python
est_tz = pytz.timezone('US/Eastern')
```

Replace `'US/Eastern'` with the [time zone code](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) for the time zone you want to use.

## Support

If you have any questions or issues with the bot, feel free to open a new issue on GitHub or contact me on Twitter [@ompatel_24](https://twitter.com/ompatel_24).

## Contributing

Contributions are always welcome! If you have any ideas or improvements for the bot, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.