# Démostration-Web-Django Python / Web Django Python Demostration

[en] An web based application that will read a pre-loaded csv file and display a linear chart according to provided dates.

[fr] Une application Web qui lira un fichier CSV préchargé et affichera un graphique linéaire en fonction des dates fournies.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Project Overview

[en] This project is designed to provide a simple web-based interface for visualizing data points stored in a CSV file. Users can generate line charts based on the selected date range, offering a quick and interactive way to explore trends and patterns in the data.

[fr] Ce projet est conçu pour fournir une interface Web simple pour visualiser les points de données stockés dans un fichier CSV. Les utilisateurs peuvent générer des graphiques linéaires basés sur la plage de dates sélectionnée, offrant ainsi un moyen rapide et interactif d'explorer les tendances et les modèles dans les données.

## Features

- **CSV Data Import:** Users can upload CSV files containing date-value pairs for visualization accordingly to the existing.
- **Date Range Selection:** A user-friendly form allows users to specify the date range for generating line charts.
- **Line Chart Generation:** Utilizing the Matplotlib library, the project dynamically creates line charts based on user input.
- **Interactive Web Interface:** The project includes a web interface accessible through a browser.
- **Generated Graphic Download:** Users can download the generated graphic as PNG.


## Getting Started

### Prerequisites

- Python 3.x
- Django (installed via `pip install django`)
- Matplotlib (installed via `pip install matplotlib`)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/adelriorz/D-mostration-Web-Django-Python.git
    cd D-mostration-Web-Django-Python
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the development server:

    ```bash
    python manage.py runserver
    ```

Visit `http://127.0.0.1:8000/` in your browser to access the web interface.

## Usage

1. Make sure the CSV file is using the provided form.
2. Specify the date range for the line chart.

## Configuration

The project has minimal configuration requirements. Ensure that the necessary Python packages are installed.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- The project uses Matplotlib for data visualization.