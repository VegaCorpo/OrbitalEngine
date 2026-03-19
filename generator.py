import json
import random
import argparse


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
