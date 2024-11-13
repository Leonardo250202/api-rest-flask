from flask import Flask, jsonify, request, render_template, redirect

app = Flask(__name__)

# Datos en memoria
tasks = [
    {"id": 1, "title": "Estudiar Flask", "done": False},
    {"id": 2, "title": "Implementar API", "done": True}
]

# Página principal con HTML
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Obtener todas las tareas en formato JSON
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Agregar una nueva tarea desde el formulario HTML
@app.route('/tasks', methods=['POST'])
def create_task():
    new_title = request.form.get('title')
    new_task = {
        "id": len(tasks) + 1,
        "title": new_title,
        "done": False
    }
    tasks.append(new_task)
    return redirect('/')

# Marcar una tarea como completada
@app.route('/tasks/<int:task_id>/complete', methods=['POST'])
def complete_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        task['done'] = True
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
