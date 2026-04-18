# Russia-whitelist-rules-gen

[RU](/README.md) | [EN](/README-en.md)

The project contains a list of Russian internet services that remain accessible under internet restrictions in Russia, and a Python script for generating a set of rules for VPN clients based on xray-core or sing-box.

## Background

In Russia, "white lists" are being introduced where internet access is limited to only services included in the whitelist. This list was compiled from the [Megafon site](https://moscow.megafon.ru/offline_services/#whitelist).

## Project Structure

- [`whitelist.yaml`](whitelist.yaml) - YAML file containing categorized whitelist entries
- [`gen_list.py`](gen_list.py) - Python script that generates routing rules from the whitelist

## Categories

The whitelist includes services in the following categories:

- **Telecom** - Mobile operators (Megafon, MTS, Beeline, Tele2, Yota)
- **Government** - Government services, state agencies, and state companies (Gosuslugi, Goskey, Bank of Russia, etc.)
- **Finance** - Banks and payment systems (Mir, SBP, Moscow Exchange, Alfa-Bank, VTB, PSB)
- **Retail & Food** - Online stores and food delivery (Ozon, Wildberries, Samokat, X5, Magnit, etc.)
- **Media & IT** - TV channels, streaming services, news portals, and IT companies (Yandex, VK, Kinopoisk, Rutube, IVI, etc.)
- **Transport** - Transportation and travel services (RZD, Aeroflot, Tutu, etc.)
- **Other** - Miscellaneous services (2GIS, Avito, HeadHunter, CDEK, etc.)

## Installation

Install the required dependencies before running the script:

```bash
pip install pyyaml
```

## Usage

Run `gen_list.py` to generate routing rules:

```bash
# Generate rules for xray-core clients
python gen_list.py x

# Generate rules for sing-box clients
python gen_list.py s

# Generate both formats
python gen_list.py
```

## Output Formats

- **xray-core**: Uses `domain:` and `geosite:` prefixes
- **sing-box**: Converts `geosite:` to `set:geosite-` prefix

## Sources

The list is based on [v2fly/domain-list-community](https://github.com/v2fly/domain-list-community).

## License

This project is for informational purposes. Use at your own risk.