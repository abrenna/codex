"""Energy unit converter for gas and oil.

Usage examples:
  python energy_converter.py gas 10 MWh MMBTU
  python energy_converter.py oil 50 fat sm3
"""

import argparse

GAS_TO_MWH = {
    "MWh": 1.0,
    "MMBTU": 0.293071,
    "sm3": 0.01055,
    "fat": 1.701,  # barrel of oil equivalent
}

OIL_VOL_CONV = {
    "fat": 1.0,           # barrel
    "sm3": 6.2898,        # barrels in one cubic meter
}


def convert_gas(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit not in GAS_TO_MWH:
        raise ValueError(f"Unknown gas unit: {from_unit}")
    if to_unit not in GAS_TO_MWH:
        raise ValueError(f"Unknown gas unit: {to_unit}")
    mwh = value * GAS_TO_MWH[from_unit]
    return mwh / GAS_TO_MWH[to_unit]


def convert_oil(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit not in OIL_VOL_CONV:
        raise ValueError(f"Unknown oil unit: {from_unit}")
    if to_unit not in OIL_VOL_CONV:
        raise ValueError(f"Unknown oil unit: {to_unit}")
    barrels = value * OIL_VOL_CONV[from_unit]
    return barrels / OIL_VOL_CONV[to_unit]


def main():
    parser = argparse.ArgumentParser(description="Convert energy units for gas and oil")
    parser.add_argument("category", choices=["gas", "oil"], help="Category of conversion")
    parser.add_argument("value", type=float, help="Numeric value to convert")
    parser.add_argument("from_unit", help="Unit to convert from")
    parser.add_argument("to_unit", help="Unit to convert to")
    args = parser.parse_args()

    if args.category == "gas":
        result = convert_gas(args.value, args.from_unit, args.to_unit)
    else:
        result = convert_oil(args.value, args.from_unit, args.to_unit)

    print(f"{args.value} {args.from_unit} = {result:.4f} {args.to_unit}")


if __name__ == "__main__":
    main()
