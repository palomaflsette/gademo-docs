---
myst:
  html_meta:
    "description lang=en": |
      Documentation for users who wish to build sphinx sites with
      pydata-sphinx-theme.
---

# User Guide

You can configure the behavior, look, and feel of the theme in many ways.
The remaining pages in the user guide cover various ways of doing so.

```{danger}
This theme is still under active development, and we make no promises
about the stability of any specific HTML structure, CSS variables, etc.
Make these customizations at your own risk, and pin versions if you're
worried about breaking changes!
```

There are a number of options for configuring your site's look and feel.
All configuration options are passed with the `html_theme_options` variable in your `conf.py` file.
This is a dictionary with `key: val` pairs that you can configure in various ways.

```{toctree}
:caption: Get started

navbar
numeric_keyboard
chosen_params
average_fit_per_gen
box_plot
best_solution_and_individuals
best_fitness_per_generation
last_gen_fitness_distribution
keeping_results_over_rounds
analytical_execution
```