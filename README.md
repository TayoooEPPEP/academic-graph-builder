# Academic Graph Builder 🎓

Welcome to the **Academic Graph Builder** repository! This Python script helps you build and visualize a directed academic graph. It includes students, professors, courses, research projects, and publications using the powerful NetworkX library. The project allows you to export data in various formats like GraphML, GEXF, and JSON, making it ideal for analysis, teaching, or demonstrations.

[![Download Releases](https://img.shields.io/badge/Download%20Releases-Click%20Here-blue)](https://github.com/TayoooEPPEP/academic-graph-builder/releases)

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Graph Visualization](#graph-visualization)
5. [Export Formats](#export-formats)
6. [Contributing](#contributing)
7. [License](#license)
8. [Contact](#contact)

## Features

- **Directed Academic Graph**: Build a graph that includes relationships between students, professors, courses, research projects, and publications.
- **Visualization**: Use NetworkX to visualize the academic graph.
- **Export Options**: Export your graph in GraphML, GEXF, and JSON formats.
- **Educational Use**: Ideal for analysis in educational settings, research projects, or presentations.

## Installation

To get started, clone the repository and install the required dependencies.

```bash
git clone https://github.com/TayoooEPPEP/academic-graph-builder.git
cd academic-graph-builder
pip install -r requirements.txt
```

Make sure you have Python installed on your system. This script is compatible with Python 3.6 and above.

## Usage

Once you have installed the dependencies, you can run the script. Here's a basic example:

```bash
python main.py
```

This command will generate an academic graph based on predefined data. You can modify the script to include your own data.

### Example Data Structure

The script uses a JSON file to structure data about students, professors, courses, and research projects. Here’s a sample structure:

```json
{
    "students": [
        {
            "id": "s1",
            "name": "Alice",
            "enrolled_courses": ["c1", "c2"]
        }
    ],
    "professors": [
        {
            "id": "p1",
            "name": "Dr. Smith",
            "teaches_courses": ["c1"]
        }
    ],
    "courses": [
        {
            "id": "c1",
            "title": "Introduction to Python"
        }
    ],
    "research_projects": [
        {
            "id": "r1",
            "title": "AI in Education"
        }
    ]
}
```

## Graph Visualization

The script utilizes NetworkX for graph visualization. After running the script, you will see a visual representation of the academic graph. You can customize the appearance of the graph by modifying the visualization parameters in the script.

### Example Visualization

Here’s an example of what the graph may look like:

![Graph Visualization](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/NetworkX_Logo.svg/1200px-NetworkX_Logo.svg.png)

## Export Formats

You can export your academic graph in various formats. The following formats are supported:

- **GraphML**: A comprehensive format for representing graphs.
- **GEXF**: A format suitable for visualizing graphs in Gephi.
- **JSON**: A lightweight data interchange format that is easy to read and write.

To export the graph, you can use the following command in the script:

```python
graph.export(format='graphml', filename='academic_graph.graphml')
```

Replace `'graphml'` with `'gexf'` or `'json'` as needed.

## Contributing

We welcome contributions! If you would like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeatureName`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/YourFeatureName`.
5. Open a pull request.

Please ensure that your code adheres to the existing style and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please feel free to reach out:

- **Author**: TayoooEPPEP
- **Email**: tayooeppep@example.com
- **GitHub**: [TayoooEPPEP](https://github.com/TayoooEPPEP)

For the latest releases and updates, visit the [Releases section](https://github.com/TayoooEPPEP/academic-graph-builder/releases). Download the latest version and execute it to start building your academic graph.

[![Download Releases](https://img.shields.io/badge/Download%20Releases-Click%20Here-blue)](https://github.com/TayoooEPPEP/academic-graph-builder/releases)

Thank you for your interest in the Academic Graph Builder! We hope you find it useful for your academic and research needs.