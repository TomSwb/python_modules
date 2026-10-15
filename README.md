*This project has been created as part of the 42 curriculum by [tschwab](https://profile-v3.intra.42.fr/users/tschwab).*

# Python modules – 42 Python piscine by TomSwb

## Description

My work for the Python piscine of 42's new common core: a series of modules that teach Python from the basics up, all built around managing community-garden data.

**Status:** modules 00 and 01 are completed and documented below. A review and correction pass on both is planned. Later modules are in progress and will be documented once completed.

The subjects require Python 3.10+, **flake8**-clean code and type hints on every function and method, checked with **mypy**. Bringing all of module 01 fully in line with these rules is part of the planned correction pass.

## Module 00 – Growing Code: Python fundamentals

Expressions, variables, functions, input, conditions and loops, ending with type annotations.

| Exercise | File | What it does |
|---|---|---|
| ex0 | `ft_hello_garden.py` | First function: print a greeting |
| ex1 | `ft_garden_name.py` | Read user input and use it in an f-string |
| ex2 | `ft_plot_area.py` | Compute a plot's area from length and width |
| ex3 | `ft_harvest_total.py` | Add up three days of harvest |
| ex4 | `ft_plant_age.py` | Condition: is the plant ready to harvest? |
| ex5 | `ft_water_reminder.py` | Condition: does the plant need watering? |
| ex6 | `ft_count_harvest_iterative.py` · `ft_count_harvest_recursive.py` | Print each day until harvest, once with a loop and once with recursion |
| ex7 | `ft_seed_inventory.py` | Seed inventory with type annotations, formatted by unit |

## Module 01 – Code Cultivation: object-oriented programming

One `Plant` class, grown exercise by exercise into a small garden system.

| Exercise | File | What it adds |
|---|---|---|
| ex0 | `ft_garden_intro.py` | A first program with a `main()` entry point |
| ex1 | `ft_garden_data.py` | The `Plant` class (name, height, age, `show()`) and a `Garden` that holds plants |
| ex2 | `ft_plant_grow.py` | Methods that change state: simulate a week of growth |
| ex3 | `ft_plant_factory.py` | Create many plants at once through the constructor |
| ex4 | `ft_garden_security.py` | Encapsulation: protected data, getters and setters that validate values and print clear errors |
| ex5 | `ft_plant_types.py` | Inheritance: `Flower`, `Tree` and `Vegetable` subclasses with their own behaviour |
| ex6 | `ft_garden_analytics.py` | Garden analytics: class and static methods, a nested statistics class, deeper inheritance (`Seed` from `Flower`) |

## Instructions

Requires Python 3.10 or newer.

Module 01 exercises run on their own:

```bash
python3 python01/ex1/ft_garden_data.py
```

Module 00 exercises are functions; the subject's helper `python00/main.py` (provided by 42) calls them and reports errors.

Run the same checks as the subjects:

```bash
pip install flake8 mypy
flake8 python00 python01
mypy python00 python01
```

## Resources

- The official [Python tutorial](https://docs.python.org/3/tutorial/) and [typing docs](https://docs.python.org/3/library/typing.html)
- [flake8](https://flake8.pycqa.org/) and [mypy](https://mypy.readthedocs.io/) documentation

### AI use

- **Code:** written by hand. AI assistants were used as a learning aid, to explain concepts and debug ideas, not to generate the exercise code.
- **Documentation:** this README was drafted with Claude (Anthropic) from the repository's code and subjects, then reviewed and corrected by me.
