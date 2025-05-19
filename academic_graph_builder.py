import networkx as nx
import matplotlib.pyplot as plt

# Create graph
G = nx.DiGraph()  # We use a directed graph (DiGraph) because the links have direction

# Students
# Adding a student node: name, type, faculty number, major, course year, and academic status
G.add_node("Student: Akira Yamamoto", type="Student", faculty_number="12345",
           major="Computer Science", course="1", academic_status="Bachelor")
G.add_node("Student: Sofia Hernandez", type="Student", faculty_number="67890",
           major="Mathematics", course="2", academic_status="Master")

# Adding professor nodes with name, type, position, major, and list of courses taught
G.add_node("Professor: Dr. Miguel Oliveira", type="Professor",
           position="Associate Professor", major="Artificial Intelligence",
           courses_taught=["Machine Learning", "Artificial Neural Networks"])
G.add_node("Professor: Dr. Aisha Al-Mansoori", type="Professor",
           position="Full Professor", major="Computer Science", courses_taught=["Algorithms", "Data Structures"])

# Adding course nodes with name, type, course code, and credit value
G.add_node("Course: Machine Learning", type="Course", course_code="CS101", credits=6)
G.add_node("Course: Algorithms", type="Course", course_code="CS102", credits=6)

# Adding research project nodes with title, type, project leader, and a list of participants
G.add_node(
    "Research Project: AI Innovation Initiative",
    type="Research Project",
    project_leader="Dr. Miguel Oliveira",
    participants=["Student: Akira Yamamoto", "Student: Sofia Hernandez"]
)

G.add_node(
    "Research Project: Algorithmic Research Studies",
    type="Research Project",
    project_leader="Dr. Aisha Al-Mansoori",
    participants=["Student: Akira Yamamoto"]
)

# Adding a publication node with title, type, and list of authors
G.add_node(
    "Publication: Paper on Neural Networks",
    type="Publication",
    authors=["Professor: Dr. Miguel Oliveira", "Student: Akira Yamamoto"]
)

# Edges between students and courses (enrolled in course)
G.add_edge("Student: Akira Yamamoto", "Course: Machine Learning", relation="Enrolled In")
G.add_edge("Student: Sofia Hernandez", "Course: Algorithms", relation="Enrolled In")

# Edges between professors and courses (teaches course)
G.add_edge("Professor: Dr. Miguel Oliveira", "Course: Machine Learning", relation="Teaches")
G.add_edge("Professor: Dr. Aisha Al-Mansoori", "Course: Algorithms", relation="Teaches")

# Edges between students and research projects (participates in project)
G.add_edge("Student: Akira Yamamoto", "Research Project: AI Innovation Initiative",
           relation="Participates In")
G.add_edge("Student: Sofia Hernandez", "Research Project: AI Innovation Initiative",
           relation="Participates In")
G.add_edge("Student: Akira Yamamoto", "Research Project: Algorithmic Research Studies",
           relation="Participates In")

# Edges between professors and research projects (leads project)
G.add_edge("Professor: Dr. Miguel Oliveira", "Research Project: AI Innovation Initiative",
           relation="Leads")
G.add_edge("Professor: Dr. Aisha Al-Mansoori", "Research Project: Algorithmic Research Studies",
           relation="Leads")

# Edges between students and publications (author of publication)
G.add_edge("Student: Akira Yamamoto", "Publication: Paper on Neural Networks", relation="Author")

# Edges between professors and publications (author of publication)
G.add_edge("Professor: Dr. Miguel Oliveira", "Publication: Paper on Neural Networks",
           relation="Author")

# Generate positions for nodes using spring layout
pos = nx.spring_layout(G)

# Visualizing the academic graph
color_map = []
for node in G.nodes(data=True):
    node_type = node[1].get("type")
    if node_type == "Student":
        color_map.append("lightgreen")
    elif node_type == "Professor":
        color_map.append("orange")
    elif node_type == "Course":
        color_map.append("skyblue")
    elif node_type == "Research Project":
        color_map.append("violet")
    elif node_type == "Publication":
        color_map.append("gold")
    else:
        color_map.append("grey")

plt.figure(figsize=(12, 12))
nx.draw(G, pos, with_labels=True, node_color=color_map, node_size=3000, font_size=10, font_weight="bold", arrows=True)
plt.title("Graph of the Academic System with Node Types")
plt.show()
