## 🎓 Academic Graph Builder

Visual modeling and visualization of academic entities (students, professors, courses, projects, and publications) using Python and NetworkX.

---

### 📦 Dataset Structure

This synthetic dataset represents the core components of an academic environment:

* **Students** (name, faculty number, major, course year, academic status)
* **Professors** (name, position, major, courses taught)
* **Courses** (course code, credits)
* **Research Projects** (title, leader, participants)
* **Publications** (title, authors)

All entities are stored as nodes in a directed graph (DiGraph), and relationships are edges with labels such as `Enrolled In`, `Teaches`, `Participates In`, `Leads`, and `Author`.

---

### 🛠️ Technologies Used

* `Python 3.x`
* `NetworkX` for graph creation and export
* `Matplotlib` for static visualization
* Export formats: `.graphml`, `.gexf`, `.json`

---

### 🔄 Graph Construction Logic

The graph includes:

* 7 students with varying majors and academic levels
* 2 professors leading courses and projects
* 2 core university courses
* 2 research projects with multi-student participation
* 1 academic publication with student-professor co-authorship

Each edge encodes a directional relationship (e.g., `Professor -> Course`, `Student -> Research Project`).

---

### 📈 Visualization

The script visualizes the graph using a spring layout and assigns node colors by type:

* 🟩 Students
* 🟧 Professors
* 🟦 Courses
* 🟪 Research Projects
* 🟨 Publications

Result: a clear, color-coded view of the academic ecosystem.

---

### 📤 Export Options

The final graph is exported in 3 formats:

* `academic_graph.graphml` – for use in Gephi, yEd, Neo4j
* `academic_graph.gexf` – for large-scale graph platforms
* `academic_graph.json` – for D3.js or custom visualization

---

### 📌 Topics

`python` `networkx` `graph-visualization` `academic-graph` `education-data` `students` `professors` `courses` `research-projects` `graph-export`

---

### 📎 About

This project is a compact and educational example of using graphs to model real-world academic data. It is suitable for:

* 📚 Teaching graph theory
* 🎓 University demos
* 📊 Visual analysis tools
* 🧪 Data modeling experiments
