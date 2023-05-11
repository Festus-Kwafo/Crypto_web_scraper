import re


def get_digits_int(field_dat: str):
    digits_only = ''.join(c for c in field_dat if c.isdigit())
    return int(digits_only)


def get_digits_float(field_dat: str):
    digits_only = ''.join(c for c in field_dat if c.isdigit())
    return float(digits_only)


def format_market_cap(field_data: str):
    pattern = "^.*?\$.*?\$"
    return re.sub(pattern, '', field_data)


def remove_percent_sign(field_data: str):
    field_data = field_data.replace('%', "")
    return field_data
