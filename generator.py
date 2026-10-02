import json
import random
import argparse

MIN_ROTATION_PERIOD = 3.6e4
MAX_ROTATION_PERIOD = 2.2e7
RETROGRADE_PROBABILITY = 0.1


def random_rotation():
    period = random.uniform(MIN_ROTATION_PERIOD, MAX_ROTATION_PERIOD)
    if random.random() < RETROGRADE_PROBABILITY:
        period = -period
    return {
        "period": round(period, 2),
        "obliquity": round(random.uniform(0.0, 90.0), 2),
        "axisAzimuth": round(random.uniform(0.0, 360.0), 2),
        "initialAngle": round(random.uniform(0.0, 360.0), 2),
    }


def map_generator(num_entities, output_file):
    entities = []

    for i in range(num_entities):
        entity = {
            "name": f"entity_{i}",
            "components": {
                "Mass": {
                    "mantissa": round(random.uniform(1.0, 10.0), 2),
                    "exponent": random.randint(20, 30),
                },
                "Name": {"value": f"entity_{i}"},
                "Texture": {"path": "default.png"},
                "Acceleration": {
                    "x": round(random.uniform(-1.0, 1.0), 2),
                    "y": round(random.uniform(-1.0, 1.0), 2),
                    "z": round(random.uniform(-1.0, 1.0), 2),
                },
                "Position": {
                    "x": round(random.uniform(-1000000000.0, 1000000000.0), 2),
                    "y": round(random.uniform(-1000000000.0, 1000000000.0), 2),
                    "z": round(random.uniform(-1000000000.0, 1000000000.0), 2),
                },
                "Velocity": {
                    "x": round(random.uniform(-30.0, 30.0), 2),
                    "y": round(random.uniform(-30.0, 30.0), 2),
                    "z": round(random.uniform(-30.0, 30.0), 2),
                },
                "Radius": {
                    "value": round(random.uniform(-1000.0, 100000.0), 2),
                },
                "Rotation": random_rotation(),
            },
        }
        entities.append(entity)

    map_data = {"entities": entities}

    with open(output_file, "w") as f:
        json.dump(map_data, f, indent=4)


def parser():
    parser = argparse.ArgumentParser(description="Generate a map with random entities.")
    parser.add_argument(
        "-n",
        "--num_entities",
        type=int,
        default=10,
        help="Number of entities to generate",
    )
    parser.add_argument(
        "-o",
        "--output_file",
        type=str,
        default="map.json",
        help="Output file name for the generated map",
    )

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parser()
    map_generator(args.num_entities, args.output_file)
