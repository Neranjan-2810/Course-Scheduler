import tkinter as tk
from tkinter import messagebox
from collections import deque
def findOrder(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    in_degree = [0] * numCourses
    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        in_degree[course] += 1
    queue = deque()
    for course in range(numCourses):
        if in_degree[course] == 0:
            queue.append(course)
    order = []
    while queue:
        course = queue.popleft()
        order.append(course)
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    if len(order) == numCourses:
        return order
    else:
        return []
def find_order():
    num_courses = int(num_courses_entry.get())
    prerequisites = parse_prerequisites(prerequisites_entry.get())
    order = findOrder(num_courses, prerequisites)
    if order:
        messagebox.showinfo("Course Order", f"The course order is: {order}")
    else:
        messagebox.showwarning("Course Order", "It is impossible to finish all courses!")
def parse_prerequisites(prerequisites_str):
    prerequisites = []
    pairs = prerequisites_str.strip().split(',')
    for pair in pairs:
        course, prerequisite = map(int, pair.strip().split())
        prerequisites.append([course, prerequisite])
    return prerequisites
window = tk.Tk()
window.title("Course Order")
window.geometry("400x200")
num_courses_label = tk.Label(window, text="Total Number of Courses:")
num_courses_label.pack()
num_courses_entry = tk.Entry(window)
num_courses_entry.pack()
prerequisites_label = tk.Label(window, text="Prerequisites (separated by comma):")
prerequisites_label.pack()
prerequisites_entry = tk.Entry(window)
prerequisites_entry.pack()
find_order_button = tk.Button(window, text="Find Course Order", command=find_order)
find_order_button.pack()
window.mainloop()
